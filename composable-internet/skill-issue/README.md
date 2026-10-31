# SKILL ISSUE.

**The problem isn't a shortage of AI skills. It's what happens between them.**

Five experimental, independently authored **orchestration skills** assembled around outcomes for builders, designers, founders, marketers and investors. Developed as a collection within [The Composable Internet](../README.md).

These are original coordination instructions, **not copied or repackaged versions** of the upstream skill repositories. Each pack identifies its ingredients, what it asks the agent to do, what evidence to produce, and when not to claim success.

> **Status:** Experimental source files. Not tested across Claude Code, Codex, Cursor, OpenCode, or other agent runtimes. Recommended upstream skills are **not installed, bundled, security-audited, or license-cleared** here. No one-click install is promised.

## Choose your problem

| Pack | Who it's for | Result | Source |
| --- | --- | --- | --- |
| **[SHIP OR IT DIDN'T HAPPEN](packs/ship-or-it-didnt-happen/SKILL.md)** | Developers | Spec → build → verify → show. | [Skill](packs/ship-or-it-didnt-happen/SKILL.md) |
| **[NO MORE SLOP](packs/no-more-slop/SKILL.md)** | Designers | References → art direction → implementation → adversarial critique. | [Skill](packs/no-more-slop/SKILL.md) |
| **[NO PERMISSION REQUIRED](packs/no-permission-required/SKILL.md)** | Entrepreneurs | Observed pain → alternatives → test → offer → first customer. | [Skill](packs/no-permission-required/SKILL.md) |
| **[ANTI-GURU](packs/anti-guru/SKILL.md)** | Marketers | Audience → promise → proof → channel → measurable experiment. | [Skill](packs/anti-guru/SKILL.md) |
| **[SHOW THE RECEIPTS](packs/show-the-receipts/SKILL.md)** | Investors | Thesis → sources → contradictions → scenarios → decision. | [Skill](packs/show-the-receipts/SKILL.md) |

## Why these are different from another awesome list

Each pack has a **bounded workflow, mandatory evidence, a failure rule, and explicit upstream references**. That is the original contribution to test. The first target is not thousands of skills; it is five combinations that consistently improve one defined outcome each.

### How to experiment safely

1. Read the original [SKILL.md](packs/) and the upstream repositories before use. Inspect scripts, filesystem access, network calls, and licensing; popularity is not a safety review.
2. Copy **only the original orchestration folder** to a compatible agent's skills directory, following that runtime's documented installation method. Do not automatically install all recommended sources.
3. Give the agent a non-sensitive test task and confirm the outcome, recorded evidence, and clear failures.
4. Use the [validation script](scripts/validate.py) for local consistency checks. It does not execute skills or validate runtime behavior.

```bash
python3 composable-internet/skill-issue/scripts/validate.py
```

## Credits and source materials

**Developers:** [obra/superpowers](https://github.com/obra/superpowers) · [mattpocock/skills](https://github.com/mattpocock/skills) · [garrytan/gstack](https://github.com/garrytan/gstack).

**Designers:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable) · [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) · [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md).

**Entrepreneurs:** [slavingia/skills](https://github.com/slavingia/skills) · [phuryn/pm-skills](https://github.com/phuryn/pm-skills) · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [BradKhan/Khan-AIOS-Venture-Studio-MVP-Framework](https://github.com/BradKhan/Khan-AIOS-Venture-Studio-MVP-Framework).

**Marketers:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill).

**Investors:** [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [Ruinius/financial-analyst-skills](https://github.com/Ruinius/financial-analyst-skills) · [phuryn/pm-skills](https://github.com/phuryn/pm-skills) · [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal).

Sources retain their individual authorship and license terms. Upstream names identify capabilities to investigate, not endorsements or guaranteed compatibility. We will publish per-runtime tests and actual adapter code before labeling these bundles production-ready.

## Next useful release

The highest-leverage next version is a small compiler that checks which referenced skills a user actually has installed, resolves conflicts and redundant instructions, and generates a minimal scoped configuration. Crucially, it must **never silently run arbitrary downloaded scripts**.

The project names are working titles; no trademark clearance has been performed.
