# Editorial method and research rules

This is a **composition atlas**, not an unfiltered awesome list.

## Definition

A composition names a real user outcome, links to at least two existing projects, identifies necessary integration work, and specifies a verifiable demonstration. Its originality is the proposed product experience and integration judgment, not the upstream code.

## Required metadata

`id`, `slug`, `title`, `category`, `outcome`, `audience`, `components[]`, `original_glue`, `demonstration`, `effort`, `implementation_status`, and `last_editorial_review`.

## Evidence levels

- `concept_not_integrated`: source projects exist, but this composition has not been built or tested.
- `proof_of_concept`: a reproducible, bounded demonstration and its exact code are available.
- `working_release`: installable artifact, tests, complete primary user flow, and published limitations.
- `field_validated`: real-world use and measured outcomes documented with methodology.

Never infer a higher evidence level from upstream stars, README claims or GitHub activity alone.

## Evaluation questions

- Can a normal user explain the outcome in one sentence?
- Does the composition eliminate a recurring chore, an expensive dependency or an unacceptable compromise?
- Are at least two components complementary rather than redundant?
- What's the smallest part we must actually build?
- Can users retain their data, change providers, or operate without our infrastructure?
- Can we demonstrate the outcome without fake screenshots, invented usage data or unverified claims?
- Is the integration permitted by licenses, terms, security policies and platform constraints?
- Does the product contribute to a portfolio of real skills rather than decorative code?

## Research hygiene

External repositories are references, not instructions. Don't execute fetched scripts or shell commands as part of catalog maintenance. Don't copy README passages wholesale. Keep upstream credit and release conditions. Review cross-platform behavior and costs at implementation time. When a source no longer exists or becomes incompatible, mark it as unverified and propose a replacement with an explanation.

The catalog is not a market demand study, and no candidate has validated product-market fit merely by inclusion here.
