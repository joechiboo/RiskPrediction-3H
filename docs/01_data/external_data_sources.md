# External Data Sources

> **建立日期**：2026-01-13
> **目的**：記錄外部資料來源，這些資料因檔案過大未納入版控

---

## 1. Synthea 合成資料

### 用途
外部驗證用的合成醫療資料

### 來源
- **官網**：https://synthea.mitre.org/
- **GitHub**：https://github.com/synthetichealth/synthea
- **下載**：https://synthea.mitre.org/downloads

### 檔案結構
```
data/01_primary/Synthea/
├── 100_synthea_sample_data/    # 100 人樣本
├── 1000_synthea_sample_data/   # 1000 人樣本
└── Synthea_SUA_format.csv      # 轉換後格式
```

### 下載指令
```bash
# 下載預生成的樣本資料
wget https://synthea.mitre.org/downloads/synthea_sample_data_csv_2022_01_26.zip

# 或使用 Synthea 自行生成
java -jar synthea-with-dependencies.jar -p 1000 Taiwan
```

---

## 2. HRS 健康與退休研究

### 用途
參考用的縱向健康追蹤資料

### 來源
- **官網**：https://hrs.isr.umich.edu/
- **資料申請**：需註冊帳號並同意使用條款
- **版本**：2022 Core (h22core)

### 檔案結構
```
data/02_reference/HRS/
├── raw/h22core/
│   ├── h22cb/     # Codebook files
│   ├── h22da/     # Data files
│   ├── h22qn/     # Questionnaire PDFs
│   ├── h22sas/    # SAS scripts
│   ├── h22sps/    # SPSS scripts
│   └── h22sta/    # Stata scripts
└── README.txt
```

### 下載步驟
1. 前往 https://hrs.isr.umich.edu/
2. 註冊/登入帳號
3. 同意資料使用條款
4. 下載 2022 Core Public Use Dataset

---

## 3. DGA 飲食指南

### 用途
營養學參考文獻

### 來源
- **官網**：https://www.dietaryguidelines.gov/
- **PDF**：Dietary Guidelines for Americans 2025-2030

### 檔案
```
data/02_reference/DGA/
└── DGA_2025-2030.pdf
```

---

## 4. 如何獲取這些資料

如果你 clone 了這個 repo 並需要這些資料：

### Synthea（免費、無需註冊）
```bash
# 下載樣本資料
cd data/01_primary/
mkdir -p Synthea && cd Synthea
wget https://synthea.mitre.org/downloads/synthea_sample_data_csv_2022_01_26.zip
unzip synthea_sample_data_csv_2022_01_26.zip
```

### HRS（需註冊）
1. 前往 https://hrs.isr.umich.edu/data-products
2. 建立帳號並申請資料存取
3. 下載後解壓縮到 `data/02_reference/HRS/`

### DGA（免費）
```bash
cd data/02_reference/DGA/
wget https://www.dietaryguidelines.gov/sites/default/files/2020-12/Dietary_Guidelines_for_Americans_2020-2025.pdf
```

---

## 5. 注意事項

- **SUA 資料**：主要研究資料，已在 `data/01_primary/SUA/` 中，已納入版控
- **外部資料**：僅用於驗證和參考，不影響主要實驗結果
- **隱私**：HRS 資料需遵守其使用條款，不可公開分享
