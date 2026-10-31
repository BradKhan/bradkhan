#!/usr/bin/env python3
"""SKILL ISSUE: compile an original role-based skill into a portable text guide.

No network use. No third-party skill copying, downloading, installing, or execution.
The output is a local document, not a compatibility guarantee.
"""
import argparse
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


def available_packs():
    document = json.loads((BASE / "packs.json").read_text(encoding="utf-8"))
    return {entry["slug"]: entry for entry in document["packs"]}


def render(pack, target):
    original = (BASE / pack["orchestrator"]).read_text(encoding="utf-8")
    if target == "skill":
        return original
    if not original.startswith("---\n") or "\n---\n" not in original:
        raise ValueError("SKILL.md frontmatter is missing or malformed")
    _, content = original.split("\n---\n", 1)
    return (
        f"# SKILL ISSUE: {pack['title']}\n\n"
        "This is an original, experimental workflow guide for a coding agent. "
        "It does not install or execute any referenced upstream software. "
        "Read external skill files and check permissions before integrating them.\n\n"
        f"{content.strip()}\n"
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compile an original experimental role skill offline")
    parser.add_argument("pack", nargs="?", help="Pack slug, or omit with --list")
    parser.add_argument("--list", action="store_true", help="Print available pack names")
    parser.add_argument("--format", choices=["agents", "skill"], default="agents",
                        help="Output plain AGENTS-style instructions or a SKILL.md")
    parser.add_argument("--output", type=Path, help="Required path for the generated file")
    parser.add_argument("--force", action="store_true", help="Allow replacement of an existing output")
    args = parser.parse_args(argv)
    packs = available_packs()
    if args.list:
        for x in packs.values():
            print(f"{x['slug']}\t{x['title']}\t{x['audience']}")
        return 0
    if not args.pack or args.pack not in packs:
        parser.error("provide a published pack slug; use --list to see choices")
    if args.output is None:
        parser.error("an explicit --output path is required; nothing is installed automatically")
    if args.output.exists() and not args.force:
        parser.error("output exists; use --force to replace it")
    try:
        content = render(packs[args.pack], args.format)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    except (OSError, ValueError) as exc:
        print(f"Unable to compile pack: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {args.output} from {args.pack}; third-party sources were not copied or executed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
