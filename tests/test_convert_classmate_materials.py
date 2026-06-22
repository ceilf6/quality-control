"""Regression checks for classmate workbook conversion outputs."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "files-from-classmate"
SCRIPT = ROOT / "scripts" / "convert_classmate_materials.py"


class ClassmateWorkbookConversionTests(unittest.TestCase):
    def test_workbooks_generate_readable_markdown_and_sheet_previews(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)

        workbook_outputs = {
            "Copie de TD CUMSUM.xlsx": ["n-1", "n-2", "n-4", "n-8", "arl"],
            "TD CUMSUM.xlsx": ["n-1", "n-2", "n-4", "n-8", "arl"],
        }
        for source_name, sheet_slugs in workbook_outputs.items():
            source = SOURCE_DIR / source_name
            readable = source.with_suffix(".readable.md")
            self.assertTrue(readable.exists(), f"missing readable workbook: {readable}")
            text = readable.read_text(encoding="utf-8")
            self.assertIn(f"Source: `{source_name}`", text)
            self.assertIn("Review priority: P3 classmate auxiliary material.", text)
            self.assertIn("Formula cells are preserved", text)
            self.assertNotIn("colors1.xml", text)
            self.assertNotIn("style1.xml", text)
            self.assertNotIn("C2==", text)

            for slug in sheet_slugs:
                preview = source.with_name(f"{source.stem}.sheet-{slug}.html")
                self.assertTrue(preview.exists(), f"missing sheet preview: {preview}")
                html = preview.read_text(encoding="utf-8")
                self.assertIn(source_name, html)
                self.assertIn("Teacher P0 source", html)

        index = (SOURCE_DIR / "classmate-materials.index.md").read_text(encoding="utf-8")
        self.assertIn("`TD CUMSUM.xlsx`", index)
        self.assertIn("`Copie de TD CUMSUM.xlsx`", index)
        self.assertIn("暂用的 P3 参考", index)
        self.assertNotIn("`Copie de TD control charts.xlsx`", index)

        removed_source = SOURCE_DIR / "Copie de TD control charts.xlsx"
        self.assertFalse(removed_source.exists(), f"official correction replaces {removed_source}")
        self.assertEqual(list(SOURCE_DIR.glob("Copie de TD control charts.*")), [])


if __name__ == "__main__":
    unittest.main()
