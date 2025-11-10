## 📋 下一步任務

### ✅ Meeting 16 完成：Taiwan MTL (2025) 論文報告
- [x] 下載 Taiwan MTL (2025) 論文
  - 標題：Multitask learning multimodal network for chronic disease prediction
  - 期刊：Scientific Reports (2025年5月)
  - 連結：https://www.nature.com/articles/s41598-025-99554-z
  - DOI: 10.1038/s41598-025-99554-z
- [x] 閱讀與分析論文
- [x] 準備詳細解析文檔（Taiwan_MTL_2025_中文翻譯.md）
- [x] 準備演講稿（10 分鐘版本）
- [x] 重點關注：
  - Multi-Task Learning 架構與實作 ✅
  - 同時預測 4 種疾病（糖尿病、高血壓、心臟病、中風）✅
  - 疾病間相關性的建模方法 ✅
  - 與本研究（三高預測）的異同 ✅

### 📝 Meeting 記錄整理
- [x] 建立 Meeting 1-16 總結文檔
  - 檔案：[Meeting_Summary_1-16.md](docs/meeting_notes/Meeting_Summary_1-16.md)
  - 包含：題目、檔案、DOI 位置、重點總結
  - 方便快速比對與參考

### 🎯 下一步研究方向

#### 📚 文獻閱讀 - 第一階段：台灣研究（優先）

**已讀完**：
- [x] Taiwan MTL (2025) - 4種慢性病 MTL 預測 ✅

**待讀**：
- [ ] **Liu et al. (2024)** - 台灣糖尿病 10 年預測
  - 標題：Use of Machine Learning to Predict the Incidence of Type 2 Diabetes
  - 期刊：Diagnostics, 15(1), 72
  - DOI: 10.3390/diagnostics15010072
  - 已有深度解析文檔
  - 重點：10年縱向追蹤、99% 準確率

- [ ] **Hung et al. (2021)** - 台灣高血壓預測
  - 標題：Prediction of Masked Hypertension Using Machine Learning
  - 期刊：Frontiers in Cardiovascular Medicine
  - DOI: 10.3389/fcvm.2021.778306
  - 重點：多中心研究、外部驗證、SMOTE

#### 📚 文獻閱讀 - 第二階段：多疾病預測方法

- [ ] **DHDIP (2022)** - 高血壓與高血脂聯合預測
  - 標題：DHDIP: An interpretable model for hypertension and hyperlipidemia prediction based on EMR data
  - 期刊：Computer Methods and Programs in Biomedicine
  - 連結：https://www.sciencedirect.com/science/article/abs/pii/S0169260722004692
  - 重點：Multi-objective learning + 高可解釋性

- [ ] **Multi-Disease Prediction (2010)** - 高血壓與高血脂共同風險因子
  - 標題：Using data mining techniques for multi-diseases prediction modeling of hypertension and hyperlipidemia by common risk factors
  - 期刊：Expert Systems with Applications
  - 連結：https://www.sciencedirect.com/science/article/abs/pii/S0957417410012303
  - 重點：兩階段方法（個別風險因子 → 共同風險因子）

#### 📚 文獻閱讀 - 第三階段：Related Work 追蹤

閱讀完台灣研究後，追蹤以下方向：

- [ ] **Liu 2024 的 Related Work**
  - 追蹤 References 中的糖尿病預測研究
  - 特別關注：縱向研究 + ML 方法

- [ ] **Hung 2021 的 Related Work**
  - 追蹤 References 中的高血壓預測研究
  - 特別關注：SMOTE、外部驗證方法

- [ ] **Taiwan MTL 2025 的 Related Work**
  - 追蹤 References 中的 MTL 架構論文
  - 特別關注：Attention mechanism、ICD embedding

- [ ] **Google Scholar 引用追蹤**
  - 查看「被這些論文引用」的最新研究（2024-2025）
  - 查看「這些論文引用」的經典研究

#### 🔬 技術研究與實作
- [ ] 開始實作 Multi-Task Learning 框架（參考 Taiwan MTL）
- [ ] 研究 Attention 機制在三高預測中的應用
- [ ] 設計 HRS 資料的 Feature Embedding 策略

#### 📊 下次 Meeting 準備
- [ ] 準備 Liu 2024 糖尿病預測論文報告（已有深度解析）
