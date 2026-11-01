"""Offline tests for the fail-closed upstream index refresh."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "refresh_index.py"
SPEC = importlib.util.spec_from_file_location("stack_mutiny_refresh", SCRIPT)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class RefreshTests(unittest.TestCase):
    def test_add_modify_and_remove(self):
        responses = [
            {"default_branch": "main"},
            {"sha": "tree-ref", "truncated": False, "tree": [
                {"type": "blob", "path": "skills/new/SKILL.md", "sha": "a" * 40},
                {"type": "blob", "path": "skills/keep/SKILL.md", "sha": "b" * 40},
                {"type": "blob", "path": "node_modules/bad/SKILL.md", "sha": "c" * 40},
                {"type": "blob", "path": "README.md", "sha": "d" * 40},
            ]},
        ]
        with patch.object(mod, "api", side_effect=responses):
            result = mod.refresh_repository("owner/example", [
                ("skills/keep/SKILL.md", "f" * 40, "keep"),
                ("skills/gone/SKILL.md", "e" * 40, "gone"),
            ])
        self.assertEqual(result["added"], ["skills/new/SKILL.md"])
        self.assertEqual(result["changed"], ["skills/keep/SKILL.md"])
        self.assertEqual(result["removed"], ["skills/gone/SKILL.md"])
        self.assertEqual(len(result["entries"]), 2)

    def test_truncated_tree_fails_closed(self):
        with patch.object(mod, "api", side_effect=[
            {"default_branch": "main"},
            {"truncated": True, "tree": []},
        ]):
            with self.assertRaisesRegex(ValueError, "truncated"):
                mod.refresh_repository("owner/example", [])

    def test_invalid_sha_rejected(self):
        with patch.object(mod, "api", side_effect=[
            {"default_branch": "main"},
            {"truncated": False, "tree": [
                {"type": "blob", "path": "skills/bad/SKILL.md", "sha": "invalid"}
            ]},
        ]):
            with self.assertRaisesRegex(ValueError, "invalid Git blob SHA"):
                mod.refresh_repository("owner/example", [])


if __name__ == "__main__":
    unittest.main()
