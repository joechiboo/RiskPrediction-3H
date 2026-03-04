# Kanegae et al. (2020) J Clin Hypertension — AI 高血壓預測深度解析

> **論文**：Highly precise risk prediction model for new-onset hypertension using artificial intelligence techniques
> **期刊**：The Journal of Clinical Hypertension, 2020; 22(3): 445–450
> **作者**：Hiroshi Kanegae, Kenji Suzuki, Kyohei Fukatani, Tetsuya Ito, Nakahiro Harada, Kazuomi Kario
> **機構**：自治醫科大學 心血管內科（日本栃木）/ Genki Plaza 健診中心 / 日本健康促進基金會 / Fukuda Denshi
> **DOI**：[10.1111/jch.13759](https://doi.org/10.1111/jch.13759)
> **PDF**：[Kanegae_Hypertension_2020.pdf](../papers/Kanegae_Hypertension_2020.pdf)
> **與本研究關聯度**：⭐⭐⭐⭐⭐（Tier 1 — 縱向變化量特徵設計與本研究最相似）
> **先前筆記**：[Paper_Kanegae_Hypertension_2020.md](../summaries/Paper_Kanegae_Hypertension_2020.md)（2026-01-10 初版）

---

## 一句話摘要

**使用日本職場健檢 18,258 人資料，以 Year(-2)、Year(-1) 及兩年間變化量 (Δ) 建構 XGBoost/Ensemble 高血壓預測模型，Ensemble 驗證 AUC 0.881，證實「縱向 Δ 變化量特徵 + ML」是高精度預測路線。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **研究主題** | 新發高血壓風險預測 |
| **研究設計** | 回顧性世代研究（隨機 75/25 分割驗證） |
| **資料來源** | 日本健康促進基金會 — 職場年度健檢 |
| **時間範圍** | 2005–2016（11 年） |
| **樣本數** | 18,258 人（原始 21,758 人，排除後） |
| **新發高血壓** | 2,672 例（14.6%） |
| **Derivation set** | 75%，n=13,694 |
| **Validation set** | 25%，n=4,564 |
| **納入條件** | ≥3 年連續健檢、未服降壓藥、Year(-2) 及 Year(-1) BP<140/90 |
| **高血壓定義** | SBP/DBP ≥ 140/90 mmHg 或開始服降壓藥且自報高血壓 |

### 基線特徵（Year(-2)，n=18,258）

| 變項 | 數值 |
|------|------|
| 年齡 | 46.4 ± 12.1 歲 |
| 男性 | 44.6% |
| BMI | 22.3 ± 3.2 |
| 腰圍 | 79.1 ± 7.4 cm |
| 門診 SBP | 118.7 ± 11.2 mmHg |
| 門診 DBP | 70.0 ± 8.7 mmHg |
| CAVI | 7.5 ± 0.9 |
| CAVI 測量時 SBP | 116.1 ± 12.0 mmHg |
| HDL-C | 69.5 ± 18.1 mg/dL |
| LDL-C | 126.2 ± 26.7 mg/dL |
| 尿酸 | 5.0 ± 1.3 mg/dL |
| 空腹血糖 | 87.0 ± 11.8 mg/dL |
| 糖尿病 | 1.6% |
| CKD | 0.5% |
| 目前吸菸 | 17.2% |

---

## 核心方法論

### 特徵工程（最大創新）

```
時間軸：
Year(-2) → Year(-1) → Year(0)
   ↓          ↓          ↓
 特徵組1    特徵組2     預測目標
       \____Δ____/
       變化量特徵組3
```

| 步驟 | 說明 |
|------|------|
| **原始變數** | 65 個（來自健檢） |
| **時間展開** | Year(-2)×65 + Year(-1)×65 + Δ×65 + 交互項 = **244 個預測變數** |
| **缺失值處理** | 連續→均值插補；類別→眾數插補 |
| **偏態處理** | 對數轉換 |
| **缺少年份** | LOCF（Last Observation Carried Forward） |

### 模型

| 模型 | 組成 |
|------|------|
| **XGBoost** | 單一梯度提升決策樹 |
| **Ensemble** | Bagging 法結合 3 個子模型：正則化 LR + Random Forest + XGBoost |
| **Logistic Regression** | 傳統統計基準 |

---

## 主要結果

### 模型效能

| 模型 | Derivation AUC | Validation AUC | Precision (PPV) | Recall (TPR) |
|------|---------------|---------------|----------------|-------------|
| **Ensemble** | 0.992 | **0.881** | 0.635 | 0.253 |
| XGBoost | 0.976 | 0.877 | 0.601 | 0.317 |
| Logistic | 0.855 | 0.859 | 0.638 | 0.290 |

**觀察**：
- Ensemble 最高 AUC 但 Derivation-Validation gap 最大（0.992→0.881），**過擬合嚴重**
- XGBoost 同樣有明顯過擬合（0.976→0.877）
- LR 最穩定（0.855→0.859），幾乎無過擬合
- Recall 都偏低（0.25–0.32），表示**高精度但低召回率**

### Top 20 特徵重要性（XGBoost）

| 排名 | 特徵 | 相對重要性 |
|------|------|----------|
| 1 | **SBP at CAVI measurement, Year(-1)** | 100.0% |
| 2 | Clinic SBP, Year(-1) | 57.3% |
| 3 | DBP at CAVI measurement, Year(-1) | 47.8% |
| 4 | SBP at CAVI measurement, Year(-2) | 40.0% |
| 5 | Clinic SBP, Year(-2) | 26.4% |
| 6 | Clinic DBP, Year(-2) | 23.3% |
| 7 | DBP at CAVI measurement, Year(-2) | 23.2% |
| 8 | Clinic DBP, Year(-1) | 12.4% |
| 9 | BMI, Year(-1) | 10.6% |
| 10 | Age, Year(-2) | 10.3% |
| 11 | BMI, Year(-2) | 8.5% |
| 12 | Age, Year(-1) | 7.3% |
| 13 | CAVI, Year(-2) | 7.2% |
| 14 | Clinic SBP/SBP at CAVI, Year(-1) | 7.2% |
| 15 | Waist, Year(-1) | 7.0% |
| 16 | Triglycerides, Year(-2) | 6.7% |
| 17 | Clinic DBP/DBP at CAVI, Year(-1) | 6.6% |
| 18 | CAVI, Year(-1) | 6.6% |
| 19 | ALP, Year(-1) | 6.6% |
| 20 | Fasting glucose, Year(-2) | 6.1% |

**關鍵發現**：
- **前 8 名全是血壓相關**（門診 BP + CAVI 測量 BP）
- **仰臥 BP（CAVI 測量時）> 坐姿門診 BP** 作為預測因子
- 代謝因子（BMI、腰圍、TG、空腹血糖）排在 BP 之後
- **CAVI（動脈硬度指標）**獨立出現在 top 20

---

## 與本研究的深度比較

### 高度相似設計

| 面向 | Kanegae (2020) | 本研究 |
|------|---------------|------|
| **縱向時間結構** | Year(-2) → Year(-1) → Year(0) | T1 → T2 → T3 |
| **Δ 變化量特徵** | ✅ Changes from Year(-2) to Year(-1) | ✅ Delta1 = T2 − T1 |
| **健檢數值型特徵** | ✅ 血壓、BMI、血糖、血脂等 | ✅ 相同類型 |
| **正常人群追蹤** | ✅ 排除已有高血壓者 | ✅ 排除基線已有三高者 |
| **ML 模型** | XGBoost, Ensemble, LR | LR, NB, LDA, DT, RF, XGB, SVM, MLP |

### 關鍵差異

| 面向 | Kanegae (2020) | 本研究 | 本研究優勢 |
|------|---------------|------|---------|
| **預測疾病** | 僅高血壓 | 高血壓+高血糖+血脂異常 | 更全面 |
| **模型數量** | 3 | 8 + PySR | 更系統性比較 |
| **可解釋性** | 僅特徵重要性 | SHAP + PySR 符號回歸 | 更深入 |
| **不平衡處理** | 未處理（14.6%） | SMOTE | 更嚴謹 |
| **驗證方式** | 隨機 75/25 分割 | 交叉驗證 | — |
| **CAVI 指標** | ✅ 有（動脈硬度） | ❌ 無 | Kanegae 優勢 |
| **樣本量** | 18,258 | 6,056 | Kanegae 較大 |
| **人群** | 日本職場 | 中國杭州社區 | 不同亞洲人群 |

### 本研究可引用的論證

1. **Δ 特徵有效性的文獻支持**：Kanegae 是首批在高血壓預測中使用縱向變化量特徵的研究之一，證實此設計的價值
2. **ML > LR 的一致性**：Ensemble 0.881 > XGBoost 0.877 > LR 0.859，與文獻趨勢一致
3. **健檢數值型資料的可行性**：僅用健檢數值（非 EHR 全面資料）即可達 AUC 0.88
4. **血壓作為頂級預測因子**：與我們的 SHAP 分析一致

---

## 作者自引 Ye (2018) 的比較

Kanegae 在 Discussion 中直接引用 Ye et al. (2018)：

> "Ye et al used a ML algorithm (XGBoost) to construct and prospectively validated a risk prediction model... The model achieved predictive accuracy of 0.917 and 0.870... **Similar predictive performance values from our prediction model using the XGBoost were achieved** (0.976 and 0.876)... **This shows that our model based on variables at 2 years was better than the previous model based on variables at 1 year.**"

→ Kanegae 聲稱 2 年縱向資料 > 1 年橫斷面 EHR，支持縱向設計的價值

---

## 研究限制

1. **僅門診血壓**：無法識別白袍高血壓/隱匿性高血壓
2. **僅 2 年健檢資料**：時間窗口有限
3. **僅日本人群**：需在其他族群驗證
4. **過擬合明顯**：Ensemble derivation 0.992 vs validation 0.881（gap=0.111）
5. **Recall 偏低**：最佳模型也只有 0.253-0.317，漏診率高
6. **無類別不平衡處理**：14.6% 陽性率雖不算極端，但仍有偏
7. **無 SHAP 或其他可解釋性分析**：只報告特徵重要性排名
8. **工業資助**：Fukuda Denshi（CAVI 設備製造商）資助

---

## 對本論文寫作的引用建議

### 第二章（文獻回顧）
- 作為「縱向 Δ 變化量特徵 + ML」的先行研究引用
- 與 Ye (2018)、Wang (2024) 並列為高血壓 ML 預測的三個典範
- 強調 Kanegae 用健檢數值（非 EHR）即達 AUC 0.88

### 第七章（討論）
- 直接比較 AUC
- 討論 Δ 特徵的一致性（Kanegae 也發現 Year(-1) 比 Year(-2) 更重要）
- 指出本研究的額外貢獻：同時預測 3H、SHAP 可解釋性、SMOTE 不平衡處理
- 過擬合議題：Kanegae 也有此問題，可作為共同挑戰討論

---

## 關鍵引述

> "The prediction model for new-onset hypertension was constructed to predict an individual's hypertension risk at Year (0) based on variables at Year (−1), Year (−2), and **changes from Year (−2) to Year (−1)**."

> "SBP during CAVI measurement in the supine position at Year (−1) was the **strongest predictor** of future hypertension."

> "This shows that our model based on variables at 2 years was **better than the previous model** based on variables at 1 year."