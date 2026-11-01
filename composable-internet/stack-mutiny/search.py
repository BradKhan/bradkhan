#!/usr/bin/env python3
"""Stack Mutiny: compact skill search over thousands of indexed upstream paths.

The index contains paths and git blob hashes, NOT fully reviewed skill bodies.
Reads three JSON shards, locally or from the public repository. No installer is
executed. A query returns a few ranked candidates and exact source provenance.
"""
import argparse
import json
import math
from pathlib import Path
import re
import sys
import urllib.request

ROOT = Path(__file__).resolve().parent
BASE = "https://raw.githubusercontent.com/BradKhan/bradkhan/main/composable-internet/stack-mutiny/"
STOP = frozenset("a an the and or of to for on in with by from how can i my me we do is build create find use skills skill agent agents ai tool tools best good".split())
ALIAS = {
 "founder": "startup business venture customer product validate",
 "startup": "founder venture mvp community launch pricing",
 "investor": "investment finance equity valuation portfolio diligence",
 "investment": "investor equity portfolio financial valuation underwriting",
 "family": "family-office wealth portfolio investment planning",
 "office": "family-office portfolio wealth investment",
 "design": "ux ui frontend typography visual art",
 "designer": "design ux ui interface",
 "creator": "content media video writing graphics publishing",
 "content": "writing marketing publishing creator social",
 "marketer": "marketing seo conversion campaign growth",
 "marketing": "seo copywriting growth audience content",
 "developer": "code testing engineer architecture debugging",
 "engineer": "developer engineering code architecture testing",
 "memory": "context persistence retrieval knowledge database",
 "context": "memory token optimization retrieval",
 "inference": "models serving routing llm latency compute",
 "compute": "inference models gpu serving edge",
 "privacy": "security sovereignty encrypted local",
 "security": "vulnerability audit privacy threat",
 "research": "scientific deep-research evidence citations investigation",
 "browser": "playwright web automation testing",
 "finance": "financial investment valuation accounting",
 "video": "animation editing media creator",
 "presentation": "slides deck powerpoint investor",
 "cloudflare": "workers edge d1 r2 cloud",
 "open": "open-source independence local self-hosted",
}
ROLES = {
 "developer": "coding programming debugging testing architecture security release",
 "design": "ui ux typography art visual accessibility",
 "founder": "venture startup validation customers pricing product",
 "marketing": "seo copywriting growth campaigns content",
 "creator": "article writing illustration video image publishing",
 "investor": "equity investment finance due-diligence portfolio",
 "family-office": "financial portfolio wealth macro investment risk",
 "ai-memory": "context memory retrieval knowledge persistence",
 "ai-compute": "inference routing models cloud gpu serving",
 "research": "scientific sources methodology literature evidence",
 "agent": "agent skills orchestration tools mcp harness",
}
TRUST = {"official": 2.7, "specialist": 1.7, "selector": 1.5, "aggregator": 0.0}
SHARD_NAMES = ("primary", "specialist", "community")


def read_json(relative, offline=False):
    path = ROOT / relative
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    if offline:
        raise FileNotFoundError("offline index missing: " + str(path))
    with urllib.request.urlopen(BASE + relative, timeout=25) as response:
        raw = response.read(2_500_001)
    if len(raw) > 2_500_000:
        raise ValueError("index shard too large")
    return json.loads(raw)


def load_index(offline=False):
    manifest = read_json("index/manifest.json", offline=offline)
    records = []
    curated = read_json("catalog.json", offline=offline)
    reviewed = {(x["repo"].lower(), x.get("source_path")): x
                for x in curated.get("skills", []) if x.get("source_path")}
    for shard in manifest["shards"]:
        data = read_json(shard["path"], offline=offline)
        repositories = data["repositories"]
        for rid, path, sha, slug in data["entries"]:
            if rid < 0 or rid >= len(repositories):
                raise ValueError("invalid source index")
            source = repositories[rid]
            known = reviewed.get((source["repo"].lower(), path))
            records.append({
                "name": known["skill"] if known else slug, "path": path, "sha": sha,
                "repo": source["repo"], "tier": source["tier"],
                "purpose": known.get("purpose", "") if known else "",
                "index_status": "skill_file_inspected" if known else "path_indexed_unreviewed",
            })
    if len(records) != manifest["total_paths"]:
        raise ValueError(f"index length mismatch: {len(records)} vs {manifest['total_paths']}")
    return manifest, records


def words(value):
    value = re.sub(r"([a-z])([A-Z])", r"\1 \2", value)
    return [x for x in re.findall(r"[a-z0-9]+", value.lower()) if len(x) > 1 and x not in STOP]


def query_words(query, role=None):
    original = words(query)
    expanded = list(original)
    for token in original:
        expanded.extend(words(ALIAS.get(token, "")))
    if role:
        expanded.extend(words(ROLES.get(role, "")))
    return list(dict.fromkeys(expanded)), set(original)


def score_entry(entry, query, tokens, essential, role=None):
    name = entry["name"].replace("_", "-").lower()
    path = entry["path"].lower()
    repo = entry["repo"].lower()
    name_tokens = set(words(name))
    path_tokens = set(words(path))
    repo_tokens = set(words(repo))
    purpose_tokens = set(words(entry.get("purpose", "")))
    matched_original = essential & (name_tokens | path_tokens | repo_tokens | purpose_tokens)
    if essential and not matched_original:
        # Allow role-suitable candidates only when a meaningful expansion matches.
        if not role or not set(tokens).intersection(name_tokens | path_tokens):
            return 0.0, []
    match = []
    value = TRUST.get(entry["tier"], 0)
    for token in tokens:
        if token in name_tokens:
            value += 5.0 if token in essential else 2.1
            match.append(token)
        elif token in path_tokens:
            value += 1.9 if token in essential else 0.65
            match.append(token)
        elif token in purpose_tokens:
            value += 1.35 if token in essential else 0.45
            match.append(token)
        elif token in repo_tokens:
            value += 0.55
    for word in essential:
        if name == word or name.replace("-", " ") == query.strip().lower():
            value += 7.0
    if role:
        role_words = set(words(ROLES.get(role, "")))
        value += min(3, len(role_words.intersection(name_tokens)) * 1.25)
    if entry.get("index_status") == "skill_file_inspected":
        value += 2.0
    # Favor specific skill names over catch-all lists and descriptive directory paths.
    value -= max(0, len(path_tokens) - 8) * 0.04
    return value if match else 0.0, list(dict.fromkeys(match))


def search(records, query, top=5, role=None, include_aggregators=False):
    tokens, essential = query_words(query, role)
    results = []
    for entry in records:
        if not include_aggregators and entry["tier"] == "aggregator":
            continue
        score, match = score_entry(entry, query, tokens, essential, role)
        if score <= 0:
            continue
        results.append({**entry, "score": round(score, 2), "matches": match,
                        "source_url": "https://github.com/" + entry["repo"] + "/blob/main/" + entry["path"]})
    results.sort(key=lambda x: (-x["score"], -TRUST.get(x["tier"], 0), len(x["path"]), x["repo"]))
    unique_sha = set()
    deduped = []
    for item in results:
        if item["sha"] in unique_sha:
            continue
        unique_sha.add(item["sha"])
        deduped.append(item)
        if len(deduped) >= top:
            break
    return deduped


def main(argv=None):
    parser = argparse.ArgumentParser(description="Find relevant upstream skills without loading their bodies")
    parser.add_argument("query", nargs="*", help="task description or skill keywords")
    parser.add_argument("--role", choices=sorted(ROLES), help="optional domain context to improve ranking")
    parser.add_argument("--top", type=int, default=5, help="how many candidates to return, default five")
    parser.add_argument("--include-aggregators", action="store_true", help="also search large mirrored community libraries")
    parser.add_argument("--offline", action="store_true", help="do not fetch missing index shards")
    parser.add_argument("--json", action="store_true", help="machine-readable compact output")
    parser.add_argument("--stats", action="store_true", help="show index size and data quality")
    args = parser.parse_args(argv)
    if not 1 <= args.top <= 20:
        parser.error("--top must be 1..20; loading dozens of skills at once is discouraged")
    try:
        manifest, records = load_index(offline=args.offline)
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        print("Index unavailable: " + str(exc), file=sys.stderr)
        return 2
    if args.stats:
        print(json.dumps({"paths": len(records), "unique_blob_shas": manifest["unique_blob_shas"],
                          "repositories": sum(x["repos"] for x in manifest["shards"]),
                          "note": "paths indexed, source contents not individually audited"}, indent=2))
        return 0
    query = " ".join(args.query).strip()
    if not query:
        parser.error("provide a specific task or use --stats")
    found = search(records, query, top=args.top, role=args.role, include_aggregators=args.include_aggregators)
    if args.json:
        print(json.dumps({"query": query, "count": len(found), "note": "inspect before install", "results": found}, indent=2))
        return 0
    print(f"Top {len(found)} candidates for {query!r}, chosen from an index of {len(records)} skill paths:")
    for n, x in enumerate(found, 1):
        print(f"{n}. {x['name']} [{x['tier']}, {x['score']:.1f}, {x['index_status']}]\n"
              f"   {x['source_url']}\n"
              f"   matched: {', '.join(x['matches'])}")
        if x["index_status"] == "skill_file_inspected":
            print(f"   after approval: npx skills add {x['repo']} --skill {x['name']}")
        else:
            print("   Inspect SKILL.md frontmatter and scripts first; folder name may not be install name.")
    print("These are index-level recommendations, NOT a license, security or compatibility audit.")
    print("Review the actual SKILL.md and its scripts; install only what the task requires.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
