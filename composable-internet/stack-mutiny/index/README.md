# Stack Mutiny / Discovery Index

**A large index is not a giant prompt.**

This collection contains **4,965 GitHub-tree-confirmed `SKILL.md` paths** across 33 source repositories, representing **4,920 distinct git blob content hashes** at the capture date of November 1, 2026.

Only a smaller subset has been individually inspected for valid `SKILL.md` metadata. These indexed file paths are **not** 4,965 audited, tested, licensed or directly installable skills. Some are third-party mirrors or community copies. The source blob hash supports comparison and deduplication, but does not prove that the contents are safe.

## Source layers

| Shard | Skill paths | Repository type |
| --- | ---: | --- |
| [Primary](primary.json) | 329 | Official provider skills and recognized specialized creators |
| [Specialist](specialist.json) | 1,965 | Engineering, context, scientific and broad specialist collections |
| [Professional verticals](verticals.json) | 1,283 | Finance, investing, marketing, social media and creator collections |
| [Community](community.json) | 1,388 | Mirrored and aggregated collections, lower priority by default |
| **Total** | **4,965** | **33 repositories** |

[Machine-readable manifest](manifest.json) · [15 role source pools](role-pools.json) · [Search tool](../search.py) · [Installation guidance](../README.md).

## Search without loading every skill

```bash
python3 composable-internet/stack-mutiny/search.py "analyse portfolio risk" --role family-office --top 3
python3 composable-internet/stack-mutiny/search.py "build excellent mobile UI" --role design --top 3
python3 composable-internet/stack-mutiny/search.py "memory retrieval and long-term context" --role ai-memory --top 3
```

The selector searches **only short path/name data and curated descriptions**. It prioritizes original/official sources, uses task keywords and domain context, and ignores duplicated blob hashes in the selected results. It doesn't open or execute the actual skill body.

An agent then retrieves the **actual SKILL.md for at most three promising results** and checks the skill name, license, requirements, scripts and expected outcome. Most tasks should use only one of them. Installation is a separate, explicitly approved operation.

The search is lexical with synonym expansion and source-quality weighting, not embedding-based semantic similarity. For additional discovery beyond this snapshot, use the official [find-skills](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md), or a separate skill-search MCP server if the user has configured one.

## Role pools

The [role source pools](role-pools.json) identify relevant upstream **repositories to search**, not an instruction to load every entry they contain. Pools overlap. They include:

- Development and engineering
- Interface design and creative production
- Founders, product management and operations
- Marketing and publishing
- Investment research and family offices
- Academic and investigative research
- AI agents, inference, context and memory
- Privacy, portability and independent infrastructure

Some roles intentionally share sources. A skill relevant to both a designer and a developer is indexed once and discovered in both contexts.

## Maintenance

Each indexed path retains its source repository, its Git tree snapshot identifier, and its file's blob SHA. The [upstream source audit](../audit.py) tracks individually reviewed entries. [Discovery](../discover.py) can refresh candidate source lists without automatically adding them to the installable catalog.

**Known gaps:** exact licensing and security audits, runtime-level benchmark results, ranking evaluations, and verified skill-installation coverage remain open. A GitHub tree listing alone does not validate those attributes.

## Contributing

Contributions should improve actual coverage and retrieval quality, not inflate counters. Supply the canonical original repository, exact `SKILL.md` source path and name, provenance or upstream source, and a real task for evaluating its usefulness. Avoid adding redundant mirror copies when the original project is available.
