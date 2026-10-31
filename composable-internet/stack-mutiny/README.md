# STACK MUTINY.

**The problem isn't a shortage of AI skills. It's what happens between them.**

Five role-specific skill packs for software development, design, venture creation, marketing, and investment research. They draw on existing open-source approaches and are organized around a specific result. Part of [The Composable Internet](../README.md).

The value is in the combination: **select useful methods, adapt them to a purpose, put them in the right sequence, and make the result usable.** Each pack contains its own orchestration, identifies upstream resources, and defines a concrete deliverable. The first edition references those resources; deeper integrations and testing are next.

> **Status:** Experimental source files. Not tested across Claude Code, Codex, Cursor, OpenCode, or other agent runtimes. Recommended upstream skills are **not installed, bundled, security-audited, or license-cleared** here. No one-click install is promised.

## Choose your problem

| Pack | Who it's for | Result | Source |
| --- | --- | --- | --- |
| **[SHIP OR IT DIDN'T HAPPEN](packs/ship-or-it-didnt-happen/SKILL.md)** | Developers | Spec → build → verify → show. | [Skill](packs/ship-or-it-didnt-happen/SKILL.md) |
| **[STOP SHIPPING BEIGE](packs/stop-shipping-beige/SKILL.md)** | Designers | References → art direction → implementation → adversarial critique. | [Skill](packs/stop-shipping-beige/SKILL.md) |
| **[NO PERMISSION REQUIRED](packs/no-permission-required/SKILL.md)** | Entrepreneurs | Observed pain → alternatives → test → offer → first customer. | [Skill](packs/no-permission-required/SKILL.md) |
| **[ANTI-GURU](packs/anti-guru/SKILL.md)** | Marketers | Audience → promise → proof → channel → measurable experiment. | [Skill](packs/anti-guru/SKILL.md) |
| **[SHOW THE RECEIPTS](packs/show-the-receipts/SKILL.md)** | Investors | Thesis → sources → contradictions → scenarios → decision. | [Skill](packs/show-the-receipts/SKILL.md) |

### Offline compile, no automatic installation

The collection includes a tiny Python compiler that turns any of the five original role skills into a single AGENTS-style Markdown guide or an unchanged SKILL.md. It does not fetch, copy, or execute external sources.

```bash
python3 composable-internet/stack-mutiny/scripts/compile.py --list
python3 composable-internet/stack-mutiny/scripts/compile.py stop-shipping-beige --output /tmp/DESIGN-AGENT.md
python3 composable-internet/stack-mutiny/scripts/compile.py show-the-receipts --format skill --output /tmp/SKILL.md
python3 -m unittest discover -s composable-internet/stack-mutiny/tests -p "test_*.py"
```

Run from the **profile repository root**. Only the original published orchestration instructions are included in the generated file. Actual agent-harness testing and upstream integrations remain unverified.

## More than a directory

Each pack has a defined workflow, deliverable, and upstream references. Rather than collecting hundreds of links, we are testing whether a small, deliberately composed set of methods can produce better results on a specific task.

### How to experiment safely

1. Read the original [SKILL.md](packs/) and the upstream repositories before use. Inspect scripts, filesystem access, network calls, and licensing; popularity is not a safety review.
2. Copy **only the original orchestration folder** to a compatible agent's skills directory, following that runtime's documented installation method. Do not automatically install all recommended sources.
3. Give the agent a non-sensitive test task and confirm the outcome, recorded evidence, and clear failures.
4. Use the [validation script](scripts/validate.py) for local consistency checks. It does not execute skills or validate runtime behavior.

```bash
python3 composable-internet/stack-mutiny/scripts/validate.py
```

## Credits and source materials

**Developers:** [obra/superpowers](https://github.com/obra/superpowers) · [mattpocock/skills](https://github.com/mattpocock/skills) · [garrytan/gstack](https://github.com/garrytan/gstack).

**Designers:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable) · [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) · [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md).

**Entrepreneurs:** [slavingia/skills](https://github.com/slavingia/skills) · [phuryn/pm-skills](https://github.com/phuryn/pm-skills) · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [BradKhan/Khan-AIOS-Venture-Studio-MVP-Framework](https://github.com/BradKhan/Khan-AIOS-Venture-Studio-MVP-Framework).

**Marketers:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) · [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill).

**Investors:** [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · [Ruinius/financial-analyst-skills](https://github.com/Ruinius/financial-analyst-skills) · [phuryn/pm-skills](https://github.com/phuryn/pm-skills) · [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal).

These are credited open-source foundations and reference materials. We can adapt, remix, and integrate them under their applicable licenses. The current packs include original orchestration; full upstream integrations and measured comparisons have not yet been completed.

## Next useful release

The highest-leverage next version is a small compiler that checks which referenced skills a user actually has installed, resolves conflicts and redundant instructions, and generates a minimal scoped configuration. Crucially, it must **never silently run arbitrary downloaded scripts**.

The project names are working titles; no trademark clearance has been performed.
