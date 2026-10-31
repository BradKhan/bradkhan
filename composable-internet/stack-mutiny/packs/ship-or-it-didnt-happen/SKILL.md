---
name: ship-or-it-didnt-happen
description: "Ship a small code change with reproducible evidence rather than celebratory prose."
---

# SHIP OR IT DIDN'T HAPPEN

> Ideas don't pass tests. Software does.

**Audience:** Developer
**Outcome:** Spec → build → verify → show.

This is an **experimental original orchestration skill**. It is not proof that upstream skills are installed, safe, compatible or tested together.

## When to use

Use this when a user wants to: ship a small code change with reproducible evidence rather than celebratory prose.

## Required inputs

- Requested user-visible outcome
- Repository and exact target branch
- Constraints and permitted actions
- Existing test commands or acceptance fixtures

## Workflow

1. Define the smallest demonstrable result and concrete acceptance tests. Confirm the permitted scope before changing code.
2. Inspect the current implementation; cite files and versions rather than hallucinating architecture.
3. Build a minimal reversible change. Use existing installed source skills only after reviewing their actual contents and permissions.
4. Run deterministic tests and capture their real output. Check regressions and accessibility when UI changes.
5. Produce a short demo script, source links, test results, and a concise change summary. State failures and omissions.

## Output contract

A runnable change or clear refusal, passing or failing test evidence, and a 30-second product demonstration plan.

## Stop conditions and honesty

Do not claim shipped, tested, merged or deployed unless the exact command, commit and artifact substantiate it.

Use only the permissions the user has actually authorized. Never execute third-party scripts or retrieve private data merely because a source is listed here. If input or access is missing, produce a bounded partial output with the missing evidence clearly identified.

## Complementary upstream candidates

- [obra/superpowers](https://github.com/obra/superpowers): Planning, TDD and review discipline. **External and not bundled.**
- [mattpocock/skills](https://github.com/mattpocock/skills): Domain modeling and engineering review patterns. **External and not bundled.**
- [garrytan/gstack](https://github.com/garrytan/gstack): Coding-agent QA and launch coordination. **External and not bundled.**

Review the upstream skill files, version, licenses and security before integrating. If an optional upstream skill is unavailable, continue using this self-contained workflow rather than pretending it ran.

## Evaluation

Status: **Not tested in a live agent harness.** A credible test must provide the original task, runtime and model versions, which skills were loaded, output artifacts, known failures, and an independently inspectable assessment of the outcome.
