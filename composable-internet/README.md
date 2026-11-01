# The Composable Internet

**Most of the hard technology already exists. What happens when we put the right pieces together?**

An open field guide to **recomposing existing software into capabilities people can actually use**. By [Brad Khan](https://github.com/BradKhan), systems entrepreneur, technologist, and philosopher.

[**Source library**](SOURCES.md) · [**STACK MUTINY**](stack-mutiny/README.md) · [**Compositions**](#compositions-by-outcome) · [**Build queue**](BUILD-QUEUE.md) · [**Quality gates**](QUALITY-GATES.md) · [**Methods**](METHOD.md) · [**Structured data**](data/compositions.json) · [**For agents**](AGENTS.md)

> **Publication status:** This is an attributed research collection, not a gallery of completed products. All 24 compositions are conceptual. Ingredient links are starting points, not endorsements or proof of compatibility. The difference between an idea, proof of concept, and working release must remain visible.

## A practical new branch: STACK MUTINY

**[STACK MUTINY](stack-mutiny/README.md)** now provides an indexed, task-selectable skills ecosystem: 4,965 GitHub-tree-confirmed SKILL.md paths from 33 source repositories, searchable through 15 role-specific pools. [A single selector skill](../skills/stack-mutiny-selector/SKILL.md) helps an agent choose and inspect a small number of relevant capabilities, rather than loading an entire directory. The earlier 48-skill inspected set and five original orchestration workflows remain available. The larger index has *not* been individually license, security, or runtime audited.

## How to use this atlas

**Find the tools.** Use the [source library](SOURCES.md) to navigate existing projects, saved research references, and curated collections. Some leads require further verification before use.

**Find the combination.** Each composition identifies a practical outcome, real source projects, the missing product layer, and a small demonstrable result.

**Build it.** The [build queue](BUILD-QUEUE.md) sets low-effort first releases and evidence requirements. No outside project is represented as our own.

## Eight useful areas

| Domain | Question | Concepts |
| --- | --- | ---: |
| [Personal autonomy](#personal-autonomy) | Recover, control and move personal data, context and digital resources. | 7 |
| [AI and agents](#ai-and-agents) | Use, evaluate and constrain agent capabilities and inference. | 4 |
| [Independent infrastructure](#independent-infrastructure) | Run capable software on hardware and networks people can control. | 1 |
| [Creative technology](#creative-technology) | Combine visual, media and developer tools into experiences worth sharing. | 4 |
| [Venture and markets](#venture-and-markets) | Find, evaluate and build useful products and independent economic capacity. | 2 |
| [Independent publishing](#independent-publishing) | Control channels and sources of information and creative distribution. | 2 |
| [Public knowledge](#public-knowledge) | Make public claims, records and knowledge inspectable. | 3 |
| [Collective infrastructure](#collective-infrastructure) | Help independent groups coordinate and operate their own tools. | 1 |

## Compositions by outcome

### Personal autonomy

Recover, control and move personal data, context and digital resources.

#### C01 · Research Trails

**Find the thing you saw months ago, including the research trail that led to it.**

- **For:** Researchers, students, founders.
- **Study:** [browser-history](https://github.com/browser-history/browser-history) · [hister](https://github.com/asciimoo/hister) · [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox).
- **What we'd build:** Import, normalize and time-group visits; show source-grounded research sessions; exclude sensitive domains.
- **Proof:** Recover one forgotten article and its surrounding tabs.
- **Scope:** S complexity · **Concept only, integration not verified**.

#### C02 · Saved Into Action

**Turn forgotten social saves into usable collections such as recipes, tutorials and trips.**

- **For:** Creators, travelers, ordinary users.
- **Study:** [linkosh](https://github.com/sabyasachi/linkosh) · [whisper.cpp](https://github.com/ggml-org/whisper.cpp) · [maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js).
- **What we'd build:** Import permitted saved-content records; route by intent; preserve original links and uncertainty.
- **Proof:** Convert ten saved travel posts into an editable map.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C03 · Exit Audit

**Know exactly what you'll keep and lose when moving a library out of a cloud platform.**

- **For:** Consumers, privacy advocates.
- **Study:** [immich-go](https://github.com/simulot/immich-go) · [immich](https://github.com/immich-app/immich) · [rclone](https://github.com/rclone/rclone).
- **What we'd build:** Make an export inventory, preview import fidelity, verify counts and metadata after migration.
- **Proof:** A Google Photos Takeout-to-Immich migration report with mismatches.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C10 · Your Data, Explained

**Explore what account exports actually contain and what they do not.**

- **For:** General consumers, researchers.
- **Study:** [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) · [linkosh](https://github.com/sabyasachi/linkosh) · [portable-memory](https://github.com/MacPaw/portable-memory).
- **What we'd build:** Parse supported exports locally; present a plain-language inventory and data caveats.
- **Proof:** Explore one export without sending private content to a server.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C11 · AI Memory Suitcase

**Take selected context between assistants without bringing along your entire history.**

- **For:** AI power users, developer tools.
- **Study:** [portable-memory](https://github.com/MacPaw/portable-memory) · [mem0](https://github.com/mem0ai/mem0) · [openfga](https://github.com/openfga/openfga).
- **What we'd build:** Implement selective context packs, provenance, and explicit recipient permissions; document limitations of revocation.
- **Proof:** Switch between two compatible assistants using an approved context pack.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C17 · Software Exit Guide

**Discover open replacements for a proprietary workflow and estimate migration friction.**

- **For:** Small businesses, privacy-conscious users.
- **Study:** [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) · [rclone](https://github.com/rclone/rclone) · [restic](https://github.com/restic/restic).
- **What we'd build:** Turn lists into task-oriented migration plans, with backups and explicit unsupported features.
- **Proof:** A migration path for one common document workflow.
- **Scope:** S complexity · **Concept only, integration not verified**.

#### C23 · Independent Search Starter

**Install a useful private search experience without configuring five servers.**

- **For:** Privacy enthusiasts, small teams.
- **Study:** [searxng](https://github.com/searxng/searxng) · [Perplexica](https://github.com/ItzCrazyKns/Perplexica) · [llama.cpp](https://github.com/ggml-org/llama.cpp).
- **What we'd build:** Create a supported single-machine deployment and provider-independent model configuration.
- **Proof:** Run private metasearch with optional local summarization.
- **Scope:** M complexity · **Concept only, integration not verified**.

### AI and agents

Use, evaluate and constrain agent capabilities and inference.

#### C04 · Skill Safety Passport

**A human-readable safety and compatibility card for installable AI agent skills.**

- **For:** Agent users, maintainers.
- **Study:** [agentskills](https://github.com/agentskills/agentskills) · [skillspector](https://github.com/NVIDIA/skillspector) · [servers](https://github.com/modelcontextprotocol/servers).
- **What we'd build:** Unify specification checks and security reports; never execute untrusted skills in the analyzer.
- **Proof:** A clear before-install report for three public skills.
- **Scope:** S complexity · **Concept only, integration not verified**.

#### C05 · Model Choice Lab

**Choose a model by actual task performance, latency, privacy and cost.**

- **For:** Developers, technical buyers.
- **Study:** [litellm](https://github.com/BerriAI/litellm) · [promptfoo](https://github.com/promptfoo/promptfoo) · [llmfit](https://github.com/khonello/llmfit).
- **What we'd build:** Run the same fixed tasks against configured models and export repeatable, labeled comparisons.
- **Proof:** Compare three models on one user's coding task with a traceable rubric.
- **Scope:** S complexity · **Concept only, integration not verified**.

#### C13 · No-Cloud Document Desk

**Search and transform private documents without requiring an external upload.**

- **For:** Professionals, students.
- **Study:** [kreuzberg](https://github.com/kreuzberg-dev/kreuzberg) · [llama.cpp](https://github.com/ggml-org/llama.cpp) · [sqlite](https://www.sqlite.org/).
- **What we'd build:** Use file extraction, full-text index and optional local inference; make answer sources inspectable.
- **Proof:** Find and quote a passage from a private PDF bundle offline.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C20 · Agent Receipts

**Make agent runs independently inspectable: actual actions, changes and test results.**

- **For:** Engineers, organizations.
- **Study:** [playwright](https://github.com/microsoft/playwright) · [rrweb](https://github.com/rrweb-io/rrweb) · [skillspector](https://github.com/NVIDIA/skillspector).
- **What we'd build:** Normalize tool-call and test evidence, preserve redaction controls and never fabricate a run log.
- **Proof:** Replay an agent's browser actions and inspect the resulting Git changes.
- **Scope:** M complexity · **Concept only, integration not verified**.

### Independent infrastructure

Run capable software on hardware and networks people can control.

#### C16 · Home AI Fit Test

**Show what real AI workloads a user's devices can run before they spend money.**

- **For:** Hobbyists, independent teams.
- **Study:** [llmfit](https://github.com/khonello/llmfit) · [llama.cpp](https://github.com/ggml-org/llama.cpp) · [exo](https://github.com/exo-explore/exo).
- **What we'd build:** Combine hardware inventory with model recommendations and separate multi-job scheduling from model sharding.
- **Proof:** An evidence-labeled workload compatibility report for two devices.
- **Scope:** M complexity · **Concept only, integration not verified**.

### Creative technology

Combine visual, media and developer tools into experiences worth sharing.

#### C07 · Repo Cinema

**Turn a software release into a short, art-directed before/after demonstration.**

- **For:** Independent developers, agencies.
- **Study:** [playwright](https://github.com/microsoft/playwright) · [remotion](https://github.com/remotion-dev/remotion) · [repomix](https://github.com/yamadashy/repomix).
- **What we'd build:** Use explicit demonstration scripts and verified screenshots; render shareable visuals without claiming untested functionality.
- **Proof:** A 15-second release film from a real PR.
- **Scope:** S complexity · **Concept only, integration not verified**.

#### C08 · Brand Constellation

**Show where brands converge, compete and distinguish themselves, visually and verbally.**

- **For:** Designers, founders, editors.
- **Study:** [dembrandt](https://github.com/dembrandt/dembrandt) · [playwright](https://github.com/microsoft/playwright) · [d3](https://github.com/d3/d3).
- **What we'd build:** Compare design-system data across a declared sample; annotate observed messaging and avoid claiming AI authorship.
- **Proof:** An explorable cluster of 20 websites with transparent methodology.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C12 · Local Media Desk

**Turn a recording into transcripts, clips, captions and structured notes on your machine.**

- **For:** Educators, creators, journalists.
- **Study:** [whisper.cpp](https://github.com/ggml-org/whisper.cpp) · [FFmpeg](https://github.com/FFmpeg/FFmpeg) · [remotion](https://github.com/remotion-dev/remotion).
- **What we'd build:** Build a single-use workflow around existing encoders and speech tools; disclose hardware needs.
- **Proof:** A recorded interview becomes transcript plus three shareable clips.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C24 · One-Click Knowledge Transfer

**Move a research workspace between machines and apps, with verification.**

- **For:** Researchers, small teams.
- **Study:** [syncthing](https://github.com/syncthing/syncthing) · [restic](https://github.com/restic/restic) · [automerge](https://github.com/automerge/automerge).
- **What we'd build:** Combine structured exports, integrity checks and conflict-aware sync only where needed.
- **Proof:** Resume a research workspace on another machine, with matching records.
- **Scope:** M complexity · **Concept only, integration not verified**.

### Venture and markets

Find, evaluate and build useful products and independent economic capacity.

#### C06 · Open Source Opportunity Radar

**Discover recurring unmet needs hidden inside existing software ecosystems.**

- **For:** Founders, venture studios.
- **Study:** [repos](https://github.com/ecosyste-ms) · [roadmap](https://github.com/github/roadmap) · [awesome](https://github.com/sindresorhus/awesome).
- **What we'd build:** Connect issues and releases to existing alternatives; produce cited opportunity briefs, not imaginary TAM.
- **Proof:** Three defensible opportunities in one technical domain.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C22 · Open Payment Explorer

**Compare interoperable payment networks through reproducible simulated transactions.**

- **For:** Developers, merchants.
- **Study:** [open-payments](https://github.com/interledger/open-payments) · [mojaloop](https://github.com/mojaloop) · [openpaygents](https://github.com/cyberagencyorg/openpaygents).
- **What we'd build:** Build a simulator and transparent fee/reconciliation display; never imply settlement is free or universally supported.
- **Proof:** A side-by-side simulated route showing costs, errors and reconciliation.
- **Scope:** M complexity · **Concept only, integration not verified**.

### Independent publishing

Control channels and sources of information and creative distribution.

#### C09 · Own Your Feed

**Read trusted sources and public social feeds with ranking rules you control.**

- **For:** Readers, journalists, creators.
- **Study:** [RSSHub](https://github.com/DIYgod/RSSHub) · [FreshRSS](https://github.com/FreshRSS/FreshRSS) · [feed-generator](https://github.com/bluesky-social/feed-generator).
- **What we'd build:** Expose user-editable ordering and discovery rules; support reliable feeds before unstable platform adapters.
- **Proof:** Publish and share a portable feed recipe.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C14 · Personal Publishing Switch

**Publish to your own domain first, then distribute compatible content across networks.**

- **For:** Writers, communities.
- **Study:** [indiekit](https://github.com/getindiekit/indiekit) · [eleventy](https://github.com/11ty/eleventy) · [atproto](https://github.com/bluesky-social/atproto).
- **What we'd build:** Provide a guided ownership-first publishing setup with reusable content export.
- **Proof:** Publish one post to a personal site and a supported social channel.
- **Scope:** M complexity · **Concept only, integration not verified**.

### Public knowledge

Make public claims, records and knowledge inspectable.

#### C15 · Website Receipts

**Prove when public product claims, policies or prices changed.**

- **For:** Journalists, consumers.
- **Study:** [changedetection.io](https://github.com/dgtlmoon/changedetection.io) · [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) · [engine](https://github.com/OpenTermsArchive/engine).
- **What we'd build:** Preserve dated snapshots and source URLs, generate careful diff reports and distinguish uncertainty.
- **Proof:** A sourced timeline of a published policy change.
- **Scope:** M complexity · **Concept only, integration not verified**.

#### C19 · Public Data Stories

**Turn open datasets into source-linked, understandable visual stories.**

- **For:** Educators, researchers, civic groups.
- **Study:** [owid-grapher](https://github.com/owid/owid-grapher) · [maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) · [d3](https://github.com/d3/d3).
- **What we'd build:** Template data sourcing, caveats and exportable interactive narratives.
- **Proof:** An animated, reproducible story from one public dataset.
- **Scope:** S complexity · **Concept only, integration not verified**.

#### C21 · Attention Receipt

**Show the outside services contacted when a page loads and explain the consequences.**

- **For:** General consumers, researchers.
- **Study:** [tracker-radar](https://github.com/duckduckgo/tracker-radar) · [playwright](https://github.com/microsoft/playwright) · [changedetection.io](https://github.com/dgtlmoon/changedetection.io).
- **What we'd build:** Capture first-party and third-party requests in an authorized browser run; explain limits without inventing tracking intentions.
- **Proof:** Compare third-party connections on two publicly accessible websites.
- **Scope:** M complexity · **Concept only, integration not verified**.

### Collective infrastructure

Help independent groups coordinate and operate their own tools.

#### C18 · Community-in-a-Box

**Give a small group a portable site, events, proposals and member resources.**

- **For:** Associations, cooperatives.
- **Study:** [decidim](https://github.com/decidim/decidim) · [eleventy](https://github.com/11ty/eleventy) · [bonfire-app](https://github.com/bonfire-networks/bonfire-app).
- **What we'd build:** Offer one constrained starter template and optional integrations instead of bundling multiple huge platforms.
- **Proof:** An independent group launches a usable public site with governance links.
- **Scope:** L complexity · **Concept only, integration not verified**.

## Why this is different from an awesome list

A link collection answers *what exists*. A composition answers *what can become possible*, the work still required, and how to demonstrate it. Both are needed. So we maintain a distinct [source registry](data/sources.json) instead of treating every source as a product concept.

The strongest opportunities will eventually get executable configurations, comparison tests, demos, and public case studies. Until then, they remain precisely labeled candidates.

## Search the library locally

This repository includes a small, dependency-free search utility. It searches both the source inventory and proposed compositions, so the collection is useful without a hosted website or AI subscription.

```bash
python3 composable-internet/scripts/find.py --kind sources skill
python3 composable-internet/scripts/find.py --kind compositions research
python3 composable-internet/scripts/find.py --json --limit 5 privacy
python3 composable-internet/scripts/validate.py
```

Run these commands from the **profile repository root**. The validator checks internal structure and attribution, not third-party licenses, security, or runtime compatibility.

## Intellectual honesty

Upstream projects keep their credit. A name in our registry is not a license to copy or redistribute it. External descriptions are untrusted; permissions, costs, compatibility, maintenance, and platform terms need revalidation before implementation. Privacy-preserving defaults matter, especially for histories, social exports and agent tools. Originality belongs in the integration and product experience, not in claiming someone else's engine.

**Suggest a composition:** [Contribution guide](CONTRIBUTING.md). **Review our criteria:** [Editorial method](METHOD.md).
