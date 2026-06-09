<!--
中英對照工作稿（供校稿/與教授討論用，非投稿稿）。
英文 = 投稿用；中文（引用區塊）= 對照翻譯。數字兩邊一致，取自論文 Ch4/Ch6。
英文正式版見 manuscript_v1.md。
-->

# Simultaneous machine-learning prediction of hypertension, hyperglycemia, and dyslipidemia from longitudinal health-checkup data: a comprehensive model comparison with interpretable symbolic regression

> **以縱向健檢資料同時預測高血壓、高血糖與高血脂：結合可解釋符號回歸的機器學習模型全面比較**

**Running title:** Predicting the "three highs" from longitudinal checkups

> **短題名：** 以縱向健檢資料預測「三高」

**Po-Chiao Chi¹ (紀伯喬), Yang Syu¹ (許揚)** *(作者順序/通訊作者待定)*
¹ Department of Computer Science, College of Science, National Taipei University of Education, Taipei, Taiwan（國立臺北教育大學理學院資訊科學系）

---

## Abstract

> ## 摘要

**Background.** Hypertension, hyperglycemia, and dyslipidemia—collectively the "three highs"—are the principal modifiable risk factors for cardiovascular disease and frequently co-occur. Conventional risk scores rely on a single time point and do not exploit the dynamic information embedded in repeated health checkups. Existing machine-learning studies typically target a single disease, compare few models, and seldom address interpretability. We aimed to build and systematically evaluate a longitudinal framework that predicts all three conditions simultaneously, while quantifying the value of change (delta) features and exploring interpretable models.

> **背景。** 高血壓、高血糖與高血脂（合稱「三高」）是心血管疾病的主要可控風險因子，且常共病發生。傳統風險評分僅依賴單一時間點，未利用重複健檢中蘊含的動態資訊。現有機器學習研究多聚焦單一疾病、比較模型數量有限、且少有探討可解釋性。本研究旨在建立並系統性評估一個同時預測三高的縱向框架，量化變化量（Δ）特徵的價值，並探索可解釋模型。

**Methods.** We used a publicly available longitudinal community health-checkup cohort (Luo et al., Dryad; Hangzhou, China, 2010–2018; adults aged ≥40). After excluding participants with fewer than three checkups, 6,056 individuals remained. A three-time-point design (Y−2, Y−1, Y0) with a sliding-window expansion produced 13,514 modeling records. Twenty-six features were derived: demographics, biomarkers at Y−2 and Y−1, and eight delta features (Y−1 − Y−2). Ten classifiers plus symbolic regression (PySR) were evaluated with stratified group 5-fold cross-validation. The primary metric was AUC-ROC.

> **方法。** 使用公開於 Dryad 的縱向社區健檢世代（Luo 等人；中國杭州，2010–2018；≥40 歲成人）。排除健檢少於三次者後保留 6,056 人。採三時間點設計（Y−2、Y−1、Y0），以滑動窗口擴增為 13,514 筆建模紀錄。萃取 26 個特徵：人口學、Y−2 與 Y−1 的生物標記，以及 8 個 Δ 特徵（Y−1 − Y−2）。以分層分組 5 折交叉驗證評估十種分類器加符號回歸（PySR），主要指標為 AUC-ROC。

**Results.** LR was the most consistent model, achieving AUC 0.721 (hypertension), 0.938 (hyperglycemia), and 0.867 (dyslipidemia), with a balanced sensitivity/specificity profile and negligible overfitting (gap ≤0.004). With both Y−2 and Y−1 present, delta features were predictively redundant; given only the most recent visit, adding deltas raised AUC by 1.5–2.3%. Using only the top two features retained AUC within ~0.8% of the full model. Class-imbalance methods left AUC unchanged (<0.2%) but raised sensitivity from 0.04–0.34 to 0.70–0.88. Symbolic regression's 0.114 × FBG_(Y−1) reached AUC 0.943 for hyperglycemia and was fold-stable.

> **結果。** 邏輯迴歸（LR）最為穩定，AUC 達 0.721（高血壓）、0.938（高血糖）、0.867（高血脂），敏感度/特異度平衡良好且幾乎無過擬合（差距 ≤0.004）。當 Y−2 與 Y−1 皆存在時，Δ 特徵在預測上為冗餘；但僅有最近一次健檢時，加入 Δ 可提升 AUC 1.5–2.3%。僅用前兩大特徵即可保留 AUC 在完整模型的 ~0.8% 以內。類別不平衡處理方法對 AUC 幾乎無影響（<0.2%），但將敏感度從 0.04–0.34 提升至 0.70–0.88。符號回歸的 0.114 × FBG_(Y−1) 在高血糖達 AUC 0.943，且跨折穩定。

**Conclusions.** Longitudinal checkup data combined with simple feature engineering and a linear model achieve clinically useful, well-generalizing, and interpretable prediction of all three conditions. A two-feature model or a one-variable formula suffices for several tasks, supporting low-cost early-warning deployment in primary care.

> **結論。** 縱向健檢資料結合簡單特徵工程與線性模型，即可對三高達到臨床可用、泛化良好且可解釋的預測。雙特徵模型或單變數公式在多項任務已足夠，支持在基層醫療部署低成本早期預警系統。

**Keywords:** hypertension; hyperglycemia; dyslipidemia; machine learning; delta features

> **關鍵詞：** 高血壓；高血糖；高血脂；機器學習；變化量特徵

---

## 1. Background

> ## 1. 背景

### 1.1 The public-health burden of the "three highs"

> ### 1.1 「三高」的公共衛生負擔

Hypertension, hyperglycemia, and dyslipidemia are the dominant modifiable contributors to cardiovascular disease, stroke, and chronic kidney disease. Cardiovascular disease causes roughly 20 million deaths each year, close to one-third of global mortality [1]. The burden is especially heavy in Asia: more than a quarter of adults in the WHO Western Pacific region are hypertensive [2], and a small group of Asian countries accounts for nearly half of the world's diabetes cases [3]. Metabolic disease in East Asia has risen sharply, driven by genetic susceptibility, distinctive body-fat distribution, and rapid dietary westernization [4]. In Taiwan, the prevalence among adults aged ≥40 is 38.3% (hypertension), 34.1% (dyslipidemia), and 16.4% (hyperglycemia), yet 40–70% of affected individuals are unaware of their condition [5].

> 高血壓、高血糖與高血脂是心血管疾病、中風與慢性腎病的主要可控成因。心血管疾病每年造成約 2,000 萬人死亡，近全球死亡人數的三分之一 [1]。亞洲負擔尤重：WHO 西太平洋區逾四分之一成人罹患高血壓 [2]，少數亞洲國家即占全球糖尿病病例近半 [3]。東亞代謝疾病急遽上升，肇因於遺傳易感性、特殊體脂分布與飲食快速西化 [4]。在台灣，≥40 歲成人盛行率為高血壓 38.3%、高血脂 34.1%、高血糖 16.4%，但其中 40–70% 並不知道自己罹病 [5]。

The three conditions are mutually correlated and co-occur as the core of the metabolic syndrome: over 70% of patients with diabetes also have hypertension or dyslipidemia [6]. Metabolic-syndrome patients carry roughly twice the cardiovascular risk and five times the risk of type 2 diabetes [7]. This comorbidity argues for predicting the three conditions jointly rather than in isolation.

> 三者相互關聯，並共同構成代謝症候群核心：逾 70% 糖尿病患者同時合併高血壓或高血脂 [6]。代謝症候群患者的心血管風險約為兩倍、第二型糖尿病風險約為五倍 [7]。此共病性說明應同時（而非個別）預測三高。

### 1.2 The clinical value of early, longitudinal prediction

> ### 1.2 早期縱向預測的臨床價值

The three highs are typically asymptomatic early on and are often detected only at routine checkups or after complications arise. Because progression from health to disease usually passes through a multi-year prodromal phase—during which lifestyle change can still reverse risk—identifying high-risk individuals early is key. The trend toward younger onset prompted Taiwan to lower the eligibility age for adult preventive-health services from 40 to 30 in 2025 [8], extending screening demand to younger adults.

> 三高初期多無症狀，常於例行健檢或併發症出現後才發現。由於從健康到發病通常歷經數年「前驅期」，期間透過生活型態調整仍可逆轉風險，因此及早辨識高風險者至關重要。疾病年輕化趨勢促使台灣於 2025 年將成人預防保健服務年齡由 40 歲下修至 30 歲 [8]，將篩檢需求延伸至青壯年。

As checkups have become routine, large volumes of *longitudinal* checkup data have accumulated, recording how biomarkers evolve within an individual. Because health-status changes often precede a clinical diagnosis, longitudinal data are uniquely valuable for early prediction. Yet conventional risk-assessment tools rely on a single time point and do not exploit this dynamic information—the gap this study addresses.

> 隨健檢普及，大量*縱向*健檢資料持續累積，記錄個體生物標記隨時間的演變。由於健康狀態變化常先於臨床診斷，縱向資料在早期預測上具獨特價值。然而傳統風險評估工具僅依賴單一時間點，未利用此動態資訊——這正是本研究欲填補的缺口。

### 1.3 Related work and gaps

> ### 1.3 相關研究與缺口

Machine learning has been applied widely to single-disease checkup prediction. For hypertension, Kanegae et al. used XGBoost on Japanese occupational checkups (n=18,258, AUC 0.881) with longitudinal change features [9]; Ye et al. predicted one-year incident hypertension from US EHRs (n=823,627, AUC 0.917), though top features were antihypertensive drugs, raising leakage concerns [10]; Wang et al. showed on Taiwanese checkups (n=207,488) that more checkups improve accuracy (AUC 0.889) [11]. For diabetes, Liu et al. reached AUC 0.93 over a 10-year cohort [12], and Yang et al. found baseline fasting glucose overwhelmingly dominant [13]. Broader work includes Alaa et al. (UK Biobank, AUC 0.774) [14], Dinh et al. (NHANES, AUC 0.862) [15], Hung et al. (masked hypertension, AUC 0.851) [16], and Majcherek et al. (BRFSS) [17].

> 機器學習已廣泛用於單一疾病的健檢預測。高血壓方面，Kanegae 等人以 XGBoost 處理日本職場健檢（n=18,258，AUC 0.881）並使用縱向變化量特徵 [9]；Ye 等人以美國 EHR 預測一年內新發高血壓（n=823,627，AUC 0.917），但前幾名特徵為降壓藥物，有資料洩漏疑慮 [10]；Wang 等人在台灣健檢（n=207,488）證實健檢次數越多準確度越高（AUC 0.889）[11]。糖尿病方面，Liu 等人於十年世代達 AUC 0.93 [12]，Yang 等人發現基線空腹血糖具壓倒性重要性 [13]。其他研究包括 Alaa 等人（UK Biobank，AUC 0.774）[14]、Dinh 等人（NHANES，AUC 0.862）[15]、Hung 等人（隱匿性高血壓，AUC 0.851）[16] 與 Majcherek 等人（BRFSS）[17]。

Three gaps recur. First, almost all studies predict a *single* disease, despite strong comorbidity. Second, model comparisons are narrow, leaving clinicians without comprehensive model-selection evidence [18]. Third, interpretability—essential for clinical adoption—is rarely addressed. Multi-task learning has been proposed for joint chronic-disease prediction (Tsai et al. found multi-task and single-task comparable with fewer parameters [19]) but not for the three highs with delta features.

> 三個缺口反覆出現。其一，儘管共病性強，幾乎所有研究僅預測*單一*疾病。其二，模型比較範圍狹窄，臨床端缺乏完整的模型選擇依據 [18]。其三，對臨床採用至關重要的可解釋性少被探討。多任務學習雖被提出用於慢性病聯合預測（Tsai 等人發現多任務與單任務效能相當但參數更少 [19]），但尚未用於結合 Δ 特徵的三高預測。

### 1.4 Objectives and contributions

> ### 1.4 研究目標與貢獻

We build a longitudinal framework predicting the three highs simultaneously, evaluated comprehensively. Contributions: (1) a systematic comparison of ten classifiers plus symbolic regression across the three conditions, with leakage-controlled validation; (2) a complete ablation disentangling the predictive versus interpretive roles of delta features; (3) interpretability analysis combining SHAP and symbolic regression, including single-variable formulas with clinically useful accuracy; and (4) robustness experiments (class imbalance, data filtering, checkup frequency, multi-task vs single-task) establishing the stability of the findings. All data are public, making the study fully reproducible.

> 本研究建立同時預測三高的縱向框架並全面評估。貢獻包括：(1) 跨三項疾病系統性比較十種分類器加符號回歸，並以無洩漏驗證；(2) 完整消融實驗釐清 Δ 特徵在「預測」與「解釋」上的不同角色；(3) 結合 SHAP 與符號回歸的可解釋性分析，含具臨床可用準確度的單變數公式；(4) 多組穩健性實驗（類別不平衡、資料篩選、健檢次數、多任務 vs 單任務）確立發現的穩定性。所有資料公開，研究完全可重現。

---

## 2. Methods

> ## 2. 方法

### 2.1 Data source and cohort

> ### 2.1 資料來源與世代

We used the longitudinal community health-checkup dataset published by Luo et al. on Dryad [20,21]: community health surveys in Hangzhou, China, 2010–2018, enrolling adults aged ≥40 (6,119 participants, 25,744 records), most with three or more checkups. The dataset records visit number rather than calendar date; intervals were inferred from age differences. About 90% kept a fixed 2-year interval (mean 1.90 years, SD 0.36), so delta features are directly comparable. We excluded 63 individuals (1.03%) with fewer than three valid records, leaving **6,056 participants** (98.97% retention). Disease labels follow international thresholds [22–24]: hypertension SBP ≥140 or DBP ≥90 mmHg; hyperglycemia FBG ≥7.0 mmol/L; dyslipidemia TC ≥6.22 mmol/L, recoded to binary 0/1.

> 使用 Luo 等人公開於 Dryad 的縱向社區健檢資料 [20,21]：中國杭州 2010–2018 年社區健康調查，納入 ≥40 歲成人（6,119 人、25,744 筆紀錄），多數有三次以上健檢。資料僅記錄「第幾次健檢」而非日期，間隔以年齡差推算。約 90% 維持固定 2 年間隔（平均 1.90 年、標準差 0.36），故 Δ 特徵可直接比較。本研究排除 63 位（1.03%）有效紀錄不足三次者，保留 **6,056 人**（保留率 98.97%）。疾病標記依國際閾值 [22–24]：高血壓 SBP ≥140 或 DBP ≥90 mmHg；高血糖 FBG ≥7.0 mmol/L；高血脂 TC ≥6.22 mmol/L，並重新編碼為二元 0/1。

### 2.2 Study design and sliding window

> ### 2.2 研究設計與滑動窗口

We adopted a three-time-point design, naming time points relative to target year Y0: Y−2 (≈4 years prior), Y−1 (≈2 years prior), Y0 (target). Inputs are biomarkers at Y−2 and Y−1 plus their changes; the target is disease status at Y0. Predicting Y0 rather than Y−1 avoids leakage and provides a ~2-year warning window. A sliding window (a participant with N checkups yields N−2 records) expanded 6,056 participants to **13,514 records**. Because one participant contributes multiple records, cross-validation must keep all of a participant's records in the same fold.

> 採三時間點設計，相對於目標年 Y0 命名：Y−2（約四年前）、Y−1（約兩年前）、Y0（目標）。輸入為 Y−2 與 Y−1 的生物標記及其變化量；目標為 Y0 的疾病狀態。以 Y0（而非 Y−1）為目標可避免洩漏，並提供約兩年的預警窗口。滑動窗口（N 次健檢者產生 N−2 筆紀錄）將 6,056 人擴增為 **13,514 筆**。由於同一人貢獻多筆紀錄，交叉驗證須將同一人所有紀錄留在同一折。

### 2.3 Feature engineering

> ### 2.3 特徵工程

Twenty-six features (Table 1): two demographics; eight biomarkers each at Y−2 and Y−1 (FBG, TC, Cr, UA, eGFR, BMI, SBP, DBP); and eight deltas, Δ_i = X_(i,Y−1) − X_(i,Y−2). Deltas encode trend: positive ΔFBG = rising glucose; negative ΔeGFR = declining renal function.

> 共 26 個特徵（表 1）：兩個人口學變數；Y−2 與 Y−1 各八個生物標記（FBG、TC、Cr、UA、eGFR、BMI、SBP、DBP）；以及八個變化量 Δ_i = X_(i,Y−1) − X_(i,Y−2)。Δ 編碼趨勢：ΔFBG 為正表示血糖上升；ΔeGFR 為負表示腎功能下降。

**Table 1. Feature set (26 features). 表 1　特徵集（26 個特徵）**

| Category 類別 | Features 特徵 | n |
|---|---|---|
| Demographics 人口學 | Sex, Age | 2 |
| Y−2 biomarkers Y−2 生物標記 | FBG, TC, Cr, UA, eGFR, BMI, SBP, DBP | 8 |
| Y−1 biomarkers Y−1 生物標記 | FBG, TC, Cr, UA, eGFR, BMI, SBP, DBP | 8 |
| Delta 變化量 (Y−1 − Y−2) | ΔFBG, ΔTC, ΔCr, ΔUA, ΔeGFR, ΔBMI, ΔSBP, ΔDBP | 8 |

### 2.4 Class imbalance

> ### 2.4 類別不平衡

Positive rates differed markedly: hypertension 16.68% (1,010/6,056), hyperglycemia 5.53% (335), dyslipidemia 5.96% (361). We used cost-sensitive learning via class weights, w_k = n / (K·n_k) [33], and benchmarked SMOTE [34], ADASYN, and random under-sampling.

> 陽性率差異明顯：高血壓 16.68%（1,010/6,056）、高血糖 5.53%（335）、高血脂 5.96%（361）。採成本敏感學習，以類別權重 w_k = n / (K·n_k) 處理 [33]，並與 SMOTE [34]、ADASYN、隨機欠採樣比較。

### 2.5 Models and validation

> ### 2.5 模型與驗證

Ten classifiers span statistical (LR, NB, LDA [25]), instance-based (KNN), tree-based (DT, RF [26], XGBoost [27], LightGBM [28]), kernel (SVM [29]), and neural (MLP [30]) families. Symbolic regression used PySR [31] (operators +,−,×,÷,exp,log,abs,square; maxsize 35; 200 iterations). Interpretability used SHAP [32]. All experiments used **stratified group 5-fold cross-validation**: stratification preserves class ratio; grouping on patient identity prevents leakage from the sliding window. The primary metric was AUC-ROC (robust to imbalance at prevalences >5%, above the regime where PR-AUC is preferred [35]); sensitivity, specificity, and F1 were also reported, with sensitivity emphasized for screening.

> 十種分類器涵蓋統計（LR、NB、LDA [25]）、實例式（KNN）、樹模型（DT、RF [26]、XGBoost [27]、LightGBM [28]）、核方法（SVM [29]）與神經網路（MLP [30]）。符號回歸使用 PySR [31]（運算子 +,−,×,÷,exp,log,abs,square；maxsize 35；200 次迭代）。可解釋性使用 SHAP [32]。所有實驗採**分層分組 5 折交叉驗證**：分層維持類別比例，依病患身分分組以避免滑動窗口造成的洩漏。主要指標為 AUC-ROC（在盛行率 >5% 時對不平衡穩健，高於偏好 PR-AUC 的極端區間 [35]）；並報告敏感度、特異度與 F1，篩檢情境下特別重視敏感度。

### 2.6 Experiments

> ### 2.6 實驗

Ten experiments: (1) model comparison; (2) SHAP importance; (3) delta ablation; (4) feature-count ablation; (5) class-imbalance comparison; (6) data-filtering comparison; (7) checkup-frequency effect; (8) per-time-point power; (9) multi-task vs single-task; (10) symbolic regression with stability checking. All ran on consumer hardware (Intel Core i7-11700, 32 GB RAM, RTX 3050; Python 3.10; scikit-learn, XGBoost, LightGBM, PySR, SHAP); full 5-fold runs completed within minutes per model.

> 十項實驗：(1) 模型比較；(2) SHAP 重要性；(3) Δ 消融；(4) 特徵數量消融；(5) 類別不平衡比較；(6) 資料篩選比較；(7) 健檢次數效應；(8) 各時間點預測力；(9) 多任務 vs 單任務；(10) 符號回歸含穩定性檢驗。全部於消費級硬體執行（Intel Core i7-11700、32 GB RAM、RTX 3050；Python 3.10；scikit-learn、XGBoost、LightGBM、PySR、SHAP）；每個模型的完整 5 折皆於數分鐘內完成。

---

## 3. Results

> ## 3. 結果

### 3.1 Model comparison

> ### 3.1 模型比較

LR achieved the highest AUC for hyperglycemia (0.938) and dyslipidemia (tied, 0.867); RF was best for hypertension (0.743). Hyperglycemia was easiest (all models except KNN >0.83), hypertension hardest (0.630–0.743), consistent with blood pressure's larger short-term variability (Table 2).

> LR 在高血糖（0.938）與高血脂（並列 0.867）達最高 AUC；高血壓以 RF 最佳（0.743）。高血糖最易預測（除 KNN 外所有模型 >0.83），高血壓最難（0.630–0.743），與血壓短期波動較大一致（表 2）。

**Table 2. Test AUC by model (mean ± SD, 5-fold CV). 表 2　各模型測試集 AUC（平均 ± 標準差）** *[Bootstrap 95% CI to be added 投稿前補]*

| Model | Hypertension 高血壓 | Hyperglycemia 高血糖 | Dyslipidemia 高血脂 |
|---|---|---|---|
| LR | 0.721 ± 0.017 | **0.938 ± 0.010** | **0.867 ± 0.012** |
| NB | 0.709 ± 0.022 | 0.917 ± 0.010 | 0.847 ± 0.015 |
| LDA | 0.720 ± 0.017 | 0.936 ± 0.011 | 0.867 ± 0.012 |
| KNN | 0.630 ± 0.018 | 0.782 ± 0.020 | 0.673 ± 0.013 |
| DT | 0.658 ± 0.012 | 0.835 ± 0.014 | 0.744 ± 0.037 |
| RF | **0.743 ± 0.013** | 0.932 ± 0.008 | 0.859 ± 0.014 |
| XGBoost | 0.738 ± 0.012 | 0.930 ± 0.014 | 0.857 ± 0.016 |
| LightGBM | 0.730 ± 0.011 | 0.926 ± 0.015 | 0.852 ± 0.011 |
| SVM | 0.726 ± 0.011 | 0.919 ± 0.012 | 0.845 ± 0.012 |
| MLP | 0.703 ± 0.033 | 0.919 ± 0.021 | 0.742 ± 0.136 |

With balanced class weights, LR kept a strong sensitivity/specificity balance (e.g., hyperglycemia 0.858/0.882), whereas LDA, MLP, and KNN behaved extremely conservatively despite competitive AUC—LDA reached dyslipidemia AUC 0.867 but sensitivity only 0.118 versus LR's 0.799 at the same AUC—illustrating why a single metric is insufficient for screening.

> 採平衡類別權重時，LR 維持良好的敏感度/特異度平衡（如高血糖 0.858/0.882）；而 LDA、MLP、KNN 雖 AUC 不差卻極度保守——LDA 在高血脂達 AUC 0.867，但敏感度僅 0.118，相同 AUC 下 LR 為 0.799——凸顯單一指標不足以評估篩檢用途。

Comparing train and test AUC (Table 3), statistical models showed near-zero overfitting (gap ≤0.010), whereas tree ensembles overfit heavily (RF train AUC 0.997 for hypertension, gap 0.254; LightGBM train AUC 1.000 for hyperglycemia). Tree models' apparent edge derives partly from greater fitting capacity rather than better generalization; LR's low-variance behavior is advantageous for deployment.

> 比較訓練與測試 AUC（表 3），統計模型幾乎無過擬合（差距 ≤0.010），樹集成則嚴重過擬合（RF 高血壓訓練 AUC 0.997、差距 0.254；LightGBM 高血糖訓練 AUC 1.000）。樹模型的表面優勢部分源於更強的擬合能力而非更佳泛化；LR 的低變異特性對部署有利。

**Table 3. Train AUC and generalization gap (train − test). 表 3　訓練集 AUC 與泛化差距（訓練 − 測試）**

| Model | HTN train / gap | HG train / gap | DL train / gap |
|---|---|---|---|
| LR | 0.724 / 0.003 | 0.940 / 0.003 | 0.871 / 0.004 |
| NB | 0.712 / 0.003 | 0.919 / 0.002 | 0.857 / 0.010 |
| LDA | 0.724 / 0.004 | 0.938 / 0.001 | 0.870 / 0.003 |
| KNN | 0.863 / 0.234 | 0.976 / 0.194 | 0.937 / 0.264 |
| DT | 0.853 / 0.195 | 0.980 / 0.145 | 0.944 / 0.201 |
| RF | 0.997 / **0.254** | 0.996 / 0.064 | 0.993 / 0.134 |
| XGBoost | 0.909 / 0.170 | 0.995 / 0.064 | 0.974 / 0.117 |
| LightGBM | 0.969 / 0.239 | 1.000 / 0.074 | 0.997 / 0.146 |
| SVM | 0.863 / 0.137 | 0.983 / 0.063 | 0.946 / 0.101 |
| MLP | 0.712 / 0.009 | 0.935 / 0.015 | 0.763 / 0.021 |

### 3.2 Feature importance (SHAP)

> ### 3.2 特徵重要性（SHAP）

SHAP rankings (XGBoost) were disease-specific and clinically coherent (Table 4): hypertension led by SBP and age; hyperglycemia by FBG; dyslipidemia by TC and ΔeGFR. Two time points of the same biomarker usually co-appeared, indicating the model uses both recent value and historical trend. ΔeGFR was the only delta in the top 10 of all three diseases, suggesting renal-function change as a shared early marker. Deltas made up 30%/40%/30% of the top-10, showing nonlinear models split on change directly.

> SHAP 排序（XGBoost）具疾病特異性且符合臨床直覺（表 4）：高血壓由 SBP 與年齡主導；高血糖由 FBG；高血脂由 TC 與 ΔeGFR。同一標記的兩個時間點常同時出現，顯示模型兼用近期值與歷史趨勢。ΔeGFR 是唯一同時進入三疾病前十的 Δ 特徵，暗示腎功能變化為共通早期指標。Δ 在前十中佔 30%/40%/30%，顯示非線性模型直接以變化量分裂。

**Table 4. Top-5 SHAP features per disease (XGBoost). 表 4　各疾病前五 SHAP 特徵（XGBoost）**

| Rank 名次 | Hypertension 高血壓 | Hyperglycemia 高血糖 | Dyslipidemia 高血脂 |
|---|---|---|---|
| 1 | SBP_(Y−2) | FBG_(Y−1) | TC_(Y−1) |
| 2 | SBP_(Y−1) | FBG_(Y−2) | TC_(Y−2) |
| 3 | Age | ΔTC | ΔeGFR |
| 4 | ΔDBP | BMI_(Y−1) | Age |
| 5 | DBP_(Y−1) | BMI_(Y−2) | eGFR_(Y−2) |

### 3.3 Delta-feature ablation

> ### 3.3 Δ 特徵消融

With both Y−2 and Y−1 present, removing deltas changed AUC by essentially zero (Table 5): since Δ = Y−1 − Y−2, a linear model recovers the effect from the two raw coefficients, making deltas redundant. But with only Y−1, adding deltas raised AUC by 1.5–2.3% (Table 6)—because deltas reintroduce Y−2 information—confirming that more time points help. A delta-only model performed poorly (AUC 0.593/0.668/0.636): change direction alone, without the baseline value, has limited standalone power.

> 當 Y−2 與 Y−1 皆存在時，移除 Δ 對 AUC 幾乎無影響（表 5）：因 Δ = Y−1 − Y−2，線性模型可由兩個原始係數還原此效果，故 Δ 為冗餘。但僅有 Y−1 時，加入 Δ 可提升 AUC 1.5–2.3%（表 6）——因 Δ 重新帶入 Y−2 資訊——印證更多時間點有助預測。僅用 Δ 的模型表現不佳（AUC 0.593/0.668/0.636）：缺乏基線值時，變化方向本身的獨立預測力有限。

**Table 5. Full (26) vs No-Delta (18), LR. 表 5　完整(26) vs 去 Δ(18)，LR**

| Disease 疾病 | Full 完整 | No-Delta 去 Δ | Δ |
|---|---|---|---|
| HTN 高血壓 | 0.721 | 0.721 | 0.0% |
| HG 高血糖 | 0.938 | 0.938 | 0.0% |
| DL 高血脂 | 0.867 | 0.867 | 0.0% |

**Table 6. Y−1 + Delta vs Y−1 only, LR (AUC). 表 6　Y−1 + Δ vs 僅 Y−1，LR（AUC）**

| Disease 疾病 | Y−1 + Δ | Y−1 only 僅 Y−1 | Gain 提升 |
|---|---|---|---|
| HTN 高血壓 | 0.721 | 0.698 | **+2.3%** |
| HG 高血糖 | 0.938 | 0.923 | +1.5% |
| DL 高血脂 | 0.867 | 0.846 | +2.1% |

### 3.4 Feature-count ablation

> ### 3.4 特徵數量消融

Predictive power concentrated in very few features (Table 7). The top two SHAP features—two time points of one core biomarker—retained AUC within ~0.8% of the full model (HTN 0.715, HG 0.933, DL 0.861). A single feature sufficed for hyperglycemia (0.920). Beyond five features, differences were ≤0.005. This supports a low-cost scheme needing only two measurements of one core biomarker.

> 預測力高度集中於少數特徵（表 7）。前兩大 SHAP 特徵——同一核心標記的兩個時間點——即可保留 AUC 在完整模型 ~0.8% 內（高血壓 0.715、高血糖 0.933、高血脂 0.861）。單一特徵對高血糖已足夠（0.920）。超過五個特徵後差異 ≤0.005。此支持只需量測單一核心標記兩次的低成本方案。

**Table 7. Feature-count ablation, AUC (LR). 表 7　特徵數量消融，AUC（LR）**

| # features 特徵數 | HTN 高血壓 | HG 高血糖 | DL 高血脂 |
|---|---|---|---|
| 1 | 0.686 | 0.920 | 0.842 |
| 2 | 0.715 | 0.933 | 0.861 |
| 5 | 0.716 | 0.935 | 0.864 |
| 10 | 0.717 | 0.937 | 0.864 |
| 26 (all 全部) | 0.721 | 0.938 | 0.867 |

### 3.5 Robustness: class imbalance and data filtering

> ### 3.5 穩健性：類別不平衡與資料篩選

Across five imbalance strategies, AUC varied by <0.2% while sensitivity rose from 0.04–0.34 to 0.70–0.88 (Table 8). Strategies differed by <2% in sensitivity; class-weight is the simplest practical choice. Excluding windows already diagnosed at Y−2 changed AUC by ≤1.3% with no consistent direction, confirming that retaining all windows does not bias results.

> 五種不平衡策略中，AUC 變動 <0.2%，敏感度則由 0.04–0.34 提升至 0.70–0.88（表 8）。各策略敏感度差異 <2%，class_weight 為最簡便的實務選擇。排除 Y−2 已確診的窗口使 AUC 變動 ≤1.3% 且無一致方向，證實保留全部窗口不致偏誤。

**Table 8. Imbalance handling, LR (sensitivity). 表 8　不平衡處理，LR（敏感度）**

| Disease 疾病 | Baseline 無處理 | class-weight | SMOTE | ADASYN | Under-sample 欠採樣 |
|---|---|---|---|---|---|
| HTN 高血壓 | 0.041 | 0.698 | 0.698 | 0.696 | 0.699 |
| HG 高血糖 | 0.335 | 0.861 | 0.852 | 0.877 | 0.864 |
| DL 高血脂 | 0.135 | 0.791 | 0.785 | 0.794 | 0.790 |

### 3.6 Longitudinal accumulation and per-time-point power

> ### 3.6 縱向累積與各時間點預測力

Increasing historical checkups (same 2,526 participants) raised hyperglycemia/dyslipidemia only slightly (~1.4–1.5%), but hypertension jumped from ~0.67 (one checkup) to 0.835 (four)—concentrated at the earliest checkup. Per-time-point analysis confirmed this: for hyperglycemia/dyslipidemia the most recent visit was most predictive (declining with distance), but for hypertension the *earliest* visit (T1) reached AUC 0.786, far above T2–T4 (0.627–0.666). We hypothesize this reflects enrollment screening (excluding baseline hypertensives leaves T1 as a drug-naïve baseline) plus later antihypertensive treatment suppressing measured pressure without removing risk; blood-pressure drugs act fast and are frequently titrated, whereas lipid/glucose drugs perturb measurements more gradually. The dataset lacks medication records, so this remains a hypothesis.

> 增加歷史健檢次數（同一批 2,526 人）僅使高血糖/高血脂略升（~1.4–1.5%），但高血壓由 ~0.67（一次）跳升至 0.835（四次）——增幅集中於最早一次。各時間點分析印證此點：高血糖/高血脂以最近一次最具預測力（隨距離遞減），但高血壓以*最早*一次（T1）達 AUC 0.786，遠高於 T2–T4（0.627–0.666）。我們推測此反映入組篩選（排除基線高血壓者使 T1 為未用藥基線）加上後續降壓治療壓低量測值卻未消除風險；降壓藥見效快且常調整劑量，而降血脂/降血糖藥對量測值的干擾較緩。資料集缺乏用藥紀錄，故此為待驗證假說。

### 3.7 Multi-task vs single-task learning

> ### 3.7 多任務 vs 單任務學習

A multi-task MLP (shared 64→32 trunk, three heads) matched three single-task MLPs within ≤0.8% AUC, using 3,907 vs 11,523 parameters (66% fewer) and training ~1.4× faster (11.0 vs 15.9 s/fold). Weak label correlation (Phi <0.1) and unequal task difficulty likely dilute shared representations. Given comparable accuracy and simpler design, single-task models were used for the main experiments.

> 多任務 MLP（共享 64→32 主幹、三個輸出頭）與三個單任務 MLP 的 AUC 差距 ≤0.8%，參數量 3,907 vs 11,523（少 66%），訓練快約 1.4 倍（每折 11.0 vs 15.9 秒）。標籤相關性弱（Phi <0.1）與任務難度不均可能稀釋共享表徵。鑑於準確度相當且架構更簡單，主要實驗採單任務模型。

### 3.8 Symbolic regression

> ### 3.8 符號回歸

PySR discovered compact formulas, each depending on a single feature coinciding with the top SHAP feature (Table 9). The hyperglycemia formula, 0.114 × FBG_(Y−1), reached AUC 0.943—slightly above XGBoost—and was the most stable (all five folds converged; 5-fold AUC 0.918 ± 0.016). The hypertension and dyslipidemia formulas used exponential terms but were unstable, degenerating to constant solutions in 3 of 5 folds. We position symbolic regression as exploratory: clinically intuitive and, for hyperglycemia, robustly reproducible, but not yet a stand-alone tool for the other two.

> PySR 發現了極簡公式，各自僅依賴一個與最高 SHAP 特徵一致的特徵（表 9）。高血糖公式 0.114 × FBG_(Y−1) 達 AUC 0.943——略高於 XGBoost——且最穩定（五折皆收斂；5 折 AUC 0.918 ± 0.016）。高血壓與高血脂公式使用指數項但不穩定，五折中有三折退化為常數解。我們將符號回歸定位為探索性：臨床直覺強、對高血糖可穩定重現，但尚不適合作為其餘兩項疾病的獨立工具。

**Table 9. Best symbolic-regression formulas. 表 9　最佳符號回歸公式**

| Disease 疾病 | Formula 公式 | AUC | 5-fold stability 五折穩定性 |
|---|---|---|---|
| HTN 高血壓 | 0.130 × exp(SBP_(Y−2)) | 0.745 | 2/5 valid; 0.580 ± 0.110 |
| HG 高血糖 | 0.114 × FBG_(Y−1) | 0.943 | 5/5; 0.918 ± 0.016 |
| DL 高血脂 | 0.043 × exp(TC_(Y−2)) | 0.801 | 2/5 valid; 0.640 ± 0.192 |

---

## 4. Discussion

> ## 4. 討論

### 4.1 Principal findings

> ### 4.1 主要發現

Across ten classifiers and three conditions, logistic regression was the most consistent and best-generalizing model, matching or exceeding more complex methods on AUC while retaining a balanced sensitivity/specificity profile and negligible overfitting. This echoes the long-standing prominence of logistic regression in disease-prediction reviews [18] and carries a practical message: on structured checkup data, simple linear models already capture the core signal, and added complexity mainly increases overfitting risk. Tree ensembles can equal LR on test AUC (e.g., RF for hypertension) but memorize training data, making generalization less predictable.

> 在十種分類器與三項疾病中，邏輯迴歸最穩定、泛化最佳，AUC 與更複雜方法相當或更優，同時維持敏感度/特異度平衡且幾乎無過擬合。此呼應邏輯迴歸在疾病預測回顧中長期居主流 [18]，並帶來實務訊息：在結構化健檢資料上，簡單線性模型已能掌握核心信號，增加複雜度主要徒增過擬合風險。樹集成在測試 AUC 上可與 LR 相當（如高血壓的 RF），但會記憶訓練資料，使泛化較不可預測。

### 4.2 The dual role of delta features

> ### 4.2 Δ 特徵的雙重角色

Our ablation clarifies a frequently conflated point. Deltas are *predictively redundant* when both raw time points are available, yet carry *interpretive value*: appearing in 30–50% of top-10 SHAP features, they let clinicians read "trend" directly rather than inferring it from two coefficients. This reconciles our results with Kanegae et al. [9], whose XGBoost top-20 contained no deltas despite their inclusion. When only one visit is available, deltas do add 1.5–2.3% AUC, reinforcing the value of repeated checkups.

> 本消融釐清一個常被混淆的點。當兩個原始時間點皆存在時，Δ 在預測上*冗餘*，但具*解釋價值*：佔前十 SHAP 特徵的 30–50%，讓臨床人員可直接讀取「趨勢」，而非從兩個係數推導。此可調和本研究與 Kanegae 等人 [9] 的結果——其 XGBoost 前二十名雖納入 Δ 卻無一上榜。當僅有一次健檢時，Δ 確可增加 1.5–2.3% AUC，強化重複健檢的價值。

### 4.3 Toward low-cost, interpretable screening

> ### 4.3 邁向低成本、可解釋的篩檢

Two findings support frugal deployment. First, two features preserve AUC within ~0.8% of the 26-feature model, so a primary-care system need not collect an expensive panel. Second, symbolic regression yields transparent formulas; for hyperglycemia, a one-variable rule reaches AUC 0.943 and is fold-stable. Such rules are trivially computable at the point of care—while the instability of the other two formulas marks a clear boundary on this approach.

> 兩項發現支持精簡部署。其一，雙特徵即可保留 AUC 在 26 特徵模型的 ~0.8% 內，基層系統無需收集昂貴檢驗組。其二，符號回歸產出透明公式；高血糖的單變數規則達 AUC 0.943 且跨折穩定，於照護現場即可輕易計算——而其餘兩項公式的不穩定性則標示出此法的明確界線。

### 4.4 Robustness

> ### 4.4 穩健性

The conclusions are stable across analytic choices: imbalance methods differ by <0.2% in AUC; excluding baseline-diagnosed windows shifts AUC by ≤1.3%; multi-task matches single-task within ≤0.8%. These establish that the headline results are not artifacts of a particular preprocessing or modeling decision.

> 結論在各種分析選擇下皆穩定：不平衡方法的 AUC 差異 <0.2%；排除基線已確診窗口使 AUC 變動 ≤1.3%；多任務與單任務差距 ≤0.8%。這些確立主要結果並非特定前處理或建模決策的產物。

### 4.5 Limitations

> ### 4.5 研究限制

(1) *Selection bias*: voluntary checkup attendees may be healthier than the general population, limiting generalizability. (2) *No external validation*: lacking a comparable dataset, we relied on internal CV; a Synthea attempt [37] failed on data quality (99.4% hyperglycemia positivity; 72% missing TC), and the only feasible hypertension test dropped (AUC 0.718→0.625) due to cohort differences—a temporal-split validation is planned. (3) *Label/medication ambiguity*: labels behave as per-visit snapshots (≈24.8% of positives later reverted), and missing medication records mean the model predicts threshold breach rather than persistent disease—also underlying the unverified blood-pressure hypothesis. (4) *No lifestyle data*: diet, exercise, smoking [36] were unavailable. (5) *Limited time points*: with three visits, deep sequence models (LSTM, GRU, Transformer) were not explored.

> (1) *選擇偏差*：自願受檢者可能較一般人口健康，限制外推性。(2) *無外部驗證*：缺乏可比資料集，僅以內部交叉驗證；Synthea 嘗試 [37] 因資料品質失敗（高血糖陽性率 99.4%；TC 缺失 72%），唯一可行的高血壓測試因世代差異而下降（AUC 0.718→0.625）——已規劃時間切分驗證。(3) *標記/用藥不明確*：標記呈現為單次健檢快照（約 24.8% 陽性者後續翻轉），且缺乏用藥紀錄，模型預測的是「是否超過閾值」而非持續性疾病——亦是前述血壓假說的根源。(4) *無生活型態資料*：飲食、運動、吸菸 [36] 不可得。(5) *時間點有限*：僅三次，未探索深度時序模型（LSTM、GRU、Transformer）。

### 4.6 Future work

> ### 4.6 未來工作

Priorities are a temporal-split (and eventually external) validation, calibration assessment, incorporation of medication and lifestyle features, deep temporal models if longer series become available, and extension of the framework to other chronic diseases.

> 優先方向為時間切分（最終外部）驗證、校準評估、納入用藥與生活型態特徵、若取得更長序列則採深度時序模型，以及將框架推廣至其他慢性病。

---

## 5. Conclusions

> ## 5. 結論

Using a public longitudinal checkup cohort, we showed that simple feature engineering and a linear model predict the three highs with clinically useful, well-generalizing, and interpretable performance (LR AUC 0.721/0.938/0.867). Delta features are predictively redundant when raw time points are present but interpretively valuable; two features—or, for hyperglycemia, a single-variable formula (AUC 0.943)—suffice for near-complete accuracy; and the results are robust to imbalance handling, data filtering, and multi-task versus single-task design. These findings support deploying low-cost, interpretable early-warning screening in primary care, and provide comprehensive model-selection evidence for longitudinal three-highs prediction.

> 以公開縱向健檢世代，我們證明簡單特徵工程與線性模型即可對三高達到臨床可用、泛化良好且可解釋的預測（LR AUC 0.721/0.938/0.867）。Δ 特徵在原始時間點存在時於預測上冗餘，但具解釋價值；雙特徵——或對高血糖而言，單變數公式（AUC 0.943）——即足以達到近乎完整的準確度；且結果對不平衡處理、資料篩選、多任務 vs 單任務設計皆穩健。這些發現支持在基層醫療部署低成本、可解釋的早期預警篩檢，並為縱向三高預測提供完整的模型選擇依據。

---

<!-- References 同 manuscript_v1.md（[1]–[37]），對照稿不重複，以節省篇幅。投稿時以英文正式版為準。 -->

**References / 參考文獻：** 見英文正式版 [manuscript_v1.md](manuscript_v1.md)（[1]–[37]，IEEE/Vancouver 編號）。
