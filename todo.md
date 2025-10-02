## Meeting 14 教授提出的問題整理

### Q1. 台灣三高文獻回顧
找看看有沒有類似議題的三高預測，要**台灣的**
**Status**: ✅ 已完成
**文件**: [docs/Q2_Taiwan_Literature_Review.md](docs/Q2_Taiwan_Literature_Review.md)
**重點發現**:
- 找到 10 篇台灣相關研究（高血壓、糖尿病、代謝症候群）
- 🎯 發現 3 篇**多疾病同時預測**研究，其中 Taiwan MTL (2025) 極度相關
- 已下載 2 篇重點論文：Liu et al. 2024 (糖尿病)、Hung et al. 2021 (高血壓)
- 詳見：[docs/references/README.md](docs/references/README.md)

---

### Q2. 預測規格、定義問題
**Inputs**: 前兩次的檢查結果（T₁, T₂ 的生理測量、血液檢驗、診斷狀態 + 變化量特徵）
**Outputs**: 第三次（T₃）的三高風險（多標籤二元分類：高血壓/高血糖/高血脂 Yes/No）
**Status**: ✅ 已完成回應
**文件**: [docs/Q1_Prediction_Problem_Definition.md](docs/Q1_Prediction_Problem_Definition.md)

📋 簡單來說，「預測規格、定義問題」就是要你說清楚：
1️⃣ 你要預測什麼？
→ 預測第三次檢查時會不會得三高（高血壓/高血糖/高血脂）
2️⃣ 用什麼資料來預測？
→ 前兩次的檢查數據（血壓、血糖、血脂、BMI 等 28 個特徵）
3️⃣ 預測結果長什麼樣？
→ 三個 Yes/No（或 0-1 的機率值）
4️⃣ 怎麼知道預測得好不好？
→ 用 AUC-ROC, F1-Score, Recall 等指標衡量

**重點摘要**：
- 問題類型：多標籤二元分類（同時預測三種疾病）
- 特徵數：約 28 個（T₁ + T₂ + Δ變化量 + 時間間隔）
- 評估指標：AUC-ROC > 0.75, F1-Score > 0.65, Recall > 0.65
- 資料分割：按病患分割（避免資料洩漏）
- 可用樣本：1,155 位病患有 3+ 次記錄，約可產生 10,000+ 訓練樣本

---

### Q3. 資料集選擇與取得
上次 HPS 2016 好像有血液檢驗的資料，繼續 dig 看看結果
改用 Synthea 資料（更容易取得）
**Status**: ✅ 已完成
**文件**:
- [docs/Synthea_Dataset_Summary.md](docs/Synthea_Dataset_Summary.md)
- [docs/Synthea_to_SUA_Format_Conversion.md](docs/Synthea_to_SUA_Format_Conversion.md)

---

## 📝 備忘錄重點總結

🚨 **關鍵問題**

HRS 缺乏所有血液檢驗指標（血糖、膽固醇、肌酸酐、尿酸），這對三高風險預測研究造成致命限制。

💡 **主要建議**

轉換至 NHANES 資料集 - 包含完整血液檢測且公開可取得。

📂 **檔案位置**

[docs/HRS_Data_Limitation_Memo.md](docs/HRS_Data_Limitation_Memo.md)

這份備忘錄記錄了詳細的分析過程、限制評估和替代方案，可作為研究決策的重要參考文件。雖然 HRS 分析沒有達到預期目標，但這個探索過程本身很有價值，避免了後續更大的時間投入！