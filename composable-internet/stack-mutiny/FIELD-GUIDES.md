# STACK MUTINY / Field Guides

**15 field-tested-in-concept compositions for combining open skills with real tools.** These are action plans to try, **not a claim that every integration has been built or benchmarked**. Start with a profile from [the installable library](README.md), then follow the relevant guide.

[Install a role](README.md#one-line-install) · [Explore 48 skill entrypoints and 50 tools](catalog.json) · [Agent instructions](AGENTS.md)

The underlying strategy is simple: **select, combine, adapt, verify, publish.** Every guide specifies a user outcome, recommended ingredients, a concrete deliverable, and an unacceptable shortcut.

## 01 / Ship and prove a software release

**Profiles:** `developer,engineering`.

**Composition:** Use the original delivery workflow, `webapp-testing`, Vercel React guidance, Playwright, and a real Git diff. Start by inspecting the repository and defining one observable user outcome. Implement the smallest change; run the existing tests; render the affected page at mobile and desktop widths; capture one before/after artifact.

**Done when:** An exact commit, test log, passing and failing results, and a 30-second demonstration. Nothing is described as deployed without evidence.

**Do not:** An agent reporting success because it wrote files, even when it never built the project.


## 02 / Find the design identity that a generic generator misses

**Profiles:** `design,creator`.

**Composition:** Use `stop-shipping-beige`, `frontend-design`, `web-design-guidelines` and [Impeccable](https://github.com/pbakaus/impeccable). Inspect actual reference designs before writing CSS. Select a coherent type pairing, define hierarchy and imagery, implement one complete screen, and evaluate a real render. For an existing interface, use Impeccable's `typeset`, `critique`, and `polish` workflows via its own installer.

**Done when:** A source-backed design decision record and real screenshots on target widths, with concrete defects resolved.

**Do not:** Decorative stripes, empty aesthetic claims, generic typography, or falsely asserting that a page was visually tested.


## 03 / Validate a venture before building it

**Profiles:** `founder,product`.

**Composition:** Use `find-community`, `validate-idea`, `no-permission-required`, `mvp`, and selected recent public discussions through `last30days`. Find existing alternatives, define an unmet job, and propose a test that a customer can actually accept or reject.

**Done when:** A customer/problem map, alternative solutions, falsifiable assumptions, prototype or manual offer, and a dated evidence ledger.

**Do not:** Invented interviews, market sizing, willingness to pay, and speculative traction.


## 04 / Turn one source recording into a creator campaign

**Profiles:** `creator,marketing`.

**Composition:** Start with locally processed transcription using [whisper.cpp](https://github.com/ggml-org/whisper.cpp) where the user's hardware permits; combine `baoyu-format-markdown`, `baoyu-cover-image`, `baoyu-slide-deck`, `content-strategy`, and `copywriting`. Separate exact quotes and timestamps from editorial interpretation. Publish only to accounts the user has authorized.

**Done when:** A sourced article, visual cover, slide narrative, approved social variations, and a compact distribution test.

**Do not:** Fake quotes, AI-invented testimonials, unattributed ideas, or automatic cross-posting without approval.


## 05 / Build a research-driven founder launch

**Profiles:** `founder,marketing,creator`.

**Composition:** Use `validate-idea` to establish the offer, `copywriting` for the landing page, `seo-audit` and `content-strategy` for discoverability, and `baoyu-article-illustrator` for one high-quality explainer. Use real screenshots and working examples as proof, not generic promotional visuals.

**Done when:** A live landing page or testable preview with an actual offer, source-linked demo, and one defined acquisition experiment.

**Do not:** Optimizing keywords for a product that has no compelling reason to exist.


## 06 / Research an investment without outsourcing judgment

**Profiles:** `investor`.

**Composition:** Use `show-the-receipts`, `buffett-investment-framework`, and `equity-research-skill-v1-2` where its language and runtime fit. Supplement with public filings, primary company sources, and financial tools from the [tool atlas](catalog.json). If inputs are incomplete, document the missing evidence instead of inventing a valuation.

**Done when:** A dated diligence memo, claim/source register, opposing case, sensitivity assumptions and unresolved questions.

**Do not:** Presenting projections as historical facts, ignoring financial-statement comparability, or implying a buy/sell recommendation is verified.


## 07 / Operate a private family-office research desk

**Profiles:** `family-office`.

**Composition:** Start with portable, reviewable financial notes. The cross-agent core provides a source-driven diligence process. Claude Code users may optionally add `cio`, `risk`, `macro`, `equity-research`, and `ventures` from [Cantrell's family-office project](https://github.com/acantrell0523/family-office), whose parallel-agent orchestration is specific to that environment. Keep private statements in local, excluded paths and authorize any external requests.

**Done when:** A private research briefing, source dates, portfolio-risk questions, and an investment committee agenda.

**Do not:** Assuming a downloaded skill is a regulated adviser, granting broad access to account statements, or silently uploading personal data.


## 08 / Give an agent memory that can leave with its owner

**Profiles:** `ai-memory,sovereignty`.

**Composition:** Combine `agent-memory`, `memory-systems`, `context-optimization`, and `mcp-builder`. Evaluate portable formats alongside [Mem0](https://github.com/mem0ai/mem0), [Letta](https://github.com/letta-ai/letta), [Graphiti](https://github.com/getzep/graphiti), and portable-memory standards. Keep the canonical resource store independent from the current model provider. Use [Context7](https://github.com/upstash/context7) for current library documentation, not as a personal memory store.

**Done when:** Import, selective retrieval, provenance display, a permission boundary, and a round-trip export test.

**Do not:** Assuming revoking an access token can delete data that a third party already copied.


## 09 / Run useful AI with minimal provider dependency

**Profiles:** `ai-compute,engineering`.

**Composition:** Start with a measured model workload. Choose **one** gateway, [OmniRoute](https://github.com/cheaper-inference/OmniRoute), [9Router](https://github.com/decolua/9router), or [LiteLLM](https://github.com/BerriAI/litellm). Add a user-controlled local model through [llama.cpp](https://github.com/ggml-org/llama.cpp) or [Ollama](https://github.com/ollama/ollama); add a permitted hosted provider only if needed. Check the [free inference tracker](https://github.com/surendranb/free-inference) and the actual provider terms before claiming a free tier. Run the same small test across routes.

**Done when:** A documented provider-switch test with observed latency, usage, cost assumptions, and failure behavior.

**Do not:** Claiming all inference is free, violating account terms, exposing local gateways publicly, or confusing model sharding with parallel independent tasks.


## 10 / Build an edge-hosted agent without making the cloud mandatory

**Profiles:** `ai-agents,ai-compute`.

**Composition:** Use `cloudflare`, `mcp-builder`, `tool-design`, and `harness-engineering`. Choose whether [Workers](https://developers.cloudflare.com/workers/), D1, R2, and Workers AI actually fit the workload. Create typed tool contracts, authentication, testing and usage budgets. Preserve ordinary export formats, local development, and at least one migration plan.

**Done when:** An independently testable edge application, tool schema, authentication policy, and documented spending and portability limits.

**Do not:** Embedding credentials in source, treating Cloudflare as the only possible host, or claiming deployment tests never performed.


## 11 / A private research workspace with recoverable sources

**Profiles:** `research,sovereignty`.

**Composition:** Combine `last30days`, `context-optimization`, [SearXNG](https://github.com/searxng/searxng), and [Perplexica](https://github.com/ItzCrazyKns/Perplexica) with a local full-text index. Preserve source URLs and capture dates. Sensitive browser history must be opt-in; archived third-party material must respect rights and access boundaries.

**Done when:** A search interface that recovers a specific useful source and explains its provenance.

**Do not:** Treating generated summaries as primary evidence, retaining private history without user consent, or implying privacy merely because a UI says 'local'.


## 12 / Discover opportunities already hiding in open source

**Profiles:** `founder,product,investor`.

**Composition:** Combine `find-community`, `validate-idea`, GitHub issues, and [ecosyste.ms](https://ecosyste.ms/). Identify repeated, evidenced pain points and compare existing alternatives. Record licensing and maintenance context before recommending a fork or commercial wrapper. Use the [Composable Internet](../README.md) as a starting corpus, not as ground truth for demand.

**Done when:** Three opportunity briefs each with source links, a missing product experience, a narrow MVP, and what evidence could invalidate the idea.

**Do not:** Equating stars or issue counts with demand, presenting hypothetical customers as verified, or copying incompatible source code.


## 13 / Test whether a skill pack actually helps

**Profiles:** `ai-agents,developer`.

**Composition:** Use `skill-creator`, `harness-engineering`, `tool-design`, and a deterministic test harness. Define paired tasks, run an agent with and without a selected skill under comparable conditions, capture full tool usage and outcome artifacts, and evaluate using a written rubric.

**Done when:** A comparative benchmark with reproducible tasks, exact installed revisions, output artifacts, and failures.

**Do not:** Marking a skill 'production ready' because its README says so, or comparing different models and treating the result as a skill-only effect.


## 14 / Launch an independent publishing and community presence

**Profiles:** `sovereignty,creator`.

**Composition:** Use a static site framework with [Indiekit](https://github.com/getindiekit/indiekit), RSS, and selected supported federation tools. Use `content-strategy` and `baoyu-format-markdown` for publishing. Keep the original content and audience exportable. Verify cross-posting integrations individually, especially for gated social networks.

**Done when:** A personal-domain publication with RSS, exportable archives, and an optional authorized distribution route.

**Do not:** Claiming a social audience can always be transferred intact between proprietary platforms.


## 15 / Make a serious technology company legible

**Profiles:** `design,founder,marketing`.

**Composition:** Combine `frontend-design`, `stop-shipping-beige`, `copywriting`, `vercel-react-best-practices`, and a real comparison of competitors. Make one coherent proposition, one visual concept, and one proof asset. Let [Impeccable](https://github.com/pbakaus/impeccable) review the implemented interface. Choose a flagship example that can be opened and evaluated.

**Done when:** A credible company or founder landing page with named audiences, authentic project proof, strong typography and usable mobile behavior.

**Do not:** Superlatives, abstract promises, ornamental diagrams, hidden feature gaps, or invented credentials.


## Evidence and attribution

The `SKILL.md` entrypoints in the catalog were inspected, but the guides above remain integration plans. Feature support varies across agents, external APIs and user hardware. Tools remain owned by their maintainers. Read their licenses and setup guides before copying, installing or modifying code.

For a shareable result, publish one real example, the exact source projects and revisions used, a short explanation of the original integration, and a limitation that matters. A reproducible demonstration is more valuable than a collection that claims to have every tool.
