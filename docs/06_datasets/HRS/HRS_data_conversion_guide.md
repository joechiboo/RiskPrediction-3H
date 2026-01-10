# HRS 資料轉換指南

## 📋 總覽

本指南說明如何將 HRS (Health and Retirement Study) 的 SPSS 格式資料轉換為 Excel 格式，專門針對三高疾病（高血壓、高血糖、高血脂）風險預測研究。

## 🗂️ 腳本檔案說明

### 核心轉換腳本 (推薦使用)

#### 1. `extract_3h_variables.py` ⭐⭐⭐⭐⭐
**用途**: 最終產品，提取三高相關的優先變數
**狀態**: 長期使用，核心腳本
**功能**:
- 提取 94 個已識別的三高相關變數
- 生成可直接用於分析的 Excel 檔案
- 包含變數說明和基本統計
**輸出**: 4個核心 Excel 檔案 + 總結報告
**使用時機**: 當需要最新的三高相關資料時

#### 2. `decode_hrs_variables.py` ⭐⭐⭐⭐
**用途**: 解碼 HRS 變數命名規則，識別三高相關變數
**狀態**: 長期使用，當有新資料時重複使用
**功能**:
- 根據 HRS 標準命名慣例解碼變數
- 自動分類變數主題 (健康狀況、慢性疾病、藥物等)
- 評估變數對三高研究的相關性
**輸出**: 變數解碼結果和優先順序清單

#### 3. `verify_hrs_data.py` ⭐⭐⭐
**用途**: 驗證 HRS 資料檔案是否正確下載
**狀態**: 長期使用，每次取得新資料時使用
**功能**:
- 檢查必要的資料檔案是否存在
- 顯示檔案大小和基本資訊
- 嘗試讀取範例資料
**使用時機**: 下載新的 HRS 資料後

### 探索性腳本 (單次使用)

#### 4. `check_hrs_files.py` ⭐⭐
**用途**: 檢查哪些 HRS 檔案可用
**狀態**: 單次使用，已完成任務
**功能**: 列出找到的檔案和建議轉換順序

#### 5. `quick_explore_hrs.py` ⭐⭐
**用途**: 快速探索 HRS 資料結構
**狀態**: 單次使用，已完成任務
**功能**: 讀取範例資料並生成變數清單

#### 6. `examine_hrs_variables.py` ⭐⭐
**用途**: 詳細檢查 HRS 變數命名模式
**狀態**: 單次使用，已完成任務
**功能**: 分析變數前綴和命名規律

#### 7. `explore_health_modules.py` ⭐
**用途**: 探索健康相關模組
**狀態**: 單次使用，功能已整合到其他腳本
**功能**: 初步識別健康相關變數

### 過時腳本 (不建議使用)

#### 8. `convert_hrs_to_excel.py` ⭐
**用途**: 原始的完整轉換腳本
**狀態**: 過時，被更精確的腳本取代
**問題**: 嘗試轉換所有變數，效率低且不聚焦

#### 9. `convert_hrs_simple.py` ⭐
**用途**: 簡化版轉換腳本
**狀態**: 過時，被更好的方案取代
**問題**: 功能重複且不完整

## 🔄 建議的工作流程

### 初次設置
1. **下載 HRS 資料** → 參考 `docs/HRS_data_download_guide.md`
2. **驗證資料** → 運行 `verify_hrs_data.py`
3. **提取三高變數** → 運行 `extract_3h_variables.py`

### 後續使用
- **有新 HRS 資料時**: 重複上述流程
- **需要不同變數時**: 修改 `decode_hrs_variables.py` 的分類邏輯
- **資料更新時**: 僅需運行 `extract_3h_variables.py`

## 📁 輸出檔案結構

```
data/processed/HRS_Excel/
├── 2022_Health_3H_Variables.xlsx      # 2022年健康狀況 (27變數)
├── 2022_Medical_3H_Variables.xlsx     # 2022年醫療史 (16變數)
├── 2020_Health_3H_Variables.xlsx      # 2020年健康狀況 (36變數)
├── 2020_Medical_3H_Variables.xlsx     # 2020年醫療史 (15變數)
├── HRS_3H_Extraction_Summary.xlsx     # 轉換總結報告
└── HRS_3H_Priority_Variables.xlsx     # 優先變數清單
```

## 🎯 三高疾病相關變數類型

### 高血壓 (Hypertension)
- 血壓測量相關變數
- 降血壓藥物使用
- 高血壓診斷史

### 高血糖 (Hyperglycemia)
- 糖尿病診斷
- 血糖控制相關
- 糖尿病藥物使用

### 高血脂 (Dyslipidemia)
- 膽固醇檢測
- 降血脂藥物
- 心血管風險因子

## 🔧 技術需求

### Python 套件
```bash
pip install pandas pyreadstat openpyxl
```

### 系統需求
- Python 3.7+
- 至少 4GB RAM (處理大型 SPSS 檔案)
- 2GB 可用磁碟空間

## ⚠️ 注意事項

1. **資料大小**: 原始 HRS 資料約 2.x GB，處理時需足夠記憶體
2. **變數命名**: HRS 使用特定命名慣例 (SC=Section C, SE=Section E等)
3. **資料年份**: 目前支援 2020 和 2022 年資料
4. **編碼問題**: 在某些系統可能出現 Unicode 編碼警告，不影響功能

## 🚀 快速開始

```bash
# 1. 驗證資料
python scripts/verify_hrs_data.py

# 2. 提取三高變數 (一步完成所有轉換)
python scripts/extract_3h_variables.py
```

## 📞 故障排除

### 常見問題
- **記憶體不足**: 關閉其他程式或使用更強的機器
- **檔案未找到**: 確認 HRS 資料已正確下載到 `data/raw/other/`
- **套件錯誤**: 確認已安裝所有必要的 Python 套件

### 支援
- 查看腳本內的錯誤訊息
- 檢查 `data/processed/HRS_Excel/` 資料夾的輸出檔案
- 參考 HRS 官方文件和 Tracker 說明