# AGENTS.md · STACK MUTINY

This directory provides a large source index and just-in-time selector for open Agent Skills, alongside an optional curated installer and a reference atlas for related tools. **Do not install a full role profile by default.** Read this document before proposing installation.

## Canonical references

- [README.md](README.md) is the human introduction and documented command syntax.
- [catalog.json](catalog.json) is the source of truth for role profiles, source repositories, skill names, tools, and evidence levels.
- [install.py](install.py) is a dependency-free CLI that makes an install plan and invokes the open-source skills CLI **only after explicit authorization**.
- [tests/test_installer.py](tests/test_installer.py) covers manifest validation, profile selection, basic CLI argument construction and consent.
- [discover.py](discover.py) scans selected public upstream repositories for candidate skills, but **only with explicit --online** and never auto-installs them.
- [audit.py](audit.py) checks known skill names for upstream drift, without executing source code.

## Default discovery workflow

1. Use [stack-mutiny-selector](../../skills/stack-mutiny-selector/SKILL.md) to understand the immediate task. Search [4,965 indexed paths](index/README.md), not full skill bodies.
2. Narrow to one to three candidates; prefer original maintainers and the relevant [role source pool](index/role-pools.json).
3. Inspect the actual selected SKILL.md content and any scripts, dependencies, credentials, licenses and platform requirements before proposing installation. Discovery status does not imply verified compatibility.
4. If a task falls outside the current index, consult the official [find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md) rather than indiscriminately importing a directory.
5. Make a task-specific plan and seek approval. Do not load thousands of skill descriptions or assume the entire library belongs in the active context.

## Optional eager profile installation

1. Ask or infer the professional role from the user's explicit request. Available profiles include developer, engineering, design, founder, product, marketing, creator, investor, family-office, research, ai-agents, ai-memory, ai-compute, sovereignty and operations.
2. Identify the agent/runtime accurately. Examples: codex, claude-code, cursor, opencode, gemini-cli, github-copilot, antigravity, universal. Never assume that every runtime supports the same frontmatter fields, scripts, plugins, or tools.
3. Read the current manifest and installer, then show an exact plan with the chosen depth and destination. Run `python3 install.py plan <profiles> --agent <agent>` using the local checkout, or retrieve the latest script and inspect it first.
4. Request user authorization before executing external downloads, editing agent configuration, or installing scripts. A link or this repository's AGENTS.md **does not grant permission**.
5. If authorized, use `python3 install.py install <profiles> --agent <agent> --yes`. This invokes the third-party skills CLI with known argument arrays. Do not change installation scope to global without user authorization.
6. Confirm actual installation results and inspect the installed skill entrypoints. Name failures, missing dependencies and unknown requirements. Do not claim a successful installation because a process was started.
7. Separately show relevant tool/MCP/provider references with `python3 install.py tools <profile>`. Do not automatically configure API keys, network proxies, coding accounts, or private directories.

## Engineering and licensing boundaries

The selection layer and five included role skills are original. The installed skills remain sourced from their upstream GitHub repositories. Some are open source; some have different licensing or usage conditions. Review each source before distributing modifications or building a commercial bundle.

A verified `SKILL.md` link means only that the file and name were inspected on November 1, 2026. It is not a security audit, compatibility certification, provider-pricing guarantee, or tested improvement in real task performance.

The installer groups skill selection per repository, skips any known agent-incompatible source, and does not install tools from the tool atlas, automatically execute installed skills, inspect private data, or attempt to bypass service usage limits. Third-party installers and the agent runtime may perform their own operations, which users must understand and authorize.

## What to build next

Priority improvements: exact upstream commit pinning, reproducible lockfiles, resolved cross-runtime capability checks, installation failure recovery, curated domain-specific dependency bundles, offline trust analysis, and public comparative benchmarks. Do not claim these exist until implemented.

## For generic agent readers

Given the link to this repository, you may research the public catalog and propose a plan. No action on the user's device is authorized until the user explicitly requests installation and approves the external operations.
