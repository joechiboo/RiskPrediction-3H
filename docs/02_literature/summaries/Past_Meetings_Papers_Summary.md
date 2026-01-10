# 過去 Meeting 論文總結 (編號 01-12)

**整理日期**：2025-11-13
**用途**：總結 Meeting 1-14 中報告的其他研究論文（編號 01-12）
**資料來源**：[Systematic_Literature_Review.md](Systematic_Literature_Review.md)

---

## 📑 文獻總覽

| 編號 | 研究標的 | 期刊分級 | 疾病 | 資料集 | 最佳模型 | 重要性 |
|------|---------|---------|------|--------|---------|--------|
| 01 | 腎臟疾病預測 | - | 腎臟病 | NHANES (可下載) | DT | ⭐⭐ |
| 02 | 心臟疾病預測 | - | 心臟病 | UCI/Framingham | XGBoost | ⭐⭐⭐ |
| 03 | 腎病病理分類 | - | 腎臟病 | 台灣醫院 (不可下載) | RF, XGBoost | ⭐⭐⭐ |
| 04 | 中風風險評估 | SCI | 中風 | 中國 EHR (不可下載) | CNN | ⭐⭐⭐ |
| 05 | miRNA疾病預測 | SCI | 癌症 | HMDD v3.0 (可下載) | BLS | ⭐ |
| 06 | 慢性病風險預測 | SCI | 慢性病 | Catapult Health | GB | ⭐⭐⭐ |
| 07 | 尿酸回歸預測 | SCI | 高尿酸 | 公司健檢 (不可下載) | RF | ⭐⭐⭐⭐ |
| 08 | 糖尿病分類預測 | - | 糖尿病 | CDC (可下載) | GBM | ⭐⭐⭐ |
| 10 | 醫療資料集分類 | - | 多疾病 | UCI (可下載) | Proposed GP | ⭐⭐ |
| 12 | 血糖回歸預測 | - | 糖尿病 | Ohio2020 (申請) | MOGE | ⭐⭐ |

---

## 論文 01：腎臟疾病預測

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 腎臟疾病預測 |
| **處理問題** | 比較參數與準確度的影響 |
| **期刊分級** | - (非 SCI) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | 美國 NCHS (CDC) - NHANES |
| **資料集狀態** | ✅ 可下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 血液檢驗 (Blood tests)
- 尿液檢驗 (Urine tests)

### 方法

**前處理**：
- 資料不平衡處理：Under-Sampling

**機器學習方法**：
- Decision Tree (CART)

### 評估準則

- **Recall**（召回率）

### 輸出

- 預測腎臟病風險

### 提出解決方案

- 無特定名稱

### 與本研究的關聯

⭐⭐ **低關聯**
- ✅ 公開可下載資料集 (NHANES)
- ❌ 單一模型 (DT)，方法較簡單
- ❌ 預測腎臟病，非三高

---

## 論文 02：心臟疾病預測

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 心臟疾病預測 |
| **處理問題** | 媒合保險與顧客 |
| **期刊分級** | - (非 SCI) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | UCI (Cleveland Clinic Foundation) / Framingham Heart Study |
| **資料集狀態** | ✅ 可下載 (公開資料集) |
| **樣本數** | 未提供 |

### 輸入特徵

- 年齡性別 (Demographics)
- 生活習慣 (Lifestyle)
- 血液檢驗 (Blood tests)
- 生理量測 (Physical measurements)

### 方法

**前處理**：
- 資料不平衡處理：上採樣、下採樣、SMOTE
- 缺失值處理：有處理

**機器學習方法**：
- Decision Tree (DT)
- Random Forest (RF)
- Logistic Regression (LR)
- Support Vector Machine (SVM)
- XGBoost
- Light GBM
- Artificial Neural Network (ANN)

### 評估準則

- **Recall**（召回率）

### 輸出

- 預測心臟疾病風險

### 提出解決方案

- 無特定名稱，但比較多種 ML 模型

### 與本研究的關聯

⭐⭐⭐ **中等關聯**
- ✅ 公開可下載資料集 (UCI, Framingham)
- ✅ 包含血液檢驗 + 生理量測
- ✅ 多種 ML 模型比較（包含 XGBoost, Light GBM）
- ✅ 處理資料不平衡（SMOTE）
- ❌ 預測心臟病，非三高

---

## 論文 03：腎病病理分類

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 腎病病理分類 |
| **處理問題** | 檢驗數據分型預測 |
| **期刊分級** | - (非 SCI) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | 台灣醫院：北醫、萬芳、馬偕、雙和 |
| **資料集狀態** | ❌ 無法下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 年齡性別 (Demographics)
- 檢驗結果 (Laboratory results)

### 方法

**前處理**：
- 資料不平衡處理：SMOTE
- 缺失值處理：KNN

**機器學習方法**：
- Random Forest (RF)
- Logistic Regression (LR)
- Support Vector Machine (SVM)
- XGBoost
- K-Nearest Neighbors (KNN)

### 評估準則

- Accuracy
- AUC

### 輸出

- 預測腎臟病風險

### 提出解決方案

- 無特定名稱

### 與本研究的關聯

⭐⭐⭐ **中等關聯**
- ✅ 台灣本土資料（北醫、萬芳、馬偕、雙和）
- ✅ 多種 ML 模型比較（包含 RF, XGBoost）
- ✅ 處理缺失值（KNN）和資料不平衡（SMOTE）
- ❌ 預測腎臟病，非三高

---

## 論文 04：中風風險評估 (SCI)

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 中風風險評估 |
| **處理問題** | 融合結構化與非結構化資訊提高並加速疾病風險準確率 |
| **期刊分級** | ✅ **SCI** |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | 中國中部某醫院的電子健康記錄 (EHR) |
| **資料集狀態** | ❌ 無法下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 生活習慣 (Lifestyle)
- 檢驗結果 (Laboratory results)
- 醫生記錄 (Doctor's notes)
- 病歷描述 (Medical records descriptions)

**特色**：結合結構化與非結構化資料

### 方法

**前處理**：
- 缺失值處理
- LFM (Latent Factor Model)

**機器學習方法**：
- Decision Tree (DT)
- Convolutional Neural Network (**CNN**)
- Naïve Bayes
- K-Nearest Neighbors (KNN)

### 評估準則

- Accuracy
- Recall

### 輸出

- 預測慢性疾病風險

### 提出解決方案

**CNN-MDRP** (CNN-based Multi-Disease Risk Prediction)

**創新點**：
- 使用 CNN 處理非結構化文本資料
- 融合結構化與非結構化資訊

### 與本研究的關聯

⭐⭐⭐ **中等關聯**
- ✅ SCI 期刊論文
- ✅ 融合多種資料類型
- ✅ CNN 用於醫療文本處理
- ❌ 非結構化資料（病歷描述），本研究無此類資料
- ❌ 預測中風，非完整三高

---

## 論文 05：miRNA 疾病預測 (SCI)

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | miRNA 疾病預測 |
| **處理問題** | 新增資料時的災難性遺忘問題 (Catastrophic Forgetting) |
| **期刊分級** | ✅ **SCI** |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | HMDD v3.0, miRBase |
| **資料集狀態** | ✅ 可下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 基因序列 (Gene sequences)
- 基因疾病關聯 (Gene-disease associations)
- 疾病語意資料 (Disease semantic data)
- 基因功能資料 (Gene functional data)

### 方法

**前處理**：
- 未提供

**機器學習方法**：
- Decision Tree (DT)
- Random Forest (RF)
- Support Vector Machine (SVM)
- Broad Learning System (**BLS**)

### 評估準則

- Accuracy
- AUC

### 輸出

- 基因與癌症關聯

### 提出解決方案

**MISSIM** (miRNA-disease association prediction with Incremental learning)

**創新點**：
- 解決災難性遺忘問題
- 適用於增量學習場景

### 與本研究的關聯

⭐ **低關聯**
- ✅ SCI 期刊論文
- ✅ 公開可下載資料集
- ❌ 基因序列預測，與三高預測領域差異大
- ❌ 方法論（增量學習）不適用於本研究

---

## 論文 06：慢性病風險預測 (SCI)

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 慢性病風險預測 |
| **處理問題** | 即時計算預測風險值 |
| **期刊分級** | ✅ **SCI** |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | Catapult Health |
| **資料集狀態** | ❌ 私有資料集 |
| **樣本數** | 未提供 |

### 輸入特徵

- 血液檢查 (Blood tests)
- 生理量測 (Physical measurements)

### 方法

**前處理**：
- 資料不平衡處理：Oversampling, Undersampling, SMOTE

**機器學習方法**：
- Decision Tree (DT)
- Random Forest (RF)
- Logistic Regression (LR)
- Support Vector Machine (SVM)
- Naïve Bayes (NB)
- K-Nearest Neighbors (KNN)
- Gradient Boosting (**GB**)

### 評估準則

- Accuracy
- AUC

### 輸出

- 即時預測慢性疾病風險

### 提出解決方案

- 無特定名稱，但強調即時計算能力

### 與本研究的關聯

⭐⭐⭐ **中等關聯**
- ✅ SCI 期刊論文
- ✅ 包含血液檢查 + 生理量測（與本研究資料類型相同）
- ✅ 多種 ML 模型比較（包含 GB）
- ✅ 處理資料不平衡（SMOTE）
- ✅ 慢性病風險預測（廣義包含三高）
- ❌ 強調即時計算，本研究重點為縱向預測

---

## 論文 07：尿酸回歸預測 (SCI) ⭐⭐⭐⭐

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 尿酸回歸預測 |
| **處理問題** | 降低檢測成本與頻率 |
| **期刊分級** | ✅ **SCI** |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | 公司員工健檢數據 |
| **資料集狀態** | ❌ 無法下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 生理量測 (Physical measurements)
- 檢驗結果 (Laboratory results)
- 飲食習慣 (Dietary habits)

### 方法

**前處理**：
- 未提供

**機器學習方法**：
- Boosted Decision Tree (BDT)
- Random Forest (**RF**)
- Logistic Regression (LR)
- Neural Network (NN)
- Bayesian Linear Regression (BLR)

### 評估準則

- **RMSE** (Root Mean Squared Error)

**注意**：這是回歸問題，不是分類問題

### 輸出

- 預測血中尿酸值（連續值）

### 提出解決方案

- 無特定名稱

### 與本研究的關聯

⭐⭐⭐⭐ **高度相關**
- ✅ SCI 期刊論文
- ✅ 健檢數據（與本研究資料來源相似）
- ✅ 包含生理量測 + 檢驗結果
- ✅ **尿酸預測與本研究極度相關**（尿酸是本研究的核心特徵之一）
- ✅ 多種 ML 模型比較（包含 RF）
- ❌ 回歸問題（預測連續值），本研究為分類問題

**重要性**：
- 本研究資料集來源：**SUA_CVDs**（血清尿酸與心血管疾病）
- 尿酸是三高的重要風險因子
- 可參考其特徵工程方法

---

## 論文 08：糖尿病分類預測

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 糖尿病分類預測 |
| **處理問題** | 探討各種 ML 模型預測糖尿病風險 |
| **期刊分級** | - (非 SCI) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | 美國 CDC 健康調查資料集 |
| **資料集狀態** | ✅ 可下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 血液檢查 (Blood tests)
- 生理量測 (Physical measurements)
- 社會經歷 (Social history)

### 方法

**前處理**：
- 變數處理
- 欄位轉換
- 移除缺失值

**機器學習方法**：
- Decision Tree (DT)
- Random Forest (RF)
- Logistic Regression (LR)
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Gradient Boosting Machine (**GBM**)
- Multivariate Adaptive Regression Splines (**MARS**)

### 評估準則

- Accuracy
- Precision
- Recall
- F1-Score
- AUC

### 輸出

- 糖尿病風險預測值
- **對應 SHAP 解釋** ⭐

### 提出解決方案

- 無特定名稱，但使用 **SHAP 進行可解釋性分析**

### 與本研究的關聯

⭐⭐⭐ **中等關聯**
- ✅ 公開可下載資料集 (CDC)
- ✅ 包含血液檢查 + 生理量測
- ✅ 多種 ML 模型比較（包含 GBM, MARS）
- ✅ **使用 SHAP 進行可解釋性分析**（本研究計畫使用）
- ✅ 預測糖尿病（三高之一）
- ❌ 單一疾病預測，非多標籤

---

## 論文 10：醫療資料集分類

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 醫療資料集分類 |
| **處理問題** | 類別不平衡 |
| **期刊分級** | - (非 SCI) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | UCI 機器學習庫 |
| **資料集狀態** | ✅ 可下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 血液檢查 (Blood tests)
- 腫瘤影像 (Tumor images)
- 飲酒頻率 (Alcohol frequency)

### 方法

**前處理**：
- 移除缺失值
- 欄位轉換

**機器學習方法**：
- Support Vector Machine (SVM)
- Genetic Programming (**GP**) + Fave fitness

### 評估準則

- Accuracy
- Precision
- Specificity
- Recall
- F1-Score
- AUC

### 輸出

- 預測腎病、乳癌、肝病與不孕症等疾病

### 提出解決方案

**Proposed GP** (Genetic Programming with Fave fitness)

**創新點**：
- 使用基因演算法處理類別不平衡

### 與本研究的關聯

⭐⭐ **低關聯**
- ✅ 公開可下載資料集 (UCI)
- ✅ 包含血液檢查
- ❌ 使用 GP（較少見方法），本研究使用主流 ML 模型
- ❌ 預測多種疾病（腎病、乳癌、肝病、不孕症），非三高

---

## 論文 12：血糖回歸預測

### 基本資訊

| 項目 | 內容 |
|------|------|
| **研究標的** | 血糖回歸預測 |
| **處理問題** | 比較模型準確度 |
| **期刊分級** | - (非 SCI) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | Ohio2020 dataset |
| **資料集狀態** | ⚠️ 要申請才可下載 |
| **樣本數** | 未提供 |

### 輸入特徵

- 血糖值 (Glucose values)
- 胰島素劑量 (Insulin dosage)
- 皮膚電反應 (Galvanic skin response)

### 方法

**前處理**：
- 特徵交集化
- 缺值處理

**機器學習方法**：
- Genetic Programming (GP)
- GP with Over-Sampling (GP-OS)
- Grammatical Evolution (GE)
- Multi-Objective Grammatical Evolution (**MOGE**)
- Logistic Regression (LR)
- Random Forest (RF)
- ARIMA (時間序列模型)

### 評估準則

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- **Clarke Error Grid** (醫療專用評估)

### 輸出

- 30 分鐘與 60 分鐘血糖值預測

### 提出解決方案

- 無特定名稱，但使用多種時間序列預測方法

### 與本研究的關聯

⭐⭐ **低關聯**
- ✅ 血糖預測（與糖尿病相關）
- ✅ 時間序列預測（本研究也有時序特徵）
- ❌ 短期血糖預測（30-60分鐘），本研究為長期疾病風險預測
- ❌ 回歸問題，本研究為分類問題
- ❌ 需要胰島素劑量、皮膚電反應（本研究無此資料）

---

## 綜合比較表

### 按關聯度排序

| 排名 | 編號 | 研究標的 | 關聯度 | 主要原因 |
|------|------|---------|--------|---------|
| 1 | 07 | 尿酸回歸預測 | ⭐⭐⭐⭐ | SCI + 健檢數據 + 尿酸 (本研究核心特徵) |
| 2 | 02 | 心臟疾病預測 | ⭐⭐⭐ | 公開資料 + 血液檢驗 + 多模型比較 + SMOTE |
| 3 | 03 | 腎病病理分類 | ⭐⭐⭐ | 台灣資料 + 多模型 + SMOTE + KNN |
| 4 | 04 | 中風風險評估 | ⭐⭐⭐ | SCI + CNN + 結構化+非結構化資料 |
| 5 | 06 | 慢性病風險預測 | ⭐⭐⭐ | SCI + 血液檢驗 + 生理量測 + SMOTE |
| 6 | 08 | 糖尿病分類預測 | ⭐⭐⭐ | 公開資料 + SHAP 可解釋性 |
| 7 | 01 | 腎臟疾病預測 | ⭐⭐ | 公開資料 (NHANES) + 單一模型 |
| 8 | 10 | 醫療資料集分類 | ⭐⭐ | 公開資料 (UCI) + GP 方法 |
| 9 | 12 | 血糖回歸預測 | ⭐⭐ | 時間序列 + 短期血糖預測 |
| 10 | 05 | miRNA疾病預測 | ⭐ | SCI + 基因序列 (領域差異大) |

### 按疾病類型分類

| 疾病類別 | 編號 | 研究標的 |
|---------|------|---------|
| **心血管疾病** | 02 | 心臟疾病預測 |
| | 04 | 中風風險評估 |
| **糖尿病** | 08 | 糖尿病分類預測 |
| | 12 | 血糖回歸預測 |
| **腎臟疾病** | 01 | 腎臟疾病預測 |
| | 03 | 腎病病理分類 |
| **高尿酸** | 07 | 尿酸回歸預測 ⭐ |
| **多種疾病** | 06 | 慢性病風險預測 |
| | 10 | 醫療資料集分類 |
| **基因疾病** | 05 | miRNA疾病預測 |

### 按資料集狀態分類

| 狀態 | 編號 | 研究標的 | 資料來源 |
|------|------|---------|---------|
| **✅ 可下載** | 01 | 腎臟疾病預測 | NHANES (CDC) |
| | 02 | 心臟疾病預測 | UCI, Framingham |
| | 05 | miRNA疾病預測 | HMDD v3.0, miRBase |
| | 08 | 糖尿病分類預測 | CDC 健康調查 |
| | 10 | 醫療資料集分類 | UCI |
| **⚠️ 需申請** | 12 | 血糖回歸預測 | Ohio2020 |
| **❌ 不可下載** | 03 | 腎病病理分類 | 台灣醫院 (北醫/萬芳/馬偕/雙和) |
| | 04 | 中風風險評估 | 中國 EHR |
| | 06 | 慢性病風險預測 | Catapult Health |
| | 07 | 尿酸回歸預測 | 公司員工健檢 |

### 按 SCI 期刊分類

| 分類 | 編號 | 研究標的 |
|------|------|---------|
| **✅ SCI** | 04 | 中風風險評估 |
| | 05 | miRNA疾病預測 |
| | 06 | 慢性病風險預測 |
| | 07 | 尿酸回歸預測 |
| **❌ 非 SCI** | 01 | 腎臟疾病預測 |
| | 02 | 心臟疾病預測 |
| | 03 | 腎病病理分類 |
| | 08 | 糖尿病分類預測 |
| | 10 | 醫療資料集分類 |
| | 12 | 血糖回歸預測 |

---

## 對本研究的啟示

### 資料處理方法

| 方法 | 出現次數 | 相關論文 |
|------|---------|---------|
| **SMOTE** | 4 | 02, 03, 06, 08 |
| **Under-Sampling** | 1 | 01 |
| **Over-Sampling** | 1 | 06 |
| **缺失值處理 (KNN)** | 1 | 03 |
| **移除缺失值** | 2 | 08, 10 |

**結論**：SMOTE 是最常用的類別不平衡處理方法

### 常用模型

| 模型 | 出現次數 | 相關論文 |
|------|---------|---------|
| **Random Forest (RF)** | 6 | 02, 03, 06, 07, 08, 12 |
| **Logistic Regression (LR)** | 6 | 02, 03, 06, 07, 08, 12 |
| **Decision Tree (DT)** | 5 | 01, 02, 04, 05, 06 |
| **SVM** | 5 | 02, 03, 05, 06, 08 |
| **XGBoost** | 2 | 02, 03 |
| **KNN** | 3 | 03, 04, 06 |
| **Neural Network (NN/ANN)** | 2 | 02, 07 |
| **Gradient Boosting (GB/GBM)** | 2 | 06, 08 |

**結論**：Random Forest 和 Logistic Regression 是最常用的基準模型

### 評估指標

| 指標 | 出現次數 | 相關論文 |
|------|---------|---------|
| **AUC** | 6 | 03, 05, 06, 08, 10 |
| **Accuracy** | 6 | 04, 05, 06, 08, 10 |
| **Recall** | 5 | 01, 02, 04, 08, 10 |
| **Precision** | 3 | 08, 10 |
| **F1-Score** | 3 | 08, 10 |
| **RMSE** | 2 | 07, 12 (回歸問題) |

**結論**：AUC 和 Accuracy 是最常用的評估指標

### 創新方法

| 方法 | 論文 | 特點 |
|------|------|------|
| **SHAP 可解釋性** | 08 | 糖尿病分類預測 |
| **CNN 融合非結構化資料** | 04 | 中風風險評估 |
| **Genetic Programming** | 10, 12 | 醫療資料集分類、血糖預測 |
| **Incremental Learning** | 05 | miRNA 疾病預測 |
| **Clarke Error Grid** | 12 | 醫療專用評估 |

---

## 📌 快速導航

- 📂 [返回 Literature Notes 目錄](.)
- 📊 [查看文獻總覽索引](Literature_Master_Index.md)
- 📋 [查看 Meeting 15-16 論文總結](Meeting_15-16_Papers_Summary.md)
- 📖 [查看系統性文獻回顧](Systematic_Literature_Review.md)
- 🎯 [查看 Q2 台灣文獻回顧](../research_plans/Q2_Taiwan_Literature_Review.md)

---

**文檔建立日期**：2025-11-13
**維護者**：紀伯喬
