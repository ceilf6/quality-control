#!/usr/bin/env python3
"""Convert classmate-provided review materials into LLM-readable files."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import unicodedata
import zipfile
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "files-from-classmate"

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "ws": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


@dataclass(frozen=True)
class ClassmateMaterial:
    filename: str
    topic: str
    teacher_anchor: str


@dataclass(frozen=True)
class SheetContent:
    name: str
    slug: str
    rows: list[tuple[str, dict[int, str]]]
    max_column: int
    formula_count: int


@dataclass(frozen=True)
class ConversionResult:
    material: ClassmateMaterial
    output: Path
    extraction_check: str


MATERIALS = [
    ClassmateMaterial(
        "FQ01_Plans_dexperiences_完整复习资料.pdf",
        "Plans d'experiences review notes: DOE, effects, ANAVAR, Fisher, fractional plans and robustness.",
        "Teacher P0 anchors: 25, 22, 24, 26, 27, 28, 29 and 30.",
    ),
    ClassmateMaterial(
        "FQ01_系统可靠性_复习笔记.pdf",
        "Surete de fonctionnement review notes: FMDS/RAMS, reliability, maintainability, availability and system reliability.",
        "Teacher P0 anchors: 36, 38, 39, 40, 41, 42 and 43.",
    ),
    ClassmateMaterial(
        "SPC统计过程控制_复习笔记.pdf",
        "SPC review notes: p/np/c/u control charts, CUSUM and ARL.",
        "Teacher P0 anchors: 34, 31, 33 and 35.",
    ),
    ClassmateMaterial(
        "TD作业解答说明.pdf",
        "Classmate explanation of control-chart and CUSUM workbook tasks.",
        "Teacher P0 anchors: 31, 33 and 35.",
    ),
    ClassmateMaterial(
        "TD CUMSUM.xlsx",
        "Byte-for-byte duplicate of the teacher P0 CUSUM TD workbook; retained only for provenance, not as an answer source.",
        "Teacher P0 anchor: 33_TD CUMSUM.xlsx, with CM formula source 34.",
    ),
    ClassmateMaterial(
        "Copie de TD CUMSUM.xlsx",
        "Classmate-completed CUSUM workbook with formula-filled tables and chart objects; temporary reference while no teacher CUSUM correction is available.",
        "Teacher P0 anchor: 33_TD CUMSUM.xlsx, with CM formula source 34.",
    ),
]


def run(cmd: list[str]) -> str:
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError("Command failed: " + " ".join(cmd) + "\n" + result.stderr)
    return result.stdout


def normalize_text(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines).strip())


def clean_page(page: str) -> str:
    return normalize_text(page)


def readable_output_path(path: Path) -> Path:
    suffix = ".readable.md" if path.suffix.lower() == ".xlsx" else ".readable.txt"
    return path.with_suffix(suffix)


def convert_pdf(path: Path) -> tuple[str, int, int]:
    if shutil.which("pdftotext") is None:
        raise RuntimeError("pdftotext is required for PDF conversion")
    text = run(["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"])
    replacement_count = text.count("\ufffd")
    raw_pages = text.split("\f")
    pages = [clean_page(page) for page in raw_pages if clean_page(page)]
    body = "\n\n".join(f"## Page {index}\n\n{page}" for index, page in enumerate(pages, start=1))
    return body, len(pages), replacement_count


def column_index(cell_ref: str) -> int:
    letters = re.match(r"[A-Z]+", cell_ref)
    if not letters:
        return 1
    total = 0
    for char in letters.group(0):
        total = total * 26 + ord(char) - ord("A") + 1
    return total


def column_name(column: int) -> str:
    letters = ""
    while column:
        column, remainder = divmod(column - 1, 26)
        letters = chr(ord("A") + remainder) + letters
    return letters


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "sheet"


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
    relation_map = {
        relation.attrib["Id"]: relation.attrib["Target"].lstrip("/")
        for relation in rels.findall("rel:Relationship", NS)
    }
    sheets: list[tuple[str, str]] = []
    for sheet in workbook.findall(".//ws:sheet", NS):
        relationship_id = sheet.attrib.get(f"{{{NS['r']}}}id")
        target = relation_map.get(relationship_id or "")
        if target:
            sheets.append((sheet.attrib.get("name", "Sheet"), "xl/" + target.lstrip("xl/")))
    return sheets


def cell_value(cell: ET.Element, shared_strings: list[str]) -> str:
    formula = cell.find("ws:f", NS)
    value = cell.find("ws:v", NS)
    inline = cell.find(".//ws:is/ws:t", NS)
    if formula is not None and formula.text:
        formula_text = "=" + formula.text
        if value is not None and value.text is not None:
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


def sheet_content(root: ET.Element, sheet_name: str, shared_strings: list[str]) -> SheetContent:
    rows: list[tuple[str, dict[int, str]]] = []
    max_column = 0
    formula_count = 0
    for row in root.findall(".//ws:sheetData/ws:row", NS):
        values: dict[int, str] = {}
        for cell in row.findall("ws:c", NS):
            reference = cell.attrib.get("r", "A1")
            column = column_index(reference)
            max_column = max(max_column, column)
            if cell.find("ws:f", NS) is not None:
                formula_count += 1
            value = normalize_text(cell_value(cell, shared_strings))
            if value:
                values[column] = value
        if values:
            rows.append((row.attrib.get("r", "?"), values))
    return SheetContent(sheet_name, slugify(sheet_name), rows, max_column, formula_count)


def chart_summaries(zf: zipfile.ZipFile) -> list[str]:
    summaries = []
    for chart_path in sorted(
        name
        for name in zf.namelist()
        if name.startswith("xl/charts/chart") and name.endswith(".xml")
    ):
        root = ET.fromstring(zf.read(chart_path))
        text = " ".join(part.strip() for part in (node.text or "" for node in root.findall(".//a:t", NS)) if part.strip())
        label = Path(chart_path).name
        summaries.append(f"{label}: {text}" if text else f"{label}: chart XML detected; title text unavailable")
    return summaries


def render_row(row_number: str, values: dict[int, str]) -> str:
    return " | ".join(f"{column_name(column)}{row_number}: {value}" for column, value in values.items())


def preview_path(source: Path, sheet: SheetContent) -> Path:
    return source.with_name(f"{source.stem}.sheet-{sheet.slug}.html")


def write_sheet_preview(source: Path, material: ClassmateMaterial, sheet: SheetContent, charts: list[str]) -> Path:
    output = preview_path(source, sheet)
    headers = "".join(f"<th>{column_name(column)}</th>" for column in range(1, sheet.max_column + 1))
    rows = []
    for row_number, values in sheet.rows:
        cells = "".join(
            f"<td data-cell=\"{column_name(column)}{html.escape(row_number)}\">{html.escape(values.get(column, ''))}</td>"
            for column in range(1, sheet.max_column + 1)
        )
        rows.append(f"<tr><th scope=\"row\">{html.escape(row_number)}</th>{cells}</tr>")
    chart_items = "".join(f"<li>{html.escape(chart)}</li>" for chart in charts)
    chart_section = f"<h2>Workbook chart XML</h2><ul>{chart_items}</ul>" if charts else ""
    output.write_text(
        "\n".join(
            [
                "<!doctype html>",
                '<html lang="zh-CN">',
                "<head>",
                '<meta charset="utf-8">',
                f"<title>{html.escape(source.name)} - {html.escape(sheet.name)}</title>",
                "<style>",
                "body { font-family: Arial, sans-serif; margin: 24px; color: #1f2933; }",
                "main { max-width: 100%; }",
                "h1 { font-size: 22px; margin-bottom: 8px; }",
                "p { line-height: 1.5; }",
                ".notice { background: #fff8e1; border-left: 4px solid #c48a00; padding: 10px 12px; }",
                ".table-wrap { overflow: auto; border: 1px solid #cbd5e1; max-height: 80vh; }",
                "table { border-collapse: collapse; white-space: pre-wrap; font-size: 13px; }",
                "th, td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; vertical-align: top; }",
                "thead th { background: #edf2f7; position: sticky; top: 0; z-index: 2; }",
                "tbody th { background: #edf2f7; position: sticky; left: 0; z-index: 1; }",
                "</style>",
                "</head>",
                "<body><main>",
                f"<h1>{html.escape(source.name)} / Sheet: {html.escape(sheet.name)}</h1>",
                "<p><strong>Review priority:</strong> P3 classmate auxiliary material.</p>",
                f"<p><strong>Teacher P0 source:</strong> {html.escape(material.teacher_anchor)}</p>",
                "<p class=\"notice\">Formula text and cached values are shown when present. This preview does not reproduce Excel chart rendering, conditional formatting or formula recalculation; verify exam answers against the teacher P0 workbook.</p>",
                f"<p>Non-empty rows: {len(sheet.rows)}. Used columns: A-{column_name(sheet.max_column)}. Formula cells: {sheet.formula_count}.</p>",
                chart_section,
                "<div class=\"table-wrap\"><table><thead><tr><th>Row</th>" + headers + "</tr></thead><tbody>",
                *rows,
                "</tbody></table></div>",
                "</main></body></html>",
            ]
        ),
        encoding="utf-8",
    )
    return output


def convert_xlsx(path: Path, material: ClassmateMaterial) -> tuple[str, str]:
    lines = [
        f"# {path.name} readable workbook",
        "",
        f"Source: `{path.name}`",
        "Review priority: P3 classmate auxiliary material.",
        f"Teacher P0 source: {material.teacher_anchor}",
        "Use rule: this is for Chinese explanation and self-check only; do not use it to override teacher CM/TD/corrections/workbooks/ASR.",
        "",
        "Formula cells are preserved as `=formula`; cached values are shown after `->` when available. Every non-empty cell is emitted with its Excel address, so values remain traceable even in wide sheets.",
        "",
    ]
    with zipfile.ZipFile(path) as zf:
        shared_strings = read_shared_strings(zf)
        charts = chart_summaries(zf)
        if charts:
            lines.extend(["## Workbook Chart XML", ""])
            lines.extend(f"- {chart}" for chart in charts)
            lines.append("")
        sheets = []
        for sheet_name, target in workbook_sheets(zf):
            if target not in zf.namelist():
                lines.extend([f"## Sheet: {sheet_name}", "", "[Sheet XML not found]", ""])
                continue
            sheet = sheet_content(ET.fromstring(zf.read(target)), sheet_name, shared_strings)
            sheets.append(sheet)
            preview = write_sheet_preview(path, material, sheet, charts)
            lines.extend(
                [
                    f"## Sheet: {sheet.name}",
                    "",
                    f"- HTML preview: `{preview.name}`",
                    f"- Non-empty rows: {len(sheet.rows)}; used columns: A-{column_name(sheet.max_column)}; formula cells: {sheet.formula_count}.",
                    "",
                ]
            )
            lines.extend(render_row(row_number, values) for row_number, values in sheet.rows)
            lines.append("")
    total_cells = sum(sum(len(values) for _, values in sheet.rows) for sheet in sheets)
    total_formulas = sum(sheet.formula_count for sheet in sheets)
    check = f"{len(sheets)} sheets, {total_cells} non-empty cells, {total_formulas} formula cells and {len(charts)} chart XML objects extracted."
    return "\n".join(lines).rstrip(), check


def convert_material(material: ClassmateMaterial) -> ConversionResult:
    source = SOURCE_DIR / material.filename
    if not source.exists():
        raise FileNotFoundError(source)
    if source.suffix.lower() == ".pdf":
        body, page_count, replacement_count = convert_pdf(source)
        check = f"{page_count} pages extracted, replacement characters = {replacement_count}."
    elif source.suffix.lower() == ".xlsx":
        body, check = convert_xlsx(source, material)
    else:
        raise ValueError(f"Unsupported file type: {source}")
    out = readable_output_path(source)
    if source.suffix.lower() == ".pdf":
        header = [
            f"# {source.name}",
            "",
            f"- Source: `{source.name}`",
            "- Review priority: P3 classmate auxiliary material.",
            f"- Role: {material.topic}",
            f"- Teacher-source check: {material.teacher_anchor}",
            "- Use rule: use this file for Chinese explanation, terminology alignment and self-check only; do not use it to override teacher CM/TD/corrections/workbooks/ASR.",
            "- Extraction: `pdftotext -layout`; accents, math formulas and table alignment may still require checking the original PDF or the teacher P0 source.",
            "",
            "## Readable Content",
            "",
        ]
        body = "\n".join(header) + body
    out.write_text(body + "\n", encoding="utf-8")
    return ConversionResult(material, out, check)


def write_index(results: list[ConversionResult]) -> None:
    lines = [
        "# 同学资料转换索引",
        "",
        "本目录存放来自同学的复习资料。定位是 P3 辅助材料：可用于中文解释、术语对照、查漏补缺和自测，但不能决定期末范围、公式权威、TD 步骤或最终答案。",
        "",
        "## 使用规则",
        "",
        "1. 先查老师 P0：`files-from-teacher/final-exam.reviewed.md`、CM、TD、TD correction、Excel workbook、CM/TD ASR。",
        "2. 同学资料只在 P0/P1 内容已经确定后，用来换一种中文说法、快速定位主题或做自测。",
        "3. 如果同学资料和老师资料冲突，以老师 CM/TD/correction/workbook/ASR 为准，并在回答中说明冲突。",
        "4. 公式题、表格填值题、ANAVAR、Fisher、控制图、CUSUM、SdF/FMDS 计算题，必须回看对应老师 P0 source 后再给考试答案。",
        "5. 同一 TD 已有老师官方 correction 时，移除并不再使用对应同学答案；只有尚无老师 correction 时，才暂用同学完成版作 P3 参考。",
        "",
        "## 转换清单",
        "",
    ]
    for result in results:
        material = result.material
        lines.append(f"- P3 `{material.filename}` -> `{result.output.name}`：{material.topic}")
        lines.append(f"  - Teacher anchor: {material.teacher_anchor}")
        lines.append(f"  - Extraction check: {result.extraction_check}")
    lines.extend(
        [
            "",
            "## 工作簿变体说明",
            "",
            "- `TD CUMSUM.xlsx` 与老师 `33_TD CUMSUM.xlsx` 完全相同；学习时只引用老师目录中的 P0 文件，避免重复题源。",
            "- 当前老师资料中没有 CUSUM TD 的官方 correction；`Copie de TD CUMSUM.xlsx` 是暂用的 P3 参考，必须先按老师 `33_TD CUMSUM.xlsx` 和 CM `34` 核对公式、步骤与结论。",
            "- 控制图 TD 已有老师 `35_TD control charts-correction.xlsx`，因此对应同学答案已移除。",
            "- 每个 workbook 的 `.readable.md` 保留非空单元格坐标、公式和缓存值；每个 sheet 的 `.html` 用于查看表格结构。",
            "",
            "## 已知不确定性",
            "",
            "- PDF 没有使用 OCR；均有可抽取文本层。部分法语重音符号可能在 PDF 文本层丢失或错位，例如 `Sûreté` 可能被抽成 `S reté`。",
            "- XLSX 输出保留公式文本和 Excel 保存的缓存值，但不会重新计算公式；没有缓存值的公式只显示公式本身。",
            "- HTML 预览保留单元格表格，不复原 Excel 图表外观、条件格式、筛选、合并单元格或坐标轴；图表判断和数值结论必须回看原工作簿及对应老师 P0 文件。",
            "- 公式、上下标、根号、分式和复杂表格在 PDF 文本层中可能丢失符号或错位。涉及考试作答时必须以老师 P0 文件为准。",
            "- 同学资料可能包含整理者自己的总结和简化，不作为老师命题范围的证据。",
            "",
        ]
    )
    (SOURCE_DIR / "classmate-materials.index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    results = []
    for material in MATERIALS:
        result = convert_material(material)
        results.append(result)
        print(f"[converted] {material.filename} -> {result.output.relative_to(ROOT)} ({result.extraction_check})")
    write_index(results)
    print(f"[index] {(SOURCE_DIR / 'classmate-materials.index.md').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
