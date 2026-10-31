#!/usr/bin/env python3
"""Discover Agent Skills across curated upstream GitHub collections.

Read-only network discovery with an explicit --online opt-in. Discovered paths
are candidates, NOT verified installable entries. No code is downloaded,
executed or copied into agent folders. Inspect SKILL.md and license first.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import sys
import urllib.parse
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parent
MAX_RESPONSE = 8 * 1024 * 1024


def github_json(endpoint, token=None):
    request = urllib.request.Request(
        "https://api.github.com/" + endpoint.lstrip("/"),
        headers={"Accept": "application/vnd.github+json", "User-Agent": "StackMutinyDiscovery/0.2",
                 **({"Authorization": "Bearer " + token} if token else {})},
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        raw = response.read(MAX_RESPONSE + 1)
    if len(raw) > MAX_RESPONSE:
        raise ValueError("GitHub response exceeded limit")
    return json.loads(raw)


def discover_repository(entry, token=None):
    repo = entry["repo"]
    result = {"repo": repo, "name": entry["name"], "candidates": [], "truncated": False, "error": ""}
    try:
        meta = github_json("repos/" + repo, token=token)
        branch = meta["default_branch"]
        encoded_branch = urllib.parse.quote(branch, safe="")
        data = github_json("repos/" + repo + "/git/trees/" + encoded_branch + "?recursive=1", token=token)
        result["truncated"] = bool(data.get("truncated"))
        for node in data.get("tree", []):
            path = node.get("path", "")
            if node.get("type") != "blob" or not path.endswith("/SKILL.md"):
                continue
            if any(x in path.lower().split("/") for x in ("node_modules", ".venv", "vendor", "test-fixtures", "testdata")):
                continue
            proposed_name = path.split("/")[-2]
            result["candidates"].append({
                "repo": repo, "path": path, "folder": proposed_name,
                "url": f"https://github.com/{repo}/blob/{branch}/{path}",
                "status": "candidate_not_verified",
            })
        result["candidates"].sort(key=lambda x: x["path"])
    except (urllib.error.URLError, urllib.error.HTTPError, KeyError, ValueError, OSError) as error:
        result["error"] = str(error)[:240]
    return result


def main(argv=None, fetcher=None):
    parser = argparse.ArgumentParser(description="Survey SKILL.md candidates in curated GitHub source collections")
    parser.add_argument("--online", action="store_true", help="explicit consent for public GitHub API reads")
    parser.add_argument("--list", action="store_true", help="list source collections without network")
    parser.add_argument("--query", default="", help="filter discovered skill folders and paths")
    parser.add_argument("--repos", default="", help="comma-separated exact owner/repo names; default all")
    parser.add_argument("--limit", type=int, default=120)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--output", default="", help="optional JSON results path")
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= 5000 or not 1 <= args.workers <= 10:
        parser.error("--limit must be 1..5000 and --workers 1..10")
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    entries = catalog["source_collections"]
    if args.repos:
        filter_repos = set(x.strip().lower() for x in args.repos.split(",") if x.strip())
        entries = [x for x in entries if x["repo"].lower() in filter_repos]
        if len(entries) != len(filter_repos):
            parser.error("unknown source repo specified")
    if args.list or not args.online:
        for item in entries:
            print(f"{item['repo']:54} {item['purpose']}")
        if not args.online:
            print("To query live source trees, add --online; no scripts will be executed.")
        return 0
    fn = fetcher or discover_repository
    token = os.environ.get("GITHUB_TOKEN")
    reports = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        tasks = [executor.submit(fn, x, token) for x in entries]
        for future in as_completed(tasks):
            reports.append(future.result())
    reports.sort(key=lambda x: x["repo"].lower())
    candidates = [s for group in reports for s in group["candidates"]
                  if args.query.lower() in (s["repo"] + " " + s["path"]).lower()]
    candidates = candidates[:args.limit]
    result = {
        "status": "discovered_unverified",
        "source_repositories_checked": len(reports),
        "source_failures": [{"repo": x["repo"], "error": x["error"]} for x in reports if x["error"]],
        "truncated_repositories": [x["repo"] for x in reports if x["truncated"]],
        "matching_candidates_in_limit": len(candidates), "candidates": candidates,
    }
    if args.output:
        Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for item in candidates:
        print(f"{item['repo']} / {item['folder']}  {item['url']}")
    print(f"Found {len(candidates)} unverified candidate paths from {len(reports)} collections; output limited to {args.limit}.")
    if result["truncated_repositories"]:
        print("GitHub truncated source trees for: " + ", ".join(result["truncated_repositories"]))
    if result["source_failures"]:
        print("Source fetch failures: " + ", ".join(x["repo"] for x in result["source_failures"]), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
