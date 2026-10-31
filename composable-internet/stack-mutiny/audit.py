#!/usr/bin/env python3
"""Check recorded upstream Agent Skills for name/path drift.

Opt-in network audit, read-only. Uses the GitHub Contents API and compares
current SKILL.md frontmatter to the manifest's inspected name. Nothing is
installed, executed, or copied into a skills directory.
"""
import argparse
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
MAX_BYTES = 256 * 1024


def check(entry, token=None):
    repo, path = entry["repo"], entry["source_path"]
    url = f"https://api.github.com/repos/{repo}/contents/{urllib.parse.quote(path)}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "StackMutinySourceAudit/0.2",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    result = {"id": entry["id"], "url": entry["source_url"], "status": "unknown"}
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            payload = response.read(MAX_BYTES * 2)
            doc = json.loads(payload)
        if doc.get("type") != "file" or doc.get("encoding") != "base64":
            result.update(status="invalid_response", reason="not a base64 file")
            return result
        raw = base64.b64decode(doc["content"], validate=False)
        if len(raw) > MAX_BYTES:
            result.update(status="too_large")
            return result
        text = raw.decode("utf-8")
        match = re.search(r"(?m)^name:\s*['\"]?([^'\"\n#]+)", text[:8000])
        actual = match.group(1).strip() if match else None
        if actual != entry["skill"]:
            result.update(status="name_changed", actual_name=actual)
        else:
            result.update(status="ok", blob_sha=doc.get("sha"), bytes=len(raw))
    except urllib.error.HTTPError as exc:
        result.update(status="http_error", reason=str(exc.code))
    except (urllib.error.URLError, ValueError, KeyError, UnicodeDecodeError, OSError) as exc:
        result.update(status="fetch_error", reason=str(exc)[:200])
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Read-only upstream skill drift audit")
    parser.add_argument("--online", action="store_true", help="required to contact GitHub")
    parser.add_argument("--output", default="", help="write result JSON to path")
    parser.add_argument("--workers", type=int, default=5)
    args = parser.parse_args(argv)
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    skills = catalog.get("skills", [])
    if not skills:
        print("No catalog skills found.", file=sys.stderr)
        return 2
    if not args.online:
        print(f"Catalog has {len(skills)} source paths. Use --online for a read-only remote audit.")
        return 0
    if args.workers < 1 or args.workers > 12:
        parser.error("--workers must be 1..12")
    token = os.environ.get("GITHUB_TOKEN")
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(check, item, token) for item in skills]
        for task in as_completed(futures):
            results.append(task.result())
    results.sort(key=lambda x: x["id"].lower())
    report = {"catalog_edition": catalog.get("edition"), "checked": len(results),
              "passing": sum(x["status"] == "ok" for x in results),
              "failures": [x for x in results if x["status"] != "ok"], "results": results}
    if args.output:
        Path(args.output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for item in report["failures"]:
        print(f"DRIFT {item['id']}: {item['status']} {item.get('reason', item.get('actual_name', ''))}")
    print(f"Upstream current SKILL.md paths: {report['passing']}/{report['checked']} match the catalog.")
    print("This does NOT audit licenses, threats, behavior, dependencies, or user outcomes.")
    return 1 if report["failures"] else 0


if __name__ == "__main__":
    sys.exit(main())
