# Raw Data Directory

本資料夾存放原始資料集，**資料檔案不會上傳到 Git**（已在 .gitignore 中排除）。

## 📥 資料下載指引

### Synthea Synthetic Patient Data（目前使用）

我們使用 Synthea 合成病患資料進行三高風險預測研究。

#### 資料來源
- **官方網站**: https://synthea.mitre.org/
- **下載頁面**: https://synthea.mitre.org/downloads
- **授權**: CC-BY-NC 4.0

#### 下載步驟

1. **前往下載頁面**
   ```
   https://synthea.mitre.org/downloads
   ```

2. **選擇以下檔案下載**：

   **方案 A：100 筆樣本（快速測試用）**
   - 檔案：`100 Sample Synthetic Patient Records, CSV` (7 MB)
   - 解壓縮到：`data/raw/synthea_sample_data/`

   **方案 B：1000 筆樣本（推薦用於研究）** ⭐
   - 檔案：`1K Sample Synthetic Patient Records, CSV` (9 MB)
   - 解壓縮到：`data/raw/1000_synthea_sample_data/`

3. **資料夾結構**
   ```
   data/raw/
   ├── README.md (本檔案)
   ├── synthea_sample_data/          # 100 筆樣本（可選）
   │   ├── patients.csv
   │   ├── observations.csv
   │   ├── conditions.csv
   │   ├── encounters.csv
   │   ├── medications.csv
   │   └── ...
   └── 1000_synthea_sample_data/     # 1000 筆樣本（推薦）
       ├── patients.csv
       ├── observations.csv
       ├── conditions.csv
       ├── encounters.csv
       ├── medications.csv
       └── ...
   ```

#### 資料規模（1000 筆樣本）

| 項目 | 數量 |
|------|------|
| 病患數 | 1,163 人 |
| 觀察記錄 | 531,144 筆 |
| 診斷記錄 | 38,094 筆 |
| 至少 3 次追蹤的病患 | 1,155 人 (99.3%) |
| 平均追蹤次數 | 11 次 |
| 追蹤間隔 | 約 1 年/次 |

#### 包含的三高相關變數

**生物標記（observations.csv）**
- 血壓：Systolic BP, Diastolic BP (14,467 筆)
- 血糖：Glucose, HbA1c (11,215 筆)
- 血脂：Total Cholesterol, LDL, Triglycerides (16,194 筆)

**診斷（conditions.csv）**
- Hypertension（高血壓）: 292 位病患
- Diabetes（糖尿病）: 73 位病患
- Hyperlipidemia（高血脂）: 138 位病患
- Prediabetes（糖尿病前期）: 341 位病患

---

## 🗂️ 其他資料集

### HRS (Health and Retirement Study)

HRS 資料需要申請才能下載，已評估後因申請流程複雜暫不使用。

相關分析文件：
- [docs/HRS_Data_Limitation_Memo.md](../../docs/HRS_Data_Limitation_Memo.md)
- [data/HRS_data/HRS_Biomarker_Analysis_Update.md](../HRS_data/HRS_Biomarker_Analysis_Update.md)

---

## 📝 注意事項

1. **資料檔案不上傳至 Git**
   - 所有 `.csv` 檔案已在 `.gitignore` 中排除
   - 只上傳此 README 和資料說明文件

2. **資料使用授權**
   - Synthea 資料為合成資料，不含真實個人資訊
   - 授權：CC-BY-NC 4.0（可用於學術研究）

3. **重現研究結果**
   - 其他研究者可依據本 README 下載相同資料
   - 確保研究可重現性

---

## 🔗 相關連結

- [Synthea 官方網站](https://synthea.mitre.org/)
- [Synthea GitHub](https://github.com/synthetichealth/synthea)
- [Synthea 文件](https://github.com/synthetichealth/synthea/wiki)

---

*更新日期: 2025-09-30*