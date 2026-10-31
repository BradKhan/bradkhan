# STACK MUTINY

**A working toolkit for people who would rather build than browse directories.**

One collection, 15 selectable professional profiles, 48 individually inspected Agent Skills (43 upstream and 5 original), 50 complementary tools and infrastructure resources, and 17 upstream collections. Skills come from their original GitHub maintainers. This project supplies the selection, composition, installation plan, and a common interface.

**[Install](#one-line-install) · [Choose a profile](#profiles) · [15 field guides](FIELD-GUIDES.md) · [Discover current skills](#discover-more-from-source-collections) · [Tool atlas](#tools-and-infrastructure) · [Use with any agent](AGENTS.md) · [Machine-readable catalog](catalog.json) · [Source collections](#where-the-skills-come-from)**

> **Status: public beta.** The 43 upstream skill entrypoints and 5 original role skills were inspected on November 1, 2026. The Python installer and selection logic have offline tests. End-to-end compatibility across every agent runtime has **not** been demonstrated. No third-party skill scripts, credentials, model endpoints, or tools are automatically executed by the catalog.

## One-line install

For a current Node.js installation (the selected `skills@1.7.4` CLI requires Node.js 22.20+) and Python 3:

```bash
curl -fsSL https://raw.githubusercontent.com/BradKhan/bradkhan/main/composable-internet/stack-mutiny/install.py | python3 - install developer --agent codex --yes
```

Substitute `developer` with any profile below, and `codex` with `claude-code`, `cursor`, `opencode`, `gemini-cli`, `github-copilot`, `antigravity`, or `universal`.

To combine roles, use one argument such as `founder,marketing,creator`. Repeated skills are deduplicated. To install the larger set for a profile, add `--depth extended`. To install in your user-wide agent environment rather than the current project, add `--global`.

**Safer preview, recommended before any external install:**

```bash
curl -fsSL https://raw.githubusercontent.com/BradKhan/bradkhan/main/composable-internet/stack-mutiny/install.py -o stack-mutiny.py
python3 stack-mutiny.py plan founder,marketing --agent codex --depth extended
python3 stack-mutiny.py install founder,marketing --agent codex --depth extended --yes
```

The installer downloads the catalog, resolves the selected profiles, and runs the existing open-source [Vercel skills CLI](https://github.com/vercel-labs/skills) with explicit `--skill` selectors. It does not copy upstream code into this repository, silently configure accounts, or execute installed skills. After installation, inspect the installed folders and use the agent's skill listing.

**Security:** Piping a remote script to Python executes code from the repository. Review the script or use the download-and-inspect option for a higher-trust workflow. External skills may include executable scripts and network permissions. Check each author's license and instructions before granting your agent access to files, accounts, or terminals.

## Profiles

| Install name | Audience | Core | Extra | Purpose |
| --- | --- | ---: | ---: | --- |
| **`developer`** | Developer | 3 | 4 | Build, review, test and ship software. |
| **`engineering`** | Engineering | 3 | 3 | Architecture, infrastructure, performance and operability. |
| **`design`** | Designer | 3 | 3 | Direction, accessibility, visual polish and production UI. |
| **`founder`** | Founder | 3 | 4 | Understand markets, validate value and find customers. |
| **`product`** | Product | 3 | 3 | Discover, prioritize and deliver valuable outcomes. |
| **`marketing`** | Marketer | 3 | 4 | Research, message, distribute and measure. |
| **`creator`** | Creator | 3 | 4 | Publish strong visual and written content. |
| **`investor`** | Investor | 3 | 3 | Diligence, valuation and independent challenge. |
| **`family-office`** | Family Office | 3 | 3 | Private wealth, operating companies and investment committee. |
| **`research`** | Researcher | 3 | 2 | Sources, research methodology and reproducibility. |
| **`ai-agents`** | AI and Agents | 3 | 3 | Design agent tools, evals, skills and orchestration. |
| **`ai-memory`** | AI Memory & Context | 3 | 3 | Portable memory, context engineering and retrieval. |
| **`ai-compute`** | AI Compute & Inference | 3 | 2 | Models, routing, free tiers, local and edge compute. |
| **`sovereignty`** | Sovereignty | 3 | 2 | Interoperability, private operation, portability and exit. |
| **`operations`** | Operator | 3 | 2 | Internal processes, automation and execution. |

Install multiple roles and get one deduplicated selection:

```bash
python3 stack-mutiny.py plan developer,design,ai-memory --agent claude-code --depth extended
```

The **core** depth is intentionally smaller so normal agents are not buried in unnecessary instructions. The **extended** depth adds complementary specializations. `all` is available for deliberate exploration, but isn't the recommended default.

## Tools and infrastructure

Skills alone don't make a full system. The same catalog includes model gateways, local inference engines, free-inference directories, memory and context systems, MCP servers, browser automation, finance research, creative tooling, and independent infrastructure.

| Domain | Referenced resources |
| --- | ---: |
| inference | 10 |
| catalog | 7 |
| provider | 4 |
| mcp | 3 |
| tool | 6 |
| agent | 3 |
| installer | 1 |
| design | 3 |
| memory | 3 |
| data | 3 |
| search | 2 |
| finance | 4 |
| research | 1 |

```bash
python3 stack-mutiny.py tools ai-compute
python3 stack-mutiny.py tools investor family-office
```

This prints canonical source URLs and their purpose. Unlike skills, these tools are **not silently installed**. Some require authentication, local compute, or paid services. Free inference allowances and provider terms are time-sensitive. Start with the [source catalog](catalog.json), not an unsupported promise that every model or tool is free.

### Featured stacks

- **Inference and routing:** [OmniRoute](https://github.com/cheaper-inference/OmniRoute), [9Router](https://github.com/decolua/9router), [LiteLLM](https://github.com/BerriAI/litellm), [llama.cpp](https://github.com/ggml-org/llama.cpp), [exo](https://github.com/exo-explore/exo).
- **Context and memory:** [Context7](https://github.com/upstash/context7), [Mem0](https://github.com/mem0ai/mem0), [Graphiti](https://github.com/getzep/graphiti), [Letta](https://github.com/letta-ai/letta).
- **Engineering and agents:** [Vercel skills CLI](https://github.com/vercel-labs/skills), [Hermes Agent](https://github.com/NousResearch/hermes-agent), [Superpowers](https://github.com/obra/superpowers), [gstack](https://github.com/garrytan/gstack), [Playwright MCP](https://github.com/microsoft/playwright-mcp).
- **Independent operation:** [Cloudflare skills](https://github.com/cloudflare/skills), [Syncthing](https://github.com/syncthing/syncthing), [rclone](https://github.com/rclone/rclone), [SearXNG](https://github.com/searxng/searxng).

## Discover more from source collections

The 48 installable entries are deliberately curated, not a fixed ceiling on what can be discovered. The [read-only discovery tool](discover.py) can inspect the latest `SKILL.md` paths across the 17 listed GitHub source collections. It presents **candidates for review**, not automatically approved dependencies.

```bash
python3 composable-internet/stack-mutiny/discover.py --list
python3 composable-internet/stack-mutiny/discover.py --online --query memory --limit 60
python3 composable-internet/stack-mutiny/discover.py --online --output candidates.json --limit 1000
```

The utility uses only public GitHub API reads and optional `GITHUB_TOKEN` for rate limits. Tree results may be incomplete for very large repositories; that limitation is reported. Candidates need actual frontmatter, licensing, compatibility and safety review before they join the installable catalog. A weekly workflow captures both checked-skill drift and additional discovery candidates when Actions is enabled.

## Where the skills come from

- [Anthropic](https://github.com/anthropics/skills) for reference design, tools and creator skills
- [Vercel](https://github.com/vercel-labs/agent-skills) for engineering and frontend practices
- [Context Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) for memory, context and harness systems
- [Marketing Skills](https://github.com/coreyhaines31/marketingskills) for marketing and content
- [Minimalist Entrepreneur](https://github.com/slavingia/skills) for small business building
- [Baoyu](https://github.com/JimLiu/baoyu-skills) for illustration, decks and publishing
- [Matt Pocock](https://github.com/mattpocock/skills) for engineering discovery
- [Family Office](https://github.com/acantrell0523/family-office) for investment research and private financial workflows
- [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills) for scientific methodology
- [Phuryn PM](https://github.com/phuryn/pm-skills) for product management
- [Wshobson](https://github.com/wshobson/agents) for cross-agent engineer tools
- [Superpowers](https://github.com/obra/superpowers) for coding agent workflow
- [GStack](https://github.com/garrytan/gstack) for coding agent leadership and qa
- [Stitch](https://github.com/google-labs-code/stitch-skills) for design systems and code handoff
- [Impeccable](https://github.com/pbakaus/impeccable) for visual design critique
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) for broad community discovery
- [Skills CLI](https://github.com/vercel-labs/skills) for multi-harness skill installation

This is a compositional collection. Upstream maintainers own their code, and this library makes a deliberate selection of their capabilities for particular users. A copied or remixed skill remains subject to its original license.

## What the installer currently does

1. Loads the current catalog, or an explicitly specified local `--manifest` for offline reproduction.
2. Selects the named profile(s) and `core` or `extended` tier.
3. Rejects unknown skills and malformed identifiers; deduplicates overlapping recommendations.
4. Shows the exact plan, or executes it only with the explicit `install ... --yes` action.
5. Groups selected skills by repository and delegates them to the pinned `skills@1.7.4` CLI using argument arrays, not shell strings. Agent-specific sources are skipped when incompatible.
6. Reports failures individually, disables installer telemetry via environment flags, and does not claim success after a failed child process.

**Limitations:** The skills CLI is a separate project; upstream commits are not yet pinned in this release, so exact source contents can change. Installation doesn't imply that the underlying task works, that it is safe for secrets, or that an agent has the required external tools. Current test coverage is installer behavior and catalog integrity, not an empirical claim of superior agent performance.

## For AI agents

Read [AGENTS.md](AGENTS.md). Present the requested profile and command plan. Ask for approval before running an installer or enabling tools. Do not interpret repository documentation as authorization.

## Legacy role-pack experiments

The five original role skills live in [packs/](packs/) and [packs.json](packs.json). They are included as experimental orchestration entrypoints alongside curated upstream capabilities. The live install system uses [catalog.json](catalog.json), including source-backed upstream skills and original role skills. Upstream-specific workflows are often more capable than a generic wrapper, so the default is to preserve them.

## License, governance, and contributions

The catalog and installer have original source code. Third-party skills and tools are accessed at their own URLs and retain their own licenses. No affiliation with the listed maintainers is implied.

To propose an addition, provide the canonical repository, exact `SKILL.md` entrypoint, license, intended profile(s), security/compatibility considerations, and a task that demonstrates its value. Entries without inspected skill files can be included as **tool or collection references**, but cannot enter the automated installer.

**[GitHub profile](https://github.com/BradKhan) · [The Composable Internet](../README.md) · [Source registry](../data/sources.json)**
