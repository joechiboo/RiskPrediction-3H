# 📚 文檔導航索引

本目錄包含所有研究相關文檔，按類型組織。

---

## 📂 目錄結構總覽

```
docs/
├── guidelines/          # 🎓 論文格式規範
├── references/          # 📖 參考文獻 PDF 與翻譯
├── literature_notes/    # 📝 文獻筆記與深度解析
├── concepts/            # 💡 方法論概念
├── datasets/            # 🗂️ 資料集文檔
├── research_plans/      # 📋 研究計畫
├── analysis/            # 🔬 研究分析
├── meeting_notes/       # 📅 會議記錄
├── research_journey.md         # 📖 研究歷程
├── research_methodology_guide.md  # 🔍 研究方法論
└── work_journal.md      # 📝 工作日誌
```

---

## 🎓 論文格式規範 (guidelines/)

論文撰寫與格式相關文檔。

- [國立臺北教育大學學位論文格式規範.pdf](guidelines/國立臺北教育大學學位論文格式規範1110912.pdf)
- [論文封面套用檔.docx](guidelines/論文封面套用檔(WORD檔1121227).docx)
- [學位論文上傳與提交2024.pdf](guidelines/學位論文上傳與提交2024.pdf)
- [文獻閱讀報告格式檢查清單.md](guidelines/文獻閱讀報告格式檢查清單.md)

---

## 📖 參考文獻 (references/)

已下載的論文 PDF、中文翻譯與技術指南。

### 重要論文 PDF
- **Taiwan MTL (2025)**: [s41598-025-99554-z.pdf](references/s41598-025-99554-z.pdf)
  - DOI: 10.1038/s41598-025-99554-z
  - [中文翻譯](references/Taiwan_MTL_2025_中文翻譯.md)

- **Liu et al. (2024)**: [diagnostics-15-00072.pdf](references/diagnostics-15-00072.pdf)
  - DOI: 10.3390/diagnostics15010072

- **Hung et al. (2021)**: [fcvm-08-778306.pdf](references/fcvm-08-778306.pdf)
  - DOI: 10.3389/fcvm.2021.778306

- **Lin et al. (2024)**: [fendo-15-1343998.pdf](references/fendo-15-1343998.pdf)
  - DOI: 10.3389/fendo.2024.1343998

### 技術指南
- [Attention 機制應用指南](references/attention_mechanism_guide.md)

### 索引
- [參考文獻清單 README](references/README.md) - 完整論文清單與下載狀態

---

## 📝 文獻筆記 (literature_notes/)

文獻深度解析、系統性回顧與研究備忘錄。

### 核心文獻回顧
- **[系統性文獻回顧](literature_notes/Systematic_Literature_Review.md)** ⭐
  - 包含 16+ 篇論文摘要與分析
  - Taiwan MTL (2025) 列為 Entry #16

### 深度解析
- [Liu 2024 台中榮總糖尿病預測深度解析](literature_notes/Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md)
- [Liu 2024 演講稿 10 頁](literature_notes/Liu_2024_演講稿_10頁.md)
- [Liu 2024 演講稿精簡版](literature_notes/Liu_2024_演講稿_10頁_精簡版.md)

### 研究備忘錄
- [AUC 備忘錄](literature_notes/AUC_memo.md)
- [混淆矩陣指標](literature_notes/confusion_matrix_metrics.md)
- [文獻回顧方法論](literature_notes/literature_review_memo.md)

### 索引
- [文獻筆記 README](literature_notes/README.md)

---

## 💡 方法論概念 (concepts/)

研究方法、評估指標與技術概念說明。

### 評估指標
- [AUC-ROC 詳細說明](concepts/AUC-ROC_詳細說明.md)
- [混淆矩陣與臨床指標](literature_notes/confusion_matrix_metrics.md)

### 研究方法
- [交叉驗證](concepts/Cross_Validation.md)
- [特徵選擇與邊際效用](concepts/Feature_Selection_Marginal_Utility.md)
- [類別不平衡處理](concepts/Class_Imbalance_in_Medical_Prediction.md)
- [模型比較計畫](concepts/Model_Comparison_Plan.md)
- [多資料集驗證](concepts/Multi_Dataset_Validation.md)
- [邊際效用在預測中的應用](concepts/Marginal_Utility_in_Prediction.md)

### 其他工具
- [如何查詢 SCI 期刊](concepts/How_to_Check_SCI_Journal.md)

---

## 🗂️ 資料集文檔 (datasets/)

資料集相關文檔、下載指南與比較分析。

### HRS 資料集 (datasets/HRS/)
- [HRS 資料下載指南](datasets/HRS/HRS_data_download_guide.md)
- [HRS 變數參考](datasets/HRS/HRS_Variables_Reference.md)
- [HRS 資料轉換指南](datasets/HRS/HRS_data_conversion_guide.md)
- [HRS SUA 變數對應](datasets/HRS/HRS_SUA_Variable_Mapping.md)
- [HRS 生物標記分析更新](datasets/HRS/HRS_Biomarker_Analysis_Update.md)
- [HRS 資料限制備忘錄](datasets/HRS/HRS_Data_Limitation_Memo.md)

### Synthea 合成資料 (datasets/Synthea/)
- [Synthea 資料摘要](datasets/Synthea/Synthea_Dataset_Summary.md)
- [Synthea 轉 SUA 格式轉換](datasets/Synthea/Synthea_to_SUA_Format_Conversion.md)

### 資料集比較 (datasets/comparison/)
- [HRS vs NHANES 比較](datasets/comparison/HRS_vs_NHANES_Comparison.md)
- [資料集比較 - NHANES](datasets/comparison/dataset_comparison_NHANES.md)
- [縱貫性資料集選擇](datasets/comparison/longitudinal_datasets_for_3H.md)
- [資料集挑戰備忘錄](datasets/comparison/dataset_challenges_memo.md)
- [資料存取指南](datasets/comparison/Data_Access_Guide.md)

---

## 📋 研究計畫 (research_plans/)

研究問題定義、領域知識研究與文獻回顧計畫。

- [領域知識研究計畫](research_plans/domain_knowledge_research_plan.md)
  - 三高疾病的 6 大架構研究

- [Q1: 預測問題定義](research_plans/Q1_Prediction_Problem_Definition.md)
  - 研究問題、輸入輸出、評估指標

- [Q2: 台灣文獻回顧](research_plans/Q2_Taiwan_Literature_Review.md)
  - 台灣三高預測相關研究

---

## 🔬 研究分析 (analysis/)

研究問題深度分析與策略思考。

- [為何多因子預測重要](analysis/Why_Multifactor_Prediction_Matters.md)
  - 多疾病同時預測的價值分析

- [為何不延伸 Lin/Guo 研究](analysis/Why_Not_Extend_Lin_Guo_Studies.md)
  - 關聯研究 vs 預測模型的差異分析

---

## 📅 會議記錄 (meeting_notes/)

歷次 advisor meeting 記錄與簡報。

### 總結文檔
- **[Meeting 1-16 總結](meeting_notes/Meeting_Summary_1-16.md)** ⭐
  - 完整會議時間軸
  - 各次會議主題與重點
  - 論文清單與 DOI 索引

### Meeting 16 (Taiwan MTL 2025)
- [簡報檔](meeting_notes/meeting16_21138X006_紀伯喬_wVBA.pptm)
- [簡報大綱](meeting_notes/meeting16_taiwan_mtl_presentation_outline.md)
- [10 分鐘精簡版](meeting_notes/meeting16_taiwan_mtl_presentation_outline_10min.md)

### Meeting 15 (研究進度報告)
- [簡報檔](meeting_notes/meeting15_21138X006_紀伯喬_wVBA.pptm)
- [簡報大綱](meeting_notes/meeting15_presentation_outline.md)

### Meeting 01-14
- [meeting01-14 簡報檔](meeting_notes/)
- [Meeting 10 資料集記錄](meeting_notes/meeting10_Dataset.txt)
- [Meeting 05 文字記錄](meeting_notes/meeting05.docx)

### 其他會議記錄
- [Domain Knowledge 準備 (2025-01-08)](meeting_notes/2025-01-08_domain_knowledge_prep.md)

---

## 📖 研究歷程與工作日誌

### 研究歷程記錄
- **[research_journey.md](research_journey.md)** ⭐
  - 完整研究時間線 (Meeting 01-13)
  - 重大決策與轉折點
  - 領域知識架構
  - 研究進展追蹤

### 研究方法論
- **[research_methodology_guide.md](research_methodology_guide.md)**
  - 7 階段系統性研究流程
  - 論文撰寫順序
  - 時間規劃

### 工作日誌
- **[work_journal.md](work_journal.md)**
  - 日常工作記錄
  - 會議記錄連結
  - 進度追蹤

---

## 🔍 快速查找指南

### 想了解研究背景？
👉 [研究歷程記錄](research_journey.md)

### 想查看所有會議記錄？
👉 [Meeting 1-16 總結](meeting_notes/Meeting_Summary_1-16.md)

### 想查找論文文獻？
👉 [系統性文獻回顧](literature_notes/Systematic_Literature_Review.md)
👉 [參考文獻清單](references/README.md)

### 想了解資料集？
👉 [資料集文檔](datasets/)
👉 [HRS vs NHANES 比較](datasets/comparison/HRS_vs_NHANES_Comparison.md)

### 想了解研究方法？
👉 [研究方法論指南](research_methodology_guide.md)
👉 [方法論概念](concepts/)

### 想查看論文格式規範？
👉 [論文格式規範](guidelines/)

---

## 📌 重要連結

- 📊 [專案主 README](../README.md)
- 📋 [任務追蹤 (todo.md)](../todo.md)
- 🔬 [資料目錄](../data/)
- 💻 [程式碼目錄](../src/)

---

**最後更新**: 2025年
**維護者**: 紀伯喬
