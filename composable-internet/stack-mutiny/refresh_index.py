#!/usr/bin/env python3
"""Refresh Stack Mutiny's unverified GitHub-tree index. Never installs upstream code."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index"
EXCLUDED = {"node_modules", ".venv", "vendor", "test-fixtures", "testdata"}
MAX_BYTES = 16 * 1024 * 1024


def api(path):
    req = urllib.request.Request("https://api.github.com/" + path, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "StackMutinyIndexRefresh/1.0",
        **({"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"]}
           if os.getenv("GITHUB_TOKEN") else {}),
    })
    with urllib.request.urlopen(req, timeout=35) as response:
        raw = response.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("GitHub response exceeded byte limit")
    return json.loads(raw)


def refresh_repository(repo, old_entries):
    meta = api("repos/" + repo)
    branch = meta["default_branch"]
    data = api("repos/" + repo + "/git/trees/" +
               urllib.parse.quote(branch, safe="") + "?recursive=1")
    if data.get("truncated"):
        raise ValueError("GitHub recursive tree truncated; preserve previous index")
    entries = []
    for node in data.get("tree", []):
        path = node.get("path", "")
        if node.get("type") != "blob" or not (path == "SKILL.md" or path.endswith("/SKILL.md")):
            continue
        if EXCLUDED.intersection(path.lower().split("/")):
            continue
        sha = node.get("sha")
        if not isinstance(sha, str) or len(sha) != 40:
            raise ValueError("invalid Git blob SHA")
        folder = path.split("/")[-2] if "/" in path else repo.rsplit("/", 1)[-1]
        entries.append((path, sha, folder))
    entries.sort()
    old = {entry[0]: entry[1] for entry in old_entries}
    new = {entry[0]: entry[1] for entry in entries}
    return {
        "entries": entries, "tree_sha": data.get("sha", ""),
        "added": sorted(set(new) - set(old)),
        "removed": sorted(set(old) - set(new)),
        "changed": sorted(p for p in old.keys() & new.keys() if old[p] != new[p]),
    }


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true", help="enable GitHub API reads")
    parser.add_argument("--report", default="stack-mutiny-refresh-report.json")
    args = parser.parse_args()
    if not args.online:
        parser.error("explicit --online is required")
    manifest = json.loads((INDEX / "manifest.json").read_text())
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    updates = {}
    report = {"date": today, "status": "candidate_index_only",
              "repositories": [], "failures": []}
    # Every tracked repo is sourced from the existing four index shards.
    for shard in manifest["shards"]:
        path = INDEX / (shard["id"] + ".json")
        doc = json.loads(path.read_text())
        old_by_repo = {r["repo"]: [] for r in doc["repositories"]}
        for rid, skill_path, blob_sha, folder in doc["entries"]:
            repo = doc["repositories"][rid]["repo"]
            old_by_repo[repo].append((skill_path, blob_sha, folder))
        new_repos = []
        new_entries = []
        for repo_record in doc["repositories"]:
            repo = repo_record["repo"]
            try:
                result = refresh_repository(repo, old_by_repo[repo])
            except (urllib.error.URLError, ValueError, KeyError, OSError) as exc:
                report["failures"].append({"repo": repo, "reason": str(exc)[:250]})
                # Do not accept partial refresh or erase skills after upstream failure.
                continue
            idx = len(new_repos)
            new_repos.append({**repo_record, "tree_sha": result["tree_sha"],
                              "total": len(result["entries"])})
            new_entries.extend([[idx, *entry] for entry in result["entries"]])
            report["repositories"].append({"repo": repo, "shard": shard["id"],
                                            "total": len(result["entries"]),
                                            **{k: result[k] for k in ("added", "removed", "changed")}})
        if report["failures"]:
            break
        doc.update(date=today, repositories=new_repos, entries=new_entries)
        updates[path] = doc
    Path(args.report).write_text(json.dumps(report, indent=2) + "\n")
    if report["failures"]:
        print("Refresh incomplete. No index files changed.", file=sys.stderr)
        return 1
    all_shas = []
    counts = {}
    for shard in manifest["shards"]:
        doc = updates[INDEX / (shard["id"] + ".json")]
        count = len(doc["entries"])
        counts[shard["id"]] = count
        shard["skills"] = count
        shard["repos"] = len(doc["repositories"])
        all_shas.extend(e[2] for e in doc["entries"])
    manifest.update(generated=today, total_paths=len(all_shas),
                    unique_blob_shas=len(set(all_shas)),
                    duplicate_content_occurrences=len(all_shas)-len(set(all_shas)))
    updates[INDEX / "manifest.json"] = manifest
    pools_path = INDEX / "role-pools.json"
    pools = json.loads(pools_path.read_text())
    repo_counts = {r["repo"]: r["total"] for doc in
                   (updates[INDEX / (s["id"] + ".json")] for s in manifest["shards"])
                   for r in doc["repositories"]}
    for role in pools["roles"].values():
        role["source_pool_paths"] = sum(repo_counts.get(r, 0) for r in role["source_repositories"])
    pools["date"] = today
    updates[pools_path] = pools
    for path, doc in updates.items():
        path.write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")) + "\n")
    print("Indexed %d paths from %d tracked repositories." %
          (len(all_shas), len(report["repositories"])))
    print("New %d, changed %d, removed %d" % tuple(
        sum(len(r[k]) for r in report["repositories"])
        for k in ("added", "changed", "removed")))
    print("The reviewed installable catalog was NOT modified.")
    return 0


if __name__ == "__main__":
    sys.exit(run())
