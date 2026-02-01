# Data Directory

本資料夾存放研究所需資料集。**資料檔案不會上傳到 Git**（已在 .gitignore 中排除）。

---

## 資料夾結構

```
data/
├── 01_primary/                # 主要研究資料
│   ├── SUA/                   # 中國浙江 (訓練/測試)
│   │   ├── raw/               # 原始資料
│   │   └── processed/         # 處理後資料
│   └── Synthea/               # 美國合成資料 (外部驗證)
│
└── 02_reference/              # 參考資料 (暫不使用)
    ├── HRS/                   # 美國 Health and Retirement Study
    └── MJ/                    # 台灣美兆健檢 (費用過高)
```

---

## 01_primary: 主要研究資料

### SUA_CVDs（主資料集）

| 項目 | 內容 |
|------|------|
| 來源 | Dryad Digital Repository |
| 地區 | 中國浙江杭州 |
| 連結 | https://datadryad.org/stash/dataset/doi:10.5061/dryad.z08kprrk1 |
| 用途 | 模型訓練與測試 |

**下載步驟**：
1. 前往上述連結
2. 下載 `SUA_CVDs_risk_factors.csv`
3. 放置到 `data/01_primary/SUA/raw/`

詳細說明：[docs/06_datasets/SUA_Dataset_Documentation.md](../docs/06_datasets/SUA_Dataset_Documentation.md)

---

### Synthea（外部驗證）

| 項目 | 內容 |
|------|------|
| 來源 | Synthea Synthetic Patient Data (MITRE) |
| 地區 | 美國（合成資料） |
| 連結 | https://synthea.mitre.org/downloads |
| 用途 | 外部驗證 |

**下載步驟**：
1. 前往上述連結
2. 下載 `1K Sample Synthetic Patient Records, CSV`
3. 解壓縮到 `data/01_primary/Synthea/`

詳細說明：[docs/06_datasets/Synthea_Dataset.md](../docs/06_datasets/Synthea_Dataset.md)

---

## 02_reference: 參考資料

### HRS (Health and Retirement Study)

| 項目 | 內容 |
|------|------|
| 來源 | University of Michigan |
| 狀態 | 探索過，資料限制多，暫不使用 |

### MJ (美兆健檢)

| 項目 | 內容 |
|------|------|
| 來源 | 台灣美兆健康管理機構 |
| 狀態 | 費用約 10 萬元，暫不考慮 |

---

## 注意事項

1. 所有 `.csv` 檔案已在 `.gitignore` 中排除
2. 其他研究者可依據本 README 下載相同資料以重現結果
3. 資料使用需遵守各來源的授權條款

---

*更新日期: 2025-01-10*
