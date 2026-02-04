# Majcherek et al. (2025) PLOS ONE — 糖尿病風險預測深度解析

> **論文**：AI-driven analysis of diabetes risk determinants in U.S. adults: Exploring disease prevalence and health factors
> **期刊**：PLoS ONE, 2025; 20(9): e0328655
> **作者**：Dawid Majcherek, Antoni Ciesielski, Paweł Sobczak
> **機構**：SGH Warsaw School of Economics / University of Applied Sciences in Konin, Poland
> **DOI**：[10.1371/journal.pone.0328655](https://doi.org/10.1371/journal.pone.0328655)
> **PDF**：[Majcherek_PLOSONE_Diabetes_BRFSS_2025.pdf](../papers/Majcherek_PLOSONE_Diabetes_BRFSS_2025.pdf)

---

## 📋 基本資訊

| 項目 | 內容 |
|------|------|
| **研究主題** | 美國成人糖尿病風險決定因子的 AI 驅動分析 |
| **研究設計** | 回顧性橫斷面研究 |
| **資料來源** | 2015 Behavioral Risk Factor Surveillance System (BRFSS) |
| **樣本數** | 253,680 名成人 |
| **糖尿病盛行率** | 14% |
| **比較模型** | **18 種**（涵蓋傳統統計、樹模型、集成學習、距離方法等） |
| **最佳模型** | Extra Trees Classifier：Accuracy 96%、AUC 0.99 |
| **可解釋性** | SHAP（Global feature importance + Decision plots） |
| **類別平衡** | ROS、SMOTE、ADASYN 三種方法比較 |

> **與本研究的關係**：此論文同時比較了 18 種模型，涵蓋傳統統計方法（LR、NB、LDA、QDA、Ridge）與機器學習方法，為我們選擇 NB 和 LDA 作為傳統統計方法對照組提供了文獻依據。

---

## 🎯 研究核心

### 研究目的

1. 比較 18 種 ML 模型在糖尿病風險預測上的效能
2. 找出前三名最佳模型
3. 使用 SHAP 分析識別最具影響力的風險因子
4. 探討社經因素（收入、教育）與糖尿病風險的關係

### 研究特色

| 面向 | 說明 |
|------|------|
| **大規模資料** | 25 萬筆 BRFSS 全國代表性調查 |
| **全面模型比較** | 18 種模型，從傳統統計到集成學習 |
| **多維度特徵** | 社會人口學 + 健康行為 + 臨床指標 |
| **可解釋性** | SHAP 全局 + 局部解釋 |

---

## 📊 18 種模型分類

### 依方法論分類（對應我們的論文架構）

| 類型 | 模型 | 與我們研究的對應 |
|------|------|-----------------|
| **傳統統計方法** | Logistic Regression | ✅ 我們有 |
| | **Naive Bayes** | ✅ 我們有 |
| | **Linear Discriminant Analysis (LDA)** | ✅ 我們有 |
| | Quadratic Discriminant Analysis (QDA) | — |
| | Ridge Classifier | — |
| | Nearest Centroid Classifier | — |
| **樹狀模型** | Decision Tree | ✅ 我們有 |
| | C5.0 Decision Tree | — |
| | Random Forest | ✅ 我們有 |
| | Extra Trees Classifier | — |
| **梯度提升** | Gradient Boosting | — |
| | XGBoost | ✅ 我們有 |
| | LightGBM | — |
| | CatBoost | — |
| | Histogram-based GB | — |
| | AdaBoost | — |
| **距離方法** | K-Nearest Neighbors (KNN) | — |
| **異常檢測** | Isolation Forest | — |

> **關鍵觀察**：該論文將 LR、NB、LDA、QDA、Ridge、Nearest Centroid 歸類為傳統/線性方法，我們從中選擇了最具代表性且實作簡單的 **NB 和 LDA**，與既有的 LR 組成三種傳統統計方法。

---

## 📈 模型效能比較（完整排名）

| 排名 | 模型 | Accuracy | Precision | Recall | AUC |
|------|------|----------|-----------|--------|-----|
| 1 | **Extra Trees Classifier** | **96%** | **0.94** | **0.99** | **0.96** |
| 2 | C5.0 Decision Tree | 92% | 0.99 | 0.99 | 0.92 |
| 3 | Decision Tree | 92% | 0.99 | 0.99 | 0.92 |
| 4 | Random Forest | 90% | 0.87 | 0.96 | 0.90 |
| 5 | KNN | 82% | 0.76 | 0.95 | 0.82 |
| 6 | CatBoost | 76% | 0.81 | 0.81 | 0.76 |
| 7 | Histogram-based GB | 75% | 0.73 | 0.80 | 0.75 |
| 8 | LightGBM | 74% | 0.72 | 0.80 | 0.75 |
| 9 | XGBoost | 74% | 0.72 | 0.76 | 0.73 |
| 10 | AdaBoost | 74% | 0.76 | 0.76 | 0.74 |
| 11 | Gradient Boosting | 74% | 0.72 | 0.78 | 0.74 |
| 12 | Ridge Classifier | 73% | 0.72 | 0.76 | 0.73 |
| 13 | **LDA** | **73%** | **0.72** | **0.76** | **0.73** |
| 14 | **Logistic Regression** | **72%** | **0.72** | **0.75** | **0.73** |
| 15 | QDA | 71% | 0.68 | 0.82 | 0.71 |
| 16 | **Naive Bayes** | **71%** | **0.70** | **0.73** | **0.71** |
| 17 | Nearest Centroid | 63% | 0.68 | 0.48 | 0.63 |
| 18 | Isolation Forest | 53% | 0.65 | 0.13 | 0.53 |

### 傳統統計方法效能摘要

| 模型 | Accuracy | AUC | 排名 |
|------|----------|-----|------|
| LDA | 73% | 0.73 | #13 |
| LR | 72% | 0.73 | #14 |
| QDA | 71% | 0.71 | #15 |
| NB | 71% | 0.71 | #16 |

> **觀察**：傳統統計方法 AUC 集中在 0.71–0.73，表現接近但低於樹模型。LDA 略優於 LR，NB 略低——與我們的實驗結果趨勢可對照。

---

## 🔍 SHAP 特徵重要性

| 排名 | 特徵 | 說明 | 與我們研究的對應 |
|------|------|------|-----------------|
| 1 | **BMI** | 最強預測因子，25-30 區間風險陡增 | ✅ 我們有 BMI + ΔBMI |
| 2 | **Age** | 非線性，45 歲後顯著上升，65-69 歲達峰 | ✅ 我們有 Age |
| 3 | **GenHlth** | 自評健康狀態，「差」者風險最高 | ❌ 我們無（問卷題） |
| 4 | **Income** | 倒 U 型：$20K-$25K 風險最高 | ❌ 我們無 |
| 5 | **PhysHlth** | 身體不適天數 | ❌ 我們無 |
| 6 | **Education** | 教育程度 | ❌ 我們無 |
| — | **HighBP** | 高血壓與糖尿病強正相關 | ✅ 我們有 SBP/DBP |

> **差異**：該研究特徵以社會人口學和健康行為為主（BRFSS 問卷），我們的特徵以臨床生化指標為主（血壓、血糖、血脂、尿酸、eGFR）。

---

## 🔄 類別不平衡處理

| 方法 | 說明 | 效果 |
|------|------|------|
| **ROS** (Random Over-Sampling) | 隨機複製少數類樣本 | ✅ 最佳 |
| **SMOTE** | 合成少數類樣本（k-NN 插值） | 次佳 |
| **ADASYN** | 自適應合成（困難樣本加權） | 第三 |

> ROS 在該研究中效果最好，與一般文獻（SMOTE 較常推薦）不同。我們採用 class_weight='balanced' 為主、SMOTE 為輔的策略。

---

## 🔍 與本研究的比較

| 面向 | Majcherek et al. (2025) | 我們的研究 |
|------|------------------------|-----------|
| **疾病** | 糖尿病（單一） | 高血壓、高血糖、高血脂（三種） |
| **資料** | BRFSS 問卷調查（橫斷面） | 杭州社區 HRS 縱向三次健檢 |
| **樣本** | 253,680 | 6,119 |
| **陽性比例** | 14% | 高血壓 19.7%、高血糖 8.3%、高血脂 15.6% |
| **特徵類型** | 社會人口學 + 健康行為 | 臨床生化指標 + Δ 變化量 |
| **模型數** | 18 種 | 9 種 |
| **傳統統計** | LR, NB, LDA, QDA, Ridge, Nearest Centroid | LR, NB, LDA |
| **類別平衡** | ROS / SMOTE / ADASYN | class_weight + SMOTE |
| **可解釋性** | SHAP | SHAP + 符號回歸 |
| **最佳 AUC** | 0.99 (Extra Trees) | 0.932 (LR for Hyperglycemia) |

### 我們的優勢

1. **縱向資料**：三次健檢 + Δ 特徵，可捕捉時間趨勢（該研究為橫斷面）
2. **多疾病預測**：同時預測三高，非單一疾病
3. **臨床特徵**：直接使用生化檢驗指標，非自填問卷（減少回憶偏差）
4. **符號回歸**：提供可解讀的數學公式，不只 SHAP 事後解釋

### 可借鏡之處

1. **模型分類框架**：將 18 種模型按方法論分類，支持我們「傳統統計 vs. ML」比較架構
2. **NB/LDA 選擇依據**：該研究同時納入 NB、LDA 作為傳統方法，佐證我們的方法選擇
3. **多種重採樣比較**：ROS vs. SMOTE vs. ADASYN 的系統性比較
4. **SHAP Decision Plot**：局部解釋的視覺化方式

---

## ⚠️ 限制與批判性評估

| 問題 | 說明 |
|------|------|
| **自填資料偏差** | BRFSS 為電話問卷，存在社會期許偏差和回憶偏差 |
| **橫斷面設計** | 無法建立因果關係，只能觀察相關性 |
| **AUC 過高** | Extra Trees 達 0.99，可能存在過擬合或資料洩漏疑慮 |
| **ROS 風險** | 隨機複製少數類可能導致過擬合（優於 SMOTE 不太常見） |
| **無外部驗證** | 僅在 BRFSS 2015 上訓練/測試，無跨年度或跨資料集驗證 |
| **特徵局限** | 無臨床生化指標（血糖值、HbA1c 等），僅有問卷自報 |

---

## 📝 論文在本研究中的引用位置

| 章節 | 用途 |
|------|------|
| Ch2 §2.3 | 傳統統計方法（NB/LDA）選擇的文獻依據 |
| Ch2 §2.6 | 表 2-1 相關研究比較（可考慮新增） |
| Ch3 §3.4.1 | NB/LDA 方法選擇說明 |

---

## 🔑 一句話總結

> 此論文系統性比較 18 種模型（含 6 種傳統統計方法）用於糖尿病預測，證實傳統方法（LR/NB/LDA）雖效能低於樹模型，仍具基準比較價值。為我們選擇 NB 和 LDA 作為傳統統計方法對照組提供了直接的文獻支持。
