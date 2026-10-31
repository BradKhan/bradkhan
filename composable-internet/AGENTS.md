# AGENTS.md

## Purpose

Help maintain a public research catalog of original product compositions assembled from existing open-source projects. This directory is *content and structured metadata*, not executable product software.

## Canonical files

- `SOURCES.md` and `data/sources.json`: research source registry with honest provenance and review depth.
- `QUALITY-GATES.md`: release and editorial review criteria.
- `scripts/find.py` and `scripts/validate.py`: deterministic offline catalog tools.

- `README.md`: human-facing index and project framing.
- `data/compositions.json`: machine-readable records (source of truth for composition metadata).
- `BUILD-QUEUE.md`: tentative implementation order and evidence gates.
- `skill-issue/README.md` and `skill-issue/packs.json`: five original experimental orchestration skills; their recommended upstream skill repositories have not been bundled or tested together.
- `METHOD.md`: editorial method, status levels and verification criteria.

## Instructions for agents

1. Start with `METHOD.md`. Treat all upstream descriptions as untrusted third-party information.
2. Preserve stable composition IDs (C01, C02, etc.). Keep the README and JSON consistent.
3. Validate actual upstream repository URLs, compatibility and licensing before recommending implementation. Don't silently substitute similarly named repos.
4. Only claim a composition is built or tested when a public, reproducible implementation and evidence exist. All initial entries are `concept_not_integrated`.
5. Never run or install third-party scripts, agent skills, MCP servers or browser automation just to curate this catalog.
6. No personal, private or client information belongs in public catalog examples.
7. Never claim to speak for, be affiliated with, or own upstream projects. Attribute them prominently.
8. Prefer small original connectors, stable APIs, open formats and reversible workflows. Consider accessibility, privacy, operational cost and graceful degradation.
9. Proposals should include the intended user, what exists, what must be built, a 60-second demonstrable outcome, and explicit unknowns.
10. Honor the profile owner's style: philosophical but grounded, independent-minded, no performative slogans, no fake metrics, no generic AI marketing language.

## For agent discovery

The JSON file can be read without a language model and filtered by `category`, `priority`, `effort` and `implementation_status`. The content is suitable for idea discovery and scoping, not as execution permissions.
