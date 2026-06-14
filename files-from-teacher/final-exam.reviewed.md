# 质量管理期末复习人工整理入口

本文件用于期末复习。最新范围：期末只考期中考试之后最近 7 周内容，也就是编号 21 之后的老师资料。`21-期中截止_TD3-CHEROUAT.pdf` 及其之前的内容不作为期末考点。

老师最新口径：“Bonjour, si vous comprenez le CM et TD, il n'y aura pas de problèmes pour l'examen final.” 因此复习建设必须把 CM 与 TD 提到最高优先级；`32_SujetExam_tytpe.pdf` 用于校准题型和答题颗粒度，但不替代 CM/TD。

## 使用纪律

1. 期末复习优先级：CM/TD -> TD correction 与 Excel workbook -> Sujet type -> 统计表/概率表。期中前资料只作为必要前置概念或查表辅助，不作为期末考点。
2. CM/TD 用于判断复习范围、核心公式、老师强调和解题步骤；Sujet type 用于判断题型、答案颗粒度、步骤顺序和常见陷阱。
3. 教学解释用中文；考试答案、答题模板、题目最终作答用法语，并保持简洁可背。
4. 遇到题目时固定输出：题目 -> 解析 -> 答案。即使 correction 先给答案，也要先重构题目，再讲思路，最后给法语考试版答案。
5. Excel 和 PDF 的公式/表格识别可能错位；遇到 ANAVAR、Fisher、控制图、CUSUM、图形判断题时，必须回看原文件或 readable workbook 中的公式缓存值。

## 最高优先级来源：CM/TD

- `25_USTEUS_Cours_PlanExp_2026.readable.txt`：Plan d'expériences CM，提供 DOE 步骤、效应、ANAVAR、Fisher、fractional plan 等公式来源。
- `22_FQ01_USTEUS_TD1_Enoncé_2026.readable.txt` 与 `29_FQ01_UTSEUS_TD1_correction 2.readable.txt`：DOE TD1 与 correction，校准完整因子设计、多水平因子、重复试验、效应、ANAVAR、最优设置。
- `24_FQ01_USTEUS_TD2.readable.txt` 与 `30_FQ01_USTEUS_TD2_correction.readable.txt`：DOE TD2 与 correction，校准 2^k、显著因素、模型、fractional plan 和 confusion/alias。
- `26_Enonce_TD_3.readable.txt` 与 `28_Correction_Plan_Experiences_Robustesse.readable.md`：plan croisé 与 robustesse，包含均值、方差、S/B、ANAVAR、最终配置。
- `34_FQ01-UTSEUS-Part 5-P26 2.readable.txt`：SPC/CUSUM CM，提供 p/np/c/u 控制图与 CUSUM 公式来源。
- `31_TD control charts.readable.md` 与 `35_TD control charts-correction.readable.md`：属性控制图 TD 与 correction，重点 p-chart/u-chart。
- `33_TD CUMSUM.readable.md`：CUSUM TD workbook，重点 C+、C-、k、H、ARL、失控判断。
- `36_FQ01P2006.readable.txt`：SdF/FMDS CM 课件，覆盖 RAMS/FMDS、R(t)、M(t)、A(t)、失效率、修复率、MTTF/MTTR/MTBF、指数分布、Weibull、串并联系统和相关练习。
- `38_FQ01_P26_SdF_CM_Seance1_360p.asr.fr.txt` 与 `40_FQ01_P26_SdF_CM_Seance2_360p.asr.fr.txt`：SdF CM 视频 ASR，用于补老师口头解释。
- `39_FQ01_P26_SdF_TD1_360p.asr.fr.txt` 与 `41_FQ01_P26_SdF_TD2_360p.asr.fr.txt`：SdF TD 视频 ASR，用于补老师口头讲题步骤和易错点。

## 题型校准来源

- `32_SujetExam_tytpe.readable.txt`：期末题型校准来源。暴露 DOE 的 V/F、步骤排序、ANAVAR 判读和计算题。若与 CM/TD 的范围或公式冲突，以 CM/TD 为准。
- `23_Lecture table Fisher.readable.md`：Fisher 查表辅助来源，用于确定 ddl 与 alpha 下的临界值。

## 期末题型信号

### 1. DOE 判断题

来自 `32_SujetExam_tytpe.readable.txt` Q1。

常考判断：

- DOE 能量化并排序 factors 和 interactions 对 response 的影响。
- DOE 的结果不只给专家用；考试中说“只能由 experts 解释”通常是错。
- DOE 比同样数量但未规划的 essais 更有效。

法语答题模板：

> Un plan d'expériences permet d'étudier simultanément plusieurs facteurs, de quantifier leurs effets et interactions, puis de choisir une configuration optimale avec un nombre d'essais maîtrisé.

### 2. DOE 步骤排序

来自 `32_SujetExam_tytpe.readable.txt` Q2 和 `25_USTEUS_Cours_PlanExp_2026.readable.txt`。

推荐顺序：

1. Phase de formalisation。
2. Construction du plan / choix de la table d'essai。
3. Réalisation des essais。
4. Calcul des effets des facteurs et interactions。
5. Réalisation de l'ANAVAR et identification des facteurs/interactions significatifs。
6. Modélisation de l'influence des facteurs sur la réponse et validation du modèle。
7. Choix de la configuration optimale。

易错点：不要把 ANAVAR 放在试验前；不要先选最优配置再建模。

### 3. ANAVAR 判读

来自 `32_SujetExam_tytpe.readable.txt` Q3、TD1/TD2 corrections、Fisher 表说明。

必会：

- `CME = SCE / ddl`。
- `F = CME_facteur / CME_residuelle`。
- 若 `F > Fseuil`，因素或交互作用显著。
- 影响最大通常看 SCE、F 或效应大小；在 sujet type 的 ANAVAR 中 A 最大。
- 因子有 `m` 个水平时 `ddl = m - 1`；若 ddl=2，则该因子是 3 modalités，不是 2 modalités。
- Total ddl = N - 1，所以 total ddl=17 表示 plan 有 18 essais。

法语答题模板：

> Le facteur est significatif si la statistique de Fisher calculée est supérieure à la valeur critique. Ici, comme F > Fseuil, l'effet du facteur est statistiquement significatif au seuil considéré.

### 4. TD1 多水平完整设计

来源：`22_FQ01_USTEUS_TD1_Enoncé_2026.readable.txt` 与 `29_FQ01_UTSEUS_TD1_correction 2.readable.txt`。

要会做：

- 对每个 factor modality 计算平均响应和 effect。
- 对 interaction 计算组合效应。
- 建 ANAVAR：SCE、ddl、CME、F、F critique、significativité。
- 画显著因素的 effect plot 或 interaction plot。
- 根据目标选择 réglage：最小化 solvant résiduel 或最大化 résistance。

考试策略：先写目标是 minimiser 还是 maximiser；最后配置必须和目标方向一致。

### 5. TD2 2^k 与 fractional plan

来源：`24_FQ01_USTEUS_TD2.readable.txt` 与 `30_FQ01_USTEUS_TD2_correction.readable.txt`。

要会做：

- 计算 plan `2^k` 的 essai 数；若有 repetitions，要乘以 repetition 数。
- 计算主效应与 interactions：A、B、C、AB、AC、BC、ABC。
- 用 ANAVAR 判断显著因素和 interaction。
- 写模型时只保留 significant terms，避免把非显著项硬塞进去。
- fractional plan 中要说明 confusion/alias：某些主效应和交互作用无法区分。

法语答题模板：

> Le modèle retenu ne doit conserver que les facteurs et interactions significatifs. Les effets non significatifs sont intégrés dans l'erreur résiduelle ou écartés de l'interprétation.

### 6. Plan croisé 与 robustesse

来源：`26_Enonce_TD_3.readable.txt` 与 `28_Correction_Plan_Experiences_Robustesse.readable.md`。

要会做：

- 区分 facteurs contrôlés 与 facteur bruit。
- 对每个 essai 计算 performance moyenne 和 variance。
- 分别对平均 performance 与 robustesse 指标做 effect/ANAVAR。
- 目标可能冲突：一个配置 performance 最优，另一个配置 robustesse 最优；最终要解释 trade-off。
- `28_Correction...` 中结论示例：A、C 显著；robustesse 分析也指向 A 与 C；最终选择要兼顾 performance 与 variance/S/B。

法语答题模板：

> La configuration finale doit satisfaire à la fois l'objectif de performance moyenne et l'objectif de robustesse. On privilégie donc un réglage qui donne une réponse proche de la cible tout en réduisant la variabilité due au facteur bruit.

### 7. Fisher 表

来源：`23_Lecture table Fisher.readable.md`。

查表三件事：

- factor 的 ddl。
- residuelle 的 ddl。
- confidence/error level，常见 `alpha = 5%`。

法语答题模板：

> La valeur critique de Fisher se lit avec les degrés de liberté du facteur au numérateur, les degrés de liberté de la résiduelle au dénominateur, et le seuil de risque alpha choisi.

### 8. 属性控制图 p/np/c/u

来源：`34_FQ01-UTSEUS-Part 5-P26 2.readable.txt`、`31_TD control charts.readable.md`、`35_TD control charts-correction.readable.md`。

必须区分：

- p-chart：proportion defective，可处理样本量变化。
- np-chart：number of defectives，要求 subgroup sample size 相等。
- c-chart：number of defects，通常单位机会固定。
- u-chart：defects per unit，适合单位数量/样本量变化。

常用公式：

- `p_i = d_i / n_i`，`p_bar = sum d_i / sum n_i`。
- p-chart variable n：`UCL_i = p_bar + 3 sqrt(p_bar(1-p_bar)/n_i)`，`LCL_i = max(0, p_bar - 3 sqrt(p_bar(1-p_bar)/n_i))`。
- `u_i = c_i / n_i`，`u_bar = sum c_i / sum n_i`。
- u-chart：`UCL_i = u_bar + 3 sqrt(u_bar/n_i)`，`LCL_i = max(0, u_bar - 3 sqrt(u_bar/n_i))`。

注意：`TODO.md` 曾标出 X/R 控制图公式有问题；期末讲控制图时不要沿用旧笔记中的 X/R 公式，必须优先回看老师表和 correction。

### 9. CUSUM

来源：`33_TD CUMSUM.readable.md` 与 `34_FQ01-UTSEUS-Part 5-P26 2.readable.txt`。

必会：

- CUSUM 比 Shewhart chart 更适合发现 small shift。
- 常见参数：target `mu0`，reference value `k`，decision interval `H`。
- 递推思想：`C+` 累积高于目标的偏移，`C-` 累积低于目标的偏移。
- 若 `C+` 或 `C-` 超过 decision interval，要判断 process out of control。

法语答题模板：

> La carte CUSUM cumule les écarts successifs par rapport à la cible. Elle est plus sensible aux petits décalages qu'une carte de Shewhart classique.

### 10. Sûreté de fonctionnement / FMDS

来源：`36_FQ01P2006.readable.txt`、`38_FQ01_P26_SdF_CM_Seance1_360p.asr.fr.txt`、`40_FQ01_P26_SdF_CM_Seance2_360p.asr.fr.txt`、`39_FQ01_P26_SdF_TD1_360p.asr.fr.txt`、`41_FQ01_P26_SdF_TD2_360p.asr.fr.txt`。

定位：老师明确提到 CM/TD 后，SdF 的 CM PDF、CM ASR、TD ASR 都属于 P0 复习来源。公式、变量和图表以 `36_FQ01P2006.readable.txt` 为准；ASR 用于补老师口头解释、TD 解题步骤和易错点。

必会：

- FMDS/RAMS：fiabilité, maintenabilité, disponibilité, sécurité。
- 区分 fiabilité 与 disponibilité：fiabilité 关注区间 `[0,t]` 内不失效，disponibilité 关注某一时刻可用。
- 基本变量：寿命 `T`、维修时间 `S`、密度 `f_T(t)`、分布函数 `F_T(t)`、可靠度 `R(t)=P(T>t)`。
- 失效率 `lambda(t)` 与修复率 `mu(t)` 的意义。
- MTTF、MTTR、MUT、MDT、MTBF、渐近可用度 `A_infty`。
- 指数分布：`R(t)=exp(-lambda t)`、`MTTF=1/lambda`、无记忆性。
- Weibull 分布：形状参数 `beta` 控制失效率趋势；`beta<1` 递减，`beta=1` 退化为指数分布，`beta>1` 递增。
- 串联系统：所有组件都工作才工作，可靠度通常相乘。
- 并联系统：至少一个组件工作即可，可靠度用失效概率互补计算。

法语答题模板：

> La sûreté de fonctionnement regroupe la fiabilité, la maintenabilité, la disponibilité et la sécurité. La fiabilité décrit la probabilité de fonctionner sans défaillance pendant une durée donnée, tandis que la disponibilité décrit l'aptitude à être en état de fonctionner à un instant donné.

## 期末知识点优先级

1. Plan d'expériences：概念、步骤、V/F。
2. Effets des facteurs et interactions：主效应、交互作用、模型。
3. ANAVAR/Fisher：显著性判断、ddl、SCE/CME/F。
4. Configuration optimale：按 minimiser/maximiser 选择设置。
5. Plan fractionnaire：alias/confusion、不可区分效应。
6. Plan croisé/robustesse：平均响应、方差、S/B、噪声因素。
7. Attribute control charts：p、np、c、u 的适用条件和控制限。
8. CUSUM：C+、C-、k、H、small shift detection。
9. Sûreté de fonctionnement：FMDS/RAMS、R(t)、M(t)、A(t)、失效率、修复率、指数分布、Weibull、串并联系统。
10. 期中前内容：CNQ/TRG/学习型质量/AI 不作为期末考点；只有编号 22 之后资料再次明确出现时才纳入复习。

## 复习智能体默认输出格式

题目：法语原题或重构后的法语题干；必要时附中文解释。

解析：中文讲思路、公式、查表方法、单位和易错点。

答案：法语完整考试版，短而可背；必要时附中文翻译。
