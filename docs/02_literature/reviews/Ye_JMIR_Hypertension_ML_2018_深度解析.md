# Ye et al. (2018) JMIR — EHR + ML 高血壓預測深度解析

> **論文**：Prediction of Incident Hypertension Within the Next Year: Prospective Study Using Statewide Electronic Health Records and Machine Learning
> **期刊**：Journal of Medical Internet Research, 2018; 20(1): e22
> **作者**：Chengyin Ye, Tianyun Fu, Shiying Hao, Yan Zhang, Oliver Wang, Bo Jin, Minjie Xia, Modi Liu, Xin Zhou, Qian Wu, Yanting Guo, Chunqing Zhu, Yu-Ming Li, Devore S Culver, Shaun T Alfreds, Frank Stearns, Karl G Sylvester, Eric Widen, Doff McElhinney, Xuefeng Ling
> **機構**：杭州師範大學 / Stanford University / HBI Solutions Inc / HealthInfoNet (Maine)
> **DOI**：[10.2196/jmir.9268](https://doi.org/10.2196/jmir.9268)
> **PDF**：[Ye_JMIR_Hypertension_ML_2018.pdf](../papers/Ye_JMIR_Hypertension_ML_2018.pdf)
> **與本研究關聯度**：⭐⭐⭐⭐⭐（Tier 1 核心論文）

---

## 一句話摘要

**利用美國緬因州 150 萬人全州 EHR 資料 + XGBoost，建構 1 年新發高血壓風險預測模型，前瞻驗證 AUC 達 0.870，並揭示多重慢性病、精神疾病用藥及社經因素為重要預測因子。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **研究主題** | 1 年新發原發性高血壓風險預測 |
| **研究設計** | 回顧性建模 + 前瞻性驗證（時間分割） |
| **資料來源** | Maine Health Information Exchange (HIE) — 全州 EHR |
| **涵蓋機構** | 35 家醫院 + 34 個聯邦社區健康中心 + 400+ 門診 |
| **覆蓋率** | ~95% 緬因州人口 |
| **回顧世代** | N=823,627（2013 年 EHR → 2014 年結局） |
| **前瞻世代** | N=680,810（2014 年 EHR → 2015 年結局） |
| **新發高血壓數** | 回顧 92,512（11.23%）；前瞻 60,065（8.82%） |
| **排除條件** | 繼發性/妊娠高血壓、已有高血壓診斷 |
| **高血壓定義** | ICD-9-CM 401 / ICD-10-CM I10（原發性高血壓） |
| **模型** | XGBoost（唯一模型） |
| **評估指標** | AUC、PPV、sensitivity、specificity、HR |

---

## 方法論詳解

### 特徵工程

| 階段 | 說明 |
|------|------|
| **原始特徵池** | >15,000 個特徵（來自 EHR + 社經資料） |
| **特徵類別** | 人口學、實驗室、診斷(ICD)、處方(NDC)、臨床利用、社經(Census/USDA) |
| **缺失值處理** | KNN 插補（K近鄰，基於歐氏距離） |
| **單變量篩選** | Cochran-Mantel-Haenszel（二元）、Cochran-Armitage（序數）、單變量 LR（連續）；P≤.05 |
| **篩選後** | 798/15,280 特徵存活 |
| **XGBoost 最終選用** | 169 個特徵 |

### 169 特徵組成

| 類別 | 數量 |
|------|------|
| 人口學 | 2（年齡、性別） |
| 社經特徵 | 14 |
| 診斷疾病 | 30 |
| 實驗室檢查 | 6 |
| 處方用藥 | 98 |
| 臨床利用指標 | 19 |

### XGBoost 設定

- 樹深度：5
- 樹數量 K=500
- 損失函數：可微凸損失 + 正則化項 Ω
- 分裂策略：近似貪婪演算法（百分位數分布）
- 校準：預測值 ŷ → PPV 映射

---

## 主要結果

### 模型效能

| 指標 | 回顧世代 | 前瞻世代 |
|------|---------|---------|
| **AUC** | 0.917 | **0.870** |

### 風險分層（前瞻世代）

| 風險分類 | 分數範圍 | 人數 | 實際發生率 |
|---------|---------|------|----------|
| Very Low | 0–0.05 | 381,544 | 1.19%（4,526） |
| Low | 0.05–0.1 | 104,565 | — |
| Medium | 0.1–0.2 | 99,415 | — |
| High | 0.2–0.4 | 53,957 | — |
| Very High | >0.4 | 41,329 | **50.93%**（21,050） |

- Very High vs Very Low 的 HR = **60.8**（95% CI 58.8–62.8）
- 確診者中 35.04% 被正確分入 Very High，僅 7.54% 被錯分為 Very Low

### 關鍵預測因子

**疾病診斷**（OR 最大者）：
- 前高血壓 (Prehypertension)：OR > 3.0
- 第二型糖尿病：OR > 3.0
- 心血管疾病（心衰、動脈硬化、冠心病、MI 合併）：OR > 3.0
- 特發性嗜睡症 (Idiopathic Hypersomnia)：OR > 3.0

**用藥**：CVD、糖尿病、血脂藥 + **18 種精神科用藥**（抗憂鬱、抗焦慮、抗精神病）

**臨床利用**：住院次數、門診次數、過去一年醫療費用、處方數、檢驗數

**社經因素**：
- 正相關（↑風險）：雜貨店/便利商店密度、農夫市集比率、Medicaid/Medicare 覆蓋率、低教育人口比率
- 負相關（↓風險）：家戶所得中位數、高教育人口比率、居住地離公園近、私人保險覆蓋率

### 精神疾病與高血壓的特殊發現

- Very High Risk 中：22.21% 有憂鬱用藥、13.40% 有焦慮用藥、2.71% 有精神分裂用藥
- **無其他慢性病但有憂鬱**的 ≥65 歲老人：1 年高血壓風險 HR = **2.0**（95% CI 1.9–2.0）
- 約 32.17% 的此類老人會在 1 年內發展為高血壓

---

## 與本研究的比較

| 面向 | Ye (2018) | 本研究 |
|------|-----------|------|
| **資料來源** | 美國 Maine 全州 EHR | 中國杭州健檢資料 (Luo 2024 Dryad) |
| **樣本量** | 823K / 680K | 6,056 |
| **特徵數** | 169（從 15K 篩選） | ~20 健檢指標 |
| **特徵類型** | EHR 全面（診斷+處方+社經） | 健檢數值（生化+體測） |
| **模型** | XGBoost 單一模型 | 8 模型比較 + PySR |
| **目標** | 高血壓（1 年新發） | 高血壓 + 高血糖 + 血脂異常（3H） |
| **高血壓定義** | ICD 診斷碼 | SBP≥140 或 DBP≥90 (JNC 8) |
| **驗證方式** | 時間分割前瞻驗證 | 交叉驗證 |
| **AUC** | 0.870（前瞻） | 待比較 |
| **類別不平衡** | 未特別處理（11.23% 發生率） | SMOTE |
| **可解釋性** | OR + 特徵重要性 | SHAP + PySR 符號回歸 |

### 本研究可借鑑之處

1. **風險分層設計**：將 risk score 分為 5 級（Very Low → Very High），非常適合臨床應用，本研究可參考
2. **PPV 校準方法**：將 XGBoost 預測值映射至 PPV，比直接用機率值更具臨床意義
3. **社經因素的重要性**：本研究缺少社經資料，此為一個明確的 limitation
4. **精神疾病作為預測因子**：本研究無法納入此面向（健檢資料無精神科診斷/用藥）
5. **多重慢性病共病模式**：Very High Risk 中 98.44% 有其他慢性病，支持本研究同時預測 3H 的理論基礎

### 本研究的相對優勢

1. **縱貫追蹤設計**：本研究使用 2010-2018 多次健檢，可捕捉 Δ 變化量；Ye 僅用 1 年橫斷面 EHR
2. **同時預測 3H**：Ye 只預測高血壓；本研究預測高血壓+高血糖+血脂異常
3. **多模型比較**：Ye 只用 XGBoost；本研究比較 8 種模型的適用性
4. **符號回歸**：PySR 提供可解讀公式，Ye 缺乏此面向
5. **SMOTE 處理不平衡**：Ye 未處理類別不平衡（發生率 11.23%，相對不嚴重）

---

## 研究限制（作者自述）

1. **KNN 插補限制**：缺失值過多的病人可能插補不準
2. **EHR 漏診**：部分高血壓患者可能未被記錄（低估盛行率）
3. **ICD-10 轉換問題**：ICD-10 (65K codes) → ICD-9 (13K codes) 映射可能不完全
4. **精神科診斷被遮蔽**：只能用處方藥作為代理變量
5. **社經因素為社區層級**：非個人層級，精確度有限
6. **種族單一**：94.88% 為白人，對其他族裔的泛化能力存疑
7. **缺少生活方式資料**：飲食、運動等無法從結構化 EHR 擷取

---

## 對本論文寫作的引用建議

### 第二章（文獻回顧）
- 作為 EHR + ML 預測高血壓的代表性研究引用
- 強調其大規模前瞻驗證（N=680K）AUC 0.870 的結果
- 與 Kanegae (2020) 對比：Ye 用 EHR 診斷碼，Kanegae 用健檢數值

### 第七章（討論）
- 比較 AUC：Ye 0.870 vs 本研究結果
- 討論資料維度差異：Ye 有 169 特徵（含社經+處方），本研究 ~20 特徵但有縱貫追蹤
- 精神疾病 & 社經因素作為本研究的 limitation 討論材料
- 多重慢性病共病支持本研究 3H 同時預測的合理性

---

## 關鍵引述

> "Type 2 diabetes, lipid disorders, CVDs, mental illness, clinical utilization indicators, and socioeconomic determinants were recognized as driving or associated features of incident essential hypertension."

> "In the subgroup of patients without other chronic physical conditions, we found that depression was associated with a two-fold hypertension risk (HR: 2.0 [95% CI 1.9-2.0])."

> "XGBoost provided a more accurate prediction model (AUC of 0.87 in the prospective cohort) than prior models... by capturing previously ignored but potentially powerful predictors."