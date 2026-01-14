# 命名對照表（Naming Convention）

> **建立日期**：2026-01-14
> **用途**：論文撰寫、圖表製作時的統一術語

---

## 時間點命名

### 對照表

| 程式碼 | 論文/圖表 | 說明 |
|--------|-----------|------|
| Tinput1 / T1 | **Y-2** | 兩年前的健檢（第一次輸入） |
| Tinput2 / T2 | **Y-1** | 一年前的健檢（第二次輸入） |
| Ttarget / T3 | **Y0** | 預測目標年 |

### 示意圖

```
時間軸：
    Y-2          Y-1          Y0
     │            │            │
   健檢1       健檢2        目標
  (輸入)      (輸入)       (預測)
     └────────────┴────────────┘
         特徵輸入          標籤
```

### 參考來源

Kanegae 2020 使用 `Year(-1)`, `Year(-2)` 的表示法，直覺且清楚。

---

## 特徵命名

### 基本特徵

| 程式碼 | 論文/圖表 | 中文 |
|--------|-----------|------|
| `SBP_Tinput1` | **SBP_Y-2** | Y-2 收縮壓 |
| `SBP_Tinput2` | **SBP_Y-1** | Y-1 收縮壓 |
| `Delta_SBP` | **ΔSBP** 或 **Delta_SBP** | 血壓變化量 |

### 完整特徵對照

| 程式碼變數 | 論文顯示 | 說明 |
|------------|----------|------|
| `FBG_Tinput1` | FBG_Y-2 | 空腹血糖（兩年前） |
| `FBG_Tinput2` | FBG_Y-1 | 空腹血糖（一年前） |
| `TC_Tinput1` | TC_Y-2 | 總膽固醇（兩年前） |
| `TC_Tinput2` | TC_Y-1 | 總膽固醇（一年前） |
| `Cr_Tinput1` | Cr_Y-2 | 肌酸酐（兩年前） |
| `Cr_Tinput2` | Cr_Y-1 | 肌酸酐（一年前） |
| `UA_Tinput1` | UA_Y-2 | 尿酸（兩年前） |
| `UA_Tinput2` | UA_Y-1 | 尿酸（一年前） |
| `GFR_Tinput1` | GFR_Y-2 | 腎絲球過濾率（兩年前） |
| `GFR_Tinput2` | GFR_Y-1 | 腎絲球過濾率（一年前） |
| `BMI_Tinput1` | BMI_Y-2 | 身體質量指數（兩年前） |
| `BMI_Tinput2` | BMI_Y-1 | 身體質量指數（一年前） |
| `SBP_Tinput1` | SBP_Y-2 | 收縮壓（兩年前） |
| `SBP_Tinput2` | SBP_Y-1 | 收縮壓（一年前） |
| `DBP_Tinput1` | DBP_Y-2 | 舒張壓（兩年前） |
| `DBP_Tinput2` | DBP_Y-1 | 舒張壓（一年前） |
| `Delta_FBG` | ΔFBG | 血糖變化量 |
| `Delta_TC` | ΔTC | 膽固醇變化量 |
| `Delta_Cr` | ΔCr | 肌酸酐變化量 |
| `Delta_UA` | ΔUA | 尿酸變化量 |
| `Delta_GFR` | ΔGFR | GFR 變化量 |
| `Delta_BMI` | ΔBMI | BMI 變化量 |
| `Delta_SBP` | ΔSBP | 收縮壓變化量 |
| `Delta_DBP` | ΔDBP | 舒張壓變化量 |

---

## 目標變數命名

| 程式碼 | 論文 | 英文 | 中文 |
|--------|------|------|------|
| `hypertension_target` | HTN | Hypertension | 高血壓 |
| `hyperglycemia_target` | HG | Hyperglycemia | 高血糖 |
| `dyslipidemia_target` | DL | Dyslipidemia | 高血脂 |

---

## 模型命名

| 縮寫 | 全名 |
|------|------|
| LR | Logistic Regression |
| RF | Random Forest |
| XGB | XGBoost |
| SVM | Support Vector Machine |
| MLP | Multi-Layer Perceptron |
| DT | Decision Tree |
| PySR | Symbolic Regression (PySR) |

---

## 論文寫作範例

### Methods 章節

> We used health checkup data from two consecutive years (Y-2 and Y-1) to predict disease onset at Y0. Features included clinical measurements at both time points (e.g., SBP_Y-2, SBP_Y-1) and their temporal changes (ΔSBP = SBP_Y-1 - SBP_Y-2).

### 圖表標題

> **Figure 1.** SHAP summary plot for hypertension prediction. Features are labeled as X_Y-2 (two years before), X_Y-1 (one year before), and ΔX (temporal change).

---

## 注意事項

1. **程式碼不改**：所有 `.py`, `.ipynb` 中的變數名稱維持 `Tinput1`, `Tinput2`
2. **資料檔案不改**：CSV 欄位名稱維持原樣
3. **論文/圖表統一**：對外呈現一律使用 Y-2, Y-1, Y0
4. **Delta 保留**：程式中用 `Delta_X`，論文中可用 `ΔX` 或 `Delta_X`

---

## 相關文件

- [Kanegae 2020](../02_literature/summaries/Paper_Kanegae_Hypertension_2020.md) - 命名參考來源
- [Data_Dictionary.md](Data_Dictionary.md) - 資料字典
