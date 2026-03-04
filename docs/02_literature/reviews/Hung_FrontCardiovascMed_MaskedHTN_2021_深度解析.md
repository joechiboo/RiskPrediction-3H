# Hung et al. (2021) Front Cardiovasc Med — 隱匿性高血壓 ML 預測深度解析

> **論文**：Prediction of Masked Hypertension and Masked Uncontrolled Hypertension Using Machine Learning
> **期刊**：Frontiers in Cardiovascular Medicine, 2021; 8: 778306
> **作者**：Ming-Hui Hung, Ling-Chieh Shih, Yu-Ching Wang, Hsin-Bang Leu, Po-Hsun Huang, Tao-Cheng Wu, Shing-Jong Lin, Wen-Harn Pan, Jaw-Wen Chen, Chin-Chou Huang
> **機構**：國立陽明交通大學 / 台北榮民總醫院 / 中央研究院
> **DOI**：[10.3389/fcvm.2021.778306](https://doi.org/10.3389/fcvm.2021.778306)
> **PDF**：[Hung_FrontCardiovascMed_Hypertension_2021.pdf](../papers/Hung_FrontCardiovascMed_Hypertension_2021.pdf)
> **與本研究關聯度**：⭐⭐⭐（Tier 2 — 台灣高血壓人群 ML 預測，使用 SMOTE-NC + RF/XGBoost/ANN）

---

## 一句話摘要

**使用台灣兩個世代（Cohort 1: 970 人、Cohort 2: 416 人外部驗證）的高血壓患者門診資料 + 24 小時動態血壓監測，以 LR、RF、XGBoost、ANN 預測隱匿性高血壓（MH/MUCH），RF 模型僅需 6 個變數即達最佳效能（內部驗證 AUC 0.851、外部驗證 0.837），sensitivity 1.000、NPV 1.000。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **研究主題** | 隱匿性高血壓 (MH) / 隱匿性未控制高血壓 (MUCH) 預測 |
| **研究設計** | 多中心橫斷面 + 外部驗證 |
| **Cohort 1** | 台灣 6 家醫學中心，2004-2005，n=970 |
| **Cohort 2（外部驗證）** | 台北榮總，2012-2020，n=416 |
| **MH/MUCH 盛行率** | Cohort 1: 39.8%；Cohort 2: 33.7% |
| **候選變數** | 33 個（人口學 + 門診 BP + 降壓藥 + 生化） |
| **模型** | LR, RF, XGBoost, ANN |
| **不平衡處理** | SMOTE-NC（合成少數類過採樣—混合連續/類別） |
| **評估指標** | AUC, Sensitivity, Specificity, PPV, NPV, Accuracy, F1 |

### MH/MUCH 定義

- **門診 BP** < 140/90 mmHg **且**
- **24 小時平均 BP** ≥ 130/80 mmHg **和/或**
- **日間 BP** ≥ 130/80 mmHg **和/或**
- **夜間 BP** ≥ 120/70 mmHg

### 基線特徵

| 變項 | Cohort 1 (n=970) | Cohort 2 (n=416) |
|------|-----------------|-----------------|
| 年齡 | 41.0 ± 7.2 | 62.0 ± 14.2 |
| 男性 | 68.5% | 57.7% |
| BMI | 26.5 ± 3.4 | 26.1 ± 3.7 |
| Office SBP | 126.1 ± 14.5 | 131.6 ± 16.8 |
| Office DBP | 84.9 ± 11.7 | 81.8 ± 10.5 |
| 降壓藥數量 | 1.5 ± 1.0 | 1.9 ± 0.9 |

→ **兩個世代差異極大**（年齡差 21 歲、用藥模式不同），但 RF 模型仍表現良好

---

## 核心方法論

### 資料分割

- Cohort 1：Training 70% (n=679) / Validation 15% (n=146) / Test 15% (n=145)
- Cohort 2：External validation (n=416)
- 缺失值：Training set 均值插補（缺失極少，3/26,190）

### 模型開發流程

1. 資料前處理 + 標準化（LR, ANN）
2. SMOTE-NC 過採樣（訓練集 events:non-events = 1:1）
3. 模型訓練
4. Random search 調參
5. Feature importance ranking + 特徵選擇
6. Threshold-moving（最大 F1 score）
7. Internal validation（Test set）
8. External validation（Cohort 2）

### 特徵選擇結果

| 模型 | 選取變數數 | Top 變數 |
|------|---------|---------|
| LR | 21 | Spironolactone, Alpha-blocker, Beta-blocker, ACEI/ARB, Male sex... |
| **RF** | **6** | **Office DBP, Office MAP, Office SBP, Office PP, Beta-blocker, HDL-C** |
| XGBoost | 27 | Office DBP, Office SBP, Potassium, Office MAP, Aldosterone, WHR... |
| ANN | 24 | Office DBP, Office MAP, eGFR, Office SBP, Spironolactone... |

→ **RF 僅需 6 個變數**即達最佳效能，極為精簡

---

## 主要結果

### 模型效能

| 模型 | Internal AUC | External AUC | Internal Sensitivity | External Sensitivity | Internal NPV | External NPV |
|------|-------------|-------------|---------------------|---------------------|-------------|-------------|
| LR | 0.674 | 0.571 | 0.914 | 0.950 | 0.853 | 0.875 |
| **RF** | **0.851** | **0.837** | **1.000** | **1.000** | **1.000** | **1.000** |
| XGBoost | 0.799 | 0.821 | 0.931 | 0.979 | 0.927 | 0.977 |
| ANN | 0.805 | 0.672 | 0.948 | 0.986 | 0.941 | 0.969 |

### RF 模型詳細效能

| 指標 | Internal (Test) | External (Cohort 2) |
|------|----------------|-------------------|
| AUC | 0.851 | 0.837 |
| Sensitivity | 1.000 | 1.000 |
| Specificity | 0.609 | 0.580 |
| PPV | 0.630 | 0.547 |
| NPV | 1.000 | 1.000 |
| Accuracy | 0.766 | 0.721 |
| F1 | 0.773 | 0.707 |

**關鍵觀察**：
- **RF 最佳**且僅用 6 變數，內外部驗證一致
- 所有模型 sensitivity 極高（≥0.914），設計偏向「不漏診」
- Specificity 偏低（0.333-0.609），代表假陽性較多
- **LR 最差**（AUC 0.674/0.571），可能因多重共線性影響
- RF 克服多重共線性的能力是其優勢
- **外部驗證世代差異極大但 RF 仍穩定**（AUC 0.837），泛化能力佳

### 重要預測因子（跨模型共識）

以下變數在 ≥3 個模型中被選為預測變數：
- **Office BP 參數**：SBP, DBP, MAP, PP（門診血壓為核心）
- **代謝指標**：HDL-C, TG, eGFR, Creatinine
- **降壓藥**：Beta-blocker, Thiazide
- **人口學**：Age, Male sex, Current smoker
- **其他**：ALT

---

## 與本研究的比較

| 面向 | Hung (2021) | 本研究 |
|------|-----------|------|
| **人群** | 台灣高血壓患者 | 中國杭州社區健檢 |
| **樣本量** | 970 + 416 | 6,056 |
| **預測目標** | 隱匿性高血壓（MH/MUCH） | 新發高血壓+高血糖+血脂異常 |
| **設計** | 橫斷面分類 | **縱貫預測** |
| **模型** | LR, RF, XGBoost, ANN | LR, NB, LDA, DT, RF, XGBoost, SVM, MLP + PySR |
| **最佳模型** | RF (AUC 0.851) | 待比較 |
| **特徵數** | 6（RF）–27（XGBoost） | ~20 + Δ 變化量 |
| **不平衡處理** | SMOTE-NC | SMOTE |
| **外部驗證** | ✅ 有（不同時期/醫院） | 交叉驗證 |
| **可解釋性** | Feature importance ranking | SHAP + PySR |
| **ABPM** | ✅ 24 小時動態血壓 | ❌ 無 |

### 本研究可引用的論證

1. **台灣 + ML + 高血壓的先例**：Hung 是台灣首篇使用 ML 預測 MH/MUCH 的研究
2. **RF 模型的優勢**：RF 僅 6 變數即達 AUC 0.851，證明精簡模型的可行性
3. **SMOTE-NC 的成功應用**：與本研究使用 SMOTE 處理不平衡一致
4. **門診 BP 為核心預測因子**：RF 的 top 4 全是 BP 參數，與本研究 SHAP 中 BP 重要性一致
5. **外部驗證的重要性**：Hung 有外部驗證（不同時期/醫院），本研究可作為 limitation 討論

### 本研究的相對優勢

1. **縱貫預測 vs 橫斷面分類**：Hung 偵測現有 MH/MUCH，本研究預測未來發病
2. **更大樣本**：6,056 vs 970+416
3. **Δ 變化量特徵**：Hung 無縱向資料
4. **同時預測 3H**：Hung 僅處理高血壓
5. **更多模型比較**：8+1 vs 4
6. **更深的可解釋性**：SHAP + PySR vs 僅 feature importance

---

## 研究限制（作者自述）

1. **僅台灣高血壓患者**：缺乏多元人群驗證
2. **兩世代納入條件不同**：Cohort 1 限制年齡 ≤50、BMI ≤35、無糖尿病
3. **未納入 HBPM**：僅用 ABPM 定義 MH/MUCH
4. **缺少超音波心臟資料**：如 LVH 等可能相關的變數
5. **MH 與 MUCH 合併預測**：兩者病理生理可能不同，分開建模可能更準確
6. **Specificity 偏低**：假陽性率高，臨床應用需搭配其他檢查
7. **樣本量偏小**：僅 970 + 416

---

## 對本論文寫作的引用建議

### 第二章（文獻回顧）
- 作為台灣高血壓 ML 預測的代表性研究引用
- 引用 RF 僅 6 變數達 AUC 0.851 的精簡模型設計
- 引用 SMOTE-NC 處理不平衡的方法

### 第七章（討論）
- 比較門診 BP 在兩研究中都是核心預測因子
- 討論 RF vs XGBoost 的表現差異（Hung 中 RF > XGBoost，與部分文獻不同）
- 引用外部驗證的成功，討論本研究缺乏外部驗證的 limitation
- 代謝指標（HDL-C、TG、eGFR）同時出現在 MH/MUCH 預測中，支持「代謝症候群與高血壓交互關聯」的論述

---

## 關鍵引述

> "The RF model, composed of 6 predictor variables, had the best overall performance in both internal and external validation (AUC = 0.851 and 0.837; sensitivity = 1.000 and 1.000)."

> "Age, male sex, current smoker, office SBP, office DBP, office MAP, office PP, eGFR, creatinine, TG, HDL-C, ALT, beta-blocker, and thiazide were selected as predictor variables in more than three models, indicating their close association with MH/MUCH."

> "The reason the RF model produced the best performance may be attributable to its ability to overcome the multicollinearity of our given data."