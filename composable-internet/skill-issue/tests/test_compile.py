"""Deterministic offline tests for the Skill Issue compiler."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import compile as skill_compiler


class CompilerTests(unittest.TestCase):
    def test_five_packs_exist(self):
        self.assertEqual(len(skill_compiler.available_packs()), 5)

    def test_every_pack_compiles_without_network(self):
        for slug, pack in skill_compiler.available_packs().items():
            with self.subTest(slug=slug):
                agents = skill_compiler.render(pack, "agents")
                skill = skill_compiler.render(pack, "skill")
                self.assertIn(pack["title"], agents)
                self.assertIn("Not tested in a live agent harness", agents)
                self.assertTrue(skill.startswith(f"---\nname: {slug}\n"))
                self.assertNotIn("https://example.com/installer", agents)

    def test_file_creation_and_no_implicit_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "AGENTS.md"
            args = ["anti-guru", "--output", str(path)]
            self.assertEqual(skill_compiler.main(args), 0)
            text = path.read_text(encoding="utf-8")
            self.assertIn("ANTI-GURU", text)
            with self.assertRaises(SystemExit):
                skill_compiler.main(args)
            self.assertEqual(skill_compiler.main(args + ["--force"]), 0)

    def test_explicit_missing_output_rejected(self):
        with self.assertRaises(SystemExit):
            skill_compiler.main(["anti-guru"])

    def test_reject_unknown_pack(self):
        with self.assertRaises(SystemExit):
            skill_compiler.main(["not-an-existing-pack", "--output", "/tmp/do-not-create.txt"])


if __name__ == "__main__":
    unittest.main()
