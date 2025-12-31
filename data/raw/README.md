# Raw Data Directory

本資料夾存放原始資料集，**資料檔案不會上傳到 Git**（已在 .gitignore 中排除）。

---

## 資料集下載指引

### 1. SUA_CVDs（主要資料集）

| 項目 | 內容 |
|------|------|
| 來源 | Dryad Digital Repository |
| 連結 | https://datadryad.org/stash/dataset/doi:10.5061/dryad.z08kprrk1 |
| 檔案 | `SUA_CVDs_risk_factors.csv` |
| 放置位置 | `data/raw/SUA_CVDs_risk_factors.csv` |

詳細說明：[docs/datasets/SUA_Dataset_Documentation.md](../../docs/datasets/SUA_Dataset_Documentation.md)

---

### 2. Synthea（外部驗證用）

| 項目 | 內容 |
|------|------|
| 來源 | Synthea Synthetic Patient Data |
| 連結 | https://synthea.mitre.org/downloads |
| 檔案 | 1K Sample Synthetic Patient Records, CSV |
| 放置位置 | `data/raw/synthea_sample_data/` |

詳細說明：[docs/datasets/Synthea_Dataset.md](../../docs/datasets/Synthea_Dataset.md)

---

## 注意事項

1. 所有 `.csv` 檔案已在 `.gitignore` 中排除
2. 其他研究者可依據本 README 下載相同資料以重現結果

---

*更新日期: 2025-12-31*
