#!/usr/bin/env python3
"""Offline structural checks for the Composable Internet catalog.

No network calls, third-party code execution, or dependency installation.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "compositions.json"
README = ROOT / "README.md"
REQUIRED = {
    "id", "slug", "title", "category", "outcome", "audience",
    "components", "original_glue", "demonstration", "effort",
    "priority", "implementation_status", "last_editorial_review",
}
STATUSES = {"concept_not_integrated", "proof_of_concept", "working_release", "field_validated"}
errors = []

try:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    text = README.read_text(encoding="utf-8")
except (OSError, ValueError) as exc:
    print(f"Catalog read failed: {exc}", file=sys.stderr)
    sys.exit(1)

entries = data.get("recipes")
if not isinstance(entries, list) or not entries:
    errors.append("recipes must be a nonempty array")
    entries = []

ids, slugs = set(), set()
for number, item in enumerate(entries, 1):
    if not isinstance(item, dict):
        errors.append(f"entry #{number} is not an object")
        continue
    missing = REQUIRED - item.keys()
    if missing:
        errors.append(f"entry #{number} missing {', '.join(sorted(missing))}")
        continue
    ident, slug = item["id"], item["slug"]
    if not isinstance(ident, str) or not re.fullmatch(r"C\d{2,3}", ident):
        errors.append(f"entry #{number} invalid id")
    if ident in ids:
        errors.append(f"duplicate id {ident}")
    if slug in slugs:
        errors.append(f"duplicate slug {slug}")
    ids.add(ident)
    slugs.add(slug)
    if item["implementation_status"] not in STATUSES:
        errors.append(f"{ident} invalid implementation status")
    if item["effort"] not in {"S", "M", "L"}:
        errors.append(f"{ident} invalid effort")
    if item["priority"] not in {"immediate", "next", "research"}:
        errors.append(f"{ident} invalid priority")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", item["last_editorial_review"]):
        errors.append(f"{ident} invalid review date")
    for field in ("title", "category", "outcome", "audience", "original_glue", "demonstration"):
        if not isinstance(item[field], str) or not item[field].strip():
            errors.append(f"{ident} missing text field {field}")
    components = item["components"]
    if not isinstance(components, list) or len(components) < 2:
        errors.append(f"{ident} requires at least two components")
    else:
        seen = set()
        for component in components:
            if not isinstance(component, dict) or not component.get("name") or not component.get("url", "").startswith("https://"):
                errors.append(f"{ident} has malformed source")
                continue
            if component["url"] in seen:
                errors.append(f"{ident} has duplicate source URL")
            seen.add(component["url"])
    if f"#### {ident} · {item['title']}" not in text:
        errors.append(f"{ident} missing from human-readable README")

if data.get("schema_version") != "1.0.0":
    errors.append("unsupported catalog schema version")
if len(entries) != len(ids):
    errors.append("recipe count does not match unique IDs")
if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(entries)} composition records, unique IDs, linked sources and README entries.")
