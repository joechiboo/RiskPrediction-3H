# 資料集取得指南

## 📋 HRS 2016 VBS Biomarker 資料下載

### 🔐 資料存取要求
1. **HRS 用戶註冊** (必要)
   - 網站：https://hrsdata.isr.umich.edu
   - 建立免費用戶帳號
   - 同意使用條款

2. **敏感健康資料申請** (可能需要)
   - 部分 Biomarker 資料需要特殊申請
   - 填寫 Sensitive Health Data Order Form
   - 等待審核批准

### 📂 可用資料集
- **2016 Biomarker Data V1**
- **2016 VBS Sub Sample Data V1**
- **2016 VBS Supplemental File V1**

### 🧪 包含的生化指標
- Homocysteine (同型半胱氨酸)
- Clusterin (集簇蛋白)
- BDNF (腦源性神經營養因子)
- 5 種細胞激素
- Vitamin D (維生素D)
- IGF-1 (胰島素樣生長因子)

### ⏰ 下載步驟
1. 前往 https://hrsdata.isr.umich.edu/data-products/2016-biomarker-data
2. 註冊/登入 HRS 帳號
3. 檢查是否需要特殊權限申請
4. 下載相關資料和說明文件

---

## 📊 NHANES 資料下載

### 🌐 資料來源
- **官方網站**：https://www.cdc.gov/nchs/nhanes/
- **完全公開**：無需註冊申請
- **標準化格式**：.XPT (SAS Transport Files)

### 📋 建議年份
- **2017-2018**：最完整的生化資料
- **2015-2016**：備選方案
- **2019-2020**：COVID影響，資料可能不完整

### 🧪 NHANES 2017-2018 血液檢驗資料檔案
| SUA 變數 | NHANES 檔案 | 說明 |
|---------|------------|------|
| **FBG** | GLU_J.XPT | Plasma Fasting Glucose |
| **HbA1c** | GHB_J.XPT | Glycohemoglobin |
| **TC** | TCHOL_J.XPT | Total Cholesterol |
| **HDL** | HDL_J.XPT | HDL Cholesterol |
| **LDL/TG** | TRIGLY_J.XPT | LDL & Triglycerides |
| **Creatinine** | ALB_CR_J.XPT | Albumin & Creatinine - Urine |
| **Uric Acid** | BIOPRO_J.XPT | Standard Biochemistry Profile |

### 📊 NHANES 樣本資訊
- **2017-2018 總樣本**：~9,000 人
- **血液檢體收集率**：
  - 成人 (18+)：95%
  - 兒童 (1-17)：80%
- **空腹血糖檢測**：僅限空腹 ≥9 小時參與者

### 📥 下載方式

#### 方法1: 官網直接下載
```
https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory&CycleBeginYear=2017
```

#### 方法2: Python 套件
```python
# 安裝 NHANES 套件
pip install nhanes

# 使用範例
import nhanes
df = nhanes.load_data_file("GLU_J", "2017-2018")
```

#### 方法3: R 套件
```r
# 安裝套件
install.packages("RNHANES")
library(RNHANES)

# 下載資料
glucose_data <- nhanes_load_data("GLU_J", "2017-2018")
```

### 📊 NHANES 資料特點
- ✅ **完整血液檢驗**：包含所有 SUA 需要的變數
- ✅ **標準化品質**：CDC 官方品質控制
- ✅ **代表性樣本**：美國全國代表性
- ✅ **豐富文檔**：詳細的 codebook
- ❌ **橫斷面**：非縱向追蹤設計
- ❌ **樣本量較小**：每個週期約 10,000 人

---

## 🎯 下一步行動計劃

### 階段 1: 並行資料取得 (本週)
1. **HRS VBS 2016**
   - [ ] 完成 HRS 用戶註冊
   - [ ] 申請 Biomarker 資料存取權限
   - [ ] 下載並分析變數完整性

2. **NHANES 2017-2018**
   - [ ] 下載 Laboratory 模組資料
   - [ ] 分析血液檢驗變數覆蓋率
   - [ ] 評估樣本量和代表性

### 階段 2: 比較分析 (下週)
- [ ] 變數對照表製作
- [ ] 樣本特性比較
- [ ] 研究目標適配性評估
- [ ] 最終資料集選擇決策

---
*建立日期: 2025-09-22*
*狀態: 執行中*