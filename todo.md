## Meeting 14 教授提出的問題整理

### Q1. 台灣三高文獻回顧
**Status**: ✅ 已完成

**簡述**：
找到 10 篇台灣相關研究，包含單一疾病預測（高血壓、糖尿病）與多疾病同時預測。
重點發現 Taiwan MTL (2025) 使用 Multi-Task Learning 同時預測 4 種慢性病，與本研究高度相關。

**關鍵文件**：
- [docs/Q2_Taiwan_Literature_Review.md](docs/Q2_Taiwan_Literature_Review.md)
- [docs/references/README.md](docs/references/README.md)

---

### Q2. 預測規格、定義問題
**Status**: ✅ 已完成

**簡述**：
使用前兩次檢查（T₁, T₂）預測第三次（T₃）的三高風險。
多標籤二元分類，28 個特徵（含 Δ 變化量），按病患分割資料避免洩漏。
目標：AUC > 0.75, F1 > 0.65, Recall > 0.65

**關鍵文件**：
- [docs/Q1_Prediction_Problem_Definition.md](docs/Q1_Prediction_Problem_Definition.md)

---

### Q3. 資料集選擇與取得
**Status**: ✅ 已完成

**簡述**：
評估 HRS 後發現缺乏血液檢驗指標，不適用。
最終選擇 Synthea 合成資料（100,000 病患），包含完整三高相關指標，無隱私問題。
已規劃轉換腳本將 Synthea 轉為 SUA 格式。

**關鍵文件**：
- [docs/Synthea_Dataset_Summary.md](docs/Synthea_Dataset_Summary.md)
- [docs/Synthea_to_SUA_Format_Conversion.md](docs/Synthea_to_SUA_Format_Conversion.md)

---

## 📋 下一步任務

### Meeting 15 簡報準備
- [x] 完成簡報大綱（16 頁，20 分鐘）
- [ ] 製作 PowerPoint 簡報內容
- [ ] 準備 Taiwan MTL (2025) 論文重點摘要
- [ ] 準備視覺化素材（架構圖、表格）

**簡報檔案**：
- [docs/meeting_notes/meeting15_presentation_outline.md](docs/meeting_notes/meeting15_presentation_outline.md) 