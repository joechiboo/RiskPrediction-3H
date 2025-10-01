# Synthea 資料轉換為 SUA_CVDs_risk_factors 格式

## 📄 文件資訊
- **建立日期**: 2025-09-30
- **轉換腳本**: `scripts/convert_synthea_to_sua_format.py`
- **輸入資料**: Synthea 1K Sample (1,163 patients)
- **輸出格式**: SUA_CVDs_risk_factors 標準格式

---

## 🎯 轉換目標

將 Synthea 的多個 CSV 檔案（patients, observations, conditions）整合並轉換為單一的 SUA 標準格式，用於三高（高血壓、高血糖、高血脂）風險預測研究。

---

## 📊 SUA 標準格式說明

### 欄位定義

| 欄位名稱 | 類型 | 單位 | 說明 | 範例 |
|---------|------|------|------|------|
| **ID** | int | - | 病患編號（sequential） | 1, 2, 3... |
| **sex** | int | - | 性別（1=男, 2=女） | 2 |
| **Age** | int | 歲 | 年齡 | 65 |
| **BMI** | float | kg/m² | 身體質量指數 | 24.35 |
| **SBP** | float | mmHg | 收縮壓 | 132 |
| **DBP** | float | mmHg | 舒張壓 | 83 |
| **FBG** | float | mmol/L | 空腹血糖 | 6.2 |
| **TC** | float | mmol/L | 總膽固醇 | 4.65 |
| **Cr** | float | mg/dL | 肌酸酐 | 0.6 |
| **GFR** | float | mL/min/1.73m² | 腎絲球過濾率 | 116.18 |
| **UA** | float | μmol/L | 尿酸 | 284 |
| **Times** | int | - | 第幾次就診 | 1, 2, 3... |
| **hypertension** | int | - | 高血壓（1=正常, 2=異常） | 1 |
| **hyperglycemia** | int | - | 高血糖（1=正常, 2=異常） | 1 |
| **dyslipidemia** | int | - | 高血脂（1=正常, 2=異常） | 1 |

---

## 🔄 轉換流程

### Step 1: 載入 Synthea 原始資料

**輸入檔案**:
- `patients.csv` - 病患基本資料
- `observations.csv` - 生物標記測量值
- `conditions.csv` - 診斷記錄

**程式碼**:
```python
patients = pd.read_csv("patients.csv")
observations = pd.read_csv("observations.csv")
conditions = pd.read_csv("conditions.csv")
```

---

### Step 2: 觀察值（Observations）欄位對應

#### LOINC Code 對應表

| SUA 欄位 | Synthea LOINC Code | 描述 | 單位 |
|---------|-------------------|------|------|
| **SBP** | 8480-6 | Systolic Blood Pressure | mmHg |
| **DBP** | 8462-4 | Diastolic Blood Pressure | mmHg |
| **FBG** | 2339-0 | Glucose [Mass/volume] in Blood | mg/dL → mmol/L |
| **TC** | 2093-3 | Cholesterol [Mass/volume] in Serum | mg/dL → mmol/L |
| **Cr** | 38483-4 | Creatinine [Mass/volume] in Blood | mg/dL |
| **BMI** | 39156-5 | Body Mass Index | kg/m² |

#### 單位轉換

**血糖 (Glucose)**:
```python
# Synthea: mg/dL → SUA: mmol/L
FBG_mmol = FBG_mg_dL / 18.0
```

**膽固醇 (Cholesterol)**:
```python
# Synthea: mg/dL → SUA: mmol/L
TC_mmol = TC_mg_dL / 38.67
```

**肌酸酐 (Creatinine)**:
```python
# 保持 mg/dL 單位（用於 GFR 計算）
# 注意: 原始 SUA 的 Cr 可能是 μmol/L (1 mg/dL = 88.4 μmol/L)
```

---

### Step 3: 診斷（Conditions）對應

#### SNOMED CT Code 對應表

| SUA 欄位 | Synthea SNOMED Code | 描述 |
|---------|-------------------|------|
| **hypertension** | 59621000 | Hypertension |
| | 38341003 | Hypertensive disorder |
| **hyperglycemia** | 44054006 | Diabetes mellitus type 2 |
| | 15777000 | Prediabetes |
| **dyslipidemia** | 55822004 | Hyperlipidemia |

#### 診斷邏輯

```python
# 預設為正常 (1)
hypertension = 1
hyperglycemia = 1
dyslipidemia = 1

# 如果診斷日期 <= 就診日期，則標記為異常 (2)
for condition in patient_conditions:
    if condition['START'] <= visit_date:
        if condition['DIAGNOSIS'] == 'hypertension':
            hypertension = 2
        elif condition['DIAGNOSIS'] == 'hyperglycemia':
            hyperglycemia = 2
        elif condition['DIAGNOSIS'] == 'dyslipidemia':
            dyslipidemia = 2
```

---

### Step 4: GFR 計算

#### 公式選擇：CKD-EPI 2021

**不使用種族係數**（符合最新國際標準）

#### 完整公式

```python
# Step 1: 單位轉換（Synthea 的 Cr 是 mg/dL）
Cr_μmol_L = Cr_mg_dL × 88.4

# Step 2: 設定參數
if sex == 2:  # Female
    κ = 62  # μmol/L
    α = -0.329
    sex_factor = 1.018
else:  # Male
    κ = 80  # μmol/L
    α = -0.411
    sex_factor = 1.0

# Step 3: 計算 GFR
GFR = 141 × min(Cr_μmol_L/κ, 1)^α × max(Cr_μmol_L/κ, 1)^(-1.209) × (0.993^Age) × sex_factor
```

#### GFR 分級參考

| GFR 值 (mL/min/1.73m²) | 腎功能狀態 |
|------------------------|-----------|
| ≥ 90 | 正常或高值 |
| 60-89 | 輕度下降 |
| 45-59 | 輕度至中度下降 |
| 30-44 | 中度至重度下降 |
| 15-29 | 重度下降 |
| < 15 | 腎衰竭 |

#### 為什麼使用 CKD-EPI？

1. **臨床金標準**: 目前最廣泛使用的 GFR 估算公式
2. **全範圍準確**: 適用於正常到腎衰竭的所有範圍
3. **考慮性別差異**: 女性和男性有不同的肌酸酐代謝
4. **無種族偏見**: 2021 版本移除種族係數，避免健康不平等

---

### Step 5: 其他欄位處理

#### ID 編號
```python
# 將 Synthea 的 UUID 轉換為連續整數
patient_id_map = {uuid: idx+1 for idx, uuid in enumerate(unique_patients)}
```

#### 性別編碼
```python
sex = 1 if gender == 'M' else 2
```

#### 年齡計算
```python
age = (visit_date - birth_date).days // 365
```

#### 就診次數 (Times)
```python
# 按病患和日期排序後，累計計數
Times = patient_visits.groupby('PATIENT').cumcount() + 1
```

#### UA (尿酸)
```python
# ⚠️ Synthea 資料中沒有尿酸測量
UA = np.nan
```

---

## 📈 轉換結果統計

### 資料規模

| 項目 | 數量 |
|------|------|
| 輸入病患數 | 1,163 |
| 輸出記錄數 | 14,466 |
| 有效病患數 | 1,158 |
| 平均追蹤次數 | 12.5 |
| ≥3 次追蹤的病患 | 1,155 (99.7%) |

### 診斷分布

| 診斷 | 記錄數 (status=2) | 百分比 |
|------|------------------|--------|
| 高血壓 | 4,356 | 30.1% |
| 高血糖 | 5,525 | 38.2% |
| 高血脂 | 2,039 | 14.1% |

### 資料完整性

| 欄位 | 完整度 | 說明 |
|------|--------|------|
| ID, sex, Age | 100% | 必要欄位 |
| SBP, DBP | 100% | 每次就診都測量 |
| BMI | 80% | 大部分就診有測量 |
| FBG | 31% | 定期檢查 |
| TC | 27.8% | 定期檢查 |
| Cr | 31% | 定期檢查 |
| GFR | 31% | 依 Cr 計算 |
| **UA** | **0%** | **⚠️ Synthea 無此資料** |

---

## ⚠️ 重要注意事項

### 1. 尿酸 (UA) 缺失

**問題**: Synthea 合成資料中沒有尿酸測量值

**影響**:
- 無法進行需要 UA 的分析
- 無法計算痛風風險
- 無法進行完整的心血管風險評估

**解決方案**:
- 選項 A: 移除 UA 欄位，只用其他變數建模
- 選項 B: 使用其他資料集（如真實臨床資料）
- 選項 C: 基於其他變數推估 UA（不建議）

### 2. 血液檢驗頻率

**現象**: 並非每次就診都有完整血液檢查
- SBP/DBP: 100% (每次都測)
- 血液檢驗: ~30% (約每 3 次就診測 1 次)

**原因**: Synthea 模擬真實臨床情況
- 常規就診: 只測血壓、體重
- 年度健檢: 完整血液檢查

**建議**:
```python
# 篩選有完整檢測的記錄
complete_records = df[df[['SBP', 'DBP', 'FBG', 'TC', 'Cr']].notna().all(axis=1)]
```

### 3. 單位一致性

**血糖單位轉換**:
- Synthea: mg/dL (範圍: 70-200)
- SUA: mmol/L (範圍: 3.9-11.1)
- 轉換: `mmol/L = mg/dL / 18.0`

**膽固醇單位轉換**:
- Synthea: mg/dL (範圍: 150-300)
- SUA: mmol/L (範圍: 3.9-7.8)
- 轉換: `mmol/L = mg/dL / 38.67`

**肌酸酐單位**:
- Synthea: mg/dL (範圍: 0.5-1.5)
- 用於 GFR 計算時轉為 μmol/L: `μmol/L = mg/dL × 88.4`

### 4. 診斷時間點

**邏輯**:
- 如果診斷日期 ≤ 就診日期 → 標記為異常 (2)
- 否則 → 標記為正常 (1)

**意義**:
- 可以看到疾病的發展過程
- 診斷前的記錄標記為正常
- 診斷後的記錄標記為異常

**範例**:
```
2018-01-01: hypertension=1 (尚未診斷)
2018-06-15: 診斷高血壓
2018-07-01: hypertension=2 (已診斷)
2019-01-01: hypertension=2 (持續)
```

---

## 🚀 使用方法

### 執行轉換腳本

```bash
# 確認資料位置
cd d:/Personal/Project/RiskPrediction-3H

# 執行轉換
python scripts/convert_synthea_to_sua_format.py
```

### 輸出檔案

```
data/processed/Synthea_SUA_format.csv
```

### 查看結果

```python
import pandas as pd

# 讀取轉換後的資料
df = pd.read_csv('data/processed/Synthea_SUA_format.csv')

# 基本統計
print(df.info())
print(df.describe())

# 查看某個病患的追蹤記錄
patient_1 = df[df['ID'] == 1]
print(patient_1)
```

---

## 📊 品質檢查清單

轉換完成後，建議進行以下檢查：

### ✅ 基本檢查

- [ ] 記錄數正確（約 14,000+）
- [ ] 病患數正確（1,158 人）
- [ ] 沒有重複的 (ID, Times) 組合
- [ ] Times 從 1 開始連續編號

### ✅ 數值範圍檢查

```python
# 年齡
assert df['Age'].between(0, 120).all()

# 血壓
assert df['SBP'].between(80, 200).all()
assert df['DBP'].between(40, 120).all()

# BMI
assert df['BMI'].between(15, 50).all()

# 診斷標記
assert df['hypertension'].isin([1, 2]).all()
assert df['hyperglycemia'].isin([1, 2]).all()
assert df['dyslipidemia'].isin([1, 2]).all()
```

### ✅ GFR 合理性檢查

```python
# GFR 應在合理範圍
assert df['GFR'].between(0, 200).all()

# 高齡者 GFR 應較低
elderly = df[df['Age'] > 70]
assert elderly['GFR'].mean() < df['GFR'].mean()

# 女性平均 GFR 略低於男性（因肌肉量較少）
female = df[df['sex'] == 2]
male = df[df['sex'] == 1]
print(f"Female GFR: {female['GFR'].mean():.2f}")
print(f"Male GFR: {male['GFR'].mean():.2f}")
```

---

## 🔗 相關文件

- [Synthea Dataset Summary](./Synthea_Dataset_Summary.md) - 原始 Synthea 資料說明
- [data/raw/README.md](../data/raw/README.md) - 資料下載指引
- `scripts/convert_synthea_to_sua_format.py` - 轉換腳本

---

## 📚 參考資料

### GFR 計算公式
- [CKD-EPI 2021 Equation](https://www.kidney.org/professionals/kdoqi/gfr_calculator) - 無種族因素版本
- Inker LA, et al. (2021). "New Creatinine- and Cystatin C–Based Equations to Estimate GFR without Race." NEJM.

### 單位轉換
- [Clinical Chemistry Unit Conversion](https://www.aacc.org/science-and-research/clinical-chemistry-trainee-council/clinical-chemistry-guide/unit-conversions)

### LOINC & SNOMED CT
- [LOINC Database](https://loinc.org/)
- [SNOMED CT Browser](https://browser.ihtsdotools.org/)

---

## 📝 版本歷史

| 日期 | 版本 | 變更內容 |
|------|------|---------|
| 2025-09-30 | 1.0 | 初始版本，完成 Synthea 到 SUA 格式轉換 |

---

## 👤 作者

Generated with [Claude Code](https://claude.com/claude-code)

---

*最後更新: 2025-09-30*