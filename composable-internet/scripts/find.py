#!/usr/bin/env python3
"""Search the Composable Internet research records without a model or account.

Examples:
  python3 composable-internet/scripts/find.py memory
  python3 composable-internet/scripts/find.py --kind sources --domain 'AI and agents' skill
  python3 composable-internet/scripts/find.py --json --limit 5 privacy
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description="Find component references and proposed compositions")
parser.add_argument("query", nargs="*", help="Keywords, matched case-insensitively")
parser.add_argument("--kind", choices=["all", "sources", "compositions"], default="all")
parser.add_argument("--domain", default="", help="Exact name of a published taxonomy domain")
parser.add_argument("--json", action="store_true", help="Print machine-readable matching records")
parser.add_argument("--limit", type=int, default=20)
args = parser.parse_args()

if args.limit < 1 or args.limit > 500:
    parser.error("--limit must be between 1 and 500")

source = json.loads((ROOT / "data" / "sources.json").read_text(encoding="utf-8"))
comp = json.loads((ROOT / "data" / "compositions.json").read_text(encoding="utf-8"))
wanted = [x.casefold() for x in args.query]
result = []

if args.kind != "compositions":
    for s in source["sources"]:
        result.append({"kind": "source", **s})
if args.kind != "sources":
    for c in comp["recipes"]:
        result.append({"kind": "composition", **c})

def searchable(item):
    fields = ["name", "title", "domain", "category", "why", "outcome", "audience",
              "original_glue", "demonstration", "subtopic", "slug"]
    value = " ".join(str(item.get(k, "")) for k in fields)
    if item["kind"] == "composition":
        value += " " + " ".join(p["name"] for p in item["components"])
    return value.casefold()

result = [s for s in result if (not args.domain or s.get("domain", s.get("category")) == args.domain)
          and all(q in searchable(s) for q in wanted)]
result = result[:args.limit]

if args.json:
    print(json.dumps({"count": len(result), "results": result}, indent=2, ensure_ascii=False))
else:
    for item in result:
        if item["kind"] == "source":
            print(f"SOURCE | {item['name']} | {item['domain']} | {item['url']}")
        else:
            print(f"{item['id']} | {item['title']} | {item['category']} | {item['outcome']}")
    if not result:
        print("No matching entries.")
