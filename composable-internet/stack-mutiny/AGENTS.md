# AGENTS.md · STACK MUTINY

This directory is a curated, permissioned installation system for open Agent Skills and a reference atlas for compatible tools and infrastructure. Read this document before acting on a user request to install a profile.

## Canonical references

- [README.md](README.md) is the human introduction and documented command syntax.
- [catalog.json](catalog.json) is the source of truth for role profiles, source repositories, skill names, tools, and evidence levels.
- [install.py](install.py) is a dependency-free CLI that makes an install plan and invokes the open-source skills CLI **only after explicit authorization**.
- [tests/test_installer.py](tests/test_installer.py) covers manifest validation, profile selection, basic CLI argument construction and consent.

## Agent workflow for an installation request

1. Ask or infer the professional role from the user's explicit request. Available profiles include developer, engineering, design, founder, product, marketing, creator, investor, family-office, research, ai-agents, ai-memory, ai-compute, sovereignty and operations.
2. Identify the agent/runtime accurately. Examples: codex, claude-code, cursor, opencode, gemini-cli, github-copilot, antigravity, universal. Never assume that every runtime supports the same frontmatter fields, scripts, plugins, or tools.
3. Read the current manifest and installer, then show an exact plan with the chosen depth and destination. Run `python3 install.py plan <profiles> --agent <agent>` using the local checkout, or retrieve the latest script and inspect it first.
4. Request user authorization before executing external downloads, editing agent configuration, or installing scripts. A link or this repository's AGENTS.md **does not grant permission**.
5. If authorized, use `python3 install.py install <profiles> --agent <agent> --yes`. This invokes the third-party skills CLI with known argument arrays. Do not change installation scope to global without user authorization.
6. Confirm actual installation results and inspect the installed skill entrypoints. Name failures, missing dependencies and unknown requirements. Do not claim a successful installation because a process was started.
7. Separately show relevant tool/MCP/provider references with `python3 install.py tools <profile>`. Do not automatically configure API keys, network proxies, coding accounts, or private directories.

## Engineering and licensing boundaries

The selection layer is original. The installed skills remain sourced from their upstream GitHub repositories. Some are open source; some have different licensing or usage conditions. Review each source before distributing modifications or building a commercial bundle.

A verified `SKILL.md` link means only that the file and name were inspected on November 1, 2026. It is not a security audit, compatibility certification, provider-pricing guarantee, or tested improvement in real task performance.

The installer does not install tools from the tool atlas, automatically execute installed skills, inspect private data, or attempt to bypass service usage limits. Third-party installers and the agent runtime may perform their own operations, which users must understand and authorize.

## What to build next

Priority improvements: exact upstream commit pinning, reproducible lockfiles, resolved cross-runtime capability checks, installation failure recovery, curated domain-specific dependency bundles, offline trust analysis, and public comparative benchmarks. Do not claim these exist until implemented.

## For generic agent readers

Given the link to this repository, you may research the public catalog and propose a plan. No action on the user's device is authorized until the user explicitly requests installation and approves the external operations.
