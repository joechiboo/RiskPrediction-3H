# Dinh et al. (2019) BMC — ML 預測糖尿病與 CVD 深度解析

> **論文**：A data-driven approach to predicting diabetes and cardiovascular disease with machine learning
> **期刊**：BMC Medical Informatics and Decision Making, 2019; 19(1): 211
> **作者**：An Dinh, Stacey Miertschin, Amber Young, Somya D. Mohanty
> **機構**：Eastern Oregon University / Winona State University / Purdue University / UNC Greensboro
> **DOI**：[10.1186/s12911-019-0918-5](https://doi.org/10.1186/s12911-019-0918-5)
> **PDF**：[Dinh_BMC_Diabetes_CVD_2019.pdf](../papers/Dinh_BMC_Diabetes_CVD_2019.pdf)
> **與本研究關聯度**：⭐⭐⭐（Tier 2 — 同時預測糖尿病+CVD 的多模型比較，概念與本研究 3H 相似）

---

## 一句話摘要

**使用美國 NHANES 全國健康調查資料（1999-2014），以 LR、SVM、RF、XGBoost 及加權集成模型（WEM）分別預測糖尿病（AUC 0.862）、前驅糖尿病（AUC 0.737）和 CVD（AUC 0.831），發現僅用問卷調查資料（無實驗室數據）即可達到接近實驗室模型的預測準確度，且糖尿病與 CVD 共享大量重要預測因子。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **研究主題** | 糖尿病 + CVD 風險偵測 |
| **研究設計** | 橫斷面分類（10-fold CV） |
| **資料來源** | NHANES（美國全國健康與營養調查） |
| **時間範圍** | 1999–2014（糖尿病）；2007–2014（CVD） |
| **模型** | LR, SVM, RF, XGBoost, WEM（加權集成） |
| **評估指標** | AU-ROC, Precision, Recall, F1 |
| **類別平衡** | Downsampling（降採樣至平衡） |
| **驗證** | 10-fold CV + 80/20 train/test split |

### 資料集結構

| 資料集 | 時間 | 樣本數 | 變數數 | 陽性 | 陰性 |
|-------|------|--------|--------|------|------|
| 糖尿病 Case I (1999-2014) | 1999-2014 | 21,131 | 123 | 5,532 | 15,599 |
| 前驅糖尿病 Case II (1999-2014) | 1999-2014 | 16,426 | 123 | 6,482 | 9,944 |
| 糖尿病 Case I (2003-2014) | 2003-2014 | 16,443 | 168 | 4,466 | 11,977 |
| 前驅糖尿病 Case II (2003-2014) | 2003-2014 | 12,636 | 168 | 5,133 | 7,503 |
| **CVD** | 2007-2014 | 8,459 | 131 | 1,447 | 7,012 |

### 疾病定義

| 疾病 | 定義 |
|------|------|
| **糖尿病 (Case I)** | 自述醫師告知有糖尿病 **或** 空腹血糖 ≥126 mg/dL |
| **前驅/未診斷 (Case II)** | 未自述糖尿病但血糖 ≥126（未診斷）或 100-125（前驅）；已確診糖尿病者排除 |
| **CVD** | 自述曾被告知有：充血性心衰竭、冠心病、心肌梗塞、中風 |

---

## 核心方法論

### 特徵工程

- 從 NHANES 約 3,900 個變數中，手動篩選跨年度連續可用者
- 排除缺失率 >50% 的變數
- 最終：123 變數（1999-2014）/ 168 變數（2003-2014）/ 131 變數（CVD）
- **兩種特徵集**：含實驗室（Lab）vs 僅問卷（No Lab）
- 標準化：z-score 標準化
- 類別變數：數值編碼

### 模型

| 模型 | 說明 |
|------|------|
| Logistic Regression (LR) | 線性基準模型 |
| SVM | 線性超平面分類 |
| Random Forest (RFC) | Bagging 樹集成 |
| XGBoost (GBT) | 梯度提升決策樹 |
| **WEM** | 加權集成（wi = AUCi² / ΣAUCi²），融合 4 模型機率 |

### 特徵選擇

- 以 XGBoost 的 error rate-based feature importance 排名
- 選取 top 24 特徵（<24 會導致 >2% AUC 下降）
- 分別對糖尿病和 CVD 做特徵排名

---

## 主要結果

### 糖尿病預測（Case I — 含已確診 + 未診斷）

| 條件 | 模型 | AUC | Precision | Recall | F1 |
|------|------|-----|-----------|--------|-----|
| No Lab, 1999-2014 | **XGBoost** | **0.862** | 0.78 | 0.78 | 0.78 |
| No Lab, 1999-2014 | WEM | 0.859 | 0.78 | 0.78 | 0.78 |
| No Lab, 1999-2014 | RF | 0.855 | 0.78 | 0.78 | 0.78 |
| No Lab, 1999-2014 | SVM | 0.849 | 0.77 | 0.77 | 0.77 |
| No Lab, 1999-2014 | LR | 0.827 | 0.75 | 0.75 | 0.75 |
| With Lab, 1999-2014 | **XGBoost** | **0.957** | 0.89 | 0.89 | 0.89 |
| With Lab, 2003-2014 | **XGBoost** | **0.962** | 0.89 | 0.89 | 0.89 |

### 前驅糖尿病預測（Case II）

| 條件 | 模型 | AUC |
|------|------|-----|
| No Lab, 1999-2014 | **WEM** | **0.737** |
| No Lab, 1999-2014 | XGBoost | 0.734 |
| With Lab, 1999-2014 | **XGBoost** | **0.802** |
| With Lab, 2003-2014 | **XGBoost** | **0.834** |

### CVD 預測

| 條件 | 模型 | AUC | Precision | Recall | F1 |
|------|------|-----|-----------|--------|-----|
| No Lab | **WEM** | **0.831** | 0.75 | 0.75 | 0.75 |
| No Lab | XGBoost | 0.830 | 0.74 | 0.74 | 0.74 |
| No Lab | RF | 0.829 | 0.75 | 0.74 | 0.74 |
| No Lab | LR | 0.822 | 0.74 | 0.74 | 0.74 |
| No Lab | SVM | 0.816 | 0.74 | 0.74 | 0.74 |
| With Lab | **WEM** | **0.839** | 0.76 | 0.76 | 0.76 |

**關鍵觀察**：
- **XGBoost 在糖尿病預測中最強**；**WEM 在 CVD 和前驅糖尿病中最強**
- CVD 中加入 Lab 僅提升 0.8%（0.831 → 0.839），問卷資料已足夠
- 糖尿病中加入 Lab 提升巨大（0.862 → 0.957，+9.5%），因血糖本身就是定義標準的一部分
- 前驅糖尿病最難預測（最高 AUC 0.737 / 0.834），邊界案例難區分
- **所有模型 CVD 效能差異極小**（AUC 差距僅 ~1.5%）

### Top 預測因子

**糖尿病（No Lab）**：
1. Waist size（腰圍）
2. Age
3. Self-reported greatest weight
4. Leg length
5. Sodium intake
6. Carbohydrate intake
7. DBP / SBP
8. BMI
9. Fiber intake / Height / Pulse

**糖尿病（With Lab）**：
1. Blood osmolality
2. Sodium
3. Blood urea nitrogen
4. Triglyceride
5. LDL cholesterol
6. Age / Waist

**CVD（No Lab）**：
1. **Age**（遠超其他）
2. Systolic blood pressure
3. Self-reported greatest weight
4. Chest pain
5. Diastolic blood pressure
6. Alcohol consumption
7. Kcal intake
8. Close relative had heart attack

**CVD（With Lab）**：
1. Age
2. LDL cholesterol
3. Chest pain
4. DBP / HDL cholesterol

### 糖尿病與 CVD 的共享預測因子

Age、BMI/Waist、Blood pressure、Self-reported weight、Dietary intake（sodium, carbohydrate, calcium）、Ethnicity、General health condition、Household income

---

## 與本研究的比較

| 面向 | Dinh (2019) | 本研究 |
|------|-----------|------|
| **資料來源** | NHANES 美國全國調查 | 杭州健檢 (Luo 2024 Dryad) |
| **樣本量** | 8,459–21,131 | 6,056 |
| **預測目標** | 糖尿病 + CVD（分開建模） | 高血壓 + 高血糖 + 血脂異常（3H，分開建模） |
| **設計** | 橫斷面分類（偵測現有疾病） | **縱貫預測（預測未來發病）** |
| **模型** | LR, SVM, RF, XGBoost, WEM | LR, NB, LDA, DT, RF, XGBoost, SVM, MLP + PySR |
| **特徵類型** | 問卷 + 體測 + 實驗室 + 飲食 | 健檢數值 + Δ 變化量 |
| **可解釋性** | XGBoost feature importance (error rate) | SHAP + PySR 符號回歸 |
| **不平衡處理** | Downsampling | SMOTE |
| **CVD AUC** | 0.831（WEM, No Lab） | — |
| **糖尿病 AUC** | 0.862（XGBoost, No Lab） | 待比較 |

### 本研究可引用的論證

1. **同時預測多種慢性病的先例**：Dinh 雖分開建模但同篇論文處理糖尿病+CVD，支持本研究 3H 同時預測的合理性
2. **共享預測因子**：糖尿病與 CVD 有大量共同預測因子（Age、BMI、BP、飲食），支持本研究使用相同健檢資料預測 3H 的理論基礎
3. **XGBoost 一致表現最佳**：又一篇證實 XGBoost 在健康預測領域的優勢
4. **問卷/問診資料即可有效預測**：CVD 加 Lab 僅提升 0.8%，支持健檢數值型資料的實用價值
5. **前驅糖尿病難預測**（AUC 僅 0.737），與邊界案例的模糊性有關

### 本研究的相對優勢

1. **縱貫預測 vs 橫斷面偵測**：Dinh 是偵測「現有」疾病（detection），本研究是預測「未來」發病（prediction）— 臨床價值更高
2. **Δ 變化量特徵**：Dinh 無縱向資料，本研究有 T1→T2→T3 + Delta
3. **更多模型**：本研究比較 8+1 模型（含 NB, LDA, DT, MLP, PySR），Dinh 僅 4+1
4. **更深的可解釋性**：SHAP 值 + PySR 符號回歸，Dinh 僅用 XGBoost error rate importance
5. **SMOTE vs Downsampling**：Downsampling 會丟棄多數類資料，SMOTE 保留完整資訊

---

## 研究限制

1. **橫斷面設計**：無法區分因果，只能「偵測」而非「預測」
2. **自述疾病標籤**：糖尿病與 CVD 標籤來自問卷自報，非臨床確診（可能有漏報）
3. **Downsampling 丟棄資料**：平衡類別時丟棄多數類樣本，損失資訊
4. **排除 Neural Network**：因「黑箱」而排除 NN，但 NN 可能表現更好
5. **缺失值處理不明確**：僅排除缺失率 >50% 的變數，未說明其餘缺失如何處理
6. **美國人群**：NHANES 以美國多種族為主，跨文化適用性需驗證
7. **無校準分析**：僅報 AUC/F1，未評估模型校準度（Brier score 等）
8. **CVD 資料嚴重不平衡**：1,447 vs 7,012（17.1%），僅用 downsampling 可能不足
9. **特徵洩漏風險**：糖尿病 Case I 含「自述有糖尿病」作為標籤，而 Lab 模型含血糖值作為特徵，接近 label leakage

---

## 對本論文寫作的引用建議

### 第二章（文獻回顧）
- 作為「同時處理糖尿病與 CVD 的多模型比較」研究引用
- 引用其發現：糖尿病與 CVD 共享大量預測因子，支持本研究以相同健檢資料同時預測 3H
- 引用 XGBoost 在糖尿病預測中最佳（AUC 0.862）的結果

### 第七章（討論）
- 比較設計差異：Dinh 橫斷面偵測 vs 本研究縱貫預測
- 引用 CVD 模型中「問卷 vs Lab 差異僅 0.8%」的發現，支持健檢數值的實用價值
- 討論共享預測因子（Age、BMI、BP、代謝指標），與本研究 SHAP 分析比較
- 強調本研究的縱向設計優勢：能預測未來發病，臨床價值更高

---

## 關鍵引述

> "A large set of common attributes exist between both diseases, suggesting that patients with diabetic issues may be also at risk of cardiovascular issues and vice-versa."

> "Models developed based on laboratory based variables do not show any significant performance gain [for CVD] with an increase of only 0.7%."

> "The WEM and XGBoost models developed in the study surpass prior research done by Yu et al. where they obtained 83.5% (Case I) and 73.2% (Case II) using non-linear SVM models."

> "Machine learned models based on survey questionnaire can provide an automated identification mechanism for patients at risk of diabetes and cardiovascular diseases."