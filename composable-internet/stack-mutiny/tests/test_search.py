"""Tests for focused discovery and provenance, with no network access."""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("stack_search", ROOT / "search.py")
search_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search_module)


def item(slug, repo="anthropics/skills", tier="official", sha="a", path=None):
    return {"name": slug, "repo": repo, "tier": tier,
            "sha": sha, "path": path or f"skills/{slug}/SKILL.md"}


class SearchTests(unittest.TestCase):
    def test_index_loads_offline(self):
        manifest, data = search_module.load_index(offline=True)
        self.assertEqual(len(data), manifest["total_paths"])
        self.assertGreater(len(data), 3000)
        self.assertGreater(manifest["unique_blob_shas"], 3000)

    def test_precision_over_bulk(self):
        candidates = [
            item("react-best-practices", sha="a"),
            item("equity-research", sha="b"),
            item("design-system", sha="c"),
        ]
        result = search_module.search(candidates, "react performance", top=2, role="developer")
        self.assertTrue(result)
        self.assertEqual(result[0]["name"], "react-best-practices")
        self.assertLessEqual(len(result), 2)

    def test_identical_source_is_deduplicated(self):
        entries = [item("test-patterns", sha="same"),
                   item("test-patterns", repo="community/mirror", tier="aggregator", sha="same")]
        matches = search_module.search(entries, "test patterns", top=5, include_aggregators=True)
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["repo"], "anthropics/skills")

    def test_different_sources_same_skill_name_are_not_repeated(self):
        entries = [
            item("risk", repo="firm/finance-a", tier="finance", sha="one"),
            item("risk", repo="firm/finance-b", tier="finance", sha="two"),
            item("portfolio-risk", repo="firm/finance-c", tier="finance", sha="three"),
        ]
        matches = search_module.search(entries, "portfolio risk", top=3, role="family-office")
        self.assertEqual(len([x for x in matches if x["name"] == "risk"]), 1)

    def test_aggregators_opt_in(self):
        entries = [item("special-idea", repo="mirror/library", tier="aggregator")]
        self.assertEqual(search_module.search(entries, "special idea"), [])
        self.assertEqual(len(search_module.search(entries, "special idea", include_aggregators=True)), 1)

    def test_context_and_memory_related(self):
        entries = [item("memory-systems", sha="m"),
                   item("react-best-practices", sha="r")]
        res = search_module.search(entries, "persistent context", top=1, role="ai-memory")
        self.assertEqual(res[0]["name"], "memory-systems")

    def test_limit_is_small(self):
        with self.assertRaises(SystemExit):
            search_module.main(["design", "--top", "500", "--offline"])

    def test_run_stats_offline(self):
        self.assertEqual(search_module.main(["--stats", "--offline"]), 0)


if __name__ == "__main__":
    unittest.main()
