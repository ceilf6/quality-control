#!/usr/bin/env python3
"""Convert classmate-provided review PDFs into LLM-readable files."""

from __future__ import annotations

import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "files-from-classmate"


@dataclass(frozen=True)
class ClassmateMaterial:
    filename: str
    topic: str
    teacher_anchor: str


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


def readable_output_path(path: Path) -> Path:
    return path.with_suffix(".readable.txt")


def clean_page(page: str) -> str:
    lines = [line.rstrip() for line in page.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    text = "\n".join(lines).strip()
    return re.sub(r"\n{3,}", "\n\n", text)


def convert_pdf(path: Path) -> tuple[str, int, int]:
    if shutil.which("pdftotext") is None:
        raise RuntimeError("pdftotext is required for PDF conversion")
    text = run(["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"])
    replacement_count = text.count("\ufffd")
    raw_pages = text.split("\f")
    pages = [clean_page(page) for page in raw_pages if clean_page(page)]
    return "\n\n".join(f"## Page {index}\n\n{page}" for index, page in enumerate(pages, start=1)), len(pages), replacement_count


def convert_material(material: ClassmateMaterial) -> tuple[ClassmateMaterial, Path, int, int]:
    source = SOURCE_DIR / material.filename
    if not source.exists():
        raise FileNotFoundError(source)
    body, page_count, replacement_count = convert_pdf(source)
    out = readable_output_path(source)
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
    out.write_text("\n".join(header) + body + "\n", encoding="utf-8")
    return material, out, page_count, replacement_count


def write_index(results: list[tuple[ClassmateMaterial, Path, int, int]]) -> None:
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
        "",
        "## 转换清单",
        "",
    ]
    for material, out, page_count, replacement_count in results:
        lines.append(f"- P3 `{material.filename}` -> `{out.name}`：{material.topic}")
        lines.append(f"  - Teacher anchor: {material.teacher_anchor}")
        lines.append(f"  - Extraction check: {page_count} pages extracted, replacement characters = {replacement_count}.")
    lines.extend(
        [
            "",
            "## 已知不确定性",
            "",
            "- 本次没有使用 OCR；PDF 均有可抽取文本层。",
            "- 部分法语重音符号可能在 PDF 文本层丢失或错位，例如 `Sûreté` 可能被抽成 `S reté`；生成法语考试答案时必须回看老师原文。",
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
        _, out, page_count, replacement_count = result
        print(f"[converted] {material.filename} -> {out.relative_to(ROOT)} ({page_count} pages, replacement={replacement_count})")
    write_index(results)
    print(f"[index] {(SOURCE_DIR / 'classmate-materials.index.md').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
