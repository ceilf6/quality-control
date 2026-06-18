# 同学资料转换索引

本目录存放来自同学的复习资料。定位是 P3 辅助材料：可用于中文解释、术语对照、查漏补缺和自测，但不能决定期末范围、公式权威、TD 步骤或最终答案。

## 使用规则

1. 先查老师 P0：`files-from-teacher/final-exam.reviewed.md`、CM、TD、TD correction、Excel workbook、CM/TD ASR。
2. 同学资料只在 P0/P1 内容已经确定后，用来换一种中文说法、快速定位主题或做自测。
3. 如果同学资料和老师资料冲突，以老师 CM/TD/correction/workbook/ASR 为准，并在回答中说明冲突。
4. 公式题、表格填值题、ANAVAR、Fisher、控制图、CUSUM、SdF/FMDS 计算题，必须回看对应老师 P0 source 后再给考试答案。

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

## 已知不确定性

- 本次没有使用 OCR；PDF 均有可抽取文本层。
- 部分法语重音符号可能在 PDF 文本层丢失或错位，例如 `Sûreté` 可能被抽成 `S reté`；生成法语考试答案时必须回看老师原文。
- 公式、上下标、根号、分式和复杂表格在 PDF 文本层中可能丢失符号或错位。涉及考试作答时必须以老师 P0 文件为准。
- 同学资料可能包含整理者自己的总结和简化，不作为老师命题范围的证据。
