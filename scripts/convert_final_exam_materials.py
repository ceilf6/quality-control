#!/usr/bin/env python3
"""Convert final-exam teacher materials into LLM-readable text files."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "files-from-teacher"


@dataclass(frozen=True)
class Material:
    filename: str
    priority: str
    note: str


MATERIALS = [
    Material("32_SujetExam_tytpe.pdf", "P0", "Sujet type: direct exam-shape source."),
    Material("22_FQ01_USTEUS_TD1_Enoncé_2026.pdf", "P0", "TD1 DOE calculations."),
    Material("24_FQ01_USTEUS_TD2.pdf", "P0", "TD2 DOE analysis and fractional plan."),
    Material("26_Enonce_TD_3.pdf", "P0", "TD3 crossed plan and robustness."),
    Material("29_FQ01_UTSEUS_TD1_correction 2.pdf", "P0", "TD1 correction."),
    Material("30_FQ01_USTEUS_TD2_correction.pdf", "P0", "TD2 correction."),
    Material("27_UTSEUS_TD_PlanExp_Corrigé_2023.xlsx", "P0", "DOE correction workbook."),
    Material("28_Correction_Plan_Experiences_Robustesse.xlsx", "P0", "Robustness correction workbook."),
    Material("31_TD control charts.xlsx", "P0", "Attribute control-chart TD data."),
    Material("33_TD CUMSUM.xlsx", "P0", "CUSUM TD workbook."),
    Material("35_TD control charts-correction.xlsx", "P0", "Attribute control-chart correction workbook."),
    Material("25_USTEUS_Cours_PlanExp_2026.pdf", "P1", "DOE course support."),
    Material("23_Lecture table Fisher.pptx", "P1", "Fisher table reading aid."),
    Material("34_FQ01-UTSEUS-Part 5-P26 2.pdf", "P1", "SPC, attribute charts and CUSUM course support."),
    Material("36_FQ01P2006.pdf", "P1", "Surete de fonctionnement course support: FMDS/RAMS, reliability, maintainability, availability, mono-composant and multi-composant modelling."),
    Material("04_Les lois de probabilités les plus importantes en contrôle qualité.pdf", "P2", "Probability-law support."),
    Material("08_Table_FQ01_2025.pdf", "P2", "Statistical tables."),
    Material("09_TP3-correction 2.xlsx", "P2", "Older control-chart correction workbook."),
]


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "ws": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def run(cmd: list[str]) -> str:
    result = subprocess.run(
        cmd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError("Command failed: " + " ".join(cmd) + "\n" + result.stderr)
    return result.stdout


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    out: list[str] = []
    blank = False
    for line in lines:
        if not line:
            if not blank:
                out.append("")
            blank = True
            continue
        out.append(line)
        blank = False
    return "\n".join(out).strip()


def output_path(path: Path) -> Path:
    if path.suffix.lower() == ".pdf":
        return path.with_suffix(".readable.txt")
    return path.with_suffix(".readable.md")


def convert_pdf(path: Path) -> str:
    if shutil.which("pdftotext") is None:
        raise RuntimeError("pdftotext is required for PDF conversion")
    return normalize_text(run(["pdftotext", str(path), "-"]))


def convert_pptx(path: Path) -> str:
    lines = [
        f"# {path.name} readable text",
        "",
        f"Source: `{path.name}`",
        "",
    ]
    with zipfile.ZipFile(path) as zf:
        slides = sorted(
            [
                name
                for name in zf.namelist()
                if name.startswith("ppt/slides/slide") and name.endswith(".xml")
            ],
            key=lambda name: int(re.search(r"slide(\d+)\.xml", name).group(1)),
        )
        for index, slide in enumerate(slides, start=1):
            xml = ET.fromstring(zf.read(slide))
            text = [html.unescape(node.text or "") for node in xml.findall(".//a:t", NS)]
            text = [part.strip() for part in text if part and part.strip()]
            lines.extend([f"## Slide {index}", ""])
            lines.append("\n".join(text) if text else "[No readable text detected]")
            lines.append("")
    return "\n".join(lines).strip()


def column_index(cell_ref: str) -> int:
    letters = re.match(r"[A-Z]+", cell_ref)
    if not letters:
        return 1
    total = 0
    for char in letters.group(0):
        total = total * 26 + ord(char) - ord("A") + 1
    return total


def read_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    values = []
    for item in root.findall("ws:si", NS):
        texts = [node.text or "" for node in item.findall(".//ws:t", NS)]
        values.append("".join(texts))
    return values


def workbook_sheets(zf: zipfile.ZipFile) -> list[tuple[str, str]]:
    workbook = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map = {
        rel.attrib["Id"]: rel.attrib["Target"].lstrip("/")
        for rel in rels.findall("rel:Relationship", NS)
    }
    sheets: list[tuple[str, str]] = []
    for sheet in workbook.findall(".//ws:sheet", NS):
        name = sheet.attrib.get("name", "Sheet")
        rel_id = sheet.attrib.get(f"{{{NS['r']}}}id")
        target = rel_map.get(rel_id or "")
        if target:
            if not target.startswith("xl/"):
                target = "xl/" + target
            sheets.append((name, target))
    return sheets


def cell_value(cell: ET.Element, shared_strings: list[str]) -> str:
    formula = cell.find("ws:f", NS)
    value = cell.find("ws:v", NS)
    inline = cell.find(".//ws:t", NS)
    if formula is not None and formula.text:
        formula_text = "=" + formula.text
        if value is not None and value.text:
            return f"{formula_text} -> {value.text}"
        return formula_text
    if inline is not None and inline.text:
        return inline.text
    if value is None or value.text is None:
        return ""
    if cell.attrib.get("t") == "s":
        index = int(value.text)
        return shared_strings[index] if index < len(shared_strings) else value.text
    return value.text


def convert_xlsx(path: Path) -> str:
    lines = [
        f"# {path.name} readable workbook",
        "",
        f"Source: `{path.name}`",
        "",
        "Formula cells are preserved as `=formula`; cached values are shown after `->` when available.",
        "",
    ]
    with zipfile.ZipFile(path) as zf:
        shared_strings = read_shared_strings(zf)
        for sheet_name, target in workbook_sheets(zf):
            lines.extend([f"## Sheet: {sheet_name}", ""])
            if target not in zf.namelist():
                lines.extend(["[Sheet XML not found]", ""])
                continue
            root = ET.fromstring(zf.read(target))
            rows = []
            max_col = 0
            for row in root.findall(".//ws:sheetData/ws:row", NS):
                cells: dict[int, str] = {}
                for cell in row.findall("ws:c", NS):
                    ref = cell.attrib.get("r", "A1")
                    col = column_index(ref)
                    max_col = max(max_col, col)
                    value = normalize_text(cell_value(cell, shared_strings))
                    if value:
                        cells[col] = value
                if cells:
                    rows.append(cells)
            if not rows:
                lines.extend(["[No readable cells detected]", ""])
                continue
            max_col = min(max_col, 18)
            for cells in rows[:240]:
                values = [cells.get(col, "") for col in range(1, max_col + 1)]
                while values and not values[-1]:
                    values.pop()
                lines.append(" | ".join(values))
            if len(rows) > 240:
                lines.append(f"... [{len(rows) - 240} additional non-empty rows omitted]")
            lines.append("")
    return "\n".join(lines).strip()


def convert_material(material: Material) -> Path:
    source = SOURCE_DIR / material.filename
    if not source.exists():
        raise FileNotFoundError(source)
    suffix = source.suffix.lower()
    if suffix == ".pdf":
        text = convert_pdf(source)
    elif suffix == ".pptx":
        text = convert_pptx(source)
    elif suffix == ".xlsx":
        text = convert_xlsx(source)
    else:
        raise ValueError(f"Unsupported file type: {source}")
    out = output_path(source)
    header = [
        f"# {source.name}",
        "",
        f"- Source: `{source.name}`",
        f"- Final-exam priority: {material.priority}",
        f"- Role: {material.note}",
        "",
        "## Readable Content",
        "",
    ]
    if suffix in {".pdf"}:
        out.write_text("\n".join(header) + text + "\n", encoding="utf-8")
    else:
        out.write_text(text + "\n", encoding="utf-8")
    return out


def write_index(outputs: list[tuple[Material, Path]]) -> None:
    lines = [
        "# 质量管理期末资料转换索引",
        "",
        "本索引用于期末复习。优先级按应试价值排序：Sujet type 与 TD/correction 最高，课程和表格用于补公式、表值和概念。",
        "",
        "## 优先级规则",
        "",
        "1. P0：`32_SujetExam_tytpe.pdf`、期末 TD、TD correction、Excel correction/workbook。用于判断题型、考法、步骤和答案颗粒度。",
        "2. P1：Plan d'expériences 课程、Fisher 表说明、SPC/CUSUM 课程、SdF/FMDS 课程与视频 ASR。用于补定义、公式来源和图表解释。",
        "3. P2：概率表、统计表和旧 TP correction。用于查表和补基础，不覆盖 P0 题源。",
        "",
        "## 转换清单",
        "",
    ]
    for material, out in outputs:
        lines.append(f"- {material.priority} `{material.filename}` -> `{out.name}`：{material.note}")
    lines.append(
        "- P1 `37_FQ01_P26_SdF_CM_Seance1_720p.mp4` -> "
        "`37_FQ01_P26_SdF_CM_Seance1_720p.asr.fr.txt`："
        "Surete de fonctionnement oral course support, ASR in French. "
        "Use PDF slides for formulas and ASR for spoken clarifications."
    )
    lines.append("")
    (SOURCE_DIR / "final-exam.index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    outputs: list[tuple[Material, Path]] = []
    for material in MATERIALS:
        out = convert_material(material)
        outputs.append((material, out))
        print(f"[converted] {material.filename} -> {out.relative_to(ROOT)}")
    write_index(outputs)
    print(f"[index] {(SOURCE_DIR / 'final-exam.index.md').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
