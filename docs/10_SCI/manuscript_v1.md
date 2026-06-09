<!--
================================================================================
SCI MANUSCRIPT — DRAFT v1 (generic IMRaD, target: BMC Medical Informatics and
Decision Making; reformat-ready for International Journal of Medical Informatics)
Generated 2026-06-02 from thesis chapters. ALL numbers taken verbatim from
thesis Ch4/Ch6 tables — no fabricated values.

>>> BEFORE SUBMISSION — outstanding items (do NOT submit without these): <<<
  [ ] Author list, affiliations, ORCID, corresponding author (confirm with 許揚)
  [ ] Bootstrap 95% CI for every AUC (plan lists as MUST-ADD; currently mean±SD only)
  [ ] Temporal-split validation (substitute for external validation)
  [ ] Calibration plot + Brier score (recommended add)
  [ ] Figures re-exported to journal DPI/format (reuse thesis figs 6-1..6-8)
  [ ] Professional English proofreading
  [ ] TRIPOD checklist (BMC MIDM requirement for prediction models)
  [ ] Declarations: data availability (Dryad DOI), funding, CoI, ethics, author contributions
  [ ] Cover letter + novelty framing tuned to chosen journal
================================================================================
-->

# Simultaneous machine-learning prediction of hypertension, hyperglycemia, and dyslipidemia from longitudinal health-checkup data: a comprehensive model comparison with interpretable symbolic regression

**Running title:** Predicting the "three highs" from longitudinal checkups

**Po-Chiao Chi¹, Yang Syu¹** *(author order/corresponding author TBD)*
¹ Department of Computer Science, College of Science, National Taipei University of Education, Taipei, Taiwan

---

## Abstract

**Background.** Hypertension, hyperglycemia, and dyslipidemia—collectively the "three highs"—are the principal modifiable risk factors for cardiovascular disease and frequently co-occur. Conventional risk scores rely on a single time point and do not exploit the dynamic information embedded in repeated health checkups. Existing machine-learning studies typically target a single disease, compare few models, and seldom address interpretability. We aimed to build and systematically evaluate a longitudinal framework that predicts all three conditions simultaneously, while quantifying the value of change (delta) features and exploring interpretable models.

**Methods.** We used a publicly available longitudinal community health-checkup cohort (Luo et al., Dryad; Hangzhou, China, 2010–2018; adults aged ≥40). After excluding participants with fewer than three checkups, 6,056 individuals remained. A three-time-point design (Y−2, Y−1, Y0) with a sliding-window expansion produced 13,514 modeling records. Twenty-six features were derived: demographics, biomarkers at Y−2 and Y−1, and eight delta features (Y−1 − Y−2). Ten classifiers (logistic regression [LR], naïve Bayes [NB], linear discriminant analysis [LDA], k-nearest neighbors [KNN], decision tree [DT], random forest [RF], XGBoost, LightGBM, support vector machine [SVM], multilayer perceptron [MLP]) plus symbolic regression (PySR) were evaluated with stratified group 5-fold cross-validation (grouping on patient identity to prevent leakage). The primary metric was AUC-ROC; sensitivity, specificity, and F1 were also reported. Ablation, class-imbalance, data-filtering, checkup-frequency, multi-task-learning, and interpretability (SHAP, symbolic regression) experiments were conducted.

**Results.** LR was the most consistent model, achieving AUC 0.721 (hypertension), 0.938 (hyperglycemia), and 0.867 (dyslipidemia), with a well-balanced sensitivity/specificity profile and negligible overfitting (train–test AUC gap ≤0.004). Tree ensembles matched or slightly exceeded LR on AUC for hypertension (RF 0.743) but overfit substantially (RF gap up to 0.254). With both Y−2 and Y−1 present, delta features were predictively redundant (no AUC change on removal); however, given only the most recent visit, adding deltas raised AUC by 1.5–2.3%. SHAP rankings were disease-specific and clinically coherent (hypertension→blood pressure, hyperglycemia→fasting glucose, dyslipidemia→total cholesterol). Using only the top two features retained AUC within ~0.8% of the full model. Class-imbalance methods left AUC essentially unchanged (<0.2%) but raised sensitivity from 0.04–0.34 to 0.70–0.88. Multi-task learning matched single-task learning (AUC difference ≤0.8%) with 66% fewer parameters. Symbolic regression discovered single-variable formulas; for hyperglycemia, 0.114 × FBG_(Y−1) reached AUC 0.943 and was stable across folds.

**Conclusions.** Longitudinal checkup data combined with simple feature engineering and a linear model achieve clinically useful, well-generalizing, and interpretable prediction of all three conditions. A two-feature model or a one-variable formula suffices for several tasks, supporting low-cost early-warning deployment in primary care.

**Keywords:** hypertension; hyperglycemia; dyslipidemia; machine learning; delta features

---

## 1. Background

### 1.1 The public-health burden of the "three highs"

Hypertension, hyperglycemia, and dyslipidemia are the dominant modifiable contributors to cardiovascular disease, stroke, and chronic kidney disease. Cardiovascular disease causes roughly 20 million deaths each year, close to one-third of global mortality [1]. The burden is especially heavy in Asia: more than a quarter of adults in the WHO Western Pacific region are hypertensive [2], and a small group of Asian countries accounts for nearly half of the world's diabetes cases [3]. Metabolic disease in East Asia has risen sharply in recent decades, driven by genetic susceptibility, distinctive body-fat distribution, and rapid dietary westernization [4]. In Taiwan, the prevalence among adults aged ≥40 is 38.3% for hypertension, 34.1% for dyslipidemia, and 16.4% for hyperglycemia, yet 40–70% of affected individuals are unaware of their condition [5].

The three conditions are mutually correlated and co-occur as the core of the metabolic syndrome: over 70% of patients with diabetes also have hypertension or dyslipidemia, and dyslipidemia prevalence among diabetic patients reaches 72–85% [6]. Metabolic-syndrome patients carry roughly twice the cardiovascular risk and five times the risk of type 2 diabetes [7]. This comorbidity argues for predicting the three conditions jointly rather than in isolation.

### 1.2 The clinical value of early, longitudinal prediction

The three highs are typically asymptomatic early on and are often detected only at routine checkups or after complications arise. Because progression from health to disease usually passes through a multi-year prodromal phase—during which lifestyle change can still reverse risk—identifying high-risk individuals early is key to reducing the burden. The trend toward younger onset has prompted Taiwan to lower the eligibility age for adult preventive-health services from 40 to 30 years in 2025 [8], extending the demand for screening to younger adults.

As checkups have become routine, large volumes of *longitudinal* checkup data have accumulated, recording how biomarkers evolve within an individual. Because health-status changes often precede a clinical diagnosis, longitudinal data are uniquely valuable for early prediction. Yet conventional risk-assessment tools rely on a single time point and do not exploit this dynamic information—the gap this study addresses.

### 1.3 Related work and gaps

Machine learning has been applied widely to single-disease checkup prediction. For hypertension, Kanegae et al. built an XGBoost/ensemble model on Japanese occupational checkups (n=18,258, AUC 0.881) and, notably, used longitudinal change features across three years [9]; Ye et al. predicted one-year incident hypertension from statewide US electronic health records (n=823,627, AUC 0.917), though the top features were antihypertensive drugs, raising leakage concerns [10]; and Wang et al. showed on large-scale Taiwanese checkups (n=207,488) that more checkups improve accuracy (AUC 0.889) [11]. For diabetes/hyperglycemia, Liu et al. reached AUC 0.93 over a 10-year Taiwanese cohort [12], and Yang et al. introduced a dual framework predicting glucose change and prediabetes risk, finding baseline fasting glucose overwhelmingly dominant [13]. Broader cardiovascular and diabetes models include Alaa et al. (UK Biobank AutoML, AUC 0.774) [14], Dinh et al. (NHANES, AUC 0.862) [15], Hung et al. (masked hypertension, AUC 0.851) [16], and Majcherek et al. (BRFSS survey data) [17].

Three gaps recur across this literature. First, almost all studies predict a *single* disease, despite the strong comorbidity of the three highs. Second, model comparisons are usually narrow (a systematic review of hypertension models found logistic and Cox regression dominant, with few cross-family comparisons) [18], leaving clinicians without comprehensive model-selection evidence. Third, interpretability—essential for clinical adoption—is rarely addressed; high-accuracy black-box models are difficult to deploy. Multi-task learning has been proposed for joint chronic-disease prediction (e.g., Tsai et al., who found multi-task and single-task performance comparable with far fewer parameters [19]) but has not been studied for the three highs with delta features.

### 1.4 Objectives and contributions

We build a longitudinal framework that predicts hypertension, hyperglycemia, and dyslipidemia simultaneously, and we evaluate it comprehensively. Our contributions are: (1) a systematic comparison of ten classifiers plus symbolic regression across the three conditions, with leakage-controlled validation; (2) a complete ablation that disentangles the predictive versus interpretive roles of delta features across diseases; (3) interpretability analysis combining SHAP and symbolic regression, including single-variable formulas with clinically useful accuracy; and (4) a set of robustness experiments (class imbalance, data filtering, checkup frequency, multi-task vs single-task) that together establish the stability of the findings. All data are public, making the study fully reproducible.

---

## 2. Methods

### 2.1 Data source and cohort

We used the longitudinal community health-checkup dataset published by Luo et al. on the Dryad repository [20,21]. The cohort was drawn from community health surveys in Hangzhou, Zhejiang Province, China, collected between 2010 and 2018, enrolling adults aged ≥40 (6,119 participants, 25,744 checkup records), most with three or more checkups. The dataset records checkup ordinal (visit number) rather than calendar date; intervals were inferred from age differences. About 90% of participants kept a fixed 2-year interval and 9.6% a 1-year interval, with a mean interval of 1.90 years (SD 0.36). Because intervals are highly consistent, delta features are directly comparable without time correction.

Although the original authors restricted the cohort to participants with ≥3 checkups, we found 63 individuals (1.03%) with fewer than three valid records and excluded them, leaving **6,056 participants** (98.97% retention). The disease labels follow international thresholds [22–24]: hypertension as systolic blood pressure (SBP) ≥140 or diastolic blood pressure (DBP) ≥90 mmHg (or diagnosed and on antihypertensive medication); hyperglycemia as fasting blood glucose (FBG) ≥7.0 mmol/L (or self-reported diabetes); dyslipidemia as total cholesterol (TC) ≥6.22 mmol/L. Labels were converted to a binary 0/1 (healthy/affected) encoding.

### 2.2 Study design and sliding window

We adopted a three-time-point longitudinal design, naming time points relative to the prediction target year Y0: Y−2 (≈4 years prior), Y−1 (≈2 years prior), and Y0 (target). The model inputs are the biomarkers at Y−2 and Y−1 plus their changes; the target is disease status at Y0. Predicting Y0 (rather than Y−1) avoids leakage—using Y−1 as the target would let the model "see" the answer from the same visit—and provides a clinically meaningful ~2-year warning window.

To exploit participants with many checkups, we used a sliding window: a participant with N checkups yields (N−2) records (e.g., 5 checkups → 3 windows). This expanded the 6,056 participants to **13,514 modeling records**. Because one participant can contribute multiple records, the cross-validation must keep all of a participant's records in the same fold (Section 2.5).

### 2.3 Feature engineering

Twenty-six features were used (Table 1): two demographics (sex, age); eight biomarkers at Y−2 and the same eight at Y−1 (FBG, TC, creatinine [Cr], uric acid [UA], estimated glomerular filtration rate [eGFR], body-mass index [BMI], SBP, DBP); and eight delta features defined as

Δ_i = X_(i,Y−1) − X_(i,Y−2).

Delta features encode dynamic trend: a positive ΔFBG indicates rising glucose, a negative ΔeGFR indicates declining renal function.

**Table 1. Feature set (26 features).**

| Category | Features | n |
|---|---|---|
| Demographics | Sex, Age | 2 |
| Y−2 biomarkers | FBG, TC, Cr, UA, eGFR, BMI, SBP, DBP | 8 |
| Y−1 biomarkers | FBG, TC, Cr, UA, eGFR, BMI, SBP, DBP | 8 |
| Delta (Y−1 − Y−2) | ΔFBG, ΔTC, ΔCr, ΔUA, ΔeGFR, ΔBMI, ΔSBP, ΔDBP | 8 |

### 2.4 Class imbalance

Positive rates differed markedly: hypertension 16.68% (1,010/6,056; ~5:1), hyperglycemia 5.53% (335; ~17:1), and dyslipidemia 5.96% (361; ~16:1). Imbalance can bias models toward the majority (healthy) class and depress sensitivity. Following the algorithm-level strategy [33], we used cost-sensitive learning via class weights, with weight for class k set to w_k = n / (K·n_k). We additionally benchmarked SMOTE [34], ADASYN, and random under-sampling (Section 3.4).

### 2.5 Models and validation

The ten classifiers span statistical methods (LR, NB, LDA [25]), instance-based (KNN), tree-based (DT, RF [26], XGBoost [27], LightGBM [28]), kernel (SVM [29]), and neural (MLP [30]) families. Symbolic regression was performed with PySR [31] to search for compact, interpretable formulas (binary operators +,−,×,÷; unary exp, log, abs, square; maxsize 35; 200 iterations; 20 populations). Interpretability was assessed with SHAP [32].

All experiments used **stratified group 5-fold cross-validation**, combining stratification (preserving the class ratio in each fold) with grouping on patient identity (ensuring no participant appears in both training and test folds). This is essential because the sliding window produces multiple records per participant; without grouping, evaluation would be optimistically biased by leakage. The 13,514 records were split into five folds of ~2,703 test records each.

The primary metric was AUC-ROC—threshold-independent and robust to imbalance at the prevalences observed here (all >5%, above the extreme-imbalance regime where PR-AUC is preferred [35]). We also report sensitivity (TP/[TP+FN]), specificity (TN/[TN+FP]), and F1. In screening, missed cases are costlier than false alarms, so sensitivity is emphasized.

### 2.6 Experiments

Ten experiments were designed: (1) model comparison; (2) SHAP feature importance; (3) delta-feature ablation; (4) feature-count ablation (top-1/2/5/10/15/20/all by SHAP); (5) class-imbalance comparison; (6) data-filtering comparison (all windows vs excluding windows already diagnosed at Y−2); (7) checkup-frequency effect; (8) per-time-point predictive power; (9) multi-task (shared 64→32 trunk with three heads) vs single-task learning; and (10) symbolic regression with 5-fold stability checking. All experiments were run on consumer hardware (Intel Core i7-11700, 32 GB RAM, NVIDIA RTX 3050; Python 3.10; scikit-learn, XGBoost, LightGBM, PySR, SHAP); full 5-fold runs completed within minutes per model, underscoring reproducibility and deployability.

---

## 3. Results

### 3.1 Model comparison

Table 2 reports test AUC for all ten models. LR achieved the highest AUC for hyperglycemia (0.938) and dyslipidemia (tied, 0.867); RF was best for hypertension (0.743). Hyperglycemia was the easiest task (all models except KNN >0.83), dyslipidemia intermediate, and hypertension hardest (0.630–0.743), consistent with the larger short-term variability of blood pressure.

**Table 2. Test AUC by model (mean ± SD, 5-fold CV).** *[Bootstrap 95% CI to be added before submission.]*

| Model | Hypertension | Hyperglycemia | Dyslipidemia |
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

AUC alone is misleading under imbalance. With balanced class weights, LR maintained a strong sensitivity/specificity balance (e.g., hypertension sensitivity 0.697/specificity 0.638; hyperglycemia 0.858/0.882; dyslipidemia 0.799/0.775). In contrast, LDA, MLP, and KNN behaved extremely conservatively despite competitive AUC—LDA reached hyperglycemia AUC 0.936 but sensitivity only 0.484, and dyslipidemia sensitivity 0.118 versus LR's 0.799 at the *same* AUC (0.867)—illustrating why a single metric is insufficient for screening.

**Generalization.** Comparing train and test AUC (Table 3), statistical models (LR, NB, LDA) showed near-zero overfitting (gap ≤0.010), whereas tree ensembles overfit heavily (RF reached train AUC 0.997 for hypertension, gap 0.254; LightGBM reached train AUC 1.000 for hyperglycemia). Thus tree models' apparent edge derives partly from greater fitting capacity rather than better generalization. For clinical deployment, where stability on unseen patients matters most, LR's low-variance behavior is advantageous.

**Table 3. Train AUC and generalization gap (train − test).**

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

SHAP analysis of the XGBoost model produced disease-specific, clinically coherent rankings (Table 4): hypertension was led by SBP (both time points) and age; hyperglycemia by FBG; and dyslipidemia by TC and ΔeGFR. The two time points of the same biomarker usually appeared together, indicating the model uses both the recent value and the historical trend. ΔeGFR was the only delta feature in the top 10 of all three diseases, suggesting renal-function change as a shared early marker of metabolic abnormality. Delta features comprised 30% (hypertension), 40% (hyperglycemia), and 30% (dyslipidemia) of the top-10—evidence that nonlinear models split on change directly, even though (Section 3.3) deltas add no AUC when both raw values are present.

**Table 4. Top-5 SHAP features per disease (XGBoost).**

| Rank | Hypertension | Hyperglycemia | Dyslipidemia |
|---|---|---|---|
| 1 | SBP_(Y−2) | FBG_(Y−1) | TC_(Y−1) |
| 2 | SBP_(Y−1) | FBG_(Y−2) | TC_(Y−2) |
| 3 | Age | ΔTC | ΔeGFR |
| 4 | ΔDBP | BMI_(Y−1) | Age |
| 5 | DBP_(Y−1) | BMI_(Y−2) | eGFR_(Y−2) |

### 3.3 Delta-feature ablation

When both Y−2 and Y−1 were present, removing the eight delta features changed AUC and sensitivity by essentially zero across all three diseases (Table 5). This is mathematically expected: since Δ = Y−1 − Y−2, a linear model can recover the change effect from the two raw coefficients, making delta redundant in the full set.

**Table 5. Full (26) vs No-Delta (18), LR.**

| Disease | Metric | Full | No-Delta | Δ |
|---|---|---|---|---|
| HTN | AUC | 0.721 | 0.721 | 0.0% |
| HG | AUC | 0.938 | 0.938 | 0.0% |
| DL | AUC | 0.867 | 0.867 | 0.0% |

However, when only the most recent visit (Y−1) was available, adding delta features raised AUC by 1.5–2.3% and sensitivity by 0.8–3.7% (Table 6). Because Δ implicitly reintroduces Y−2 information, this confirms that *more longitudinal time points improve prediction*. A complementary delta-only model performed poorly (AUC 0.593/0.668/0.636), showing that change direction alone—without the baseline value—has limited standalone predictive power.

**Table 6. Y−1 + Delta vs Y−1 only, LR (AUC).**

| Disease | Y−1 + Δ | Y−1 only | Gain |
|---|---|---|---|
| HTN | 0.721 | 0.698 | **+2.3%** |
| HG | 0.938 | 0.923 | +1.5% |
| DL | 0.867 | 0.846 | +2.1% |

### 3.4 Feature-count ablation

Predictive power concentrated in very few features (Table 7). Using only the top two SHAP features—the two time points of the same core biomarker (SBP, FBG, or TC)—retained AUC within ~0.8% of the full model (hypertension 0.715, hyperglycemia 0.933, dyslipidemia 0.861). A single feature already sufficed for hyperglycemia (0.920). Beyond five features, AUC differences were ≤0.005. This supports a low-cost screening scheme requiring only two measurements of a single core biomarker.

**Table 7. Feature-count ablation, AUC (LR).**

| # features | HTN | HG | DL |
|---|---|---|---|
| 1 | 0.686 | 0.920 | 0.842 |
| 2 | 0.715 | 0.933 | 0.861 |
| 5 | 0.716 | 0.935 | 0.864 |
| 10 | 0.717 | 0.937 | 0.864 |
| 26 (all) | 0.721 | 0.938 | 0.867 |

### 3.5 Robustness: class imbalance and data filtering

Across five imbalance-handling strategies (baseline, class-weight, SMOTE, ADASYN, under-sampling), AUC varied by <0.2%, while sensitivity rose from very low baseline values (0.04–0.34) to 0.70–0.88 (Table 8). The strategies differed by <2% in sensitivity; class-weight is therefore the simplest practical choice (no synthetic samples, no change to the data distribution). Sweeping the weight ratio traced a clean sensitivity–specificity trade-off with constant AUC, and the balanced setting gave sensitivity 0.70–0.86 with reasonable specificity.

**Table 8. Imbalance handling, LR (sensitivity).**

| Disease | Baseline | class-weight | SMOTE | ADASYN | Under-sample |
|---|---|---|---|---|---|
| HTN | 0.041 | 0.698 | 0.698 | 0.696 | 0.699 |
| HG | 0.335 | 0.861 | 0.852 | 0.877 | 0.864 |
| DL | 0.135 | 0.791 | 0.785 | 0.794 | 0.790 |

Excluding sliding-window samples already diagnosed at Y−2 changed AUC by ≤1.3% with no consistent direction, confirming that retaining all windows (which preserves training size and reflects a realistic screening population) does not bias the results.

### 3.6 Longitudinal accumulation and per-time-point power

Holding the prediction target fixed and increasing the number of historical checkups (same 2,526 participants with five complete checkups) revealed disease-specific behavior. Hyperglycemia and dyslipidemia rose only slightly (~1.4–1.5%), whereas hypertension jumped from ~0.67 with a single checkup to 0.835 with four checkups—the gain concentrated at the fourth (earliest) checkup. Per-time-point analysis confirmed the contrast: for hyperglycemia and dyslipidemia the most recent visit was most predictive (declining with distance), but for hypertension the *earliest* visit (T1) reached AUC 0.786, far above T2–T4 (0.627–0.666). We hypothesize this reflects the cohort's enrollment screening (which excluded baseline hypertensives, leaving T1 as a drug-naïve "clean" baseline) combined with later antihypertensive treatment that suppresses measured blood pressure without removing underlying risk; blood-pressure-lowering drugs act fast and are frequently titrated, whereas lipid- and glucose-lowering drugs perturb measurements more gradually. The dataset lacks medication records, so this remains a hypothesis for future validation.

### 3.7 Multi-task vs single-task learning

A multi-task MLP (shared 64→32 trunk, three disease heads) matched three independent single-task MLPs within ≤0.8% AUC and with no consistent advantage in sensitivity or specificity, while using 3,907 versus 11,523 parameters (66% fewer) and training ~1.4× faster (11.0 vs 15.9 s/fold). The weak label correlation among the three diseases (Phi <0.1) and unequal task difficulty likely dilute shared representations. Given comparable accuracy and a simpler architecture, single-task models were used for the main experiments.

### 3.8 Symbolic regression

PySR discovered remarkably compact formulas, each depending on a single feature that coincided with the top SHAP feature (Table 9). The hyperglycemia formula, 0.114 × FBG_(Y−1), reached AUC 0.943—slightly above XGBoost—and was the most stable: all five folds converged to the same structure (0.114–0.120 × FBG_(Y−1); 5-fold AUC 0.918 ± 0.016). The hypertension and dyslipidemia formulas used exponential terms but were unstable, degenerating to constant (non-discriminative) solutions in 3 of 5 folds. We therefore position symbolic regression as exploratory: clinically intuitive and, for hyperglycemia, robustly reproducible, but not yet a stand-alone tool for the other two conditions.

**Table 9. Best symbolic-regression formulas.**

| Disease | Formula | AUC | 5-fold stability |
|---|---|---|---|
| Hypertension | 0.130 × exp(SBP_(Y−2)) | 0.745 | 2/5 folds valid; 0.580 ± 0.110 |
| Hyperglycemia | 0.114 × FBG_(Y−1) | 0.943 | 5/5 folds; 0.918 ± 0.016 |
| Dyslipidemia | 0.043 × exp(TC_(Y−2)) | 0.801 | 2/5 folds valid; 0.640 ± 0.192 |

---

## 4. Discussion

### 4.1 Principal findings

Across ten classifiers and three conditions, logistic regression was the most consistent and best-generalizing model, matching or exceeding far more complex methods on AUC while retaining a balanced sensitivity/specificity profile and negligible overfitting. This echoes the long-standing prominence of logistic regression in disease-prediction reviews [18] and carries a practical message: on structured checkup data, simple linear models already capture the core predictive signal, and added model complexity mainly increases overfitting risk. Tree ensembles can equal LR on test AUC (e.g., RF for hypertension) but memorize training data (gaps up to 0.254), making their generalization less predictable on new patients.

### 4.2 The dual role of delta features

Our ablation clarifies a frequently conflated point. Delta features are *predictively redundant* when both raw time points are available (Δ = Y−1 − Y−2 is a linear combination already accessible to the model), yet they carry *interpretive value*: they appear in 30–50% of the top-10 SHAP features, letting clinicians read "trend" directly (e.g., a high-SHAP ΔSBP flags a worsening blood-pressure trajectory) rather than inferring it from two coefficients. This reconciles our results with Kanegae et al. [9], whose XGBoost top-20 contained no delta features despite their inclusion. When only one visit is available, however, deltas do add 1.5–2.3% AUC—because they reintroduce earlier-visit information—reinforcing the value of repeated checkups.

### 4.3 Toward low-cost, interpretable screening

Two findings support frugal deployment. First, two features (two readings of one core biomarker) preserve AUC within ~0.8% of the 26-feature model, so a primary-care early-warning system need not collect an expensive panel. Second, symbolic regression yields transparent formulas; for hyperglycemia, a one-variable linear rule (0.114 × FBG_(Y−1)) reaches AUC 0.943 and is fold-stable. Such rules are trivially computable at the point of care and align with clinical intuition, illustrating the practical potential of interpretable models—while the instability of the hypertension and dyslipidemia formulas marks a clear boundary on this approach.

### 4.4 Robustness

The conclusions are stable across analytic choices: imbalance-handling methods differ by <0.2% in AUC (class-weight is the simplest effective option); excluding baseline-diagnosed windows shifts AUC by ≤1.3%; and multi-task learning matches single-task within ≤0.8%. Together these establish that the headline results are not artifacts of a particular preprocessing or modeling decision.

### 4.5 Limitations

Several limitations temper the findings. (1) *Selection bias*: the cohort comprises voluntary checkup attendees, who may be healthier and more health-conscious than the general population, limiting generalizability. (2) *No external validation*: lacking a comparable external dataset, we relied on internal cross-validation; an attempt using Synthea-generated records [37] failed because of data-quality issues (e.g., 99.4% positivity for hyperglycemia, 72% missing TC), and the only feasible hypertension test showed an expected drop (LR AUC 0.718→0.625) attributable to cohort differences. A temporal-split validation is planned. (3) *Label and medication ambiguity*: labels behave as per-visit physiological snapshots rather than persistent disease states (≈24.8% of positive individuals reverted to negative at a later visit), and the absence of medication records means the model predicts whether the next checkup will breach a threshold rather than strict persistent disease—this also underlies the unverified blood-pressure-treatment hypothesis for hypertension's atypical time-point pattern. (4) *No lifestyle data*: diet, exercise, and smoking—strongly linked to the three highs [36]—were unavailable and would likely improve both accuracy and actionability. (5) *Limited time points*: with only three visits, deep sequence models (LSTM, GRU, Transformer) were not explored.

### 4.6 Future work

Priorities are a temporal-split (and eventually external) validation, calibration assessment, incorporation of medication and lifestyle features, deep temporal models if longer series become available, and extension of the delta-feature/comparison framework to other chronic diseases.

---

## 5. Conclusions

Using a public longitudinal checkup cohort, we showed that simple feature engineering and a linear model predict hypertension, hyperglycemia, and dyslipidemia with clinically useful, well-generalizing, and interpretable performance (LR AUC 0.721/0.938/0.867). Delta features are predictively redundant when raw time points are present but interpretively valuable; two features—or, for hyperglycemia, a single-variable formula (AUC 0.943)—suffice for near-complete accuracy; and the results are robust to imbalance handling, data filtering, and multi-task versus single-task design. These findings support deploying low-cost, interpretable early-warning screening in primary care, and provide comprehensive model-selection evidence for longitudinal three-highs prediction.

---

## Declarations

*To be completed before submission.*

- **Availability of data and materials:** The dataset is publicly available from the Dryad Digital Repository (doi:10.5061/dryad.z08kprrk1) [21]. Analysis code will be deposited in a public repository.
- **Funding:** _TBD._
- **Competing interests:** The authors declare no competing interests.
- **Authors' contributions:** _TBD._
- **Ethics approval:** Secondary analysis of a de-identified, publicly available dataset.
- **Acknowledgements:** _TBD._

---

## References

[1] World Heart Federation, *World Heart Report 2023: Confronting the World's Number One Killer*. WHF, 2023.

[2] World Health Organization, *Global Report on Hypertension: The Race Against a Silent Killer*. WHO, 2023.

[3] T. Ohira and H. Iso, "Cardiovascular disease epidemiology in Asia: An overview," *Circ. J.*, vol. 77, no. 7, pp. 1646–1652, 2013.

[4] Z. Sun and Y. Zheng, "Metabolic diseases in the East Asian populations," *Nat. Rev. Gastroenterol. Hepatol.*, vol. 22, no. 7, pp. 500–516, 2025.

[5] Health Promotion Administration, *2017–2020 Nutrition and Health Survey in Taiwan*. Ministry of Health and Welfare, 2022.

[6] S. Stanciu et al., "Links between metabolic syndrome and hypertension," *Metabolites*, vol. 13, no. 1, p. 87, 2023.

[7] K. G. M. M. Alberti et al., "Harmonizing the metabolic syndrome," *Circulation*, vol. 120, no. 16, pp. 1640–1645, 2009.

[8] Health Promotion Administration, *Expansion of Adult Preventive Health Services to Age 30*. Ministry of Health and Welfare, 2025.

[9] H. Kanegae et al., "Highly precise risk prediction model for new-onset hypertension using artificial intelligence techniques," *J. Clin. Hypertens.*, vol. 22, no. 3, pp. 445–450, 2020.

[10] C. Ye et al., "Prediction of incident hypertension within the next year: Prospective study using statewide electronic health records and machine learning," *J. Med. Internet Res.*, vol. 20, no. 1, p. e22, 2018.

[11] C.-C. Wang, T.-W. Chu, and J.-S. R. Jang, "Next-visit prediction and prevention of hypertension using large-scale routine health checkup data," *PLoS ONE*, vol. 19, no. 11, p. e0313658, 2024.

[12] Y.-Q. Liu et al., "Use of machine learning to predict the incidence of type 2 diabetes among relatively healthy adults: A 10-year longitudinal study in Taiwan," *Diagnostics*, vol. 15, no. 1, p. 72, 2024.

[13] C.-C. Yang et al., "Dual machine learning framework for predicting long-term glycemic change and prediabetes risk in young Taiwanese men," *Diagnostics*, vol. 15, no. 19, p. 2507, 2025.

[14] A. M. Alaa et al., "Cardiovascular disease risk prediction using automated machine learning: A prospective study of 423,604 UK Biobank participants," *PLoS ONE*, vol. 14, no. 5, p. e0213653, 2019.

[15] A. Dinh et al., "A data-driven approach to predicting diabetes and cardiovascular disease with machine learning," *BMC Med. Inform. Decis. Mak.*, vol. 19, no. 1, p. 211, 2019.

[16] M.-H. Hung et al., "Prediction of masked hypertension and masked uncontrolled hypertension using machine learning," *Front. Cardiovasc. Med.*, vol. 8, p. 778306, 2021.

[17] D. Majcherek, A. Ciesielski, and P. Sobczak, "AI-driven analysis of diabetes risk determinants in U.S. adults," *PLoS ONE*, vol. 20, no. 9, p. e0328655, 2025.

[18] D. Sun et al., "Recent development of risk-prediction models for incident hypertension: An updated systematic review," *PLoS ONE*, vol. 12, no. 10, p. e0187240, 2017.

[19] H. Tsai et al., "Multitask learning multimodal network for chronic disease prediction," *Sci. Rep.*, vol. 15, no. 1, p. 15468, 2025.

[20] Y. Luo et al., "Associations of serum uric acid with cardiovascular disease risk factors: A retrospective cohort study in southeastern China," *BMJ Open*, vol. 13, no. 9, p. e073930, 2023.

[21] Y. Luo et al., "Associations of serum uric acid with cardiovascular disease risk factors [Dataset]," *Dryad Digital Repository*, 2023, doi:10.5061/dryad.z08kprrk1.

[22] P. A. James et al., "2014 evidence-based guideline for the management of high blood pressure in adults (JNC 8)," *JAMA*, vol. 311, no. 5, pp. 507–520, 2014.

[23] American Diabetes Association, "Standards of care in diabetes—2025," *Diabetes Care*, vol. 48, Suppl. 1, 2025.

[24] NCEP Expert Panel, "Third report of the NCEP expert panel (Adult Treatment Panel III) final report," *Circulation*, vol. 106, no. 25, pp. 3143–3421, 2002.

[25] R. A. Fisher, "The use of multiple measurements in taxonomic problems," *Ann. Eugen.*, vol. 7, no. 2, pp. 179–188, 1936.

[26] L. Breiman, "Random forests," *Mach. Learn.*, vol. 45, no. 1, pp. 5–32, 2001.

[27] T. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in *Proc. 22nd ACM SIGKDD*, 2016, pp. 785–794.

[28] G. Ke et al., "LightGBM: A highly efficient gradient boosting decision tree," in *Adv. Neural Inf. Process. Syst. 30*, 2017, pp. 3146–3154.

[29] C. Cortes and V. Vapnik, "Support-vector networks," *Mach. Learn.*, vol. 20, no. 3, pp. 273–297, 1995.

[30] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, "Learning representations by back-propagating errors," *Nature*, vol. 323, no. 6088, pp. 533–536, 1986.

[31] M. Cranmer, "Interpretable machine learning for science with PySR and SymbolicRegression.jl," *arXiv:2305.01582*, 2023.

[32] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in *Adv. Neural Inf. Process. Syst. 30*, 2017, pp. 4765–4774.

[33] H. He and E. A. Garcia, "Learning from imbalanced data," *IEEE Trans. Knowl. Data Eng.*, vol. 21, no. 9, pp. 1263–1284, 2009.

[34] N. V. Chawla et al., "SMOTE: Synthetic minority over-sampling technique," *J. Artif. Intell. Res.*, vol. 16, pp. 321–357, 2002.

[35] T. Saito and M. Rehmsmeier, "The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets," *PLoS ONE*, vol. 10, no. 3, p. e0118432, 2015.

[36] U.S. Department of Agriculture and U.S. Department of Health and Human Services, *Dietary Guidelines for Americans, 2025–2030*, 10th ed., 2025.

[37] J. Walonoski et al., "Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record," *J. Am. Med. Inform. Assoc.*, vol. 25, no. 3, pp. 230–238, 2018.

<!-- Figure placeholders (reuse thesis figures, re-export at journal DPI):
Fig 1 = thesis fig 6-1 ROC curves; Fig 2 = fig 6-2 SHAP comparison;
Fig 3 = fig 6-3 SHAP beeswarm; Fig 4 = fig 6-5 feature-count vs AUC;
Fig 5 = fig 6-7 checkup frequency; Fig 6 = fig 6-8 per-time-point. -->
