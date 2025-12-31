# Synthea 合成病患資料集

**用途**：外部驗證（External Validation）

## 基本資訊

| 項目 | 內容 |
| ---- | ---- |
| 來源 | Synthea Synthetic Patient Data |
| 網站 | [synthea.mitre.org](https://synthea.mitre.org/) |
| 授權 | CC-BY-NC 4.0 |
| 資料類型 | 合成（Synthetic） |

## 資料規模

| 項目 | 數量 |
| ---- | ---- |
| 病患數 | 1,163 人 |
| 觀察記錄 | 531,144 筆 |
| 診斷記錄 | 38,094 筆 |
| 至少 3 次追蹤 | 1,155 人（99.3%） |
| 平均追蹤次數 | 11 次 |
| 追蹤間隔 | 約 1 年/次 |

## 三高相關變數

### 生物標記（observations.csv）

| 類別 | 變數 | 記錄數 |
| ---- | ---- | ------ |
| 血壓 | Systolic BP, Diastolic BP | 14,467 筆 |
| 血糖 | Glucose, HbA1c | 11,215 筆 |
| 血脂 | Total Cholesterol, LDL, Triglycerides | 16,194 筆 |

### 診斷（conditions.csv）

| 疾病 | 病患數 |
| ---- | ------ |
| Hypertension（高血壓） | 292 人 |
| Diabetes（糖尿病） | 73 人 |
| Hyperlipidemia（高血脂） | 138 人 |
| Prediabetes（糖尿病前期） | 341 人 |

## 下載方式

1. 前往 [Synthea Downloads](https://synthea.mitre.org/downloads)
2. 下載 `1K Sample Synthetic Patient Records, CSV`（9 MB）
3. 解壓縮到 `data/raw/synthea_sample_data/`

## 檔案結構

```
data/raw/synthea_sample_data/
├── patients.csv
├── observations.csv
├── conditions.csv
├── encounters.csv
├── medications.csv
└── ...
```

## 與主資料集的差異

| 面向 | SUA_CVDs | Synthea |
| ---- | -------- | ------- |
| 資料真實性 | 真實健檢 | 合成模擬 |
| 追蹤間隔 | 約 2 年 | 約 1 年 |
| 地區 | 中國 | 美國（模擬） |
| 用途 | 訓練/測試 | 外部驗證 |

## 注意事項

1. Synthea 為合成資料，不含真實個人資訊
2. 用於驗證模型泛化能力，非主要訓練資料
3. 資料分布可能與真實世界有差異
