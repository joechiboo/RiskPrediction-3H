# 實驗假說列表

> **建立日期**：2026-01-08
> **狀態**：規劃中

---

## 假說一覽

| # | 假說 | 實驗設計 | 狀態 |
|---|------|----------|------|
| H1 | 健檢次數越多，預測準確度越高 | T1→T2 vs T1+T2→T3 vs T1+T2+T3→T4 | 待執行 |
| H2 | Delta 特徵（變化量）能提升預測效能 | 比較有/無 Delta 特徵 | ✅ 已驗證 |
| H3 | Multi-Task Learning 優於 Single-Task | MTL vs STL 比較 | 待執行 |
| H4 | 可解釋模型（LR）效能接近黑盒模型 | LR vs RF/XGB | ✅ 已驗證 |
| H5 | Class imbalance 處理能提升 Sensitivity | class_weight ablation | ✅ 已驗證 |
| H6 | 符號回歸能找到有意義的數學公式 | PySR 實驗 | 進行中 |

---

## H1：健檢次數與預測準確度

### 假說
> 使用更多次健檢資料作為輸入，能提升疾病預測的準確度

### 理論基礎
- 更多時間點 → 更完整的健康軌跡
- 能捕捉長期趨勢和變化模式
- 類似 time-series forecasting 的概念

### 實驗設計

```
實驗 A：使用不同數量的健檢次數
├── A1: T1 → T2（1次健檢預測）
├── A2: T1+T2 → T3（2次健檢預測）
├── A3: T1+T2+T3 → T4（3次健檢預測）
├── A4: T1+T2+T3+T4 → T5（4次健檢預測）
└── 比較各組的 AUC、Sensitivity、Specificity

實驗 B：Delta 特徵的累積效果
├── B1: T2 only（無歷史）
├── B2: T2 + Delta1（T2-T1）
├── B3: T2 + Delta1 + Delta2（若有 T3）
└── 驗證累積變化量的價值
```

### 預期結果
- AUC 隨健檢次數增加而上升
- 但可能有邊際遞減效應（diminishing returns）

### 評估指標
- AUC (primary)
- Sensitivity, Specificity
- 計算每增加一次健檢的 AUC 增益

### 資料需求
- 需要有 ≥4 次健檢的病患子集
- 目前資料：T1-T8（最多 8 次）

---

## H2：Delta 特徵的價值（已驗證）

### 假說
> 健檢指標的變化量（Delta）比單一時間點的絕對值更能預測未來疾病

### 實驗結果
- 參見 `09_Delta_Ablation.ipynb`
- **結論**：T2+Delta 組合表現最佳

---

## H3：Multi-Task Learning vs Single-Task Learning

### 假說
> 同時預測三高（MTL）能利用疾病間的相關性，優於分別預測（STL）

### 理論基礎
- 三高有共同風險因子（BMI, 年齡, 尿酸等）
- MTL 可以 share representation
- 參考論文：Taiwan MTL (2025)

### 實驗設計

```
STL（Single-Task Learning）:
├── Model_HT: 只預測高血壓
├── Model_HG: 只預測高血糖
└── Model_DL: 只預測高血脂

MTL（Multi-Task Learning）:
└── Model_3H: 同時預測三種疾病
    ├── 方法 A: MultiOutputClassifier
    ├── 方法 B: Shared hidden layers + 3 output heads
    └── 方法 C: Multi-label classification

比較指標:
├── 各疾病的 AUC
├── 總體 macro-AUC
└── 訓練時間
```

### 預期結果
- MTL 在資料量少的疾病上表現更好（借用其他任務的資訊）
- STL 可能在資料量大的疾病上略勝

---

## H4：可解釋性 vs 效能（已驗證）

### 假說
> 可解釋模型（LR）能達到接近黑盒模型的效能

### 實驗結果
- 參見 `13_5FoldCV_Model_Comparison.ipynb`
- **結論**：LR 在 Hyperglycemia (0.932) 和 Dyslipidemia (0.867) 表現最佳
- RF/XGB 僅在 Hypertension 略勝

---

## H5：Class Imbalance 處理（已驗證）

### 假說
> 使用 class_weight='balanced' 能提升少數類別的 Sensitivity

### 實驗結果
- 參見 `10_ClassWeight_Ablation.ipynb`
- **結論**：balanced 權重大幅提升 Sensitivity，AUC 幾乎不變

---

## H6：符號回歸的可解釋公式

### 假說
> PySR 能找到有臨床意義的數學公式

### 實驗結果（Notebook 12，單次實驗）
- 高血壓：`0.13 * exp(SBP_T1)` → 收縮壓是主要因子
- 高血糖：`0.11 * FBG_T2` → 空腹血糖是主要因子
- 高血脂：`0.04 * exp(TC_T1)` → 總膽固醇是主要因子

### 待完成
- [ ] PySR 參數調整
- [ ] 5-fold CV 驗證穩定性
- [ ] 公式的臨床意義解讀

---

## 待新增假說

- [ ] H7：年齡分層是否影響預測效能？
- [ ] H8：性別差異對預測的影響？
- [ ] H9：特定風險因子組合的交互作用？

---

## 實驗優先級

1. **H1：健檢次數實驗** ← 下一個重點
2. H3：MTL vs STL
3. H6：PySR 5-fold CV

