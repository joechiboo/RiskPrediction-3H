# Meeting 總結記錄 (Meeting 1-16)

**專案名稱**: RiskPrediction-3H
**研究生**: 紀伯喬 (學號: 21138X006)
**指導教授**: 許揚教授
**研究主題**: 可解釋與黑盒模型在三高疾病預測上的實證比較

---

## 📅 Meeting 時間軸概覽

### Phase 1: 專案奠基期 (Meeting 01-03)
- **時間**: 2024年12月 - 2025年1月
- **主題**: 專案架構建立、領域知識研究
- **里程碑**: 完成專案初始化、確立研究方向

### Phase 2: 方法論設計期 (Meeting 04-06)
- **時間**: 2025年2-4月
- **主題**: 研究方法論建立、文獻回顧策略
- **里程碑**: 建立7階段系統性研究流程

### Phase 3: 實驗設計優化期 (Meeting 07-10)
- **時間**: 2025年5-7月
- **主題**: 資料集策略重大調整
- **里程碑**: 從單一資料集轉為多資料集比較驗證

### Phase 4: 模型實驗期 (Meeting 11-13)
- **時間**: 2025年8-9月
- **主題**: 模型比較與實驗執行
- **里程碑**: 完成初步模型實作與分析

### Phase 5: 文獻深度解析期 (Meeting 14-16)
- **時間**: 2025年下半年
- **主題**: 台灣文獻深度回顧、多任務學習研究
- **里程碑**: 系統性文獻回顧、Taiwan MTL論文分析

---

## 📝 各次 Meeting 詳細記錄

### Meeting 01 - 專案啟動
**檔案**: [meeting01_21138X006_紀伯喬.pptx](meeting01_21138X006_紀伯喬.pptx)

**主題**: 專案初始化與研究方向確立

**重點內容**:
- ✅ 確立研究主題：三高疾病風險預測
- ✅ 建立完整專案架構 (RiskPrediction-3H)
- ✅ 初始資料集：SUA_CVDs_risk_factors.csv (25,744筆)
- ✅ 設定 Git 版本控制系統

**關鍵決策**:
- 研究目標：比較可解釋 vs 黑盒模型
- 目標疾病：高血壓、高血糖、高血脂

**資料集來源**:
- DOI: [10.5061/dryad.z08kprrk1](https://datadryad.org/dataset/doi%3A10.5061/dryad.z08kprrk1)
- 描述：中國東南部社區調查數據（2010-2018）

---

### Meeting 02-03 - Domain Knowledge 深度研究
**檔案**:
- [meeting02_21138X006_紀伯喬_wVBA.pptm](meeting02_21138X006_紀伯喬_wVBA.pptm)
- [meeting03_21138X006_紀伯喬_wVBA.pptm](meeting03_21138X006_紀伯喬_wVBA.pptm)
- [2025-01-08_domain_knowledge_prep.md](2025-01-08_domain_knowledge_prep.md)

**主題**: 三高領域知識體系建立

**6大架構研究計畫**:
1. 基礎定義 & 臨床診斷標準
2. 三高的流行病學背景
3. 臨床與生理關聯
4. 資料來源與常見指標
5. 研究方法 & 應用場景
6. 爭議與研究空白

**專家諮詢**:
- 日期：2025/01/08（週三）
- 對象：醫師
- 目的：討論三高疾病的 domain knowledge

**關鍵洞察**:
- 了解診斷 cutoff 值是做任何標註/分類的基礎
- 高血壓：≥140/90 mmHg
- 高血糖：空腹血糖 ≥126 mg/dL, HbA1c ≥6.5%
- 高血脂：高 LDL-C, 高 TG, 低 HDL

---

### Meeting 04-06 - 研究方法論建立
**檔案**:
- [meeting04_21138X006_紀伯喬_wVBA.pptm](meeting04_21138X006_紀伯喬_wVBA.pptm)
- [meeting05_21138X006_紀伯喬_wVBA.pptm](meeting05_21138X006_紀伯喬_wVBA.pptm)
- [meeting05.docx](meeting05.docx)
- [meeting06_21138X006_紀伯喬_wVBA.pptm](meeting06_21138X006_紀伯喬_wVBA.pptm)

**主題**: 7階段系統性研究流程設計

**研究流程**:
1. **Literature Review** (2-4週)
2. **Research Question & Hypothesis** (1週)
3. **Data Collection & Understanding** (1-2週)
4. **Methodology Design** (1-2週)
5. **Experiments** (3-4週)
6. **Analysis & Results** (2-3週)
7. **Paper Writing** (4-6週)

**論文寫作順序**:
- Methods → Results → Discussion → Introduction → Abstract

**預估總研究時間**:
- 22週 (約5-6個月)

**關鍵學習**:
- 先規劃後執行，避免盲目實驗
- 系統性方法確保研究完整性

---

### Meeting 07-10 - 資料集策略重大調整
**檔案**:
- [meeting07_21138X006_紀伯喬_wVBA.pptm](meeting07_21138X006_紀伯喬_wVBA.pptm)
- [meeting08_21138X006_紀伯喬_wVBA.pptm](meeting08_21138X006_紀伯喬_wVBA.pptm)
- [meeting09_21138X006_紀伯喬_wVBA.pptm](meeting09_21138X006_紀伯喬_wVBA.pptm)
- [meeting10_21138X006_紀伯喬_wVBA.pptm](meeting10_21138X006_紀伯喬_wVBA.pptm)
- [meeting10_Dataset.txt](meeting10_Dataset.txt)

**主題**: 從單一資料集轉為多資料集比較驗證

**策略調整**:

**原始計畫**:
- 單一大型心血管資料集 (25,744筆)
- 專注三高疾病預測

**調整後策略**:
- 多個標準醫學資料集驗證
- 擴展到不同醫學預測任務
- 提升模型通用性驗證

**新增4個標準資料集**:

1. **Chronic Kidney Disease (CKD)**
   - 連結: https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease
   - 資料筆數：400
   - 類別：CKD / not CKD（不平衡比約 27:73）

2. **Fertility Diagnosis**
   - 連結: https://archive.ics.uci.edu/ml/datasets/Fertility
   - 資料筆數：100
   - 類別：N（正常）/ O（異常），不平衡比約 88:12

3. **Wisconsin Diagnostic Breast Cancer (WDBC)**
   - 連結: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
   - 資料筆數：569
   - 類別：Benign / Malignant（良性 / 惡性）

4. **BUPA Liver Disorders**
   - 連結: https://archive.ics.uci.edu/ml/datasets/liver+disorders
   - 資料筆數：345
   - 類別：有肝病 / 無肝病

**決策理由**:
1. 增強研究結論的廣泛適用性
2. 使用標準benchmark資料集便於比較
3. 避免單一資料集的特殊性限制
4. 提升論文發表競爭力

---

### Meeting 11-13 - 模型比較與實驗
**檔案**:
- [meeting11_21138X006_紀伯喬_wVBA.pptm](meeting11_21138X006_紀伯喬_wVBA.pptm)
- [meeting12_21138X006_紀伯喬_wVBA.pptm](meeting12_21138X006_紀伯喬_wVBA.pptm)
- [meeting13_21138X006_紀伯喬_wVBA.pptm](meeting13_21138X006_紀伯喬_wVBA.pptm)

**主題**: 模型實作與初步實驗

**實驗內容**:
- ✅ 模型實作與訓練
- ✅ 交叉驗證策略執行
- ✅ 效能指標分析：Accuracy, Precision, Recall, F1-score, ROC-AUC
- ✅ SHAP解釋性分析

**模型比較**:
- **可解釋模型**: Logistic Regression, Decision Tree
- **黑盒模型**: Random Forest, SVM, Neural Networks

**評估指標**:
- 主要：AUC-ROC, F1-Score, Recall
- 次要：Precision, Specificity, NPV/PPV

---

### Meeting 14 - 台灣文獻回顧策略
**檔案**: [meeting14_21138X006_紀伯喬_wVBA.pptm](meeting14_21138X006_紀伯喬_wVBA.pptm)

**主題**: 台灣三高文獻系統性回顧

**任務目標**:
- **Q1**: 完成台灣三高文獻回顧（找到 10 篇相關研究）
- **Q2**: 預測規格定義
- **Q3**: 資料集選擇

**文獻搜尋範圍**:
- 地區：台灣及華人地區
- 關鍵字：機器學習、高血壓、糖尿病、高血脂、代謝症候群
- 時間範圍：2010-2025

**文獻分類**:
- 單一疾病預測：6篇（高血壓 2篇、糖尿病 3篇、代謝症候群 3篇）
- **多疾病同時預測：3篇**（重點關注）

---

### Meeting 15 - 研究進度報告與預測規格定義
**檔案**:
- [meeting15_21138X006_紀伯喬_wVBA.pptm](meeting15_21138X006_紀伯喬_wVBA.pptm)
- [meeting15_presentation_outline.md](meeting15_presentation_outline.md)

**主題**: 三高風險預測研究進度報告（20分鐘，18頁）

**簡報結構**:

#### 第一部分：開場與目標回顧（2頁）
- Meeting 14 任務回顧
- 本次重點：多疾病同時預測

#### 第二部分：Q1 台灣三高文獻回顧（4頁）
- 文獻搜尋策略
- 🎯 **突破性發現**：Taiwan MTL (2025) - 同時預測4種疾病
- 其他多疾病預測研究
- 文獻回顧總結與 Benchmark

#### 第三部分：Q2 預測規格定義（5頁）
- 研究問題定義：使用前兩次健康檢查資料，預測第三次檢查的三高風險
- **輸入特徵設計**（28個特徵）：
  - T₁ 特徵（第一次檢查）
  - T₂ 特徵（第二次檢查）
  - Δ 變化量特徵
  - 時間特徵
- 輸出與診斷標準
- 評估指標
- 資料分割策略

#### 第四部分：Q3 資料集選擇（3頁）
- 資料集探索歷程：HRS 2016 → NHANES → Synthea
- Synthea 資料集特性
- 資料轉換與預處理

#### 第五部分：與文獻對比與研究優勢（2頁）
- 本研究 vs. 現有文獻
- 研究缺口（Research Gap）
- 下一步計劃與時程

**台灣研究性能基準**:
| 疾病 | AUC 範圍 | 準確率 |
|------|---------|--------|
| 高血壓 | 0.75-0.85 | - |
| 糖尿病 | 0.76-0.99 | 98-99% |
| 代謝症候群 | 0.90-0.93 | - |

**本研究目標**:
- AUC-ROC > 0.75
- F1-Score > 0.65
- Recall > 0.65

---

### Meeting 16 - Taiwan MTL (2025) 論文深度解析與未來研究方向
**檔案**:
- [meeting16_21138X006_紀伯喬_wVBA.pptm](meeting16_21138X006_紀伯喬_wVBA.pptm)
- [meeting16_taiwan_mtl_presentation_outline.md](meeting16_taiwan_mtl_presentation_outline.md)
- [meeting16_taiwan_mtl_presentation_outline_10min.md](meeting16_taiwan_mtl_presentation_outline_10min.md)

**主題**: Multitask learning multimodal network for chronic disease prediction

**論文資訊**:
- **標題**: Multitask learning multimodal network for chronic disease prediction
- **期刊**: Scientific Reports (2025年5月) - **SCI 期刊** (IF ~4.0, Q2)
- **作者**: Tsai et al. (台大資工系 × 長庚醫院 × 國家太空中心)
- **DOI**: [10.1038/s41598-025-99554-z](https://doi.org/10.1038/s41598-025-99554-z)
- **PDF位置**: [docs/references/s41598-025-99554-z.pdf](../references/s41598-025-99554-z.pdf)
- **中文翻譯**: [Taiwan_MTL_2025_中文翻譯.md](../references/Taiwan_MTL_2025_中文翻譯.md)

**Meeting 討論重點**:

#### 1. 多資料集交叉驗證策略 🔄
**研究問題**: 使用不同資料集驗證結論的可靠性

**現有資料集**:
- **中國東南部資料集** (2010-2018)
  - 樣本數: 25,744 筆
  - 完整特徵: 包含 11 項血液檢驗（含尿酸）
  - 優勢: 資料完整度高

- **加拿大 HRS 資料集**
  - 樣本數: 待確認
  - 特徵限制: ⚠️ 缺失值較多、無尿酸數據
  - 挑戰: 需評估預測準確度

**待解決問題**:
- 比較兩個資料集的預測性能差異
- 評估缺少尿酸特徵對模型的影響
- 確定哪個資料集更適合作為主要研究對象

#### 2. Meeting 17 準備：相似論文搜尋 📚
**搜尋目標**: 尋找與本研究高度相關的論文

**論文篩選條件**:
- **輸入特徵**: 血液檢驗數據（理想為 11 項指標）
- **輸出目標**: 三高風險預測（高血壓、高血糖、高血脂）
- **替代目標**: 心臟病 / 糖尿病預測
- **相似度要求**: 高度相關，可作為直接比較基準

**搜尋策略**:
- 關鍵字: blood test + cardiovascular risk / diabetes / hypertension
- 資料類型: 臨床血液檢驗數據
- 方法: 機器學習預測模型

#### 3. 實驗環境建置：Anaconda + Python 🐍
**決策**: 開始實際模型開發

**開發環境**:
- Python 環境管理: Anaconda
- 主要套件: scikit-learn, pandas, numpy

**實作計畫**:
1. 基礎模型實作（sklearn 支援）:
   - Logistic Regression (LR)
   - Random Forest (RF)
   - XGBoost
   - Decision Tree
   - Support Vector Machine (SVM)

2. 進階模型實作（需自行實現）:
   - **Genetic Programming (GP)** ⚠️
   - 挑戰: sklearn 無內建套件
   - 解決方案: 研究 GP 套件或自行實現

#### 4. 模型理論深入學習 📖
**重要提醒**: 必須深入理解所有模型的原理

**需熟悉的模型**:
1. **Logistic Regression (LR)**
   - 原理: 線性回歸 + Sigmoid 函數
   - 可解釋性: 高（係數直接對應特徵重要性）

2. **Random Forest (RF)**
   - 原理: 集成學習（Bagging + 決策樹）
   - 優勢: 減少過擬合、特徵重要性分析

3. **XGBoost**
   - 原理: 梯度提升樹（Gradient Boosting）
   - 優勢: 效能卓越、正則化、處理缺失值

4. **Decision Tree**
   - 原理: 遞迴分割（CART、ID3、C4.5）
   - 優勢: 高度可解釋

5. **Support Vector Machine (SVM)**
   - 原理: 最大間隔分類器 + 核函數
   - 優勢: 非線性決策邊界

6. **Genetic Programming (GP)**
   - 原理: 演化計算 + 符號回歸
   - 優勢: 自動特徵工程、可解釋性

**學習重點**:
- 理解數學原理與推導
- 掌握超參數調優策略
- 理解模型優缺點與適用場景

**簡報架構**（10分鐘精簡版）:

#### Slide 1-2: 研究動機
- **傳統問題**: 預測不同疾病需獨立模型 → 耗時耗資源
- **研究目標**: 使用 MTL 同時預測 4 種慢性病
  - 糖尿病 (22.4%)
  - 心臟病 (24.6%)
  - 中風 (8.7%)
  - 高血壓 (39.0%)

#### Slide 3: 資料與任務
- **預測任務**: 過去 10 年醫療紀錄 → 預測未來 5 年疾病風險
- **資料來源**: 台灣 HWDC（健康與福利資料科學中心）
  - 200萬人樣本
  - 最終：555,124 樣本
- **輸入特徵**:
  - 180 個 ICD codes（Word2Vec Embedding）
  - 個人資訊（年齡、性別、居住地、職業）

#### Slide 4: MTL 模型架構
- **核心創新**: Multi-Task Learning (MTL)
  - STL：4個獨立模型，4倍參數量
  - MTL：1個共享模型，僅需 1/4 參數
- **模型組成**:
  - ICD Embedding (Word2Vec)
  - ICD Extraction Module (LSTM 最佳)
  - Hard Parameter Sharing
  - 4個獨立預測層

#### Slide 5-6: 效能與參數效率
**MTL vs STL（MAND-LSTM）**:
| 疾病 | STL AUC | MTL AUC |
|------|---------|---------|
| 高血壓 | 0.9346 | 0.9346 |
| 糖尿病 | 0.8926 | 0.8912 |
| 心臟病 | 0.8774 | 0.8787 ✨ |
| 中風 | 0.8700 | 0.8625 |

**參數效率**:
- 4個 STL：1,608,468 參數
- 1個 MTL：419,784 參數 ⭐（僅需 1/4）

#### Slide 7-8: 特徵重要性與風險因子
**個人資訊重要性**:
- **年齡** → AUC 下降最多（-0.054）⭐
- 性別、居住地區：次要影響

**Attention Score 分析**（前2000高風險患者）:
1. **可修改因子**: 高血脂 (272.0, 272.2, 272.4)
2. **多重慢性病**: 痛風、白內障、慢性肝炎、腎衰竭
3. **新興因子**: 焦慮症、憂鬱症

#### Slide 9: 研究貢獻
**5大貢獻**:
1. ✅ 證明 MTL 可同時預測多種慢性病
2. ✅ Word2Vec Embedding 有效捕捉疾病關聯
3. ✅ 參數效率：1/4 參數達相同效能
4. ✅ 高可解釋性：風險因子符合文獻
5. ✅ 高穩健性：60% 紀錄遮蔽仍維持效能

**與本研究關聯**:
- Taiwan MTL：4 種疾病（糖尿病、高血壓、心臟病、中風）
- 本研究：3 種疾病（高血壓、高血糖、高血脂）
- 可參考：ICD embedding + Attention 機制

#### Slide 10: 限制與啟發
**研究限制**:
- ⚠️ 資料不平衡 → 中風 FNR 高
- ⚠️ 依賴 10 年完整醫療紀錄
- ⚠️ Balanced Accuracy 60-80%（適合輔助診斷）

**對本研究的啟發**:
1. 可考慮 MTL 框架
2. 使用 Word2Vec 處理疾病代碼
3. Attention 機制提升可解釋性

**相關文檔**:
- [Attention 機制應用指南](../references/attention_mechanism_guide.md)
- [系統性文獻回顧](../literature_notes/Systematic_Literature_Review.md)（Taiwan MTL 列為 Entry #16）

---

## 📊 重要論文與 DOI 清單

### 主要研究論文（已讀）

#### 1. Taiwan MTL (2025) - 多任務學習預測慢性病 ⭐⭐⭐⭐⭐
- **DOI**: [10.1038/s41598-025-99554-z](https://doi.org/10.1038/s41598-025-99554-z)
- **期刊**: Scientific Reports (SCI, IF ~4.0)
- **檔案**: [s41598-025-99554-z.pdf](../references/s41598-025-99554-z.pdf)
- **報告**: Meeting 16
- **重要性**: 與本研究高度相關，多疾病同時預測

#### 2. Liu et al. (2024) - 台灣糖尿病 10 年預測 ⭐⭐⭐⭐⭐
- **DOI**: [10.3390/diagnostics15010072](https://doi.org/10.3390/diagnostics15010072)
- **期刊**: Diagnostics, 15(1), 72
- **檔案**: [diagnostics-15-00072.pdf](../references/diagnostics-15-00072.pdf)
- **報告**: Meeting 14-15（下次預告）
- **重要性**: 台灣第一個 EHR + ML 糖尿病預測，10年追蹤，準確率99%
- **深度解析**: [Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md](../literature_notes/Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md)

#### 3. Hung et al. (2021) - 台灣高血壓預測 ⭐⭐⭐⭐⭐
- **DOI**: [10.3389/fcvm.2021.778306](https://doi.org/10.3389/fcvm.2021.778306)
- **期刊**: Frontiers in Cardiovascular Medicine, 8:778306
- **檔案**: [fcvm-08-778306.pdf](../references/fcvm-08-778306.pdf)
- **報告**: Meeting 14-15（下次預告）
- **重要性**: 台灣多中心研究，完整的 ML pipeline 與外部驗證

#### 4. Lin et al. (2024) - 尿酸控制與高血壓風險 ⚠️ 關聯研究（非預測模型）
- **DOI**: [10.3389/fendo.2024.1343998](https://doi.org/10.3389/fendo.2024.1343998)
- **期刊**: Frontiers in Endocrinology
- **檔案**: [fendo-15-1343998.pdf](../references/fendo-15-1343998.pdf)
- **資料來源**: 中國東南部社區調查（2010-2018）- **與本研究使用相同 Dataset**
- **研究類型**: 關聯研究（Association Study），非預測模型（Prediction Model）
- **分析文檔**: [Why_Not_Extend_Lin_Guo_Studies.md](../Why_Not_Extend_Lin_Guo_Studies.md)

#### 5. Guo et al. (2025) - 尿酸與總膽固醇的劑量反應關係
- **DOI**: [10.1177/03000605251318203](https://doi.org/10.1177/03000605251318203)
- **期刊**: Journal of International Medical Research, 53(2), 1–15
- **檔案**: [guo-et-al-2025-the-dose-response-relationship...pdf](../references/)
- **資料來源**: 中國東南部社區調查（2010-2018）- **與 Lin et al. 相同數據集**
- **研究類型**: 橫斷面研究
- **樣本數**: 6,119 位成人

### 待研究論文

#### DHDIP (2022) - 高血壓與高血脂聯合預測
- **期刊**: Computer Methods and Programs in Biomedicine
- **預測目標**: 同時預測高血壓和高血脂
- **特色**: Multi-objective learning + 高可解釋性

#### Multi-Disease Prediction (2010) - 共同風險因子
- **期刊**: Expert Systems with Applications
- **預測目標**: 同時預測高血壓和高血脂
- **方法**: 兩階段多疾病預測（共同風險因子分析）

---

## 🎯 研究進展總結

### ✅ 已完成項目
- [x] 專案架構建立與版本控制
- [x] 6大領域知識架構研究
- [x] 7階段研究方法論設計
- [x] 多資料集選擇與文檔化（5個資料集）
- [x] 16次正式 advisor meeting
- [x] 臨床專家諮詢與驗證（2025/01/08）
- [x] 系統性文獻回顧（16+ 篇論文）
- [x] Taiwan MTL (2025) 深度解析

### 🔄 進行中項目
- [ ] Literature Review 深化（Stage 1/7）
- [ ] 模型實驗與比較分析
- [ ] SHAP 解釋性分析
- [ ] 統計顯著性檢驗

### 📋 待執行項目
- [ ] Research Question 具體化（Stage 2）
- [ ] 資料探索與前處理（Stage 3）
- [ ] 完整實驗執行（Stage 5）
- [ ] 結果分析與討論（Stage 6）
- [ ] 論文撰寫（Stage 7）

---

## 📚 關鍵文檔索引

### Meeting 記錄
- [Meeting 01-16 簡報](.) - 所有 .pptx / .pptm 檔案
- [Meeting 15 簡報大綱](meeting15_presentation_outline.md)
- [Meeting 16 簡報大綱（10分鐘）](meeting16_taiwan_mtl_presentation_outline_10min.md)
- [Domain Knowledge 準備](2025-01-08_domain_knowledge_prep.md)

### 文獻回顧
- [系統性文獻回顧](../literature_notes/Systematic_Literature_Review.md) - 16+ 篇論文
- [Liu 2024 深度解析](../literature_notes/Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md)
- [Taiwan MTL 中文翻譯](../references/Taiwan_MTL_2025_中文翻譯.md)
- [參考文獻清單](../references/README.md)

### 方法論與概念
- [研究方法論指南](../research_methodology_guide.md)
- [AUC-ROC 詳細說明](../concepts/AUC-ROC_詳細說明.md)
- [交叉驗證](../concepts/Cross_Validation.md)
- [類別不平衡處理](../concepts/Class_Imbalance_in_Medical_Prediction.md)
- [Attention 機制應用指南](../references/attention_mechanism_guide.md)

### 研究分析
- [為何不延伸 Lin/Guo 研究](../Why_Not_Extend_Lin_Guo_Studies.md)
- [為何多因子預測重要](../Why_Multifactor_Prediction_Matters.md)

### 進度追蹤
- [工作日誌](../work_journal.md)
- [研究歷程](../research_journey.md)

---

## 💡 關鍵洞察與學習

### 成功經驗
1. **系統性方法**: 6大領域知識架構 + 7階段研究流程確保完整性
2. **專家諮詢**: 臨床醫師參與提升研究品質
3. **文檔管理**: 完整版本控制與進度追蹤
4. **持續溝通**: 定期 advisor meeting 確保方向正確

### 重大轉折點
1. **Meeting 10**: 從單一資料集轉為多資料集驗證策略
2. **Meeting 15**: 發現 Taiwan MTL 多疾病預測研究
3. **Meeting 16**: 深度解析 MTL 架構，為本研究找到新方向

### 研究創新點
1. **縱向時序預測**: T₁→T₂→T₃ 的動態變化（Δ 特徵）
2. **多標籤同時預測**: 三高綜合評估
3. **可解釋性權衡**: 準確性 vs 可解釋性的實證比較
4. **多資料集驗證**: 提升模型通用性

---

**文檔建立日期**: 2025年（基於 Meeting 1-16 記錄彙整）
**最後更新**: 2025年
**下一次 Meeting**: 待定

---

## 📌 快速導航

- 📂 [返回 Meeting Notes 目錄](.)
- 📖 [查看系統性文獻回顧](../literature_notes/Systematic_Literature_Review.md)
- 📊 [查看研究歷程](../research_journey.md)
- 🎯 [查看專案 README](../../README.md)
