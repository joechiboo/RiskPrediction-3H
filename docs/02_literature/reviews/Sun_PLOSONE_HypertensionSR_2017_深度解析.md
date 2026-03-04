# Sun et al. (2017) PLoS ONE — 高血壓預測模型系統性回顧深度解析

> **論文**：Recent development of risk-prediction models for incident hypertension: An updated systematic review
> **期刊**：PLoS ONE, 2017; 12(10): e0187240
> **作者**：Dongdong Sun, Jielin Liu, Lei Xiao, Ya Liu, Zuoguang Wang, Chuang Li, Yongxin Jin, Qiong Zhao, Shaojun Wen
> **機構**：首都醫科大學 北京安貞醫院 高血壓研究室 / NIH NHLBI / Virginia Commonwealth University
> **DOI**：[10.1371/journal.pone.0187240](https://doi.org/10.1371/journal.pone.0187240)
> **PDF**：[Sun_Hypertension_SystematicReview_2017.pdf](../papers/Sun_Hypertension_SystematicReview_2017.pdf)
> **與本研究關聯度**：⭐⭐⭐⭐（Tier 2 — 高血壓預測模型的全景綜述，定位本研究的學術脈絡）

---

## 一句話摘要

**系統性回顧 26 篇文獻中 48 個高血壓預測模型（1990-2016），發現傳統因子（BMI、年齡、血壓、吸菸）仍是主流預測變數，pooled AUC = 0.767；遺傳風險分數(GRS)的加入效果有限（C-index 提升僅 0.3–0.5%），且所有模型均使用傳統統計方法（LR/Cox/Weibull），無一使用機器學習。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **研究類型** | 系統性文獻回顧 + Meta-analysis |
| **搜尋範圍** | PubMed + Embase，截至 2016-09-05 |
| **遵循指引** | PRISMA |
| **初始搜尋結果** | 7,332 篇 |
| **最終納入** | 26 篇，報告 48 個預測模型 |
| **總受試者** | 162,358 人 |
| **地區分布** | 美國 5、歐洲 5、中國 7、韓國 4、日本 2、伊朗 2、印度 1 |
| **追蹤期** | 3–30 年 |
| **高血壓定義** | 24/26 篇用 JNC-VII（SBP≥140 或 DBP≥90 或服藥） |

---

## 核心發現

### 1. 模型效能總覽

| 指標 | 範圍 | Pooled 值 |
|------|------|---------|
| **AUC** | 0.64 – 0.97 | **0.767** (95% CI: 0.742–0.792) |
| **C-statistic** | 60% – 90% | — |
| **異質性** | I² = 99.5% | 極高 |

### 2. 常用預測因子

| 預測因子 | 使用頻率 | 備註 |
|---------|---------|------|
| **年齡 (Age)** | 幾乎所有模型 | 最基本 |
| **BMI** | 幾乎所有模型 | 肥胖指標 |
| **SBP** | 多數模型 | 基線血壓 |
| **DBP** | 多數模型 | |
| **性別** | 多數模型 | |
| **吸菸** | 多數模型 | |
| **高血壓家族史** | 部分模型 | |
| 空腹血糖 | 少數模型 | 代謝因子 |
| TG / HDL-C | 少數模型 | 血脂指標 |
| 腰圍 | 少數模型 | 中心型肥胖 |
| GRS (遺傳風險分數) | 6/26 篇 | SNPs 2-32 個 |

### 3. 統計方法分布

| 方法 | 篇數 |
|------|------|
| Logistic regression | 12 |
| Cox regression | 7 |
| Weibull regression | 6 |
| Linear regression | 1 |
| **機器學習** | **0** |

→ **截至 2016 年，尚無一篇高血壓預測模型使用 ML 方法**（Ye 2018、Kanegae 2020 是後來的突破）

### 4. 遺傳風險分數 (GRS) 的效果

- 6 篇納入 GRS（SNPs 數量 2–32 個）
- 加入 GRS 後 C-index 提升僅 **0.3%–0.5%**（p<0.05 但幅度小）
- 原因：SNPs 數量有限、跨族群不一致、基因-環境交互作用未考慮
- **結論**：GRS 對預測的邊際貢獻有限，傳統因子仍是主力

### 5. 模型驗證狀況

| 驗證類型 | 篇數 | C-statistic 範圍 |
|---------|------|----------------|
| 內部驗證 (split-sample) | 7 | 0.79–0.90 |
| 外部驗證 | 3 | 0.733–0.77 |
| 無驗證 | 16 | — |

- **Framingham 模型**被 7 篇外部驗證：在美國白人/黑人表現良好，在韓國低估發生率，在**中國農村表現差**（C = 0.5–0.6）
- **結論**：「一個人群建的模型不能直接應用到另一個人群」

---

## 主要具名模型彙整

| 模型名稱 | 年份 | 國家 | AUC/C-stat | 特點 |
|---------|------|------|-----------|------|
| Johns Hopkins | 1990 | 美國 | NR | 最早，Age+SBP+父親HTN+BMI |
| **Framingham** | 2008 | 美國 | C=0.788 | 最常被外部驗證 |
| WHS | 2009 | 美國 | C=0.703-0.705 | 女性專用 |
| **Whitehall II** | 2009 | 英國 | C=0.80 | 加入重複測量 |
| ARIC/CHC | 2010 | 美國 | AUC=0.739-0.800 | 9 年追蹤 |
| TLGS | 2011 | 伊朗 | C=0.727-0.741 | 腰圍+CVD家族史 |
| Taiwan BP | 2011 | 台灣 | AUC=0.732-0.735 | 含 WBC+尿酸 |
| KoGES | 2013 | 韓國 | AUC=0.79 | 有外部驗證 |
| **SHIP** | 2013 | 德國 | AUC=0.78-0.79 | 含 SNP + 尿白蛋白 |
| **Otsuka (日本)** | 2015 | 日本 | C=0.861 | 職場健檢，最高 |
| InterASIA | 2015 | 中國 | C=0.650-0.774 | 加 SBP/DBP 後大幅提升 |

---

## 與本研究的關聯

### 本研究在此系統性回顧的脈絡中的定位

Sun (2017) 回顧了截至 2016 年的所有高血壓預測模型，揭示了幾個**尚未被填補的研究缺口**，而本研究正好回應了其中多個：

| Sun (2017) 指出的缺口 | 本研究的回應 |
|---------------------|---------|
| **無一使用機器學習** | ✅ 使用 8 種 ML 模型 + PySR |
| 多數僅用傳統因子 | ✅ 使用健檢數值 + Δ 變化量特徵 |
| 缺少中國人群的驗證 | ✅ 使用中國杭州人群資料 |
| 模型間缺乏系統性比較 | ✅ 8 模型平行比較 |
| 無可解釋性分析 | ✅ SHAP + PySR 符號回歸 |
| 僅預測高血壓 | ✅ 同時預測高血壓+高血糖+血脂異常 |
| 無類別不平衡處理 | ✅ SMOTE |
| Framingham 在中國農村表現差 | ✅ 本地化建模更適合中國人群 |

### 可引用的關鍵數據

- **Pooled AUC = 0.767**：截至 2016 年的傳統模型平均水準，可作為本研究的 benchmark
- **最高 C-stat = 0.861**（日本 Otsuka 2015）：傳統統計最佳，ML 後期突破
- **Framingham 在中國 C = 0.5-0.6**：強調本地化建模的必要性

---

## 研究限制（作者自述）

1. 多數模型**非專為預測模型設計**，資料品質參差
2. 部分研究樣本量過小
3. 跨人群泛化能力差
4. GRS 的 SNP 選擇缺乏標準化方法
5. 多數 BP 在醫院測量，可能有白袍效應
6. 無一模型在前瞻性研究中被證明能**改善臨床結局**
7. 僅 3 篇有外部驗證
8. Meta-analysis **異質性極高**（I² = 99.5%）

---

## 對本論文寫作的引用建議

### 第二章（文獻回顧）
- 作為高血壓預測模型的「全景地圖」引用，用一段話概述 48 個模型的現狀
- 引用 pooled AUC 0.767 作為傳統方法的基準線
- 強調「截至 2016 年無一篇使用機器學習」→ 引出 Ye (2018)、Kanegae (2020) 及本研究的 ML 貢獻
- 引用 Framingham 在中國表現差的結論，支持本地化建模

### 第七章（討論）
- 比較本研究 AUC 與 pooled AUC 0.767 及各模型
- 討論本研究如何填補 Sun (2017) 指出的多個研究缺口
- 支持「ML 優於傳統統計」的論點

---

## 關鍵引述

> "AUC ranged from 0.64 to 0.97, and C-statistic ranged from 60% to 90%."

> "The traditional models are still the predominant risk prediction models for hypertension."

> "A model derived from one particular population could not be directly applied to a distinct population, and the fittest model for one particular population is that derived from the same population."

> "The discrimination (C-statistics = 0.5 to 0.6) and calibration ability (p<0.0001) in rural Chinese was poor." [referring to Framingham model]