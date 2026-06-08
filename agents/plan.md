# 质量管理期末复习路线计划

## Summary

本计划只按知识点组织，不按时间推进。当前阶段为期末考试复习，最高优先级来源是 `files-from-teacher/final-exam.reviewed.md`、`32_SujetExam_tytpe.readable.txt`、期末 TD、TD correction 和 Excel workbook/correction。

期中旧计划以 `21-期中截止_TD3-CHEROUAT.pdf` 为边界，现已不再作为复习边界。期中资料只用于补质量管理基础，不应覆盖期末题源。

默认主线：Sujet type 题型 -> Plan d'expériences -> effets/interactions -> ANAVAR/Fisher -> configuration optimale -> plan fractionnaire -> plan croisé/robustesse -> cartes p/np/c/u -> CUSUM -> sûreté de fonctionnement/FMDS。

## Source Map

- `files-from-teacher/final-exam.reviewed.md`：期末人工整理入口，先读。
- `files-from-teacher/final-exam.index.md`：期末转换索引。
- `files-from-teacher/32_SujetExam_tytpe.readable.txt`：期末题型最高优先级来源。
- `files-from-teacher/22_FQ01_USTEUS_TD1_Enoncé_2026.readable.txt`：DOE TD1 题干。
- `files-from-teacher/29_FQ01_UTSEUS_TD1_correction 2.readable.txt`：DOE TD1 correction。
- `files-from-teacher/24_FQ01_USTEUS_TD2.readable.txt`：DOE TD2 题干。
- `files-from-teacher/30_FQ01_USTEUS_TD2_correction.readable.txt`：DOE TD2 correction。
- `files-from-teacher/26_Enonce_TD_3.readable.txt`：plan croisé 与 robustesse 题干。
- `files-from-teacher/28_Correction_Plan_Experiences_Robustesse.readable.md`：robustesse correction。
- `files-from-teacher/27_UTSEUS_TD_PlanExp_Corrigé_2023.readable.md`：DOE workbook correction。
- `files-from-teacher/31_TD control charts.readable.md`：attribute control charts 数据。
- `files-from-teacher/35_TD control charts-correction.readable.md`：attribute control charts correction。
- `files-from-teacher/33_TD CUMSUM.readable.md`：CUSUM workbook。
- `files-from-teacher/25_USTEUS_Cours_PlanExp_2026.readable.txt`：DOE 课程。
- `files-from-teacher/23_Lecture table Fisher.readable.md`：Fisher 查表。
- `files-from-teacher/34_FQ01-UTSEUS-Part 5-P26 2.readable.txt`：SPC、attribute charts、CUSUM 课程。
- `files-from-teacher/36_FQ01P2006.readable.txt`：SdF/FMDS 课程课件。
- `files-from-teacher/37_FQ01_P26_SdF_CM_Seance1_720p.asr.fr.txt`：SdF 第一讲视频 ASR，用于补老师口头解释。

## Knowledge Route

1. **期末题型识别**
   先读 Sujet type，掌握题型：V/F、步骤排序、ANAVAR 判读、DOE 计算题。
   来源：`32_SujetExam_tytpe.readable.txt`

2. **Plan d'expériences 基础**
   学会 DOE 的目的：同时研究多个 factors，量化 effects/interactions，用较少 essais 找到最优 configuration。
   来源：`final-exam.reviewed.md`，`25_USTEUS_Cours_PlanExp_2026.readable.txt`

3. **DOE 步骤排序**
   掌握 formalisation -> choix table -> essais -> effects -> ANAVAR -> modèle -> configuration optimale。
   来源：`32_SujetExam_tytpe.readable.txt`

4. **效应与交互作用**
   学会主效应、interaction、effect plot、interaction plot；理解 effect 的正负如何服务 minimiser/maximiser 目标。
   来源：`22_FQ01_USTEUS_TD1_Enoncé_2026.readable.txt`，`29_FQ01_UTSEUS_TD1_correction 2.readable.txt`

5. **ANAVAR 与显著性**
   掌握 `CME=SCE/ddl`、`F=CME_facteur/CME_residuelle`、`F>Fseuil` 判显著。
   来源：`32_SujetExam_tytpe.readable.txt`，`29_FQ01_UTSEUS_TD1_correction 2.readable.txt`，`30_FQ01_USTEUS_TD2_correction.readable.txt`

6. **Fisher 查表**
   学会用 factor ddl、residual ddl、alpha 读 `F critique`。
   来源：`23_Lecture table Fisher.readable.md`

7. **完整因子设计与 2^k**
   掌握 `2^k` 试验数、repetition、A/B/C/AB/AC/BC/ABC 效应、显著项模型。
   来源：`24_FQ01_USTEUS_TD2.readable.txt`，`30_FQ01_USTEUS_TD2_correction.readable.txt`

8. **最优配置选择**
   学会先判断目标是 minimiser 还是 maximiser，再根据显著 effects/interactions 选 factor levels。
   来源：`29_FQ01_UTSEUS_TD1_correction 2.readable.txt`，`30_FQ01_USTEUS_TD2_correction.readable.txt`

9. **Plan fractionnaire 与 confusion**
   掌握 fractional plan 的效率和代价：减少 essais，但可能混杂主效应与 interaction。
   来源：`24_FQ01_USTEUS_TD2.readable.txt`，`30_FQ01_USTEUS_TD2_correction.readable.txt`

10. **Plan croisé 与 robustesse**
    学会 controlled factors、noise factor、performance moyenne、variance/S/B、robust configuration。
    来源：`26_Enonce_TD_3.readable.txt`，`28_Correction_Plan_Experiences_Robustesse.readable.md`

11. **Attribute control charts**
    区分 p-chart、np-chart、c-chart、u-chart 的使用条件和控制限公式。
    来源：`31_TD control charts.readable.md`，`35_TD control charts-correction.readable.md`，`34_FQ01-UTSEUS-Part 5-P26 2.readable.txt`

12. **CUSUM**
    掌握 target、k、H、C+、C-、small shift detection 和 out-of-control 判断。
    来源：`33_TD CUMSUM.readable.md`，`34_FQ01-UTSEUS-Part 5-P26 2.readable.txt`

13. **Sûreté de fonctionnement / FMDS**
    掌握 FMDS/RAMS、fiabilité/maintenabilité/disponibilité/sécurité、`R(t)`、`M(t)`、`A(t)`、失效率、修复率、MTTF/MTTR/MTBF、指数分布、Weibull、串并联系统。
    来源：`36_FQ01P2006.readable.txt`，`37_FQ01_P26_SdF_CM_Seance1_720p.asr.fr.txt`

14. **期中旧知识补基础**
    CNQ、TRG、学习型质量管理、AI/ML 只在期末题源需要时补充。
    来源：`notes/ceilf6/_知识点.md` 和期中 TD。

## Review Method

每次只学一个小知识点，固定用这个结构：

1. 前置概念：先补零基础需要的词。
2. 核心定义：用简单话解释。
3. 为什么重要：说明质量管理中的作用。
4. 考试问法：从 P0 题源中提炼常见题型。
5. 答题模板：用法语给出可背答案，必要时附中文翻译。
6. 易错点：说明容易混淆处。
7. 小练习：立刻做一道检查理解。

遇到题目时使用：

1. 题目：法语原题或重构后的法语题干；必要时附中文翻译。
2. 解析：中文讲思路、公式、单位、查表方法、易错点。
3. 答案：法语完整考试版；必要时附中文翻译。

即使 correction 或 Excel 中题目和答案混排，也必须重新组织为“题目 -> 解析 -> 答案”。

## Test Scenarios

- V/F：DOE 作用、专家解释、DOE 效率、ANAVAR 判读。
- 排序题：DOE 执行和分析步骤。
- 表格判读：ANAVAR 的 SCE、ddl、CME、F、Fseuil。
- 计算题：effects、interactions、ANAVAR、Fisher、模型、configuration optimale。
- Robustesse：mean response、variance、noise factor、S/B、trade-off。
- Control charts：p/np/c/u 的选择和控制限计算。
- CUSUM：C+、C-、k、H、失控判断。
- SdF/FMDS：R(t)、M(t)、A(t)、失效率、指数分布、Weibull、串联系统、并联系统。

## Visual And Table Discipline

遇到 ANAVAR、Fisher、控制图、CUSUM、Excel workbook、复杂表格或公式时，不要只凭 OCR/readable 文本猜。必须优先回看对应 readable workbook 的公式缓存值；如仍不清楚，打开原文件或生成 HTML 可视化解释。

`TODO.md` 曾标记“控制图 X, R 的计算公式有问题”。讲控制图时不要沿用旧 X/R 公式笔记，优先使用老师表格、期末 control charts correction 和课程公式。

遇到 SdF 视频 ASR 中的公式、变量名或法语术语不自然时，必须回到 `36_FQ01P2006.pdf` 或 `36_FQ01P2006.readable.txt` 核对；ASR 只作为口头解释辅助，不作为公式来源。

## Assumptions

- 当前复习范围首先由期末 P0 题源决定。
- 期中资料不是废弃，只是降级为基础补充。
- 如果用户说“继续复习”，默认沿 `Knowledge Route` 从当前未掌握的最小知识点继续，而不是按日期推进。
