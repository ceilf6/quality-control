# 同学资料转换索引

本目录存放来自同学的复习资料。定位是 P3 辅助材料：可用于中文解释、术语对照、查漏补缺和自测，但不能决定期末范围、公式权威、TD 步骤或最终答案。

## 使用规则

1. 先查老师 P0：`files-from-teacher/final-exam.reviewed.md`、CM、TD、TD correction、Excel workbook、CM/TD ASR。
2. 同学资料只在 P0/P1 内容已经确定后，用来换一种中文说法、快速定位主题或做自测。
3. 如果同学资料和老师资料冲突，以老师 CM/TD/correction/workbook/ASR 为准，并在回答中说明冲突。
4. 公式题、表格填值题、ANAVAR、Fisher、控制图、CUSUM、SdF/FMDS 计算题，必须回看对应老师 P0 source 后再给考试答案。
5. 同一 TD 已有老师官方 correction 时，移除并不再使用对应同学答案；只有尚无老师 correction 时，才暂用同学完成版作 P3 参考。

## 转换清单

- P3 `FQ01_Plans_dexperiences_完整复习资料.pdf` -> `FQ01_Plans_dexperiences_完整复习资料.readable.txt`：Plans d'experiences review notes: DOE, effects, ANAVAR, Fisher, fractional plans and robustness.
  - Teacher anchor: Teacher P0 anchors: 25, 22, 24, 26, 27, 28, 29 and 30.
  - Extraction check: 15 pages extracted, replacement characters = 0.
- P3 `FQ01_系统可靠性_复习笔记.pdf` -> `FQ01_系统可靠性_复习笔记.readable.txt`：Surete de fonctionnement review notes: FMDS/RAMS, reliability, maintainability, availability and system reliability.
  - Teacher anchor: Teacher P0 anchors: 36, 38, 39, 40, 41, 42 and 43.
  - Extraction check: 12 pages extracted, replacement characters = 0.
- P3 `SPC统计过程控制_复习笔记.pdf` -> `SPC统计过程控制_复习笔记.readable.txt`：SPC review notes: p/np/c/u control charts, CUSUM and ARL.
  - Teacher anchor: Teacher P0 anchors: 34, 31, 33 and 35.
  - Extraction check: 7 pages extracted, replacement characters = 0.
- P3 `TD作业解答说明.pdf` -> `TD作业解答说明.readable.txt`：Classmate explanation of control-chart and CUSUM workbook tasks.
  - Teacher anchor: Teacher P0 anchors: 31, 33 and 35.
  - Extraction check: 5 pages extracted, replacement characters = 0.
- P3 `TD CUMSUM.xlsx` -> `TD CUMSUM.readable.md`：Byte-for-byte duplicate of the teacher P0 CUSUM TD workbook; retained only for provenance, not as an answer source.
  - Teacher anchor: Teacher P0 anchor: 33_TD CUMSUM.xlsx, with CM formula source 34.
  - Extraction check: 5 sheets, 1438 non-empty cells, 210 formula cells and 1 chart XML objects extracted.
- P3 `Copie de TD CUMSUM.xlsx` -> `Copie de TD CUMSUM.readable.md`：Classmate-completed CUSUM workbook with formula-filled tables and chart objects; temporary reference while no teacher CUSUM correction is available.
  - Teacher anchor: Teacher P0 anchor: 33_TD CUMSUM.xlsx, with CM formula source 34.
  - Extraction check: 5 sheets, 6110 non-empty cells, 4876 formula cells and 8 chart XML objects extracted.

## 工作簿变体说明

- `TD CUMSUM.xlsx` 与老师 `33_TD CUMSUM.xlsx` 完全相同；学习时只引用老师目录中的 P0 文件，避免重复题源。
- 当前老师资料中没有 CUSUM TD 的官方 correction；`Copie de TD CUMSUM.xlsx` 是暂用的 P3 参考，必须先按老师 `33_TD CUMSUM.xlsx` 和 CM `34` 核对公式、步骤与结论。
- 控制图 TD 已有老师 `35_TD control charts-correction.xlsx`，因此对应同学答案已移除。
- 每个 workbook 的 `.readable.md` 保留非空单元格坐标、公式和缓存值；每个 sheet 的 `.html` 用于查看表格结构。

## 已知不确定性

- PDF 没有使用 OCR；均有可抽取文本层。部分法语重音符号可能在 PDF 文本层丢失或错位，例如 `Sûreté` 可能被抽成 `S reté`。
- XLSX 输出保留公式文本和 Excel 保存的缓存值，但不会重新计算公式；没有缓存值的公式只显示公式本身。
- HTML 预览保留单元格表格，不复原 Excel 图表外观、条件格式、筛选、合并单元格或坐标轴；图表判断和数值结论必须回看原工作簿及对应老师 P0 文件。
- 公式、上下标、根号、分式和复杂表格在 PDF 文本层中可能丢失符号或错位。涉及考试作答时必须以老师 P0 文件为准。
- 同学资料可能包含整理者自己的总结和简化，不作为老师命题范围的证据。
