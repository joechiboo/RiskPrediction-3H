# 文獻總覽索引

**最後更新**：2026-03-04
**用途**：統整所有已讀論文的狀態與分類

---

## 📊 閱讀狀態總覽

| 狀態 | 數量 | 說明 |
|------|------|------|
| ✅ 已完整分析（有深度解析＋簡報） | 6 | Meeting 15-20 論文 |
| ✅ 已深度解析（尚未簡報） | 11 | Tier 2 全部 + SMOTE+SHAP 2025 |
| 📋 已閱讀摘要與方法 | 2 | Prediabetes 2024, China Prediabetes 2025 |
| 📌 待瀏覽（Tier 3-4） | 20 | 背景文獻+經典方法 |

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
| 20 | **Majcherek et al. 2025 (PLOS ONE) - 18 種模型糖尿病風險預測** | ✅ **已簡報** |
| - | Luo et al. 2024 (BMJ Open) - 資料集原始論文 | ✅ 已深度解析 |
| - | Ye et al. 2018 (JMIR) - ML + EHR 高血壓預測 | ✅ 已深度解析 |
| - | Sun et al. 2017 (Systematic Review) - 高血壓預測模型回顧 | ✅ 已深度解析 |

---

## 🎯 按疾病分類

### 📦 資料集原始論文（Dataset Source）

#### 📌 Luo et al. (2024) - SUA 與心血管疾病風險因子 ⭐⭐⭐⭐⭐【資料集來源】【Meeting 20 候選】

- **標題**：Associations of serum uric acid with cardiovascular disease risk factors: a retrospective cohort study in southeastern China
- **期刊**：BMJ Open, 13(9):e073930
- **DOI**：[10.1136/bmjopen-2023-073930](https://doi.org/10.1136/bmjopen-2023-073930)
- **PDF位置**：[Luo_BMJOpen_SUA_CVD_2024.pdf](papers/Luo_BMJOpen_SUA_CVD_2024.pdf)
- **資料**：杭州社區健檢，2010-2018，6,119 人（男 2,041、女 4,078），≥40 歲，≥3 次健檢
- **追蹤期**：中位數 6.18 年
- **方法**：回顧性世代研究，Cox proportional hazards model
- **確診定義**：
  - 高血壓：SBP ≥ 140 或 DBP ≥ 90，**或已確診且正在服用降壓藥物**
  - 高血糖：FBG ≥ 7.0，**或自我報告糖尿病**
  - 高血脂：TC ≥ 6.22
- **核心發現**：
  - SUA 升高增加兩性高血脂風險
  - 高血糖、高血壓的關聯僅出現在女性（尤其是停經後女性）
  - 肥胖族群中關聯不顯著
- **排除條件**：基線已有高血壓、高血糖、高血脂者
- **限制**：缺乏吸菸、飲酒、運動、飲食資料；單中心設計
- **狀態**：✅ 已深度解析
- **與本研究關聯度**：⭐⭐⭐⭐⭐ (最高)
  - **本研究使用的資料集即來自此論文**
  - 確診定義包含用藥者（見 [Memo 22](../06_memos/22_資料集確診定義包含用藥者.md)）
- **相關文檔**：[Luo_BMJOpen_SUA_CVD_2024_深度解析.md](reviews/Luo_BMJOpen_SUA_CVD_2024_深度解析.md)

---

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

#### ✅ Sun et al. (2017) - 高血壓預測模型系統性回顧【Ch2 綜述基礎】

- **標題**：Recent development of risk-prediction models for incident hypertension: An updated systematic review
- **期刊**：PLoS ONE (SCIE, IF 2.6, Q1/Q2)
- **DOI**：[10.1371/journal.pone.0187240](https://doi.org/10.1371/journal.pone.0187240)
- **PMC**：[PMC5662179](https://pmc.ncbi.nlm.nih.gov/articles/PMC5662179/)
- **PDF位置**：[Sun_Hypertension_SystematicReview_2017.pdf](papers/Sun_Hypertension_SystematicReview_2017.pdf)
- **內容**：系統性回顧 26 篇研究、48 個高血壓預測模型
- **常見風險因子**：BMI, Age, 血壓, 吸菸, 家族史, 生化指標
- **統計方法**：Logistic (12篇), COX (7篇), Weibull (6篇)
- **狀態**：✅ 已深度解析
- **用途**：寫第二章文獻探討的重要參考
- **相關文檔**：[Sun_PLOSONE_HypertensionSR_2017_深度解析.md](reviews/Sun_PLOSONE_HypertensionSR_2017_深度解析.md)

#### ✅ Ye et al. (2018) - ML + EHR 高血壓預測

- **標題**：Prediction of Incident Hypertension Within the Next Year: Prospective Study Using Statewide Electronic Health Records and Machine Learning
- **期刊**：JMIR (SCIE, IF 5.8, Q1)
- **DOI**：[10.2196/jmir.9268](https://doi.org/10.2196/jmir.9268)
- **PMC**：[PMC5811646](https://pmc.ncbi.nlm.nih.gov/articles/PMC5811646/)
- **PDF位置**：[Ye_JMIR_Hypertension_ML_2018.pdf](papers/Ye_JMIR_Hypertension_ML_2018.pdf)
- **資料**：美國 Maine 州 EHR，823,627 人（回顧）/ 680,810 人（前瞻）
- **方法**：XGBoost（特徵選擇 + 模型建構）
- **最佳結果**：AUC 0.917（回顧）/ 0.870（前瞻）
- **注意**：有後續評論指出可能存在 data leakage（前 5 重要特徵為降壓藥）
- **狀態**：✅ 已深度解析
- **相關文檔**：[Ye_JMIR_Hypertension_ML_2018_深度解析.md](reviews/Ye_JMIR_Hypertension_ML_2018_深度解析.md)

#### ✅ Hung et al. (2021) - 隱匿性高血壓預測
- **期刊**：Frontiers in Cardiovascular Medicine, 8:778306
- **DOI**：[10.3389/fcvm.2021.778306](https://doi.org/10.3389/fcvm.2021.778306)
- **PDF位置**：[Hung_FrontCardiovascMed_Hypertension_2021.pdf](papers/Hung_FrontCardiovascMed_Hypertension_2021.pdf)
- **資料**：台灣六家醫學中心 + 台北榮總，970+416人
- **方法**：LR, RF, XGBoost, ANN + SMOTE-NC
- **最佳模型**：RF (AUC 0.851/0.837)
- **關鍵特徵**：DBP, MAP, SBP, PP, beta-blocker, HDL-C
- **狀態**：✅ 已深度解析
- **相關文檔**：[Hung_FrontCardiovascMed_MaskedHTN_2021_深度解析.md](reviews/Hung_FrontCardiovascMed_MaskedHTN_2021_深度解析.md)

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

#### ✅ Majcherek et al. (2025) - 18 種模型糖尿病風險預測 ⭐⭐⭐⭐【Meeting 20 選定】

- **標題**：AI-driven analysis of diabetes risk determinants in U.S. adults: Exploring disease prevalence and health factors
- **期刊**：PLoS ONE, 20(9): e0328655
- **DOI**：[10.1371/journal.pone.0328655](https://doi.org/10.1371/journal.pone.0328655)
- **PMC**：[PMC12407459](https://pmc.ncbi.nlm.nih.gov/articles/PMC12407459/)
- **PDF位置**：[Majcherek_PLOSONE_Diabetes_BRFSS_2025.pdf](papers/Majcherek_PLOSONE_Diabetes_BRFSS_2025.pdf)
- **資料**：美國 BRFSS 2015，253,680 名成人
- **方法**：18 種 ML 模型（含 LR、NB、LDA、QDA、Ridge、DT、RF、XGBoost 等）
- **最佳模型**：Extra Trees Classifier (Accuracy 96%, AUC 0.99)
- **可解釋性**：SHAP（Global + Decision plots）
- **類別平衡**：ROS / SMOTE / ADASYN 比較
- **狀態**：✅ 已深度解析
- **與本研究關聯度**：⭐⭐⭐⭐
  - **18 種模型同時涵蓋 NB、LDA 等傳統統計方法**，為我們選擇 NB/LDA 提供文獻依據
  - 糖尿病為我們三高預測之一
  - 同樣使用 SHAP 可解釋性
  - 傳統方法（LR/NB/LDA）AUC 0.71–0.73，與我們的結果趨勢可對照
- **相關文檔**：
  - [Majcherek_PLOSONE_Diabetes_2025_深度解析.md](reviews/Majcherek_PLOSONE_Diabetes_2025_深度解析.md)

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

### 深度解析文檔（已完成，共 17 篇）

#### Tier 1 核心文獻（7 篇）

1. [Luo_BMJOpen_SUA_CVD_2024_深度解析.md](reviews/Luo_BMJOpen_SUA_CVD_2024_深度解析.md) — 資料集原始論文
2. [Taiwan_MJ_Hypertension_2024_深度解析.md](reviews/Taiwan_MJ_Hypertension_2024_深度解析.md) — 多次健檢預測高血壓
3. [Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md](reviews/Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md) — 台灣糖尿病預測
4. [Dual_2025_深度解析.md](reviews/Dual_2025_深度解析.md) — δ-FPG 雙框架
5. [Majcherek_PLOSONE_Diabetes_2025_深度解析.md](reviews/Majcherek_PLOSONE_Diabetes_2025_深度解析.md) — 18 模型比較
6. [Kanegae_JClinHypertens_2020_深度解析.md](reviews/Kanegae_JClinHypertens_2020_深度解析.md) — AI 高血壓預測（Δ 特徵）
7. [Ye_JMIR_Hypertension_ML_2018_深度解析.md](reviews/Ye_JMIR_Hypertension_ML_2018_深度解析.md) — EHR 大規模高血壓預測

#### Tier 2 重要文獻（9 篇）

8. [Alaa_PLOSONE_AutoML_2019_深度解析.md](reviews/Alaa_PLOSONE_AutoML_2019_深度解析.md) — AutoML CVD 預測
9. [Dinh_BMC_Diabetes_CVD_2019_深度解析.md](reviews/Dinh_BMC_Diabetes_CVD_2019_深度解析.md) — 糖尿病+CVD 預測
10. [Hung_FrontCardiovascMed_MaskedHTN_2021_深度解析.md](reviews/Hung_FrontCardiovascMed_MaskedHTN_2021_深度解析.md) — 隱匿性高血壓
11. [Tsai_SciReports_MTL_2025_深度解析.md](reviews/Tsai_SciReports_MTL_2025_深度解析.md) — MTL 慢性病預測
12. [Sun_PLOSONE_HypertensionSR_2017_深度解析.md](reviews/Sun_PLOSONE_HypertensionSR_2017_深度解析.md) — 高血壓預測系統性回顧
13. [Cranmer_arXiv_PySR_2023_深度解析.md](reviews/Cranmer_arXiv_PySR_2023_深度解析.md) — PySR 符號回歸工具
14. [He_IEEE_ImbalancedLearning_2009_深度解析.md](reviews/He_IEEE_ImbalancedLearning_2009_深度解析.md) — 不平衡學習綜述
15. [Chawla_JAIR_SMOTE_2002_深度解析.md](reviews/Chawla_JAIR_SMOTE_2002_深度解析.md) — SMOTE 原始論文
16. [Saito_PLOSONE_PRAUC_2015_深度解析.md](reviews/Saito_PLOSONE_PRAUC_2015_深度解析.md) — PR-AUC vs ROC-AUC

#### 其他

17. [SMOTE_SHAP_2025_深度解析.md](reviews/SMOTE_SHAP_2025_深度解析.md) — SMOTE + SHAP 框架（參考價值有限）

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

## 📋 待讀論文清單（Tier 3-4）

| 優先度 | 論文 | 原因 |
|--------|------|------|
| 🔶 | James et al. (2014) JNC 8 | 讀高血壓診斷標準段 |
| 🔶 | ADA (2025) Diabetes Care | 讀糖尿病診斷標準段 |
| 🔶 | NCEP ATP III (2002) | 讀血脂異常診斷標準段 |
| 🔶 | Alberti et al. (2009) | 讀代謝症候群定義 |
| ⚪ | WHO (2023) / WHF (2023) | 讀摘要+亞洲統計 |
| ⚪ | Ohira & Iso (2013) / Zhao (2021) | 讀東亞段 |
| ⚪ | Breiman (2001) / Chen & Guestrin (2016) 等 | 讀摘要 |

---

## 🎯 Meeting 19 準備重點

### 已完成的 Meeting

| Meeting | 論文主題 | 狀態 |
|---------|----------|------|
| 15 | Liu 2024 - 台中榮總糖尿病 10 年預測 | ✅ 已簡報 |
| 16 | Taiwan MTL 2025 - 多任務學習慢性病預測 | ✅ 已簡報 |
| 17 | Dual Framework 2025 - δ-FPG 雙框架 | ✅ 已簡報 |
| 18 | Taiwan MJ Hypertension 2024 - 多次健檢預測 | ✅ 已簡報 |
| 19 | Kanegae 2020 - AI 高精度高血壓預測 | ✅ 已簡報 |
| 20 | Majcherek 2025 - 18 種模型糖尿病預測（BRFSS） | 📌 選定 |

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

- **主要**：AUC-ROC + **PR-AUC**（Saito 2015 證明不平衡時需並列報告）
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
- [Luo_BMJOpen_SUA_CVD_2024.pdf](papers/Luo_BMJOpen_SUA_CVD_2024.pdf) → Luo 2024 (資料集原始論文) 📌
- [Sun_Hypertension_SystematicReview_2017.pdf](papers/Sun_Hypertension_SystematicReview_2017.pdf) → Sun 2017 (高血壓系統性回顧) 📌
- [Ye_JMIR_Hypertension_ML_2018.pdf](papers/Ye_JMIR_Hypertension_ML_2018.pdf) → Ye 2018 (ML+EHR 高血壓) 📌

### 按關鍵詞查找

- **縱向研究 / Longitudinal**: Liu 2024, Dual 2025, Kanegae 2020, Ye 2018, Wang 2024
- **SHAP**: Dual 2025, Majcherek 2025
- **台灣資料**: Liu 2024, Dual 2025, Hung 2021, Tsai 2025, Wang 2024
- **XGBoost**: Liu 2024, Hung 2021, Dual 2025, Kanegae 2020, Ye 2018
- **δ特徵 / Δ特徵**: Dual 2025, Kanegae 2020
- **類別不平衡 / SMOTE**: He & Garcia 2009, Chawla 2002, Hung 2021, Majcherek 2025
- **評估指標 / PR-AUC**: Saito 2015, He & Garcia 2009
- **符號回歸 / PySR**: Cranmer 2023
- **系統性回顧**: Sun 2017, He & Garcia 2009
- **多任務學習 / MTL**: Tsai 2025
- **AutoML**: Alaa 2019

---

**文檔建立日期**：2025-11-13
**最後更新**：2026-03-04（Tier 1 全部完成 + Tier 2 全部深度解析完成，17/36 = 47%）
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
