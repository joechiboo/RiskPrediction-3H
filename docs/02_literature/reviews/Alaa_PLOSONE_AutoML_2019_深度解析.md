# Alaa et al. (2019) PLoS ONE — AutoPrognosis CVD 風險預測深度解析

> **論文**：Cardiovascular disease risk prediction using automated machine learning: A prospective study of 423,604 UK Biobank participants
> **期刊**：PLoS ONE, 2019; 14(5): e0213653
> **作者**：Ahmed M. Alaa, Thomas Bolton, Emanuele Di Angelantonio, James H. F. Rudd, Mihaela van der Schaar
> **機構**：UCLA / University of Cambridge / University of Oxford / Alan Turing Institute
> **DOI**：[10.1371/journal.pone.0213653](https://doi.org/10.1371/journal.pone.0213653)
> **PDF**：[Alaa_PLOSONE_CVD_AutoML_2019.pdf](../papers/Alaa_PLOSONE_CVD_AutoML_2019.pdf)
> **與本研究關聯度**：⭐⭐⭐（Tier 2 — AutoML 多模型比較方法論，支持本研究系統性比較設計的合理性）

---

## 一句話摘要

**使用 UK Biobank 423,604 人資料與 AutoPrognosis 自動化機器學習框架（含 20 種分類器 × 7 種插補 × 9 種特徵處理 × 3 種校準 = 5,460 種 pipeline 組合），預測 5 年 CVD 風險，最佳模型 AUC 0.774 顯著優於 Framingham (0.724)，並發現「資訊增益」（更多變數）比「建模增益」（更複雜模型）更重要。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **研究主題** | 5 年心血管疾病（CVD）風險預測 |
| **研究設計** | 前瞻性世代研究（10-fold stratified CV） |
| **資料來源** | UK Biobank（英國 22 中心） |
| **招募期** | 2006–2010 |
| **追蹤截止** | 2016-02-17 |
| **中位追蹤** | 7 年（5th-95th: 5.7–8.4 年） |
| **樣本數** | 423,604 人（≥40 歲、無 CVD 病史） |
| **CVD 事件** | 6,703 例（全期）；4,801 例（5 年） |
| **事件率** | ~1.13%（5 年） |
| **變數數** | 473 個（9 大類） |
| **CVD 定義** | ICD-10: F01, I20-I25, I50, I60-I69；ICD-9: 410-414, 430-434, 436-438 |
| **評估指標** | AUC-ROC、NRI、Brier score、PPV、Sensitivity |

### 基線特徵

| 變項 | 數值 |
|------|------|
| 年齡 | 56.4 ± 8.1 歲 |
| 男性 | 44.5%（188,577 人） |
| CVD 案例平均年齡 | 60.5 歲（男 60.2、女 61.1） |
| 白人比例 | 94% |

---

## 核心方法論

### AutoPrognosis 框架

AutoPrognosis 是一個自動化 ML 管線選擇與調參框架，使用 **貝葉斯最佳化** 自動搜索最佳 ML pipeline 組合：

| Pipeline 階段 | 候選演算法數 | 內容 |
|-------------|---------|------|
| **Data Imputation** | 7 | MissForest, Mean, MICE, Median, EM, None, Most-frequent, Matrix completion |
| **Feature Processing** | 9 | PCA, Fast ICA, Kernel PCA, Polynomial, Feature agglomeration, Nystroem, Select Rates, R. kitchen sinks, Linear SVM |
| **Classification** | 20 | LR, NB×3, LDA, DT, RF, XGBoost, LightGBM, Gradient Boosting, AdaBoost, Neural Network, SVM, Bagging, Extra Random Trees, Survival Forest, Cox Regression, Ridge, Gaussian Process, k-NN |
| **Calibration** | 3 | Sigmoid, Isotonic, None |

**總搜索空間**：5,460 種可能 pipeline

### 訓練流程

- 200 次貝葉斯最佳化迭代
- 每次迭代探索一個新 pipeline 並調參
- 最終模型 = 200 個加權 pipeline 的集成
- **最強子 pipeline**：MissForest → 無特徵處理 → XGBoost (200 estimators) → Sigmoid 校準

### 比較模型

| 模型 | 說明 |
|------|------|
| **Framingham Score** | BMI 版本（非膽固醇版），使用原始係數 |
| **Cox PH (7 core)** | 同 Framingham 7 因子，在 UK Biobank 上重新擬合 |
| **Cox PH (all 473)** | LASSO 篩選後 Cox 回歸 |
| **Linear SVM** | 線性支持向量機 |
| **Random Forest** | 隨機森林 |
| **Neural Network** | 神經網路 |
| **AdaBoost** | 自適應提升 |
| **Gradient Boosting** | 梯度提升機 |
| **AutoPrognosis** | 4 種變體（7 core / 369 non-lab / 104 lab / all 473） |

### 缺失值處理

- MissForest 非參數插補
- 5 次多重插補 + Rubin's rules 平均
- 納入條件：CVD 病人中缺失率 <50% 的變數（整體缺失率 ≤85%）

### 變數重要性方法

- **Post-hoc Random Forest**：以 AutoPrognosis 預測值為目標，重新訓練 RF
- **Permutation importance**：置換每個變數後觀察分類精度下降幅度
- 非直接 SHAP 或內建特徵重要性

---

## 主要結果

### 模型效能比較（5 年 CVD 風險）

| 模型 | AUC-ROC | vs Framingham |
|------|---------|-------------|
| Framingham Score | 0.724 ± 0.004 | Baseline |
| Cox PH (7 core) | 0.734 ± 0.005 | +1.0% |
| Cox PH (all variables) | 0.758 ± 0.005 | +3.4% |
| Support Vector Machines | 0.709 ± 0.061 | -1.5% |
| Random Forest | 0.730 ± 0.004 | +0.6% |
| Neural Networks | 0.755 ± 0.005 | +3.1% |
| AdaBoost | 0.759 ± 0.004 | +3.5% |
| Gradient Boosting | 0.769 ± 0.005 | +4.5% |
| **AutoPrognosis (7 core)** | **0.744 ± 0.005** | +2.0% |
| AutoPrognosis (369 non-lab) | 0.761 ± 0.005 | +3.7% |
| AutoPrognosis (104 lab) | 0.735 ± 0.008 | +1.1% |
| **AutoPrognosis (all 473)** | **0.774 ± 0.005** | **+5.0%** |

**關鍵觀察**：
- AutoPrognosis (all) > Gradient Boosting > AdaBoost > Neural Networks > Cox PH (all) > Cox PH (7) > Framingham
- **SVM 表現最差**（0.709），甚至低於 Framingham（與本研究 SVM 結果可比較）
- NRI = +12.5%（AutoPrognosis vs Cox PH all）
- Brier score = 0.0121（校準良好）

### Information Gain vs Modeling Gain

| 增益來源 | 比較 | AUC 差異 |
|--------|------|---------|
| **Information gain** | AutoPrognosis (7 core) → AutoPrognosis (all) | 0.744 → 0.774 = **+3.0%** |
| **Modeling gain** | Framingham → AutoPrognosis (7 core) | 0.724 → 0.744 = **+2.0%** |
| **Combined** | Framingham → AutoPrognosis (all) | 0.724 → 0.774 = **+5.0%** |

→ **「資訊增益 > 建模增益」**：加入更多預測變數帶來的效益 > 使用更複雜模型的效益

### 臨床分類分析（7.5% 風險閾值）

| 指標 | Framingham | AutoPrognosis |
|------|-----------|---------------|
| 正確預測 CVD 案例 | 2,989 / 4,801 | 3,357 / 4,801 |
| Sensitivity | 62.2% | 69.9% |
| PPV | 1.5% | 2.6% |
| **淨增加正確預測** | — | **+368 案例** |

### Top 20 變數重要性

**男性**：

| 排名 | 變數 | 重要性 | 傳統因子? |
|------|------|--------|---------|
| 1 | **Age** | 0.346 | ✅ |
| 2 | **Smoking** | 0.101 | ✅ |
| 3 | Usual walking pace | 0.052 | ❌ 新發現 |
| 4 | **SBP** | 0.040 | ✅ |
| 5 | Microalbumin in urine | 0.032 | ❌ |
| 6 | High blood pressure | 0.030 | ✅ |
| 7 | RBC distribution width | 0.025 | ❌ |
| 8 | Self-reported health rating | 0.019 | ❌ 新發現 |
| 9 | Haematocrit % | 0.014 | ❌ |
| 10 | Father age at death | 0.014 | ❌ |

**女性**：

| 排名 | 變數 | 重要性 | 傳統因子? |
|------|------|--------|---------|
| 1 | **Age** | 0.370 | ✅ |
| 2 | **Smoking** | 0.099 | ✅ |
| 3 | Usual walking pace | 0.057 | ❌ 新發現 |
| 4 | Ankle spacing width | 0.035 | ❌ 新發現 |
| 5 | Self-reported health rating | 0.030 | ❌ 新發現 |
| 6 | **SBP** | 0.026 | ✅ |

**新穎預測因子**：
- **Usual walking pace**（步行速度）：男女皆為 top 3，反映體能/活動量
- **Self-reported health rating**（自評健康）：主觀變數竟有高預測力
- **Ankle spacing width**（女性 top 4）：可能反映周邊循環問題
- **Microalbumin in urine**：腎功能標記，尤其在糖尿病亞群中極重要

### 糖尿病亞群分析

| 模型 | Non-diabetic AUC | Diabetic AUC |
|------|-----------------|-------------|
| Framingham | 0.724 ± 0.004 | **0.578 ± 0.018** |
| AutoPrognosis | 0.774 ± 0.005 | **0.713 ± 0.010** |

- Framingham 在糖尿病人群中表現大幅下降（0.724 → 0.578）
- AutoPrognosis 維持較高精度（0.713），差距為 **+13.5%**
- 糖尿病亞群中 **microalbumin in urine** 升為第 2 重要變數（score 0.110）

---

## 與本研究的比較

| 面向 | Alaa (2019) | 本研究 |
|------|-----------|------|
| **資料來源** | UK Biobank（英國） | 杭州健檢（中國） |
| **樣本量** | 423,604 | 6,056 |
| **預測目標** | CVD 事件（5 年） | 高血壓+高血糖+血脂異常 |
| **變數數** | 473 | ~20 |
| **模型方法** | AutoML (5,460 pipeline) | 8 模型手動比較 + PySR |
| **最佳 AUC** | 0.774 | 待比較 |
| **驗證方式** | 10-fold stratified CV | 交叉驗證 |
| **特徵類型** | 多元（問卷+血液+體測+社經+家族史） | 健檢數值 + Δ 變化量 |
| **縱向設計** | ❌ 橫斷面 | ✅ T1→T2→T3 |
| **可解釋性** | Permutation importance（post-hoc RF） | SHAP + PySR 符號回歸 |
| **類別不平衡** | 未特別處理（事件率 1.13%） | SMOTE |
| **校準** | Sigmoid regression + Brier score | — |

### 本研究可引用的論證

1. **系統性模型比較的合理性**：Alaa 展示不同 ML 模型表現差異極大（SVM 0.709 vs AutoPrognosis 0.774），支持本研究比較 8 種模型的必要性
2. **SVM 表現不穩定**：Alaa 中 SVM 是唯一低於 Framingham 的 ML 模型（0.709），本研究若 SVM 表現較差可以此為佐證
3. **Information gain > Modeling gain**：加入更多變數比使用更複雜模型更有效，支持本研究使用 Δ 變化量特徵的「資訊增益」策略
4. **AutoML 自動選出 XGBoost 為最強**：驗證 XGBoost 在健康預測領域的優勢地位
5. **傳統因子仍然重要**：Age 和 Smoking 佔總重要性 >40%，與本研究 SHAP 結果可呼應

### 本研究的相對優勢

1. **縱向設計**：Alaa 使用橫斷面單次測量，本研究有 T1→T2→T3 + Δ 變化量
2. **同時預測 3H**：Alaa 僅預測 CVD 事件（含死亡），本研究預測高血壓+高血糖+血脂異常
3. **更深的可解釋性**：Alaa 用 post-hoc RF permutation importance，本研究用 SHAP + PySR 符號回歸
4. **亞洲人群**：Alaa 94% 白人，本研究為中國人群
5. **SMOTE 處理不平衡**：Alaa 未處理（事件率僅 1.13%，嚴重不平衡）

---

## 研究限制（作者自述）

1. **缺少膽固醇指標**：UK Biobank 當時未釋出 TC、HDL-C、LDL-C，無法與 QRISK2 直接比較
2. **缺少其他生化標記**：TG、HbA1c、CRP、natriuretic peptides 等
3. **種族單一**：94% 白人，無法評估種族差異
4. **事件率極低**：5 年 CVD 事件率僅 ~1.13%（4,801/423,604），嚴重類別不平衡但未處理
5. **僅報 AUC-ROC**：未報 PR-AUC（在嚴重不平衡下 ROC-AUC 可能過度樂觀）
6. **Post-hoc 變數排名**：使用代理 RF 而非直接的模型可解釋性方法（如 SHAP）

---

## 對本論文寫作的引用建議

### 第二章（文獻回顧）
- 作為「AutoML / 多模型系統性比較」的代表性研究引用
- 引用 Table 2 展示不同 ML 模型效能差異極大，強調系統性比較的必要性
- 引用 SVM 表現不穩定的發現
- 引用 "information gain > modeling gain" 的概念，支持特徵工程（Δ 變化量）的重要性

### 第七章（討論）
- 比較 AUC：Alaa AutoPrognosis 0.774 vs 本研究結果（注意 Alaa 預測 CVD 事件，非三高）
- 討論 XGBoost 在兩個研究中都表現突出
- 引用 Alaa 的 information gain 概念，論證本研究的 Δ 特徵設計屬於 information gain 策略
- 本研究優勢：縱向設計 + 同時預測 3H + SHAP 可解釋性 + 亞洲人群

---

## 關鍵引述

> "We found that the 'information gain' achieved by considering more risk factors in the predictive model was significantly higher than the 'modeling gain' achieved by adopting complex predictive models."

> "AutoPrognosis was able to agnostically discover new predictors of CVD risk. Among the discovered predictors were non-laboratory variables that can be collected relatively easily via questionnaires, such as the individuals' self-reported health ratings and usual walking pace."

> "With the exception of support vector machines, all the standard ML models achieved statistically significant improvements compared to the baseline Framingham score."

> "Unlike the Framingham score, AutoPrognosis was able to maintain high predictive accuracy for participants diagnosed with diabetes at baseline."