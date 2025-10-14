## 📋 下一步任務

### Meeting 16 準備：Taiwan MTL (2025) 論文報告
- [ ] 下載 Taiwan MTL (2025) 論文
  - 標題：Multitask learning multimodal network for chronic disease prediction
  - 期刊：Scientific Reports (2025年5月)
  - 連結：https://www.nature.com/articles/s41598-025-99554-z
- [ ] 閱讀與分析論文
- [ ] 準備詳細解析文檔（參考 Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md 格式）
- [ ] 準備演講稿（10 頁版本）
- [ ] 重點關注：
  - Multi-Task Learning 架構與實作
  - 同時預測 4 種疾病（糖尿病、高血壓、心臟病、中風）
  - 疾病間相關性的建模方法
  - 與本研究（三高預測）的異同

### 研究方法論文檔已完成 ✅ (2025-01-14)
- [x] Cross_Validation.md - 交叉驗證方法
- [x] Marginal_Utility_in_Prediction.md - 記錄數的邊際效應
- [x] Feature_Selection_Marginal_Utility.md - 特徵數的邊際效應
- [x] Model_Comparison_Plan.md - 模型比較實驗計畫
- [x] Class_Imbalance_in_Medical_Prediction.md - 類別不平衡處理
- [x] Multi_Dataset_Validation.md - 雙資料集外部驗證

---

## 📝 今日進度記錄 (2025-01-14)

### 完成項目
- ✅ Meeting 討論與筆記整理
  - 確認 Liu et al. (2024) 作者為台中榮總醫學教育部與家庭醫學科
  - 確認 Synthea_SUA dataset 有 1,158 個案，每個案最少 2 次記錄
  - 排除 2 次記錄後剩 1,155 個案
  - 資料缺失值分析：UA 100%、TC 72%、FBG/Cr/GFR 69%、BMI 20%
- ✅ 新增 6 份研究方法概念文檔（共 2,974 行新增）
  1. Cross-Validation：K-Fold, Group K-Fold, Time Series Split
  2. Marginal_Utility_in_Prediction：時間序列記錄數的邊際效應實驗
  3. Feature_Selection_Marginal_Utility：特徵選擇的邊際效應實驗
  4. Model_Comparison_Plan：LR, RF, XGBoost, MLP, MTL, GA 模型比較計畫
  5. Class_Imbalance_in_Medical_Prediction：類別不平衡處理策略
  6. Multi_Dataset_Validation：SUA（中國）+ Synthea（加拿大）雙資料集驗證
- ✅ 確認下次 meeting 論文報告主題：Taiwan MTL (2025)
- ✅ Commit 並 push 至 GitHub (commit: 210eafe)

---

## 📝 過往進度記錄 (2025-10-09)

### 完成項目
- ✅ 新增兩篇相同資料集論文分析
  - Lin et al. (2024): 尿酸控制與高血壓風險
  - Guo et al. (2025): 尿酸與總膽固醇的性別差異
  - 兩篇使用相同中國東南部社區數據（2010-2018）
- ✅ 已 commit 並 push 至 GitHub (commit: 719cdf2) 
