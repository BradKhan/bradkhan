"""Offline tests for Stack Mutiny profile selection and installation consent."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("stack_installer", ROOT / "install.py")
sm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sm)

SAMPLE = {
    "schema_version": "0.2",
    "skills": [
        {"id": "owner/repo@sample-skill", "repo": "owner/repo", "skill": "sample-skill",
         "verification": "SKILL.md inspected", "purpose": "Demo"},
        {"id": "owner/other@other-skill", "repo": "owner/other", "skill": "other-skill",
         "verification": "SKILL.md inspected", "purpose": "Other"},
    ],
    "profiles": {
        "developer": {"label": "Developer", "core": ["owner/repo@sample-skill"], "extended": ["owner/other@other-skill"]},
        "design": {"label": "Design", "core": ["owner/repo@sample-skill"], "extended": []},
    },
    "tools": []
}


class CatalogTests(unittest.TestCase):
    def test_valid_manifest(self):
        self.assertTrue(sm.validate_catalog(SAMPLE))

    def test_dedup_and_depth(self):
        self.assertEqual(len(sm.select_skills(SAMPLE, ["developer", "design"], "core")), 1)
        self.assertEqual(len(sm.select_skills(SAMPLE, ["developer"], "extended")), 2)

    def test_shell_safe_command(self):
        actual = sm.build_command(SAMPLE["skills"][0], "codex")
        self.assertEqual(actual[:5], ["npx", "--yes", "skills@1.7.4", "add", "owner/repo"])
        self.assertEqual(actual[-3:], ["-a", "codex", "-y"])
        with self.assertRaises(ValueError):
            sm.build_command(SAMPLE["skills"][0], "codex", cli_version="latest; rm -rf /")

    def test_explicit_consent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.json"
            path.write_text(json.dumps(SAMPLE), encoding="utf-8")
            self.assertEqual(sm.main(["validate", "--manifest", str(path)]), 0)
            self.assertEqual(sm.main(["plan", "developer", "--manifest", str(path)]), 0)
            self.assertEqual(sm.main(["install", "developer", "--manifest", str(path)]), 2)

    def test_reject_malformed_identifier(self):
        bad = json.loads(json.dumps(SAMPLE))
        bad["skills"][0]["id"] += ";rm"
        with self.assertRaises(ValueError):
            sm.validate_catalog(bad)

    def test_catalog_from_repository(self):
        data = sm.load_manifest(str(ROOT / "catalog.json"))
        self.assertGreaterEqual(len(data["profiles"]), 12)
        self.assertGreaterEqual(len(data["skills"]), 30)
        self.assertGreaterEqual(len(data.get("tools", [])), 40)
        self.assertGreater(len(sm.select_skills(data, ["developer", "designer"] if "designer" in data["profiles"] else ["developer", "design"], "extended")), 5)


if __name__ == "__main__":
    unittest.main()
