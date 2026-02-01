# 論文筆記：Kanegae 高血壓預測 2020

> **建立日期**：2026-01-10
> **狀態**：已完整閱讀
> **評估**：⭐⭐⭐⭐⭐ **與本研究高度相關（使用 Δ 變化量特徵！）**

---

## 一句話摘要

**使用機器學習預測「正常血壓者未來是否會發展為高血壓」，採用 Year(-1)、Year(-2) 及兩年間變化量作為特徵，XGBoost/Ensemble 表現最佳 (AUC=0.877-0.881)。**

---

## 研究問題

| 問題 | 回答 |
|------|------|
| **研究什麼？** | 新發高血壓的風險預測 |
| **對象是誰？** | 日本正常血壓成年人（18,258 人）|
| **預測什麼？** | 未來是否會發展為高血壓 |
| **用什麼方法？** | XGBoost、Ensemble、Logistic Regression |
| **最佳模型？** | Ensemble（AUC 0.881）> XGBoost（0.877）> LR（0.859）|
| **關鍵特徵？** | SBP at Year(-1)、BMI、Age、CAVI |

---

## 基本資訊

| 欄位 | 內容 |
|------|------|
| **標題** | Highly precise risk prediction model for new-onset hypertension using artificial intelligence techniques |
| **期刊** | The Journal of Clinical Hypertension |
| **年份** | 2020 |
| **DOI** | [10.1111/jch.13759](https://doi.org/10.1111/jch.13759) |
| **PMID** | 31816148 |
| **PMC** | [PMC8029685](https://pmc.ncbi.nlm.nih.gov/articles/PMC8029685/) |

---

## 作者與機構

- **Hiroshi Kanegae**, Kenji Suzuki, Kyohei Fukatani, Tetsuya Ito, Nakahiro Harada, **Kazuomi Kario**
- 機構：自治醫科大學醫學院 心血管內科（日本栃木縣）

---

## 研究設計 ⭐⭐⭐⭐⭐

### 核心創新：使用縱向變化量特徵

**特徵工程**：

| 特徵類型 | 說明 |
|----------|------|
| **Year(-2) 測量值** | 兩年前的健檢數據 |
| **Year(-1) 測量值** | 一年前的健檢數據 |
| **Changes from Year(-2) to Year(-1)** | **兩年間的變化量 (Δ)** ⭐ |

**預測目標**：Year(0) 是否診斷為高血壓

```
時間軸：
Year(-2) → Year(-1) → Year(0)
   ↓          ↓          ↓
 特徵1      特徵2      預測目標
       \____Δ____/
        變化量特徵
```

**→ 這與我們的設計完全一致！我們也是用 T1、T2 和 Delta1 來預測 T3！**

---

## 資料集

| 項目 | 內容 |
|------|------|
| **來源** | 日本職場健檢數據 |
| **樣本數** | 18,258 人 |
| **時間範圍** | 2005-2016（11 年） |
| **追蹤設計** | 每年一次健檢，使用 3 年數據 |
| **新發高血壓** | 2,672 例 |
| **平均年齡** | 46 歲 |
| **男性比例** | 44.6% |

### 資料分割

| 集合 | 比例 | 樣本數 |
|------|------|--------|
| **Derivation set** | 75% | 13,694 |
| **Validation set** | 25% | 4,564 |

---

## 方法論

### 1. 機器學習模型

| 模型 | 類型 |
|------|------|
| **XGBoost** | 梯度提升 |
| **Ensemble** | 多模型集成 |
| **Logistic Regression** | 傳統統計（基準）|

### 2. 特徵類別

- 身體測量：BMI、身高、體重
- 血壓：收縮壓 (SBP)、舒張壓 (DBP)
- **CAVI**：心踝血管指數（Cardio-Ankle Vascular Index）
- 年齡、性別

### 3. 評估指標

- AUC-ROC
- Sensitivity
- Specificity

---

## 結果 ⭐⭐⭐⭐⭐

### 模型比較

| 模型 | Validation AUC |
|------|----------------|
| **Ensemble** | **0.881** ⭐ |
| XGBoost | 0.877 |
| Logistic Regression | 0.859 |

**→ 機器學習 > 傳統統計，AUC 差異約 2%**

### 特徵重要性（XGBoost）

| 排名 | 特徵 | 相對重要性 |
|------|------|-----------|
| 1 | **SBP at CAVI measurement, Year(-1)** | 100% |
| 2 | Clinic SBP, Year(-1) | 57.3% |
| 3 | BMI | 重要 |
| 4 | Age | 重要 |
| 5 | CAVI | 重要 |

**關鍵發現**：
- **Year(-1) 的血壓測量是最重要的預測因子**
- BMI 和 Age 也是重要預測因子（與其他研究一致）
- CAVI（動脈硬化指標）提供額外預測價值

---

## 與本研究的關聯 ⭐⭐⭐⭐⭐

### 高度相似點

| 項目 | Kanegae 2020 | 我們的研究 |
|------|--------------|-----------|
| **縱向設計** | ✅ Year(-2), Year(-1), Year(0) | ✅ T1, T2, T3 |
| **Δ 變化量** | ✅ Changes from Year(-2) to Year(-1) | ✅ Delta1 特徵 |
| **機器學習** | XGBoost, Ensemble | LR, RF, XGB, MLP, SVM |
| **預測目標** | 新發高血壓 | 三高（高血壓+高血糖+高血脂）|

### 差異點

| 項目 | Kanegae 2020 | 我們的研究 |
|------|--------------|-----------|
| **疾病數量** | 單一（高血壓） | **三種（MTL）** |
| **外部驗證** | ❌ 無 | **✅ 有 (CLSA)** |
| **跨國資料** | 僅日本 | **中國 + 加拿大** |
| **SHAP 分析** | ❌ 無 | **✅ 有** |
| **可解釋模型** | ❌ 無 PySR | **✅ 有** |

---

## 這篇論文的重要性

### 1. 驗證我們的方法論

**Kanegae 證明了「縱向變化量特徵」在高血壓預測上的價值！**

> "The prediction model for new‐onset hypertension was constructed to predict an individual's hypertension risk at Year (0) based on variables at Year (−1), Year (−2), and **changes from Year (−2) to Year (−1)**."

**→ 我們的 Delta 特徵設計有文獻支持！**

### 2. 支持機器學習優於傳統統計

- Ensemble (0.881) > XGBoost (0.877) > LR (0.859)
- 與我們的結果一致：ML 模型通常優於 LR

### 3. 作為 Related Work 的重要引用

這篇論文可以在論文中引用，說明：
- 縱向變化量特徵的有效性
- 機器學習在高血壓預測上的優勢

---

## 可借鏡之處

1. **CAVI 指標**：如果我們的資料集有動脈硬化指標，可以考慮加入
2. **Ensemble 方法**：可以嘗試多模型集成
3. **特徵重要性報告**：清楚呈現相對重要性百分比

---

## 局限性

1. **僅日本人群**：未驗證其他種族
2. **無外部驗證**：僅用 75/25 分割
3. **單一疾病**：僅預測高血壓
4. **無 SHAP**：只報告特徵重要性，無詳細可解釋性分析

---

## 關鍵字

hypertension prediction, machine learning, XGBoost, ensemble, longitudinal study, temporal features, delta change, Japanese population, CAVI

---

## 引用格式

```
Kanegae H, Suzuki K, Fukatani K, Ito T, Harada N, Kario K.
Highly precise risk prediction model for new-onset hypertension using artificial intelligence techniques.
J Clin Hypertens. 2020;22:445-450.
doi:10.1111/jch.13759
```

---

**相關文件**：
- [Taiwan_MJ_Hypertension_2024_深度解析.md](../reviews/Taiwan_MJ_Hypertension_2024_深度解析.md)（Meeting 18 論文，引用了本文）
- [Literature_Master_Index.md](../literature_notes/Literature_Master_Index.md)
- [Meeting_19_Notes.md](../../04_meetings/Meeting_19_Notes.md)
