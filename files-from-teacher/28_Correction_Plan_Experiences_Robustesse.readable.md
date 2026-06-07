# 28_Correction_Plan_Experiences_Robustesse.xlsx readable workbook

Source: `28_Correction_Plan_Experiences_Robustesse.xlsx`

Formula cells are preserved as `=formula`; cached values are shown after `->` when available.

## Sheet: Données & Effets

CORRECTION DE L'EXERCICE : PLAN CROISÉ & ROBUSTESSE
1. Tableau complet des essais avec Moyennes et Variances
Essai | A (Temp) | B (Temps) | C (Pré-trt) | Y (F1) : Basse % | Y (F2) : Haute % | Moyenne (Y_barre) | Variance (S²) |  | CME | s/B
1 | -1 | -1 | -1 | 7.2 | 8.8000000000000007 | =AVERAGE(E5:F5) -> 8 | =_xlfn.VAR.S(E5:F5) -> 1.2800000000000007 |  | =1/2*(1/E5^2+1/F5^2) -> 1.6101673298642996E-2 | =-10*LOG(J5) -> 17.931289893963445
2 | 1 | -1 | -1 | 5.5 | 5.9 | 5.7 | =_xlfn.VAR.S(E6:F6) -> 8.000000000000014E-2 |  | =1/2*(1/E6^2+1/F6^2) -> 3.0892614215065964E-2 | =-10*LOG(J6) -> 15.101453389909224
3 | -1 | 1 | -1 | 6.4 | 8.1999999999999993 | 7.3 | 1.6200000000000045 |  | 1.9643081220255799E-2 | 17.067903876286383
4 | 1 | 1 | -1 | 4.8 | 5 | 4.9000000000000004 | 2.0000000000000035E-2 |  | 4.1701388888888885E-2 | 13.798494803563248
5 | -1 | -1 | 1 | 6.9 | 7.5 | 7.2 | 0.1799999999999998 |  | 1.9390884268010923E-2 | 17.124023856628543
6 | 1 | -1 | 1 | 4.2 | 4.4000000000000004 | 4.3000000000000007 | 2.0000000000000035E-2 |  | 5.4171117482805786E-2 | 12.66232205365162
7 | -1 | 1 | 1 | 6.1 | 7.1 | 6.6 | 0.5 |  | 2.3355914982763487E-2 | 16.316031142815092
8 | 1 | 1 | 1 | 3.9 | 4.0999999999999996 | 4 | 1.9999999999999948E-2 |  | 6.2617309677209923E-2 | 12.033055955731697
 |  |  |  |  | moyenne générale | =AVERAGE(G5:G12) -> 6.0000000000000009 |  |  | MOYENNE | =AVERAGE(K5:K12) -> 15.254321871568656
2. Calcul des Effets Principaux (sur la Performance Moyenne)
 |  |  |  |  |  |  | TOTAL
 | A | B | C |  |  |  | =(E5-$G$14)^2 -> 1.4399999999999984 | =(F5-$G$14)^2 -> 7.839999999999999
SQ | =SUMPRODUCT(B5:B12,$G$5:$G$12) -> -10.199999999999998 | =SUMPRODUCT(C5:C12,$G$5:$G$12) -> -2.4000000000000004 | =SUMPRODUCT(D5:D12,$G$5:$G$12) -> -3.7999999999999989 |  |  |  | =(E6-$G$14)^2 -> 0.25000000000000089 | 1.0000000000000106E-2
EQ(+1) | =B18/8 -> -1.2749999999999997 | =C18/8 -> -0.30000000000000004 | -0.47499999999999987 |  |  |  | =(E7-$G$14)^2 -> 0.15999999999999959 | 4.8399999999999928
EQ(-1) | =-B19 -> 1.2749999999999997 | =-C19 -> 0.30000000000000004 | 0.47499999999999987 |  |  |  | =(E8-$G$14)^2 -> 1.4400000000000026 | 1.0000000000000018
 |  |  |  |  |  |  | =(E9-$G$14)^2 -> 0.80999999999999905 | 2.2499999999999973
E²Q(+1) | =B19*B19 -> 1.6256249999999992 | =C19*C19 -> 9.0000000000000024E-2 | =D19*D19 -> 0.22562499999999988 |  |  |  | =(E10-$G$14)^2 -> 3.2400000000000024 | 2.5600000000000018
 |  |  |  |  |  |  | =(E11-$G$14)^2 -> 9.9999999999997521E-3 | 1.2099999999999973
 |  |  |  |  |  |  | =(E12-$G$14)^2 -> 4.4100000000000037 | 3.6100000000000048
 |  |  |  |  |  | SCE(Total) | =SUM(H17:I24) -> 35.08
 |  |  |  |  | F(ddl Q, DDL residuel)
Source de Variance | (SCE) | (ddl) | (CME) | F-calculé | F-critique (5%) | Significativité
Facteur A | =16*B22 -> 26.009999999999987 | 1 | =B32/C32 -> 26.009999999999987 | =D32/$D$35 -> 77.641791044775886 | 4.75 | =IF(E32>F32, "Significatif", "Non Significatif") -> Significatif
Facteur B | =16*C22 -> 1.4400000000000004 | 1 | =B33/C33 -> 1.4400000000000004 | =D33/$D$35 -> 4.2985074626865574 | 4.75 | =IF(E33>F33, "Significatif", "Non Significatif") -> Non Significatif
Facteur C | =16*D22 -> 3.6099999999999981 | 1 | =B34/C34 -> 3.6099999999999981 | =D34/$D$35 -> 10.776119402985042 | 4.75 | =IF(E34>F34, "Significatif", "Non Significatif") -> Significatif
Résiduelle (Interactions + Rép.) | =B36-(B32+B33+B34) -> 4.0200000000000102 | 12 | =B35/C35 -> 0.33500000000000085 | - | - | -
Total | =H27 -> 35.08 | =SUM(C32:C35) -> 15
On règle A(-) et C(-)
Robustesse
 |  |  |  |  | s/B
 | A | B | C |  | 17.931289893963445 |  | SCE (Total)
Moyenne rép niv 1 + | =AVERAGE(K6,K8,K10,K12) -> 13.398831550713947 | =AVERAGE(K7,K8,K11,K12) -> 14.803871444599105 | =AVERAGE(K9:K12) -> 14.533858252206738 |  | 15.101453389909224 |  | =(F42-$F$50)^2 -> 7.1661577929242659
Moyenne rép niv 2 - | =AVERAGE(K5,K7,K9,K11) -> 17.109812192423366 | =AVERAGE(K5:K6,K9:K10) -> 15.704772298538209 | =AVERAGE(K5:K8) -> 15.974785490930575 |  | 17.067903876286383 |  | =(F43-$F$50)^2 -> 2.3368772684860133E-2
 |  |  |  |  | 13.798494803563248 |  | =(F44-$F$50)^2 -> 3.2890796878359692
 |  |  |  |  | 17.124023856628543 |  | 2.1194324519372247
 |  |  |  |  | 12.66232205365162 |  | 3.495785512936882
Effet moyen niv 1 | =B43-$K$14 -> -1.8554903208547096 | =C43-$K$14 -> -0.45045042696955129 | -0.72046361936191872 |  | 16.316031142815092 |  | 6.7184630560819514
Effet moyen niv 2 | =B44-$K$14 -> 1.8554903208547096 | 0.45045042696955306 | 0.72046361936191872 |  | 12.033055955731697 |  | =(F48-$F$50)^2 -> 1.1272265766506373
 |  |  |  | MOYENNE | =AVERAGE(F42:F49) -> 15.254321871568656 |  | =(F49-$F$50)^2 -> 10.376554100532923
 |  |  |  |  |  | SCE(Total) | =SUM(H43:H50) -> 34.316067951584714
Eq^2 | =B49^2 -> 3.4428443307855132 | =C49^2 -> 0.20290558715705265 | 0.51906782682407571
 | Facteurs | SCE | ddl | CME | F | F0,95(ddl Q, ddl R) |  | Décision
 | A | =B52*8 -> 27.542754646284106 | 1 | =C56/D56 -> 27.542754646284106 | =E56/$E$59 -> 110.44425840366226 | 7.71 |  | Facteur significatif
 | B | =C52*8 -> 1.6232446972564212 | 1 | =C57/D57 -> 1.6232446972564212 | =E57/$E$59 -> 6.5090823012632022 | 7.71 |  | facteur non significatif
 | C | =D52*8 -> 4.1525426145926057 | 1 | =C58/D58 -> 4.1525426145926057 | =E58/$E$59 -> 16.651366047010836 | 7.71 |  | Facteur significatif
 | Résidu | =C60-SUM(C56:C58) -> 0.99752599345158188 | =D60-SUM(D56:D58) -> 4 | =C59/D59 -> 0.24938149836289547
 | Total | 34.316067951584714 | 7
 |  | pareil on règle A(-), C(-) |  |  | comme A (-) et c(-)
N | 8
na | 2
nb | 2
nc | 2
nF | 2

## Sheet: Feuil1

[No readable cells detected]

## Sheet: ANAVAR & Robustesse

3. TABLEAU D'ANALYSE DE LA VARIANCE (ANAVAR)
Source de Variance | Somme des Carrés (SCE) | Degrés de liberté (ddl) | Carré Moyen (CME) | F-calculé | F-critique (5%) | Significativité
Facteur A | =16*'Données & Effets'!B22 -> 26.009999999999987 | 1 | =B4/C4 -> 26.009999999999987 | =D4/D$7 -> 77.641791044775886 | 4.75 | =IF(E4>F4, "Significatif", "Non Significatif") -> Significatif
Facteur B | =16*'Données & Effets'!C22 -> 1.4400000000000004 | 1 | =B5/C5 -> 1.4400000000000004 | =D5/D$7 -> 4.2985074626865574 | 4.75 | =IF(E5>F5, "Significatif", "Non Significatif") -> Non Significatif
Facteur C | =16*'Données & Effets'!D22 -> 3.6099999999999981 | 1 | =B6/C6 -> 3.6099999999999981 | =D6/D$7 -> 10.776119402985042 | 4.75 | =IF(E6>F6, "Significatif", "Non Significatif") -> Significatif
Résiduelle (Interactions + Rép.) | =B8-(B4+B5+B6) -> 4.0200000000000102 | 12 | =B7/C7 -> 0.33500000000000085 | - | - | -
Total | 35.08 | =SUM(C4:C7) -> 15
4. ANALYSE DE ROBUSTESSE ET CONFIGURATION OPTIMALE
Objectif de Performance : | Minimiser le taux d'huile moyen (Y).
Choix Performance : | Les effets de A (-1.75), C (-0.475) étant tous négatifs, il faut régler tous les facteurs au niveau haut (+1) pour minimiser Y. Soit la configuration A(+1) C(+1).
Analyse de Robustesse : | On observe sur l'onglet 1 que lorsque le facteur A est au niveau bas (-1), les variances S² entre F1 et F2 sont très élevées (jusqu'à 1.62). En revanche, lorsque A est au niveau haut (+1), les variances s'effondrent et deviennent presque nulles (0.02 ou 0.08).
Conclusion Robustesse : | Le réglage A = +1 (Température à 180°C) rend le procédé totalement insensible aux variations d'humidité de la patate douce (Facteur Bruit F).
RECOMMANDATION FINALE : | La configuration A = +1, B = +1, C = +1 est à la fois la plus performante (taux d'huile minimal à 4.0%) et la plus robuste (variance minimale de 0.02). Il y a convergence parfaite des objectifs.
