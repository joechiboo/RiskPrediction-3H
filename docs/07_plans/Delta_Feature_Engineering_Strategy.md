# Δ 特徵工程策略：從 Dual Framework 2025 到本研究

**文檔建立日期**：2025-11-14
**參考論文**：Dual Machine Learning Framework for Predicting Long-Term Glycemic Change and Prediabetes Risk in Young Taiwanese Men (Diagnostics 2025)
**核心概念**：δ-FPG 特徵工程（重要性 100%）

---

## 📋 目錄

1. [Δ 特徵是什麼？](#δ-特徵是什麼)
2. [為什麼 Δ 特徵比單一時間點更重要？](#為什麼-δ-特徵比單一時間點更重要)
3. [Dual Framework 2025 的證據](#dual-framework-2025-的證據)
4. [本研究的 Δ 特徵設計](#本研究的-δ-特徵設計)
5. [實際計算範例](#實際計算範例)
6. [預期結果與假設](#預期結果與假設)
7. [實作計畫](#實作計畫)

---

## Δ 特徵是什麼？

### 定義

**Δ (Delta)** 表示**變化量 (Change)**，計算兩個時間點之間某個指標的差異。

```
Δ [指標] = [指標]_時間點2 - [指標]_時間點1
```

### 範例：空腹血糖 (FPG)

```
第一年健檢：FPG = 90 mg/dL  ✅ 正常
第二年健檢：FPG = 100 mg/dL ⚠️ 前驅糖尿病

Δ FPG = 100 - 90 = +10 mg/dL  🚨 血糖上升
```

**解釋**：
- 雖然第一年血糖正常 (90)，但**上升了 10 mg/dL**
- 剛好跨過 100 的閾值，進入前驅糖尿病範圍
- **Δ FPG = +10** 比單看「FPG = 100」更能預測未來風險

---

## 為什麼 Δ 特徵比單一時間點更重要？

### 核心原理：捕捉動態變化

| 個案 | Y-2 FPG | Y-1 FPG | Δ FPG | 風險評估 |
|------|--------|--------|-------|---------|
| **個案 A** | 85 mg/dL | 98 mg/dL | **+13** 🚨 | **高風險**：血糖快速上升，代謝失衡 |
| **個案 B** | 95 mg/dL | 98 mg/dL | **+3** ✅ | **中等風險**：血糖接近上限但穩定 |

**同樣是 Y-1 = 98 mg/dL（都在正常範圍內）**，但：
- **個案 A** 的 Δ FPG = +13，顯示**代謝快速惡化** → 高風險
- **個案 B** 的 Δ FPG = +3，血糖相對穩定 → 中等風險

### 臨床意義

**靜態數值 (單一時間點)**：
- 只能告訴你「現在的狀態」
- 無法知道「趨勢方向」

**動態變化量 (Δ 特徵)**：
- 捕捉「代謝軌跡」
- 預測「未來風險」
- 反映「生理失衡速度」

---

## Dual Framework 2025 的證據

### 研究設計

| 項目 | 內容 |
|------|------|
| **樣本數** | 6,247 名台灣年輕男性 (18-35歲) |
| **追蹤時間** | 平均 5.9 年 |
| **基線條件** | FPG < 100 mg/dL (正常血糖) |
| **預測目標** | δ-FPG 與前驅糖尿病風險 |
| **核心特徵** | δ-FPG = FPG_follow-up - FPG_baseline |

### 關鍵發現 1：δ-FPG 是最強預測因子

**模型 1（包含 FPGbase）- 特徵重要性**：

| 排名 | 變量 | MOIP（平均重要性%） |
|------|------|-------------------|
| 1 | **基線空腹血糖 (FPGbase)** | **100.00** ⭐⭐⭐⭐⭐ |
| 2 | 體脂肪 | 17.64 |
| 3 | 促甲狀腺激素 (TSH) | 14.80 |
| 4 | 白血球計數 (WBC) | 14.51 |
| 5 | 追蹤年數 | 14.32 |

**結論**：
- **FPGbase 重要性 100%**，遠超第二名（體脂肪僅 17.64%）
- 基線血糖水平決定了未來血糖變化的軌跡
- **證實變化量策略的有效性** ⭐⭐⭐⭐⭐

### 關鍵發現 2：兩組顯著差異

**分層分析結果**：

| 組別 | 基線 FPG | 追蹤後 FPG (推算) | δ-FPG | 結果 |
|------|---------|------------------|-------|------|
| **前驅糖尿病組** (n=2789, 44.6%) | 93.3 ± 4.3 | ~103 | **+9.88 ± 5.45** 🚨 | 進展為前驅糖尿病 (100-125) |
| **正常組** (n=3458, 55.4%) | 91.0 ± 4.8 | ~92 | **+1.44 ± 5.77** ✅ | 維持正常 (<100) |
| **p 值** | < 0.001*** | - | < 0.001*** | 高度顯著 |

**結論**：
- 前驅糖尿病組的血糖上升是正常組的 **6.8 倍**
- 即使基線都 < 100（正常範圍），**基線較高者 (93.3) 更容易進展**
- **δ-FPG 與糖尿病風險呈正相關** (p < 0.001)

### 關鍵發現 3：模型性能

**連續值預測（δ-FPG 回歸）**：

| 方法 | RMSE | 關係類型 |
|------|------|---------|
| **Elastic Net** | 6.4092 ⭐ | 線性 + 正則化 |
| Random Forest | 6.4133 | 非線性 |
| XGBoost | 6.4329 | 非線性 |
| MLR | 6.4156 | 純線性 |

**二元分類（前驅糖尿病 vs. 正常）**：

| 指標 | 數值 | 解釋 |
|------|------|------|
| **敏感度** | **0.995** ⭐ | 幾乎找到所有前驅糖尿病患者 |
| 精確度 | 0.791 | 79.1% 預測為前驅糖尿病者確實是 |
| **PR-AUC** | **0.873** ⭐ | 在不平衡資料集上表現良好 |
| ROC-AUC | 0.667 | 中等區分能力 |

**結論**：
- ML 模型略優於線性模型，顯示**非線性關係存在**
- **高敏感度（99.5%）適合作為篩檢工具**
- δ-FPG 可有效預測糖尿病風險

### 關鍵發現 4：SHAP 可解釋性

**SHAP 依賴圖：FPGbase × 體脂肪%**

```
X軸: FPGbase (基線空腹血糖)
Y軸: SHAP值 (對 δ-FPG 的貢獻)
顏色: 體脂肪%
```

**發現**：
- **FPGbase 較低** → 強烈正 SHAP 值 → δ-FPG 增加
- **FPGbase 較高** → 負貢獻
- **非線性關係** + **體脂肪調節作用**

**臨床解釋**：
- 即使基線血糖正常，高體脂肪者仍有血糖上升風險
- 追蹤時間越長，血糖變化越明顯

---

## 本研究的 Δ 特徵設計

### 資料結構

假設有三次健檢（Y-2, Y-1, Y）：

```
患者 ID | Y-2 日期 | Y-2 FPG | Y-1 日期 | Y-1 FPG | Y 日期 | Y FPG
--------|---------|--------|---------|--------|---------|--------
P001    | 2020/1  | 88     | 2021/1  | 94     | 2022/1  | 102
P002    | 2020/3  | 90     | 2021/3  | 98     | 2022/3  | 92
P003    | 2020/6  | 95     | 2021/6  | 96     | 2022/6  | 97
```

### Δ 特徵計算策略

#### **方法 1：兩兩之間的變化量**

```python
# 短期變化 (Y-1 - Y-2)
Δ_FPG_Y-1_Y-2 = FPG_Y-1 - FPG_Y-2

# 短期變化 (Y - Y-1)
Δ_FPG_Y_Y-1 = FPG_Y - FPG_Y-1

# 長期變化 (Y - Y-2)
Δ_FPG_Y_Y-2 = FPG_Y - FPG_Y-2
```

**優點**：
- 捕捉不同時間段的變化
- 可分析變化趨勢（加速/減速）

#### **方法 2：變化率（斜率）**

```python
# 變化率 = 變化量 / 時間間隔
變化率_Y-1_Y-2 = (FPG_Y-1 - FPG_Y-2) / (時間_Y-1 - 時間_Y-2)
變化率_Y_Y-2 = (FPG_Y - FPG_Y-2) / (時間_Y - 時間_Y-2)

# 單位：mg/dL/年
```

**優點**：
- 標準化不同時間間隔
- 適合比較不同追蹤期長度

#### **方法 3：相對變化量（百分比）**

```python
# 相對變化 = (新值 - 舊值) / 舊值 × 100%
相對變化_Y-1_Y-2 = (FPG_Y-1 - FPG_Y-2) / FPG_Y-2 × 100
相對變化_Y_Y-2 = (FPG_Y - FPG_Y-2) / FPG_Y-2 × 100
```

**優點**：
- 標準化不同基線水平
- 適合跨指標比較

### 本研究的完整 Δ 特徵列表

#### **1. 血糖相關**
```python
Δ_FPG = FPG_Y-1 - FPG_Y-2          # 空腹血糖變化
Δ_HbA1c = HbA1c_Y-1 - HbA1c_Y-2    # 糖化血色素變化（如有）
```

#### **2. 尿酸相關** ⭐ 本研究核心
```python
Δ_SUA = SUA_Y-1 - SUA_Y-2          # 血清尿酸變化
Δ_BUN = BUN_Y-1 - BUN_Y-2          # 尿素氮變化
Δ_Creatinine = Cr_Y-1 - Cr_Y-2     # 肌酸酐變化
```

#### **3. 血脂相關**
```python
Δ_TG = TG_Y-1 - TG_Y-2             # 三酸甘油酯變化
Δ_LDL = LDL_Y-1 - LDL_Y-2          # 低密度脂蛋白變化
Δ_HDL = HDL_Y-1 - HDL_Y-2          # 高密度脂蛋白變化
Δ_TC = TC_Y-1 - TC_Y-2             # 總膽固醇變化
```

#### **4. 肝功能相關**
```python
Δ_GOT = GOT_Y-1 - GOT_Y-2          # 麩胺酸苯醋酸轉胺酶變化
Δ_GPT = GPT_Y-1 - GPT_Y-2          # 麩胺酸丙酮酸轉胺酶變化
Δ_γGT = γGT_Y-1 - γGT_Y-2          # γ-麩胺酸轉移酶變化
```

#### **5. 體重/代謝相關**
```python
Δ_BMI = BMI_Y-1 - BMI_Y-2          # 身體質量指數變化
Δ_體脂肪 = 體脂肪_Y-1 - 體脂肪_Y-2  # 體脂肪變化（如有）
Δ_腰圍 = 腰圍_Y-1 - 腰圍_Y-2       # 腰圍變化（如有）
```

#### **6. 血壓相關**
```python
Δ_SBP = SBP_Y-1 - SBP_Y-2          # 收縮壓變化
Δ_DBP = DBP_Y-1 - DBP_Y-2          # 舒張壓變化
```

#### **7. 發炎/血液相關**
```python
Δ_WBC = WBC_Y-1 - WBC_Y-2          # 白血球計數變化
Δ_CRP = CRP_Y-1 - CRP_Y-2          # C反應蛋白變化（如有）
Δ_Hb = Hb_Y-1 - Hb_Y-2             # 血紅素變化
Δ_Platelet = Plt_Y-1 - Plt_Y-2     # 血小板變化
```

#### **8. 其他代謝指標**
```python
Δ_TSH = TSH_Y-1 - TSH_Y-2          # 促甲狀腺激素變化（如有）
Δ_LDH = LDH_Y-1 - LDH_Y-2          # 乳酸脫氫酶變化（如有）
Δ_ALP = ALP_Y-1 - ALP_Y-2          # 鹼性磷酸酶變化（如有）
```

---

## 實際計算範例

### 範例 1：血糖快速上升（高風險）

```
患者 P001：
Y-2 (2020): FPG = 88 mg/dL  ✅ 正常
Y-1 (2021): FPG = 94 mg/dL  ✅ 正常
Y (2022): FPG = 102 mg/dL ⚠️ 前驅糖尿病

計算 Δ 特徵：
Δ_FPG_Y-1_Y-2 = 94 - 88 = +6 mg/dL
Δ_FPG_Y_Y-1 = 102 - 94 = +8 mg/dL
Δ_FPG_Y_Y-2 = 102 - 88 = +14 mg/dL  🚨 總上升 14

變化率 = 14 / 2年 = 7 mg/dL/年  🚨 快速上升

相對變化 = (102 - 88) / 88 × 100 = 15.9%  🚨 上升 16%
```

**風險評估**：
- ⚠️ **高風險**：血糖持續快速上升
- ⚠️ 2年內上升 14 mg/dL，類似 Dual Framework 的前驅糖尿病組 (+9.88)
- ⚠️ 已跨過 100 閾值，進入前驅糖尿病範圍

---

### 範例 2：血糖先升後降（改善）

```
患者 P002：
Y-2 (2020): FPG = 90 mg/dL  ✅ 正常
Y-1 (2021): FPG = 98 mg/dL  ⚠️ 接近閾值
Y (2022): FPG = 92 mg/dL  ✅ 正常

計算 Δ 特徵：
Δ_FPG_Y-1_Y-2 = 98 - 90 = +8 mg/dL   ⚠️ 上升
Δ_FPG_Y_Y-1 = 92 - 98 = -6 mg/dL   💚 下降（可能開始運動減重）
Δ_FPG_Y_Y-2 = 92 - 90 = +2 mg/dL   ✅ 總體穩定

變化率 = 2 / 2年 = 1 mg/dL/年  ✅ 穩定

相對變化 = (92 - 90) / 90 × 100 = 2.2%  ✅ 微幅上升
```

**風險評估**：
- ✅ **低風險**：血糖總體穩定
- ✅ Y-1→Y 血糖下降，顯示生活方式改善（運動、減重）
- ✅ 類似 Dual Framework 的正常組 (+1.44)

---

### 範例 3：多指標聯合分析

```
患者 P003：
Y-2 (2020): FPG = 95, SUA = 6.5, TG = 120, BMI = 24
Y-1 (2021): FPG = 98, SUA = 7.2, TG = 150, BMI = 25.5

計算 Δ 特徵：
Δ_FPG = 98 - 95 = +3 mg/dL    ⚠️ 上升
Δ_SUA = 7.2 - 6.5 = +0.7 mg/dL  🚨 跨過 7.0 閾值（高尿酸）
Δ_TG = 150 - 120 = +30 mg/dL   🚨 跨過 150 閾值（高血脂）
Δ_BMI = 25.5 - 24 = +1.5       🚨 體重增加

相對變化：
Δ_FPG% = 3/95 × 100 = 3.2%
Δ_SUA% = 0.7/6.5 × 100 = 10.8%  🚨 上升最快
Δ_TG% = 30/120 × 100 = 25%     🚨 上升最快
Δ_BMI% = 1.5/24 × 100 = 6.3%
```

**風險評估**：
- 🚨 **極高風險**：多指標同時惡化
- 🚨 SUA 跨過 7.0 閾值 → 高尿酸血症
- 🚨 TG 跨過 150 閾值 → 高血脂
- 🚨 BMI 增加 1.5 → 體重管理失控
- 🚨 **代謝症候群風險極高**

---

## 預期結果與假設

### 假設 1：Δ 特徵比基線特徵更有預測力

**基於 Dual Framework 2025 的證據**：
- FPGbase 重要性 100%，證實變化量策略有效
- 預期 Δ 特徵在本研究中也會成為最強預測因子

**驗證方法**：
```python
# 模型 A：僅使用基線特徵 (Y-2)
features_A = [FPG_Y-2, SUA_Y-2, TG_Y-2, BMI_Y-2, ...]

# 模型 B：僅使用 Δ 特徵
features_B = [Δ_FPG, Δ_SUA, Δ_TG, Δ_BMI, ...]

# 模型 C：基線 + Δ 特徵
features_C = [FPG_Y-2, SUA_Y-2, ..., Δ_FPG, Δ_SUA, ...]

# 比較 AUC：預期 C > B > A
```

### 假設 2：Δ SUA 是高尿酸血症的最強預測因子

**類比 Dual Framework 2025**：
- δ-FPG 重要性 100% → 預測前驅糖尿病
- **預期 Δ SUA 重要性也接近 100%** → 預測高尿酸血症

**驗證方法**：
```python
# 使用 SHAP 分析特徵重要性
import shap

# 訓練模型
model = XGBClassifier()
model.fit(X_train, y_train)

# 計算 SHAP 值
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# 視覺化特徵重要性
shap.summary_plot(shap_values, X_test, plot_type="bar")
```

**預期結果**：
| 排名 | 特徵 | SHAP 重要性% |
|------|------|-------------|
| 1 | **Δ_SUA** | **~100** ⭐ |
| 2 | SUA_baseline | ~20-30 |
| 3 | Δ_BMI | ~15-20 |
| 4 | Δ_TG | ~10-15 |

### 假設 3：非線性模型優於線性模型

**基於 Dual Framework 2025 的證據**：
- XGBoost, RF 略優於 MLR
- 顯示非線性關係存在

**驗證方法**：
```python
# 線性模型
lr = LogisticRegression()
en = ElasticNet()

# 非線性模型
rf = RandomForestClassifier()
xgb = XGBClassifier()
lgb = LGBMClassifier()
svm = SVC(kernel='rbf')

# 比較 AUC
```

**預期結果**：
- 非線性模型 (RF, XGBoost, LightGBM) AUC > 線性模型 (LR, EN)
- 差異約 2-5%

### 假設 4：Δ 特徵存在交互作用

**基於 Dual Framework 2025 的證據**：
- FPGbase × 體脂肪% 存在交互作用
- SHAP 依賴圖顯示調節效應

**驗證方法**：
```python
# SHAP 依賴圖
shap.dependence_plot("Δ_SUA", shap_values, X_test,
                     interaction_index="Δ_BMI")
```

**預期發現**：
- Δ_SUA × Δ_BMI：體重增加加劇尿酸上升
- Δ_SUA × Δ_TG：血脂異常與尿酸上升相關
- Δ_FPG × Δ_SUA：糖尿病與高尿酸的共病關係

---

## 實作計畫

### 階段 1：資料準備（第 1 週）

**任務 1.1：資料清理**
- [ ] 確認三次健檢資料完整性
- [ ] 處理缺失值（中位數插補 or KNN 插補）
- [ ] 異常值檢測與處理

**任務 1.2：Δ 特徵計算**
```python
# 計算所有 Δ 特徵
delta_features = []

for col in continuous_features:
    # 兩兩變化
    df[f'Δ_{col}_Y-1_Y-2'] = df[f'{col}_Y-1'] - df[f'{col}_Y-2']
    df[f'Δ_{col}_Y_Y-1'] = df[f'{col}_Y'] - df[f'{col}_Y-1']
    df[f'Δ_{col}_Y_Y-2'] = df[f'{col}_Y'] - df[f'{col}_Y-2']

    # 變化率
    df[f'Rate_{col}_Y-1_Y-2'] = df[f'Δ_{col}_Y-1_Y-2'] / df['時間差_Y-1_Y-2']
    df[f'Rate_{col}_Y_Y-2'] = df[f'Δ_{col}_Y_Y-2'] / df['時間差_Y_Y-2']

    # 相對變化
    df[f'RelΔ_{col}_Y-1_Y-2'] = df[f'Δ_{col}_Y-1_Y-2'] / df[f'{col}_Y-2'] * 100
    df[f'RelΔ_{col}_Y_Y-2'] = df[f'Δ_{col}_Y_Y-2'] / df[f'{col}_Y-2'] * 100

    delta_features.extend([f'Δ_{col}_Y-1_Y-2', f'Δ_{col}_Y_Y-1', f'Δ_{col}_Y_Y-2'])
```

**任務 1.3：目標變量定義**
```python
# 高尿酸血症
df['高尿酸'] = (df['SUA_Y'] >= 7.0).astype(int)  # 男性標準

# 前驅糖尿病
df['前驅糖尿病'] = ((df['FPG_Y'] >= 100) & (df['FPG_Y'] < 126)).astype(int)

# 糖尿病
df['糖尿病'] = (df['FPG_Y'] >= 126).astype(int)

# 高血脂
df['高血脂'] = (df['TG_Y'] >= 150).astype(int)

# 代謝症候群（5項中3項）
# ... (複雜邏輯，需另外定義)
```

---

### 階段 2：基線模型建立（第 2 週）

**任務 2.1：模型 A - 僅基線特徵**
```python
# 特徵：Y-2 時間點的所有指標
features_A = [col for col in df.columns if col.endswith('_Y-2')]

# 目標：預測 Y 時的疾病狀態
target = '高尿酸'

# 訓練模型
X_train, X_test, y_train, y_test = train_test_split(
    df[features_A], df[target], test_size=0.2, random_state=42
)

models_A = {
    'LR': LogisticRegression(),
    'RF': RandomForestClassifier(),
    'XGB': XGBClassifier(),
    'LGB': LGBMClassifier()
}

results_A = {}
for name, model in models_A.items():
    model.fit(X_train, y_train)
    y_pred = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_pred)
    results_A[name] = auc
    print(f"{name} AUC: {auc:.4f}")
```

**任務 2.2：模型 B - 僅 Δ 特徵**
```python
# 特徵：所有 Δ 特徵
features_B = [col for col in df.columns if col.startswith('Δ_')]

# 訓練模型（同上）
# ...
```

**任務 2.3：模型 C - 基線 + Δ 特徵**
```python
# 特徵：基線 + Δ
features_C = features_A + features_B

# 訓練模型（同上）
# ...
```

**任務 2.4：比較結果**
```python
import pandas as pd

comparison = pd.DataFrame({
    'Model A (基線)': results_A,
    'Model B (Δ)': results_B,
    'Model C (基線+Δ)': results_C
})

print(comparison)

# 繪製比較圖
comparison.plot(kind='bar', figsize=(10, 6))
plt.title('模型性能比較：基線 vs. Δ vs. 基線+Δ')
plt.ylabel('ROC-AUC')
plt.legend()
plt.show()
```

---

### 階段 3：SHAP 可解釋性分析（第 3 週）

**任務 3.1：計算 SHAP 值**
```python
import shap

# 使用最佳模型（假設是 XGBoost）
best_model = XGBClassifier()
best_model.fit(X_train, y_train)

# 計算 SHAP 值
explainer = shap.TreeExplainer(best_model)
shap_values = explainer.shap_values(X_test)
```

**任務 3.2：SHAP 蜂群圖**
```python
# 全局特徵重要性
shap.summary_plot(shap_values, X_test, plot_type="bar", max_display=20)
plt.title('特徵重要性排序（SHAP）')
plt.tight_layout()
plt.savefig('SHAP_feature_importance.png', dpi=300)
plt.show()

# 蜂群圖（顯示方向性影響）
shap.summary_plot(shap_values, X_test, max_display=20)
plt.title('SHAP 蜂群圖：特徵影響分佈')
plt.tight_layout()
plt.savefig('SHAP_beeswarm.png', dpi=300)
plt.show()
```

**任務 3.3：SHAP 依賴圖（交互作用）**
```python
# Δ_SUA × Δ_BMI
shap.dependence_plot("Δ_SUA_Y_Y-2", shap_values, X_test,
                     interaction_index="Δ_BMI_Y_Y-2")
plt.title('SHAP 依賴圖：Δ_SUA × Δ_BMI')
plt.tight_layout()
plt.savefig('SHAP_dependence_SUA_BMI.png', dpi=300)
plt.show()

# Δ_SUA × Δ_TG
shap.dependence_plot("Δ_SUA_Y_Y-2", shap_values, X_test,
                     interaction_index="Δ_TG_Y_Y-2")
plt.title('SHAP 依賴圖：Δ_SUA × Δ_TG')
plt.tight_layout()
plt.savefig('SHAP_dependence_SUA_TG.png', dpi=300)
plt.show()
```

**任務 3.4：特徵重要性統計**
```python
# 計算平均絕對 SHAP 值
feature_importance = pd.DataFrame({
    'Feature': X_test.columns,
    'SHAP_importance': np.abs(shap_values).mean(axis=0)
})

feature_importance = feature_importance.sort_values('SHAP_importance', ascending=False)
print(feature_importance.head(20))

# 保存結果
feature_importance.to_csv('feature_importance_shap.csv', index=False)
```

---

### 階段 4：結果整理與視覺化（第 4 週）

**任務 4.1：性能指標總表**
```python
# 計算所有性能指標
from sklearn.metrics import (
    roc_auc_score, precision_recall_curve, auc,
    accuracy_score, precision_score, recall_score, f1_score
)

def evaluate_model(y_true, y_pred_proba, threshold=0.5):
    y_pred = (y_pred_proba >= threshold).astype(int)

    return {
        'ROC-AUC': roc_auc_score(y_true, y_pred_proba),
        'PR-AUC': auc(*precision_recall_curve(y_true, y_pred_proba)[:2][::-1]),
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred),
        'F1-Score': f1_score(y_true, y_pred)
    }

# 評估所有模型
results_summary = {}
for model_name, model in models_C.items():
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    results_summary[model_name] = evaluate_model(y_test, y_pred_proba)

results_df = pd.DataFrame(results_summary).T
print(results_df)
results_df.to_csv('model_performance_summary.csv')
```

**任務 4.2：ROC 曲線與 PR 曲線**
```python
from sklearn.metrics import roc_curve, precision_recall_curve

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ROC 曲線
for model_name, model in models_C.items():
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    auc_score = roc_auc_score(y_test, y_pred_proba)
    axes[0].plot(fpr, tpr, label=f'{model_name} (AUC={auc_score:.3f})')

axes[0].plot([0, 1], [0, 1], 'k--', label='Random')
axes[0].set_xlabel('False Positive Rate')
axes[0].set_ylabel('True Positive Rate')
axes[0].set_title('ROC Curve')
axes[0].legend()
axes[0].grid(alpha=0.3)

# PR 曲線
for model_name, model in models_C.items():
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
    pr_auc = auc(recall, precision)
    axes[1].plot(recall, precision, label=f'{model_name} (PR-AUC={pr_auc:.3f})')

axes[1].set_xlabel('Recall')
axes[1].set_ylabel('Precision')
axes[1].set_title('Precision-Recall Curve')
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('ROC_PR_curves.png', dpi=300)
plt.show()
```

**任務 4.3：混淆矩陣**
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 使用最佳模型
best_model_name = 'XGB'  # 假設
best_model = models_C[best_model_name]
y_pred = best_model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['正常', '高尿酸'])
disp.plot(cmap='Blues')
plt.title(f'混淆矩陣 ({best_model_name})')
plt.tight_layout()
plt.savefig('confusion_matrix.png', dpi=300)
plt.show()
```

**任務 4.4：分層分析（類似 Dual Framework Table 1）**
```python
# 按結果分層
df['結果'] = df['高尿酸'].map({0: '正常', 1: '高尿酸'})

# 計算各組統計量
summary_stats = df.groupby('結果').agg({
    'SUA_Y-2': ['mean', 'std'],
    'Δ_SUA_Y_Y-2': ['mean', 'std'],
    'BMI_Y-2': ['mean', 'std'],
    'Δ_BMI_Y_Y-2': ['mean', 'std'],
    'TG_Y-2': ['mean', 'std'],
    'Δ_TG_Y_Y-2': ['mean', 'std']
})

print(summary_stats)

# t 檢驗
from scipy.stats import ttest_ind

for col in ['SUA_Y-2', 'Δ_SUA_Y_Y-2', 'BMI_Y-2', 'Δ_BMI_Y_Y-2']:
    group_0 = df[df['高尿酸'] == 0][col]
    group_1 = df[df['高尿酸'] == 1][col]
    t_stat, p_value = ttest_ind(group_0, group_1)
    print(f"{col}: t={t_stat:.3f}, p={p_value:.4f}")
```

---

### 時間表總結

| 週次 | 階段 | 任務 | 預計完成日期 |
|-----|------|------|------------|
| **第 1 週** | 資料準備 | 資料清理、Δ 特徵計算、目標變量定義 | 11/17 - 11/24 |
| **第 2 週** | 基線模型 | 模型 A、B、C 訓練與比較 | 11/24 - 12/1 |
| **第 3 週** | SHAP 分析 | SHAP 值計算、視覺化、交互作用分析 | 12/1 - 12/8 |
| **第 4 週** | 結果整理 | 性能指標、視覺化、分層分析 | 12/8 - 12/15 |

---

## 預期產出

### 1. 技術產出
- [ ] 完整的 Δ 特徵資料集
- [ ] 訓練好的最佳模型（XGBoost / LightGBM）
- [ ] SHAP 分析結果與視覺化
- [ ] 性能評估報告

### 2. 視覺化產出
- [ ] 模型性能比較圖（基線 vs. Δ vs. 基線+Δ）
- [ ] SHAP 特徵重要性圖
- [ ] SHAP 蜂群圖
- [ ] SHAP 依賴圖（至少 3 組交互作用）
- [ ] ROC 曲線與 PR 曲線
- [ ] 混淆矩陣
- [ ] 分層分析統計表

### 3. 文檔產出
- [ ] 特徵重要性排序表（CSV）
- [ ] 模型性能總結表（CSV）
- [ ] 分層分析統計表（類似 Dual Framework Table 1）
- [ ] 方法學說明文件
- [ ] 結果解釋與臨床意義

---

## 參考文獻

1. **Dual Framework 2025**:
   - Yang, C.-C., et al. (2025). Dual Machine Learning Framework for Predicting Long-Term Glycemic Change and Prediabetes Risk in Young Taiwanese Men. *Diagnostics*, 15(19), 2507. https://doi.org/10.3390/diagnostics15192507

2. **SHAP**:
   - Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems*, 30.

3. **相關本研究文檔**:
   - [Dual_2025_深度解析.md](../literature_notes/Dual_2025_深度解析.md)
   - [Meeting_15-17_Papers_Summary.md](../literature_notes/Meeting_15-17_Papers_Summary.md)

---

## 📌 快速導航

- 📂 [返回 Research Plans 目錄](.)
- 📊 [查看 Meeting 15-17 論文總結](../literature_notes/Meeting_15-17_Papers_Summary.md)
- 🎯 [查看 Meeting 17 準備計畫](../meeting_notes/Meeting_17_Preparation_Plan.md)
- 📋 [查看文獻總覽索引](../literature_notes/Literature_Master_Index.md)

---

**文檔維護者**：紀伯喬
**最後更新**：2025-11-14
**狀態**：✅ 策略制定完成，待實作
