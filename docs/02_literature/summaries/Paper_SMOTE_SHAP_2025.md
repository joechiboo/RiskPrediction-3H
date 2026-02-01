# 論文筆記：SMOTE + SHAP Framework (2025)

> **建立日期**：2026-01-05
> **論文編號**：候選清單 #9
> **狀態**：已閱讀摘要與方法

---

## 基本資訊

| 欄位 | 內容 |
|------|------|
| **標題** | Interpretable Machine Learning Framework for Diabetes Prediction: Integrating SMOTE Balancing with SHAP Explainability for Clinical Decision Support |
| **期刊** | Healthcare (MDPI) |
| **年份** | 2025 (October) |
| **連結** | [MDPI](https://www.mdpi.com/2227-9032/13/20/2588) / [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563896/) |

---

## 研究目標

解決糖尿病預測中的兩大障礙：
1. **類別不平衡** (Class Imbalance) → 使用 SMOTE
2. **模型可解釋性不足** (Limited Interpretability) → 使用 SHAP

---

## 資料集

| 項目 | 內容 |
|------|------|
| **來源** | Kaggle 公開資料集 |
| **樣本數** | 100,000 筆去識別化病患紀錄 |
| **類別分布** | 34.9% 糖尿病 / 65.1% 非糖尿病 |
| **特徵** | 臨床、人口統計、生活型態變數（glucose, BMI, age, hypertension, HbA1c 等） |

---

## 方法論

### 1. SMOTE 實作細節

| 參數 | 設定 |
|------|------|
| **k-nearest neighbors** | 5 (grid search 優化) |
| **Sampling strategy** | 1:1 ratio（平衡正負樣本） |
| **Random state** | 42 |
| **公式** | x_new = x_i + λ × (x_i′ − x_i), λ ∈ [0,1] |

**關鍵設計**：SMOTE 在每個 CV fold 內獨立執行，避免 data leakage

### 2. 前處理

| 步驟 | 方法 |
|------|------|
| **缺失值處理** | <5%: Median imputation; 5-10%: MICE; >10%: Multiple imputation |
| **離群值處理** | IQR + Z-score (Winsorization at 5th/95th percentiles) |
| **標準化** | Z-score normalization (僅對 training data) |
| **特徵選擇** | RFE + Permutation importance（移除 insulin, skin thickness） |

### 3. 模型比較

- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)
- Logistic Regression
- XGBoost

### 4. SHAP 分析

| 類型 | 方法 |
|------|------|
| **Global** | Feature importance ranking, Summary plots |
| **Local** | Waterfall plots (個案解釋) |
| **Interaction** | SHAP interaction plots |
| **實作** | TreeExplainer, 100 samples for baseline |
| **驗證** | 3 位內分泌科醫師獨立審查 |

---

## 結果

### 最佳模型：Random Forest

| 指標 | 數值 |
|------|------|
| **Accuracy** | 96.91% (95% CI: 95.4–98.2%) |
| **AUC-ROC** | 0.998 |
| **Sensitivity (Recall)** | 99.5% (95% CI: 98.7–99.9%) |
| **Specificity** | 97.3% |
| **Precision** | 96.20% |
| **F1-Score** | 0.970 |
| **NPV** | 99.70% |

### SMOTE 效果比較 (Random Forest)

| 資料集 | Accuracy | AUC | Recall | Precision | F1 |
|--------|----------|-----|--------|-----------|-----|
| **Original** | 96.91% | 0.998 | 0.990 | 0.950 | 0.970 |
| **SMOTE** | 96.67% | 0.997 | 0.960 | 0.970 | 0.970 |

**觀察**：RF 對 SMOTE 相對穩健；SVM 用 SMOTE 後 Recall 從 0.83 降到 0.27（嚴重崩潰）

### 特徵重要性 (SHAP)

| 排名 | 特徵 | SHAP Value |
|------|------|------------|
| 1 | Glucose | 2.34 ± 0.67 |
| 2 | BMI | 1.87 ± 0.43 |
| 3 | Age | 1.23 ± 0.31 |
| 4 | Diabetes Pedigree Function | 0.89 ± 0.24 |
| 5 | Blood Pressure, Insulin | (較低) |

**交互作用**：Glucose × BMI interaction = 0.45（協同效應）

---

## 驗證方法

- **5-fold stratified cross-validation**
- Mean accuracy 96.9% ± 0.3%
- Mean AUC 0.998 ± 0.001
- CV = 0.31%
- McNemar's test + Bonferroni correction

---

## 與我們研究的關聯

| 面向 | 本論文 | 我們的研究 |
|------|--------|-----------|
| **SMOTE** | 1:1 ratio, k=5 | 已實作於 LR |
| **SHAP** | Global + Local + Interaction | 已做 Global，可加 Interaction |
| **CV** | 5-fold stratified | 待做 5-fold CV |
| **模型** | RF, GB, SVM, LR, XGB | LR, RF, XGB, ANN, SVM, GP |
| **資料** | Kaggle 橫斷面 | HRS 縱向三次健檢 |
| **特徵** | 靜態特徵 | T1 + T2 + Δ 特徵 |

---

## 可借鏡之處

1. **SMOTE data leakage 防範**：在 CV fold 內執行 SMOTE
2. **SHAP interaction analysis**：探索 Glucose × BMI 類似的交互作用
3. **專家驗證**：SHAP 結果由臨床醫師審查
4. **多指標報告**：不只 AUC，還有 Sensitivity, Specificity, NPV
5. **McNemar's test**：模型比較的統計檢定方法

---

## 限制與注意

- 資料來自 Kaggle，非真實臨床環境
- 論文強調「methodological proof-of-concept」
- 需外部驗證才能臨床部署
- AUC 0.998 過高，可能資料特性造成

---

## 關鍵字

diabetes prediction, machine learning, SMOTE, SHAP, explainable AI, Random Forest, clinical decision support

---

**相關文件**：
- [論文候選清單](論文候選清單_從Dual2025延伸.md)
- [Meeting_18_Notes](../meeting_notes/Meeting_18_Notes.md)
