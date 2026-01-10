# 論文筆記：Prediabetes 5.8-Year Follow-Up (2024)

> **建立日期**：2026-01-05
> **論文編號**：候選清單 #1
> **狀態**：已閱讀摘要與方法
> **備註**：此為 Dual 2025 同研究團隊的前作

---

## 基本資訊

| 欄位 | 內容 |
|------|------|
| **標題** | Machine Learning Prediction of Prediabetes in a Young Male Chinese Cohort with 5.8-Year Follow-Up |
| **期刊** | Diagnostics (MDPI) |
| **年份** | 2024 (May 8) |
| **連結** | [MDPI](https://www.mdpi.com/2075-4418/14/10/979) / [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11119884/) / [PubMed](https://pubmed.ncbi.nlm.nih.gov/38786280/) |
| **DOI** | 10.3390/diagnostics14100979 |

---

## 作者與機構

- Chi-Hao Liu, Chun-Feng Chang, I-Chien Chen, Fan-Min Lin, Shiow-Jyu Tzou, Chung-Bao Hsieh, Ta-Wei Chu, **Dee Pei**
- 機構：
  - 高雄國軍總醫院 腎臟科
  - **MJ Health Research Foundation, Taipei**（美兆健康研究基金會）
  - 輔仁大學附設醫院 內分泌新陳代謝科

**重要**：與 Dual 2025 為同一研究團隊，使用相同 Taiwan MJ Cohort 資料

---

## 研究目標

1. 評估 Machine Learning 是否優於傳統 Multiple Linear Regression (MLR)
2. 找出預測糖前期 (Prediabetes) 最重要的風險因子

---

## 資料集

| 項目 | 內容 |
|------|------|
| **來源** | Taiwan MJ Cohort（美兆健檢資料） |
| **樣本數** | 6,247 人 |
| **性別** | 僅男性 |
| **年齡** | 18-35 歲（年輕族群） |
| **追蹤期** | 5.8 年（平均） |
| **納入條件** | 基線空腹血糖正常 (Normal FPG) |
| **特徵數** | 25 個基線變數 |

---

## 方法論

### 1. 機器學習模型

| 模型 | 說明 |
|------|------|
| **Random Forest (RF)** | Ensemble decision tree with bootstrap |
| **Stochastic Gradient Boosting (SGB)** | Sequential weak learners |
| **XGBoost** | Optimized gradient boosting |
| **Elastic Net (EN)** | Hybrid L1/L2 regularization |

### 2. 交叉驗證

- **10-fold cross-validation** for hyperparameter tuning
- Training/Testing split: 80%/20%
- 重複 10 次確保穩定性

### 3. 類別平衡

**注意**：此論文未使用 SMOTE 或其他類別平衡方法

### 4. 評估指標

與傳統 AUC/Accuracy 不同，使用回歸類指標：

| 指標 | 說明 |
|------|------|
| **SMAPE** | Symmetric Mean Absolute Percentage Error |
| **RAE** | Relative Absolute Error |
| **RRSE** | Root Relative Squared Error |
| **RMSE** | Root Mean Squared Error |

---

## 結果

### ML vs. MLR 比較

**結論**：所有 ML 方法的誤差都小於 MLR，ML 在捕捉非線性關係上更優

### 特徵重要性

#### Model 1（包含 FPGbase 的 25 變數）

| 排名 | 特徵 | 相對重要性 |
|------|------|-----------|
| 1 | **FPGbase** (基線空腹血糖) | 100% |
| 2 | Body Fat (體脂率) | 28.32% |
| 3 | Creatinine (肌酸酐) | 27.07% |
| 4 | TSH (甲狀腺刺激素) | 20.51% |
| 5 | WBC (白血球) | 20.19% |
| 6 | Age (年齡) | 20.14% |

#### Model 2（排除 FPGbase 的模型）

| 排名 | 特徵 | 相對重要性 |
|------|------|-----------|
| 1 | Body Fat | 58.62% |
| 2 | WBC | 54.89% |
| 3 | Age | 36.87% |
| 4 | TSH | 32.66% |
| 5 | TG (三酸甘油酯) | 28.69% |
| 6 | LDL-C | 27.42% |

### 其他重要變數

- Triglycerides (TG)
- HDL-Cholesterol
- Uric Acid
- C-reactive protein (CRP)
- WBC（發炎指標）

---

## 與 Dual 2025 的關係

| 面向 | 本論文 (2024) | Dual 2025 |
|------|---------------|-----------|
| **預測目標** | Prediabetes（糖前期） | Diabetes + Hypertension（雙重） |
| **樣本** | 6,247 男性 | 更大樣本，含女性 |
| **追蹤期** | 5.8 年 | 類似 |
| **特徵設計** | 25 基線變數 | T1+T2+...（多時間點串接） |
| **模型** | RF, SGB, XGB, EN | 類似 |
| **創新點** | 年輕男性族群 | 雙任務預測 |

**演進**：從單一任務（糖前期）→ 多任務（糖尿病+高血壓）

---

## 與我們研究的關聯

| 面向 | 本論文 | 我們的研究 |
|------|--------|-----------|
| **資料來源** | Taiwan MJ Cohort | HRS (美國) |
| **追蹤設計** | 基線 → 5.8年後 | T1 → T2 → T3 |
| **特徵** | 單時間點 | T1 + T2 + Δ |
| **預測目標** | Prediabetes | 三高（高血壓、高血糖、高血脂） |
| **年齡** | 年輕（18-35） | 中老年（50+） |
| **性別** | 僅男性 | 男女皆有 |

---

## 可借鏡之處

1. **特徵重要性報告方式**：相對重要性 % 表示法
2. **Model 1 vs Model 2 設計**：含/不含 baseline 目標值的比較
3. **10-fold CV**：比我們計畫的 5-fold 更嚴謹
4. **年輕族群關注**：強調早期預防的重要性
5. **WBC/TSH 作為預測因子**：發炎與甲狀腺指標的角色

---

## 限制

- 僅限年輕男性，generalizability 有限
- 未使用 SMOTE 處理類別不平衡
- 使用回歸指標而非分類指標（難以直接比較 AUC）
- 無 SHAP 可解釋性分析

---

## 關鍵字

prediabetes, machine learning, Taiwan MJ Cohort, young adults, longitudinal study, Random Forest, XGBoost

---

**相關文件**：
- [論文候選清單](論文候選清單_從Dual2025延伸.md)
- [Meeting_17 (Dual 2025)](../meeting_notes/Meeting_17_Complete.md)
- [Meeting_18_Notes](../meeting_notes/Meeting_18_Notes.md)
