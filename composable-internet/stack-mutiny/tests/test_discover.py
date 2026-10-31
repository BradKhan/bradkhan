"""Offline tests for the opt-in upstream skill discovery utility."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("stack_discovery", ROOT / "discover.py")
discovery = importlib.util.module_from_spec(spec)
spec.loader.exec_module(discovery)


class TestDiscovery(unittest.TestCase):
    def test_sources_list_without_network(self):
        self.assertEqual(discovery.main(["--list"]), 0)

    def test_default_read_only_without_online(self):
        self.assertEqual(discovery.main(["--query", "security"]), 0)

    def test_mocked_live_discovery(self):
        calls = []
        def fake_fetcher(entry, token):
            calls.append(entry["repo"])
            return {"repo": entry["repo"], "name": entry["name"], "truncated": False, "error": "",
                    "candidates": [{"repo": entry["repo"], "folder": "example-skill",
                                   "path": "skills/example-skill/SKILL.md",
                                   "url": "https://github.com/" + entry["repo"] + "/blob/main/skills/example-skill/SKILL.md",
                                   "status": "candidate_not_verified"}]}
        with tempfile.TemporaryDirectory() as tmp:
            output = str(Path(tmp) / "discovery.json")
            self.assertEqual(discovery.main(["--online", "--repos", "anthropics/skills", "--query",
                                              "example-skill", "--output", output], fetcher=fake_fetcher), 0)
            data = json.loads(Path(output).read_text())
            self.assertEqual(len(calls), 1)
            self.assertEqual(data["status"], "discovered_unverified")
            self.assertEqual(len(data["candidates"]), 1)

    def test_invalid_repo_rejected(self):
        with self.assertRaises(SystemExit):
            discovery.main(["--online", "--repos", "not-a-real-repository/unused"], fetcher=lambda x, y: x)


if __name__ == "__main__":
    unittest.main()
