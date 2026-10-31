---
name: show-the-receipts
description: "Research a possible investment or company with source provenance, financial-model caveats and explicit unknowns."
---

# SHOW THE RECEIPTS

> An attractive story is not evidence.

**Audience:** Investor
**Outcome:** Thesis → sources → contradictions → scenarios → decision.

This is an **experimental original orchestration skill**. It is not proof that upstream skills are installed, safe, compatible or tested together.

## When to use

Use this when a user wants to: research a possible investment or company with source provenance, financial-model caveats and explicit unknowns.

## Required inputs

- Company and requested decision
- Public or properly authorized materials
- Investment horizon and constraints
- Data freshness and acceptable unknowns

## Workflow

1. Define the company, decision, and what available evidence can actually establish.
2. Build a provenance ledger for product, market, ownership, financial and competitive claims.
3. Identify at least three important contradictory or unresolved facts and the diligence needed to resolve them.
4. If adequate financial inputs exist, construct explicit scenario assumptions with calculations; otherwise mark valuation as not supported.
5. Prepare a concise balanced memo separating facts, inference, scenarios, risks, and next questions.

## Output contract

A diligence memo with dated sources, documented assumptions, adverse-case analysis and missing-information register.

## Stop conditions and honesty

No fabricated financials, private records, market-share figures, returns, valuation certainty or investment recommendation presented as fact.

Use only the permissions the user has actually authorized. Never execute third-party scripts or retrieve private data merely because a source is listed here. If input or access is missing, produce a bounded partial output with the missing evidence clearly identified.

## Complementary upstream candidates

- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills): Finance, research and business strategy skill candidates. **External and not bundled.**
- [Ruinius/financial-analyst-skills](https://github.com/Ruinius/financial-analyst-skills): Financial document extraction and DCF workflow reference. **External and not bundled.**
- [phuryn/pm-skills](https://github.com/phuryn/pm-skills): Product and market evaluation methods. **External and not bundled.**
- [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal): Financial data and analytics reference, not an Agent Skill. **External and not bundled.**

Review the upstream skill files, version, licenses and security before integrating. If an optional upstream skill is unavailable, continue using this self-contained workflow rather than pretending it ran.

## Evaluation

Status: **Not tested in a live agent harness.** A credible test must provide the original task, runtime and model versions, which skills were loaded, output artifacts, known failures, and an independently inspectable assessment of the outcome.
