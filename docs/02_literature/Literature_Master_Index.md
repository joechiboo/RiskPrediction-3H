# 文獻總覽索引

**最後更新**：2026-01-10
**用途**：統整所有已讀論文的狀態與分類

---

## 📊 閱讀狀態總覽

| 狀態 | 數量 | 說明 |
|------|------|------|
| ✅ 已完整分析（有深度解析＋簡報） | 5 | Meeting 15-18 論文 |
| 📋 已閱讀摘要與方法 | 2 | SMOTE+SHAP 2025, Prediabetes 2024 |
| 📌 待深入分析 | 1 | Hung et al. 2021 |
| 📋 基本資訊已整理 | 多篇 | 見系統性文獻回顧 |

### 按 Meeting 進度

| Meeting | 論文 | 狀態 |
|---------|------|------|
| 15 | Liu et al. 2024 (台中榮總糖尿病預測) | ✅ 已簡報 |
| 16 | Taiwan MTL 2025 (多任務學習) | ✅ 已簡報 |
| 17 | Dual Framework 2025 (δ-FPG) | ✅ 已簡報 |
| 18 | Taiwan MJ Hypertension 2024 (#5) | ✅ 已簡報 |
| 19 | SMOTE+SHAP 2025 (#9) | 📋 已閱讀（評估為參考價值有限）|
| 19 | Prediabetes TaiwanMJ 2024 (#1) | 📋 已閱讀摘要 |
| 19 | China Prediabetes→Diabetes 2025 (#2) | 📋 已閱讀（備選論文） |
| 19 | **Kanegae Hypertension 2020** | ✅ **選定為 Meeting 19 論文** |

---

## 🎯 按疾病分類

### 高血壓（Hypertension）

#### ✅ Kanegae et al. (2020) - 使用 AI 的高精度高血壓預測 ⭐⭐⭐⭐⭐【Meeting 19 選定】

- **標題**：Highly precise risk prediction model for new-onset hypertension using artificial intelligence techniques
- **期刊**：The Journal of Clinical Hypertension
- **DOI**：[10.1111/jch.13759](https://doi.org/10.1111/jch.13759)
- **PMC**：[PMC8029685](https://pmc.ncbi.nlm.nih.gov/articles/PMC8029685/)
- **資料**：日本職場健康檢查，18,258 人，2005-2016
- **方法**：XGBoost, Ensemble, Logistic Regression
- **最佳模型**：Ensemble (AUC 0.881)
- **核心創新**：
  - **縱向變化量特徵**：Year(-2) → Year(-1) → Year(0)
  - **Δ 特徵**：Changes from Year(-2) to Year(-1) ← 與我們的 Delta1 相同！
- **狀態**：✅ **選定為 Meeting 19 論文**
- **與本研究關聯度**：⭐⭐⭐⭐⭐ (最高)
  - 時間架構幾乎相同（Year(-2), Year(-1), Year(0) vs T1, T2, T3）
  - 同樣使用縱向變化量特徵
  - 證明 Δ 特徵在高血壓預測上有效
- **相關文檔**：
  - [Paper_Kanegae_Hypertension_2020.md](summaries/Paper_Kanegae_Hypertension_2020.md)
  - [Kanegae_Hypertension_2020_中文翻譯.md](translations/Kanegae_Hypertension_2020_中文翻譯.md)

#### ✅ Taiwan MJ Hypertension (2024) - 下次健檢高血壓預測 ⭐⭐⭐⭐⭐【Meeting 18】
- **標題**：Next-visit prediction and prevention of hypertension using large-scale routine health checkup data
- **期刊**：PLoS ONE
- **DOI**：[10.1371/journal.pone.0312370](https://doi.org/10.1371/journal.pone.0312370)
- **PMC**：[PMC11560048](https://pmc.ncbi.nlm.nih.gov/articles/PMC11560048/)
- **資料**：Taiwan MJ Cohort（美兆健檢資料），大規模健檢資料
- **方法**：RF, XGBoost, LightGBM 等
- **核心發現**：
  - **訪問次數越多，預測越準**（4+ 次最佳）
  - 多時間點特徵串接（T1 + T2 + ... + TN）
  - 與本研究的縱向設計概念一致
- **狀態**：✅ 已簡報完成（Meeting 18）
- **相關文檔**：
  - [Meeting_18_Notes.md](../meeting_notes/Meeting_18_Notes.md)
  - [論文候選清單 #5](../memos/論文候選清單_從Dual2025延伸.md)

#### 📌 Hung et al. (2021) - 隱匿性高血壓預測
- **期刊**：Frontiers in Cardiovascular Medicine, 8:778306
- **DOI**：[10.3389/fcvm.2021.778306](https://doi.org/10.3389/fcvm.2021.778306)
- **PDF位置**：[fcvm-08-778306.pdf](../references/fcvm-08-778306.pdf)
- **資料**：台灣六家醫學中心 + 台北榮總，970+416人
- **方法**：LR, RF, XGBoost, ANN + SMOTE-NC
- **最佳模型**：RF (AUC 0.851/0.837)
- **關鍵特徵**：DBP, MAP, SBP, PP, beta-blocker, HDL-C
- **狀態**：📌 有PDF，待深入分析
- **相關文檔**：[Q2_Taiwan_Literature_Review.md](../research_plans/Q2_Taiwan_Literature_Review.md)

#### 📋 Lin et al. (2024) - 血清尿酸與高血壓關係
- **期刊**：Frontiers in Endocrinology
- **DOI**：10.3389/fendo.2024.1343998
- **標題**：Poor serum uric acid control increases the risk of hypertension
- **資料**：中國，6,052人，追蹤6年
- **發現**：尿酸水平變化與高血壓風險呈線性相關
- **狀態**：📋 基本資訊已整理
- **閱讀日期**：2025-09-09

---

### 糖尿病（Diabetes）

#### ✅ Liu et al. (2024) - 台灣第二型糖尿病發病預測
- **期刊**：Diagnostics, 15(1), 72
- **DOI**：[10.3390/diagnostics15010072](https://doi.org/10.3390/diagnostics15010072)
- **PDF位置**：[diagnostics-15-00072.pdf](../references/diagnostics-15-00072.pdf)
- **資料**：台中榮總EHR，6,687人，追蹤10年
- **方法**：LR, RF, XGBoost
- **最佳模型**：XGBoost (AUC 0.93)
- **關鍵特徵**：HbA1c, FBG, Weight, fT4, TG
- **狀態**：✅ 已完整分析
- **相關文檔**：
  - [Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md](Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md)
  - 簡報檔：meeting15_21138X006_紀伯喬_wVBA.pptm (已報告完成)

#### ✅ Dual Framework (2025) - 台灣青年男性前驅糖尿病預測 ⭐⭐⭐⭐⭐【Meeting 17】
- **期刊**：Diagnostics, 15(19), 2507
- **DOI**：[10.3390/diagnostics15192507](https://doi.org/10.3390/diagnostics15192507)
- **PDF位置**：[diagnostics-15-02507.pdf](../references/diagnostics-15-02507.pdf) (3.5 MB)
- **資料**：台灣 MJ 健康篩檢中心，6,247人 (18-35歲男性)，追蹤5.9年
- **方法**：雙框架 (連續值δ-FPG + 二元分類) | RF, SGB, XGBoost, Elastic Net
- **可解釋性**：SHAP
- **關鍵發現**：δ-FPG (血糖變化量) 預測，與本研究的 Δ 特徵概念相同
- **狀態**：✅ 已簡報完成（Meeting 17）
- **與本研究關聯度**：⭐⭐⭐⭐⭐ (最高)
  - 縱向變化量特徵（δ-FPG = Δ特徵）
  - 雙框架設計（連續值 + 分類）
  - SHAP 可解釋性
  - 台灣本土資料
  - 血液檢驗項目完整（含尿酸）
- **相關文檔**：
  - [Meeting_17_Preparation_Plan.md](../meeting_notes/Meeting_17_Preparation_Plan.md)
  - [Dual_2025_深度解析.md](Dual_2025_深度解析.md)
  - [Meeting_15-17_Papers_Summary.md](Meeting_15-17_Papers_Summary.md)

#### 📋 Prediabetes TaiwanMJ (2024) - Dual 2025 前作【Meeting 19 候選】
- **標題**：Machine Learning Prediction of Prediabetes in a Young Male Chinese Cohort with 5.8-Year Follow-Up
- **期刊**：Diagnostics (MDPI)
- **DOI**：[10.3390/diagnostics14100979](https://doi.org/10.3390/diagnostics14100979)
- **PMC**：[PMC11119884](https://pmc.ncbi.nlm.nih.gov/articles/PMC11119884/)
- **資料**：Taiwan MJ Cohort，6,247 男性，5.8 年追蹤
- **方法**：RF, SGB, XGBoost, Elastic Net（無 SMOTE）
- **關鍵特徵**：FPGbase (100%), Body Fat (28%), Creatinine, TSH, WBC
- **狀態**：📋 已閱讀摘要與方法
- **與 Dual 2025 關係**：同一研究團隊的前作，單任務 → 雙任務演進
- **相關文檔**：[Paper_Prediabetes_TaiwanMJ_2024.md](../memos/Paper_Prediabetes_TaiwanMJ_2024.md)

#### 📋 SMOTE+SHAP Framework (2025) - 可解釋性框架【Meeting 19 候選】
- **標題**：Interpretable Machine Learning Framework for Diabetes Prediction: Integrating SMOTE Balancing with SHAP Explainability
- **期刊**：Healthcare (MDPI)
- **DOI**：[10.3390/healthcare13202588](https://doi.org/10.3390/healthcare13202588)
- **PMC**：[PMC12563896](https://pmc.ncbi.nlm.nih.gov/articles/PMC12563896/)
- **資料**：Kaggle 公開資料集，100,000 筆（橫斷面）
- **方法**：RF, GB, SVM, LR, XGBoost + SMOTE (k=5) + SHAP
- **最佳結果**：RF (AUC 0.998)，Recall 99.5%
- **狀態**：📋 已閱讀全文
- **評估**：⚠️ **參考價值有限**
  - 橫斷面設計（非縱向追蹤）
  - 用 glucose 預測 diabetes（近乎 tautological）
  - AUC 0.998 過高，可能資料特性造成
  - 主要貢獻為整合框架，技術創新有限
- **可借鏡之處**：
  - SMOTE 在 CV fold 內執行（防止 data leakage）
  - SHAP interaction analysis
  - 多指標報告（Sensitivity, Specificity, NPV）
- **相關文檔**：[Paper_SMOTE_SHAP_2025.md](../memos/Paper_SMOTE_SHAP_2025.md)

#### 📋 China Prediabetes→Diabetes (2025) - 5 年縱向預測【Meeting 19 備選】

- **標題**：Development of a 5-Year Risk Prediction Model for Transition From Prediabetes to Diabetes Using Machine Learning
- **期刊**：JMIR (Journal of Medical Internet Research)
- **DOI**：[10.2196/73190](https://doi.org/10.2196/73190)
- **PDF位置**：[JMIR_Prediabetes_Diabetes_2025.pdf](../references/JMIR_Prediabetes_Diabetes_2025.pdf)
- **資料**：
  - 主要隊列：山東第一醫科大學附屬醫院，6,270 人
  - 外部驗證：濱州醫學院附屬醫院，2,157 人
  - 追蹤期：5 年，**每年一次健檢**
  - 進展率：41.6%（主要）/ 35.2%（外部）
- **方法**：7 種 ML 模型比較（LR, RF, SVM, MLP, XGBoost, LightGBM, **CatBoost**）
- **最佳模型**：**CatBoost** (AUC 0.819 Test / 0.807 External)
- **特徵選擇**：RFE-Logistic，從 42 個選出 14 個特徵
- **SHAP Top 6**：FBG, HDL, ALT/AST, BMI, Age, MONO
- **狀態**：📋 已閱讀（備選論文）
- **與本研究關聯度**：⭐⭐⭐⭐
  - 資料規模相近（~6,000 + ~2,000 vs ~6,000 + ~1,000）
  - 縱向多次健檢設計
  - 有外部驗證（我們也有 CLSA）
  - **CatBoost 是我們沒試過的模型**
  - ⚠️ **他們沒用 Δ 特徵**（Kanegae 2020 有，更適合作為方法論驗證）
- **可借鏡之處**：
  - 考慮加入 CatBoost 模型
  - Calibration curves + DCA 評估
  - DeLong test 統計檢定
- **相關文檔**：
  - [Paper_China_Prediabetes_Diabetes_2025.md](summaries/Paper_China_Prediabetes_Diabetes_2025.md)
  - [JMIR_Prediabetes_Diabetes_2025_中文翻譯.md](translations/JMIR_Prediabetes_Diabetes_2025_中文翻譯.md)

---

### 高血脂（Dyslipidemia）

⚠️ **台灣高血脂預測研究較少**，主要為國際研究（見系統性文獻回顧）

---

### 代謝症候群（Metabolic Syndrome）

#### 📋 台灣成人代謝症候群相關研究
- 多篇台灣本土研究（2006-2020）
- 方法：PCA, Decision Tree, ANN
- 狀態：基本資訊已整理
- 相關文檔：[Q2_Taiwan_Literature_Review.md](../research_plans/Q2_Taiwan_Literature_Review.md)

---

## 📂 按文獔類型分類

### 深度解析文檔（已完成）

1. [Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md](Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md)
   - 研究設計、方法、結果、討論的完整分析
   - 與本研究的關聯性分析
   - 啟示與建議

### 演講稿文檔（已完成）

1. [Liu_2024_演講稿_10頁.md](Liu_2024_演講稿_10頁.md)
2. [Liu_2024_演講稿_10頁_精簡版.md](Liu_2024_演講稿_10頁_精簡版.md)

### 綜合文獻回顧文檔

1. [Q2_Taiwan_Literature_Review.md](../research_plans/Q2_Taiwan_Literature_Review.md)
   - 台灣三高預測相關文獻的系統性整理
   - 按疾病分類的詳細分析
   - 研究缺口與本研究的貢獻

2. [Systematic_Literature_Review.md](Systematic_Literature_Review.md)
   - 系統性文獻回顧表格（15篇國際研究）
   - 按研究標的、方法、資料集分類

3. [literature_review_memo.md](literature_review_memo.md)
   - 早期文獻閱讀筆記（2025-09-09）

### 其他參考文檔

1. [confusion_matrix_metrics.md](confusion_matrix_metrics.md)
   - 評估指標說明

---

## 📋 待讀論文清單

| 優先度 | 論文 | 原因 |
|--------|------|------|
| 🔥 | Dual 2025 前作 (Prediabetes TaiwanMJ 2024) | 了解演進脈絡 |
| 🔥 | SMOTE + SHAP Framework 2025 | 方法論參考 |

---

## 🎯 Meeting 19 準備重點

### 已完成的 Meeting

| Meeting | 論文主題 | 狀態 |
|---------|----------|------|
| 15 | Liu 2024 - 台中榮總糖尿病 10 年預測 | ✅ 已簡報 |
| 16 | Taiwan MTL 2025 - 多任務學習慢性病預測 | ✅ 已簡報 |
| 17 | Dual Framework 2025 - δ-FPG 雙框架 | ✅ 已簡報 |
| 18 | Taiwan MJ Hypertension 2024 - 多次健檢預測 | ✅ 已簡報 |

### Meeting 19 待完成任務

1. **論文選讀** ✅
   - [x] 閱讀 SMOTE+SHAP 2025（已評估為參考價值有限）
   - [x] 閱讀 Prediabetes TaiwanMJ 2024 摘要
   - [x] 閱讀 China Prediabetes→Diabetes 2025（備選，未使用 Δ 特徵）
   - [x] **選定 Kanegae Hypertension 2020** ← 使用 Δ 特徵，驗證我們的方法論
   - [x] 深度解析並建立 memo + 中文翻譯

2. **實驗任務**（來自 Meeting 18 Action Items）
   - [ ] 5-fold CV（所有模型重新跑交叉驗證）
   - [ ] Decision Tree (DT) 模型實驗
   - [ ] MTL vs STL 完整比較實驗
   - [ ] PySR 樹深度實驗

3. **文件任務**
   - [ ] 撰寫 Problem Definition（含數學公式）
   - [ ] 整理實驗/假說列表（Variations）

---

## 📌 研究方法論總結

### 常用模型（按台灣文獻出現頻率）

1. **Random Forest** - 多篇研究表現優異
2. **XGBoost** - 糖尿病預測最佳 (Liu 2024: AUC 0.93)
3. **Logistic Regression** - 基準模型
4. **SVM, ANN** - 特定情境有優勢

### 常用資料處理技術

1. **類別不平衡**：SMOTE, SMOTE-NC, Over/Under-sampling
2. **缺失值**：Mean imputation, KNN
3. **標準化**：Z-score normalization
4. **特徵選擇**：LASSO, RF feature importance, SHAP

### 評估指標（推薦）

- **主要**：AUC-ROC（處理不平衡資料）
- **次要**：Accuracy, Precision, Recall, F1-Score
- **臨床**：Sensitivity, Specificity, NPV, PPV
- **穩定性**：交叉驗證、外部驗證

---

## 🔍 研究缺口分析

### 本研究填補的缺口

1. ✅ **多標籤同時預測**（三高同時預測）
2. ✅ **縱向時序特徵**（Δ 變化量）
3. ✅ **台灣本土三高綜合研究**
4. ✅ **多資料集驗證**（中國 + 加拿大）

### 性能基準（Benchmark）

| 疾病 | AUC 範圍 | 參考文獻 |
|------|---------|---------|
| 高血壓 | 0.75-0.85 | Hung 2021 |
| 糖尿病 | 0.76-0.99 | Liu 2024, Dual 2025, Chen 2023 |
| 代謝症候群 | 0.90-0.93 | ANN MetS 2006-14 |

**本研究目標**：AUC > 0.75, F1 > 0.65, Recall > 0.65

---

## 📖 快速查找

### 按 PDF 檔案位置查找

- [diagnostics-15-00072.pdf](../references/diagnostics-15-00072.pdf) → Liu 2024 (糖尿病) ✅
- [diagnostics-15-02507.pdf](../references/diagnostics-15-02507.pdf) → Dual 2025 (前驅糖尿病) 📌
- [fcvm-08-778306.pdf](../references/fcvm-08-778306.pdf) → Hung 2021 (高血壓) ⚠️

### 按關鍵詞查找

- **縱向研究 / Longitudinal**: Liu 2024, Dual 2025
- **SHAP**: Dual 2025
- **台灣資料**: Liu 2024, Dual 2025, Hung 2021
- **XGBoost**: Liu 2024, Hung 2021, Dual 2025
- **δ特徵 / Δ特徵**: Dual 2025
- **類別不平衡 / SMOTE**: Liu 2024, Hung 2021

---

**文檔建立日期**：2025-11-13
**最後更新**：2026-01-09（新增 Meeting 18-19 論文）
**維護者**：紀伯喬

---

## 🔗 快速導航

- 📂 [返回 Literature Notes 目錄](.)
- 📊 [查看 Q2 台灣文獻回顧](../research_plans/Q2_Taiwan_Literature_Review.md)
- 📋 [查看系統性文獻回顧](Systematic_Literature_Review.md)
- 📖 [Meeting 15-17 論文總結](Meeting_15-17_Papers_Summary.md)
- 🎯 [Meeting 18 會議紀錄](../meeting_notes/Meeting_18_Notes.md)
- 📑 [論文候選清單](../memos/論文候選清單_從Dual2025延伸.md)
- 📝 [Paper_SMOTE_SHAP_2025 筆記](../memos/Paper_SMOTE_SHAP_2025.md)
- 📝 [Paper_Prediabetes_TaiwanMJ_2024 筆記](../memos/Paper_Prediabetes_TaiwanMJ_2024.md)
- 📝 [Paper_China_Prediabetes_Diabetes_2025 筆記](summaries/Paper_China_Prediabetes_Diabetes_2025.md)
- 📝 [Paper_Kanegae_Hypertension_2020 筆記](summaries/Paper_Kanegae_Hypertension_2020.md) ⭐ **Meeting 19 選定**
