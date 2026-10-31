#!/usr/bin/env python3
"""Offline checks for the public Composable Internet research catalog.

Tests provenance and internal consistency. Does NOT test external URLs, licenses,
availability, security, compatibility, integrations or real user adoption.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

BASE = Path(__file__).resolve().parents[1]
COMPOSITIONS = BASE / "data" / "compositions.json"
SOURCES = BASE / "data" / "sources.json"
README = BASE / "README.md"
SOURCES_MD = BASE / "SOURCES.md"
VALID_STATUS = {"concept_not_integrated", "proof_of_concept", "working_release", "field_validated"}
VALID_EFFORT = {"S", "M", "L"}
VALID_PRIORITY = {"immediate", "next", "research"}
REQ = {"id", "slug", "title", "category", "outcome", "audience", "components", "original_glue", "demonstration", "effort", "priority", "implementation_status", "last_editorial_review"}
ISSUES = []

def fail(msg):
    ISSUES.append(msg)

try:
    comp = json.loads(COMPOSITIONS.read_text(encoding="utf-8"))
    source = json.loads(SOURCES.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")
    source_md = SOURCES_MD.read_text(encoding="utf-8")
except (ValueError, OSError) as exc:
    sys.exit(f"Read error: {exc}")

tax = comp.get("taxonomy", [])
taxnames = [t.get("name") for t in tax if isinstance(t, dict)]
if len(taxnames) != 8 or len(taxnames) != len(set(taxnames)):
    fail("taxonomy must have exactly eight distinct named domains")

ids = set()
slugs = set()
items = comp.get("recipes", [])
for n, x in enumerate(items, 1):
    if not isinstance(x, dict):
        fail(f"record {n} not an object")
        continue
    missing = REQ - x.keys()
    if missing:
        fail(f"record {n}: missing {sorted(missing)}")
        continue
    cid = x["id"]
    if not re.fullmatch(r"C\d{2,3}", str(cid)):
        fail(f"{cid}: invalid ID")
    if cid in ids:
        fail(f"{cid}: duplicate ID")
    ids.add(cid)
    if x["slug"] in slugs:
        fail(f"{cid}: duplicate slug")
    slugs.add(x["slug"])
    if x["category"] not in taxnames:
        fail(f"{cid}: uncategorized or unknown domain")
    if x["implementation_status"] not in VALID_STATUS:
        fail(f"{cid}: invalid release status")
    if x["effort"] not in VALID_EFFORT or x["priority"] not in VALID_PRIORITY:
        fail(f"{cid}: invalid effort or priority")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(x["last_editorial_review"])):
        fail(f"{cid}: invalid editorial date")
    if f"#### {cid} · {x['title']}" not in readme:
        fail(f"{cid}: missing README entry")
    if len(x.get("components", [])) < 2:
        fail(f"{cid}: fewer than two source ingredients")
    for item in x.get("components", []):
        if not isinstance(item, dict) or not item.get("name") or not item.get("url", "").startswith("https://"):
            fail(f"{cid}: malformed ingredient")
for name in taxnames:
    if f"### {name}" not in readme or f"### {name}" not in source_md:
        fail(f"{name}: missing domain heading")

sources = source.get("sources", [])
if source.get("source_count") != len(sources):
    fail("source_count is not equal to actual array length")
if len(sources) < 1:
    fail("empty source registry")
urls = set()
for n, item in enumerate(sources, 1):
    if not isinstance(item, dict):
        fail(f"source {n}: not an object")
        continue
    url = item.get("url", "")
    if not url.startswith("https://") or not urlsplit(url).netloc:
        fail(f"source {n}: invalid URL")
    normalized = url.rstrip("/").lower()
    if normalized in urls:
        fail(f"source {n}: duplicate URL")
    urls.add(normalized)
    if item.get("domain") not in taxnames:
        fail(f"source {n}: unrecognized domain")
    if item.get("review_level") not in {"readme_inspected", "linked_in_composition", "inventory_only", "editorial_lead"}:
        fail(f"source {n}: unknown evidence level")
    if url not in source_md:
        fail(f"source {n}: missing from SOURCES.md")
    if item.get("origin") in {"personal_account_reference_authorship_not_assumed", "first_party_project"} and "github.com/BradKhan/" not in url:
        fail(f"source {n}: account provenance does not match URL")
    if item.get("origin") == "first_party_project" and "first-party project" not in source_md:
        fail(f"source {n}: first-party attribution missing from source guide")

# The profile identity is canonical. Check all published user- and agent-facing
# surfaces whenever the atlas or profile changes.
PROFILE = BASE.parent
CANONICAL_IDENTITY = "Systems Entrepreneur · Technologist · Philosopher"
try:
    profile = json.loads((PROFILE / "data" / "profile.json").read_text(encoding="utf-8"))
    identity_docs = {
        name: (PROFILE / name).read_text(encoding="utf-8")
        for name in ["README.md", "BRAND.md", "AGENTS.md", "llms.txt"]
    }
except (ValueError, OSError) as exc:
    fail(f"profile metadata or document unreadable: {exc}")
else:
    if profile.get("identity") != ["Systems Entrepreneur", "Technologist", "Philosopher"]:
        fail("profile.json identity must have three approved, distinct roles")
    if profile.get("positioning") != CANONICAL_IDENTITY:
        fail("profile.json positioning differs from approved identity")
    for name, content in identity_docs.items():
        if CANONICAL_IDENTITY not in content:
            fail(f"{name} is missing approved identity")
        if "Entrepreneurial Technologist" in content or "Intelligence Architect ·" in content:
            fail(f"{name} contains a superseded title")
    if "entrepreneurial technologist" in readme.lower():
        fail("atlas README contains superseded title")

known_first_party = {
    "https://github.com/bradkhan/bradkhan",
    "https://github.com/bradkhan/open-ass",
    "https://github.com/bradkhan/khan-aios-venture-studio-mvp-framework",
}
for source_item in sources:
    key = source_item.get("url", "").rstrip("/").lower()
    if key in known_first_party and source_item.get("origin") != "first_party_project":
        fail(f"original project incorrectly attributed: {key}")

if comp.get("schema_version") != "1.0.0" or source.get("schema_version") != "1.0.0":
    fail("unexpected schema version")
if ISSUES:
    for issue in ISSUES:
        print("ERROR:", issue, file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(items)} compositions, {len(taxnames)} domains, {len(sources)} attributed source records.")
print("NOTE: This does not establish functioning integrations, safe dependencies, or market demand.")
