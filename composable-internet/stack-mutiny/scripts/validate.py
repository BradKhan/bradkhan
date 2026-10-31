#!/usr/bin/env python3
"""Offline structural checks for the original STACK MUTINY pack manifest."""
import json
import sys
from pathlib import Path
BASE = Path(__file__).resolve().parents[1]
manifest = json.loads((BASE / "packs.json").read_text(encoding="utf-8"))
issues=[]
if len(manifest.get("packs",[])) != 5: issues.append("Expected five packs")
slugs=set()
for pack in manifest.get("packs",[]):
    slug=pack.get("slug","")
    if slug in slugs: issues.append(f"Duplicate slug {slug}")
    slugs.add(slug)
    path=BASE / pack.get("orchestrator","")
    if not path.is_file(): issues.append(f"Missing SKILL.md: {slug}"); continue
    content=path.read_text(encoding="utf-8")
    if not content.startswith(f"---\nname: {slug}\n"): issues.append(f"Bad frontmatter: {slug}")
    if "Status: **Not tested in a live agent harness.**" not in content: issues.append(f"Missing evidence disclaimer: {slug}")
    if len(pack.get("upstream_candidates",[])) < 2: issues.append(f"Too few source candidates: {slug}")
    for ref in pack.get("upstream_candidates",[]):
        if not ref.get("url","").startswith("https://github.com/"): issues.append(f"Non-GitHub source URL: {slug}")
    if pack.get("evaluation_status") != "not_tested": issues.append(f"Unexpected tested claim: {slug}")
if issues:
    for issue in issues: print("FAIL:",issue,file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(slugs)} experimental skill packs with source links and explicit evaluation status.")
