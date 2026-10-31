#!/usr/bin/env python3
"""Stack Mutiny profile installer. Read the code before running from a URL.

'plan' is read-only. 'install' requires explicit --yes and delegates to the
independently maintained Vercel skills CLI. No subprocess uses a shell.
"""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.request

BASE = "https://raw.githubusercontent.com/BradKhan/bradkhan/main/composable-internet/stack-mutiny"
MAX_MANIFEST_BYTES = 1024 * 1024
SUPPORTED_AGENTS = ("codex", "claude-code", "cursor", "opencode", "gemini-cli", "github-copilot", "antigravity", "universal")
ID_PATTERN = re.compile(r"^[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+@[a-z0-9][a-z0-9-]*$")


def load_manifest(manifest_path=None):
    if manifest_path:
        raw = Path(manifest_path).read_bytes()
    elif (Path(__file__).resolve().parent / "catalog.json").exists():
        raw = (Path(__file__).resolve().parent / "catalog.json").read_bytes()
    else:
        req = urllib.request.Request(BASE + "/catalog.json", headers={"User-Agent": "StackMutiny/0.2"})
        with urllib.request.urlopen(req, timeout=20) as response:
            raw = response.read(MAX_MANIFEST_BYTES + 1)
    if len(raw) > MAX_MANIFEST_BYTES:
        raise ValueError("manifest exceeds 1 MiB limit")
    data = json.loads(raw)
    validate_catalog(data)
    return data


def validate_catalog(data):
    if data.get("schema_version") != "0.2" or not isinstance(data.get("skills"), list):
        raise ValueError("expected schema_version 0.2 and skills array")
    seen = set()
    for entry in data["skills"]:
        identifier = entry.get("id", "")
        if not ID_PATTERN.fullmatch(identifier) or identifier in seen:
            raise ValueError("invalid or duplicated skill identifier: " + repr(identifier))
        seen.add(identifier)
        if entry.get("verification") != "SKILL.md inspected":
            raise ValueError("installable skill lacks direct SKILL.md verification: " + identifier)
        if entry.get("repo") + "@" + entry.get("skill") != identifier:
            raise ValueError("identifier and source fields disagree: " + identifier)
    for name, profile in data.get("profiles", {}).items():
        if not re.fullmatch(r"[a-z][a-z-]*", name):
            raise ValueError("invalid profile name")
        for level in ("core", "extended"):
            for identifier in profile.get(level, []):
                if identifier not in seen:
                    raise ValueError(f"unknown {level} skill {identifier} in {name}")
    return True


def select_skills(data, names, depth):
    profiles = data["profiles"]
    if "all" in names:
        names = list(profiles)
    unknown = [x for x in names if x not in profiles]
    if unknown:
        raise ValueError("unknown profile(s): " + ", ".join(unknown))
    keys, seen = [], set()
    for name in names:
        for tier in ("core", "extended") if depth == "extended" else ("core",):
            for identifier in profiles[name].get(tier, []):
                if identifier not in seen:
                    keys.append(identifier)
                    seen.add(identifier)
    index = {entry["id"]: entry for entry in data["skills"]}
    return [index[key] for key in keys]


def build_command(item, agent, global_scope=False, cli_version="1.7.4"):
    if not re.fullmatch(r"\d+\.\d+\.\d+", cli_version):
        raise ValueError("CLI version must be pinned to a numeric release")
    items = item if isinstance(item, list) else [item]
    if not items or len({x["repo"] for x in items}) != 1:
        raise ValueError("one install command must target exactly one upstream repository")
    command = ["npx", "--yes", f"skills@{cli_version}", "add", items[0]["repo"]]
    for entry in items:
        command.extend(["--skill", entry["skill"]])
    command.extend(["-a", agent, "-y"])
    if global_scope:
        command.append("-g")
    return command


def group_by_repository(items):
    groups = {}
    for item in items:
        groups.setdefault(item["repo"], []).append(item)
    return list(groups.values())


def main(argv=None, runner=None):
    parser = argparse.ArgumentParser(description="Curated, permissioned agent-skill profiles across GitHub")
    parser.add_argument("action", choices=["list", "plan", "install", "tools", "validate"])
    parser.add_argument("profiles", nargs="*", help="e.g. developer design founder investor ai-memory")
    parser.add_argument("--depth", choices=["core", "extended"], default="core")
    parser.add_argument("--agent", choices=SUPPORTED_AGENTS, default="universal")
    parser.add_argument("--global", dest="global_scope", action="store_true")
    parser.add_argument("--yes", action="store_true", help="required to invoke the external skills CLI")
    parser.add_argument("--manifest", help="offline local JSON catalog for reproducible use")
    parser.add_argument("--cli-version", default="1.7.4", help="pinned version of the independently maintained skills CLI")
    args = parser.parse_args(argv)
    try:
        data = load_manifest(args.manifest)
        if args.action == "validate":
            print(f"VALID: {len(data['profiles'])} profiles, {len(data['skills'])} inspected skills, {len(data.get('tools', []))} tool references")
            return 0
        if args.action == "list":
            for key, item in data["profiles"].items():
                print(f"{key:18} {item['label']:27} {len(item['core']):2} core / {len(item['extended']):2} additional")
            return 0
        if args.action == "tools":
            for tool in data.get("tools", []):
                if not args.profiles or "all" in args.profiles or any(p in tool.get("profiles", []) for p in args.profiles):
                    print(f"{tool['category']:15} {tool['name']:24} {tool['url']}\n    {tool['purpose']}")
            return 0
        names = []
        for part in args.profiles:
            names.extend(x.strip() for x in part.split(",") if x.strip())
        if not names:
            parser.error("select at least one profile; see 'list'")
        selected = select_skills(data, names, args.depth)
        skipped = [item for item in selected if item.get("supported_agents") and args.agent not in item["supported_agents"]]
        selected = [item for item in selected if item not in skipped]
        print(f"Profiles: {', '.join(names)} | {args.depth} | agent={args.agent} | selected={len(selected)} | incompatible={len(skipped)}")
        for item in skipped:
            print("  ! SKIPPED (requires a different agent): " + item["id"])
        for item in selected:
            print("  + " + item["id"] + " | " + item["purpose"])
        if not selected:
            raise ValueError("no skills remain for this agent; choose another profile or agent")
        print("Tool integrations are reference-only. Use 'tools' to review their setup requirements.")
        if args.action == "plan":
            print("\nCommands that would be executed:")
            for group in group_by_repository(selected):
                print("  " + " ".join(build_command(group, args.agent, args.global_scope, args.cli_version)))
            return 0
        if not args.yes:
            print("No changes made. Re-run with --yes after reviewing the plan.", file=sys.stderr)
            return 2
        if shutil.which("npx") is None:
            print("npx not found: install a supported Node.js release (22.20+).", file=sys.stderr)
            return 2
        run = runner or subprocess.run
        env = dict(os.environ, DISABLE_TELEMETRY="1", DO_NOT_TRACK="1")
        failed = []
        for group in group_by_repository(selected):
            command = build_command(group, args.agent, args.global_scope, args.cli_version)
            print("\nInstalling from " + group[0]["repo"] + ": " + ", ".join(x["skill"] for x in group), flush=True)
            result = run(command, env=env, check=False)
            if result.returncode:
                failed.extend(x["id"] for x in group)
                print("FAILED: " + ", ".join(x["id"] for x in group), file=sys.stderr)
        if failed:
            print(f"{len(selected) - len(failed)}/{len(selected)} skills reported successful; failures: {', '.join(failed)}", file=sys.stderr)
            return 1
        print(f"Completed {len(selected)} skill installations. Restart your agent, then verify the loaded skills.")
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
