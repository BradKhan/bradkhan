# The Composable Internet

> **Most of the technology already exists. The missing product is the combination.**

A field guide to software that can be assembled from existing open-source projects. Curated by **[Brad Khan](https://github.com/BradKhan)**, a systems entrepreneur, intelligence architect and philosopher working to expand human agency.

**24 original composition briefs** across AI, privacy, independent publishing, media, venture building, public research and collective technology. Each proposes a human outcome, identifies existing technical ingredients, and specifies the missing product experience.

[Browse the machine-readable catalog](data/compositions.json) · [Build queue](BUILD-QUEUE.md) · [Research and evaluation method](METHOD.md) · [Agent guide](AGENTS.md) · [Brad's GitHub profile](https://github.com/BradKhan)

> **Read this first:** These are researched *build concepts*, not 24 shipped applications. The individual ingredients exist; their proposed integrations have **not** been verified. Source links are for study and attribution, not blanket permission to copy code. We never describe a proposed integration as a tested product.

## Start with the result you want

| If you want to… | Start here |
| --- | --- |
| Recover and control your information | [Research Trails](#c01--research-trails), [Saved Into Action](#c02--saved-into-action), [Exit Audit](#c03--exit-audit) |
| Build and trust AI agents | [Skill Safety Passport](#c04--skill-safety-passport), [Model Choice Lab](#c05--model-choice-lab), [Agent Receipts](#c20--agent-receipts) |
| Turn open source into products | [Opportunity Radar](#c06--open-source-opportunity-radar), [Repo Cinema](#c07--repo-cinema) |
| Make independent software usable | [Own Your Feed](#c09--own-your-feed), [Independent Search Starter](#c23--independent-search-starter) |
| Publish something others will share | [Brand Constellation](#c08--brand-constellation), [Website Receipts](#c15--website-receipts), [Public Data Stories](#c19--public-data-stories) |

## The compositions

### Personal intelligence

#### C01 · Research Trails

**Outcome.** Find the thing you saw months ago, including the research trail that led to it.

**Audience.** Researchers, students, founders  
**Existing ingredients.** [browser-history](https://github.com/browser-history/browser-history) + [hister](https://github.com/asciimoo/hister) + [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox)  
**Missing product layer.** Import, normalize and time-group visits; show source-grounded research sessions; exclude sensitive domains.  
**First proof.** Recover one forgotten article and its surrounding tabs.  
**Estimated initial complexity.** S (S/M/L) · **Status:** concept, not integrated.

### Consumer liberation

#### C02 · Saved Into Action

**Outcome.** Turn forgotten social saves into usable collections such as recipes, tutorials and trips.

**Audience.** Creators, travelers, ordinary users  
**Existing ingredients.** [linkosh](https://github.com/sabyasachi/linkosh) + [whisper.cpp](https://github.com/ggml-org/whisper.cpp) + [maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js)  
**Missing product layer.** Import permitted saved-content records; route by intent; preserve original links and uncertainty.  
**First proof.** Convert ten saved travel posts into an editable map.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Digital independence

#### C03 · Exit Audit

**Outcome.** Know exactly what you'll keep and lose when moving a library out of a cloud platform.

**Audience.** Consumers, privacy advocates  
**Existing ingredients.** [immich-go](https://github.com/simulot/immich-go) + [immich](https://github.com/immich-app/immich) + [rclone](https://github.com/rclone/rclone)  
**Missing product layer.** Make an export inventory, preview import fidelity, verify counts and metadata after migration.  
**First proof.** A Google Photos Takeout-to-Immich migration report with mismatches.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### AI agents

#### C04 · Skill Safety Passport

**Outcome.** A human-readable safety and compatibility card for installable AI agent skills.

**Audience.** Agent users, maintainers  
**Existing ingredients.** [agentskills](https://github.com/agentskills/agentskills) + [skillspector](https://github.com/NVIDIA/skillspector) + [servers](https://github.com/modelcontextprotocol/servers)  
**Missing product layer.** Unify specification checks and security reports; never execute untrusted skills in the analyzer.  
**First proof.** A clear before-install report for three public skills.  
**Estimated initial complexity.** S (S/M/L) · **Status:** concept, not integrated.

### AI compute

#### C05 · Model Choice Lab

**Outcome.** Choose a model by actual task performance, latency, privacy and cost.

**Audience.** Developers, technical buyers  
**Existing ingredients.** [litellm](https://github.com/BerriAI/litellm) + [promptfoo](https://github.com/promptfoo/promptfoo) + [llmfit](https://github.com/khonello/llmfit)  
**Missing product layer.** Run the same fixed tasks against configured models and export repeatable, labeled comparisons.  
**First proof.** Compare three models on one user's coding task with a traceable rubric.  
**Estimated initial complexity.** S (S/M/L) · **Status:** concept, not integrated.

### Venture building

#### C06 · Open Source Opportunity Radar

**Outcome.** Discover recurring unmet needs hidden inside existing software ecosystems.

**Audience.** Founders, venture studios  
**Existing ingredients.** [repos](https://github.com/ecosyste-ms) + [roadmap](https://github.com/github/roadmap) + [awesome](https://github.com/sindresorhus/awesome)  
**Missing product layer.** Connect issues and releases to existing alternatives; produce cited opportunity briefs, not imaginary TAM.  
**First proof.** Three defensible opportunities in one technical domain.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Creative developer tools

#### C07 · Repo Cinema

**Outcome.** Turn a software release into a short, art-directed before/after demonstration.

**Audience.** Independent developers, agencies  
**Existing ingredients.** [playwright](https://github.com/microsoft/playwright) + [remotion](https://github.com/remotion-dev/remotion) + [repomix](https://github.com/yamadashy/repomix)  
**Missing product layer.** Use explicit demonstration scripts and verified screenshots; render shareable visuals without claiming untested functionality.  
**First proof.** A 15-second release film from a real PR.  
**Estimated initial complexity.** S (S/M/L) · **Status:** concept, not integrated.

### Design intelligence

#### C08 · Brand Constellation

**Outcome.** Show where brands converge, compete and distinguish themselves, visually and verbally.

**Audience.** Designers, founders, editors  
**Existing ingredients.** [dembrandt](https://github.com/dembrandt/dembrandt) + [playwright](https://github.com/microsoft/playwright) + [d3](https://github.com/d3/d3)  
**Missing product layer.** Compare design-system data across a declared sample; annotate observed messaging and avoid claiming AI authorship.  
**First proof.** An explorable cluster of 20 websites with transparent methodology.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Attention autonomy

#### C09 · Own Your Feed

**Outcome.** Read trusted sources and public social feeds with ranking rules you control.

**Audience.** Readers, journalists, creators  
**Existing ingredients.** [RSSHub](https://github.com/DIYgod/RSSHub) + [FreshRSS](https://github.com/FreshRSS/FreshRSS) + [feed-generator](https://github.com/bluesky-social/feed-generator)  
**Missing product layer.** Expose user-editable ordering and discovery rules; support reliable feeds before unstable platform adapters.  
**First proof.** Publish and share a portable feed recipe.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Personal data rights

#### C10 · Your Data, Explained

**Outcome.** Explore what account exports actually contain and what they do not.

**Audience.** General consumers, researchers  
**Existing ingredients.** [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) + [linkosh](https://github.com/sabyasachi/linkosh) + [portable-memory](https://github.com/MacPaw/portable-memory)  
**Missing product layer.** Parse supported exports locally; present a plain-language inventory and data caveats.  
**First proof.** Explore one export without sending private content to a server.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### AI interoperability

#### C11 · AI Memory Suitcase

**Outcome.** Take selected context between assistants without bringing along your entire history.

**Audience.** AI power users, developer tools  
**Existing ingredients.** [portable-memory](https://github.com/MacPaw/portable-memory) + [mem0](https://github.com/mem0ai/mem0) + [openfga](https://github.com/openfga/openfga)  
**Missing product layer.** Implement selective context packs, provenance, and explicit recipient permissions; document limitations of revocation.  
**First proof.** Switch between two compatible assistants using an approved context pack.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Creative independence

#### C12 · Local Media Desk

**Outcome.** Turn a recording into transcripts, clips, captions and structured notes on your machine.

**Audience.** Educators, creators, journalists  
**Existing ingredients.** [whisper.cpp](https://github.com/ggml-org/whisper.cpp) + [FFmpeg](https://github.com/FFmpeg/FFmpeg) + [remotion](https://github.com/remotion-dev/remotion)  
**Missing product layer.** Build a single-use workflow around existing encoders and speech tools; disclose hardware needs.  
**First proof.** A recorded interview becomes transcript plus three shareable clips.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Local AI

#### C13 · No-Cloud Document Desk

**Outcome.** Search and transform private documents without requiring an external upload.

**Audience.** Professionals, students  
**Existing ingredients.** [kreuzberg](https://github.com/kreuzberg-dev/kreuzberg) + [llama.cpp](https://github.com/ggml-org/llama.cpp) + [sqlite](https://www.sqlite.org/)  
**Missing product layer.** Use file extraction, full-text index and optional local inference; make answer sources inspectable.  
**First proof.** Find and quote a passage from a private PDF bundle offline.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Independent publishing

#### C14 · Personal Publishing Switch

**Outcome.** Publish to your own domain first, then distribute compatible content across networks.

**Audience.** Writers, communities  
**Existing ingredients.** [indiekit](https://github.com/getindiekit/indiekit) + [eleventy](https://github.com/11ty/eleventy) + [atproto](https://github.com/bluesky-social/atproto)  
**Missing product layer.** Provide a guided ownership-first publishing setup with reusable content export.  
**First proof.** Publish one post to a personal site and a supported social channel.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Public accountability

#### C15 · Website Receipts

**Outcome.** Prove when public product claims, policies or prices changed.

**Audience.** Journalists, consumers  
**Existing ingredients.** [changedetection.io](https://github.com/dgtlmoon/changedetection.io) + [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) + [engine](https://github.com/OpenTermsArchive/engine)  
**Missing product layer.** Preserve dated snapshots and source URLs, generate careful diff reports and distinguish uncertainty.  
**First proof.** A sourced timeline of a published policy change.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Affordable compute

#### C16 · Home AI Fit Test

**Outcome.** Show what real AI workloads a user's devices can run before they spend money.

**Audience.** Hobbyists, independent teams  
**Existing ingredients.** [llmfit](https://github.com/khonello/llmfit) + [llama.cpp](https://github.com/ggml-org/llama.cpp) + [exo](https://github.com/exo-explore/exo)  
**Missing product layer.** Combine hardware inventory with model recommendations and separate multi-job scheduling from model sharding.  
**First proof.** An evidence-labeled workload compatibility report for two devices.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Service independence

#### C17 · Software Exit Guide

**Outcome.** Discover open replacements for a proprietary workflow and estimate migration friction.

**Audience.** Small businesses, privacy-conscious users  
**Existing ingredients.** [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) + [rclone](https://github.com/rclone/rclone) + [restic](https://github.com/restic/restic)  
**Missing product layer.** Turn lists into task-oriented migration plans, with backups and explicit unsupported features.  
**First proof.** A migration path for one common document workflow.  
**Estimated initial complexity.** S (S/M/L) · **Status:** concept, not integrated.

### Collective autonomy

#### C18 · Community-in-a-Box

**Outcome.** Give a small group a portable site, events, proposals and member resources.

**Audience.** Associations, cooperatives  
**Existing ingredients.** [decidim](https://github.com/decidim/decidim) + [eleventy](https://github.com/11ty/eleventy) + [bonfire-app](https://github.com/bonfire-networks/bonfire-app)  
**Missing product layer.** Offer one constrained starter template and optional integrations instead of bundling multiple huge platforms.  
**First proof.** An independent group launches a usable public site with governance links.  
**Estimated initial complexity.** L (S/M/L) · **Status:** concept, not integrated.

### Civic creativity

#### C19 · Public Data Stories

**Outcome.** Turn open datasets into source-linked, understandable visual stories.

**Audience.** Educators, researchers, civic groups  
**Existing ingredients.** [owid-grapher](https://github.com/owid/owid-grapher) + [maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js) + [d3](https://github.com/d3/d3)  
**Missing product layer.** Template data sourcing, caveats and exportable interactive narratives.  
**First proof.** An animated, reproducible story from one public dataset.  
**Estimated initial complexity.** S (S/M/L) · **Status:** concept, not integrated.

### Trustworthy AI

#### C20 · Agent Receipts

**Outcome.** Make agent runs independently inspectable: actual actions, changes and test results.

**Audience.** Engineers, organizations  
**Existing ingredients.** [playwright](https://github.com/microsoft/playwright) + [rrweb](https://github.com/rrweb-io/rrweb) + [skillspector](https://github.com/NVIDIA/skillspector)  
**Missing product layer.** Normalize tool-call and test evidence, preserve redaction controls and never fabricate a run log.  
**First proof.** Replay an agent's browser actions and inspect the resulting Git changes.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Privacy and surveillance

#### C21 · Attention Receipt

**Outcome.** Show the outside services contacted when a page loads and explain the consequences.

**Audience.** General consumers, researchers  
**Existing ingredients.** [tracker-radar](https://github.com/duckduckgo/tracker-radar) + [playwright](https://github.com/microsoft/playwright) + [changedetection.io](https://github.com/dgtlmoon/changedetection.io)  
**Missing product layer.** Capture first-party and third-party requests in an authorized browser run; explain limits without inventing tracking intentions.  
**First proof.** Compare third-party connections on two publicly accessible websites.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Economic autonomy

#### C22 · Open Payment Explorer

**Outcome.** Compare interoperable payment networks through reproducible simulated transactions.

**Audience.** Developers, merchants  
**Existing ingredients.** [open-payments](https://github.com/interledger/open-payments) + [mojaloop](https://github.com/mojaloop) + [openpaygents](https://github.com/cyberagencyorg/openpaygents)  
**Missing product layer.** Build a simulator and transparent fee/reconciliation display; never imply settlement is free or universally supported.  
**First proof.** A side-by-side simulated route showing costs, errors and reconciliation.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Search autonomy

#### C23 · Independent Search Starter

**Outcome.** Install a useful private search experience without configuring five servers.

**Audience.** Privacy enthusiasts, small teams  
**Existing ingredients.** [searxng](https://github.com/searxng/searxng) + [Perplexica](https://github.com/ItzCrazyKns/Perplexica) + [llama.cpp](https://github.com/ggml-org/llama.cpp)  
**Missing product layer.** Create a supported single-machine deployment and provider-independent model configuration.  
**First proof.** Run private metasearch with optional local summarization.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

### Creator and team productivity

#### C24 · One-Click Knowledge Transfer

**Outcome.** Move a research workspace between machines and apps, with verification.

**Audience.** Researchers, small teams  
**Existing ingredients.** [syncthing](https://github.com/syncthing/syncthing) + [restic](https://github.com/restic/restic) + [automerge](https://github.com/automerge/automerge)  
**Missing product layer.** Combine structured exports, integrity checks and conflict-aware sync only where needed.  
**First proof.** Resume a research workspace on another machine, with matching records.  
**Estimated initial complexity.** M (S/M/L) · **Status:** concept, not integrated.

---

## What we value

1. **Recomposition over reinvention.** Cite the tools that already solved the hard parts.
2. **Human outcome over tool count.** An experience that saves someone ten clicks matters more than a directory of thousands of links.
3. **Freedom of exit.** Prefer portable data and replaceable providers to captive formats.
4. **Proof before promotion.** A working test, screenshot or video beats a fashionable claim.
5. **Respect the source.** Follow licenses, attribute authors, check maintenance and honor platform access boundaries.
6. **No hidden surveillance.** Don't collect people's information merely because a library makes it convenient.

**Build a composition?** Open an issue in the [profile repository](https://github.com/BradKhan/bradkhan/issues) identifying its composition ID, implementation URL, tested platforms and limitations. The eventual standalone repository will have its own contribution process.

## Status and provenance

- Initial editorial edition: **2026-11-01**.
- Each candidate's source links and integration assumptions require a fresh check before implementation.
- Some components carry copyleft, source-available or other obligations. No source has been imported or redistributed here.
- Complexity is an editorial estimate, not a measured engineering effort.
- The catalog is temporarily hosted within the [BradKhan profile repository](https://github.com/BradKhan/bradkhan/tree/main/composable-internet) until a standalone repository can be provisioned.
