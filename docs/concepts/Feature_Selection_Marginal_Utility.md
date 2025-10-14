# 特徵選擇中的邊際效應遞減

## 概念延伸

**邊際效應遞減不僅適用於「時間序列記錄數」，也適用於「特徵數量」**

在預測模型中：
- **投入**：使用的特徵數量（3個、5個、7個...）
- **收益**：預測準確度（AUC、F1-Score 等）
- **遞減現象**：前 3-5 個最重要特徵可能貢獻 80% 的預測力，之後每增加特徵的邊際貢獻遞減

---

## 本研究的特徵結構

### Synthea_SUA 資料集欄位（15 個）

#### 固定特徵（不隨時間變化）
1. **ID**：病患編號（用於分組，不參與預測）
2. **sex**：性別

#### 動態特徵（每次檢查會變化）
3. **Age**：年齡
4. **BMI**：身體質量指數
5. **SBP**：收縮壓
6. **DBP**：舒張壓
7. **FBG**：空腹血糖
8. **TC**：總膽固醇
9. **Cr**：肌酸酐
10. **GFR**：腎絲球過濾率
11. **UA**：尿酸（目前 100% 缺失）
12. **Times**：檢查次數

#### 預測目標（標籤）
13. **hypertension**：高血壓（Yes/No）
14. **hyperglycemia**：高血糖（Yes/No）
15. **dyslipidemia**：高血脂（Yes/No）

---

## 研究問題

### 核心問題
**使用多少個特徵，能達到最佳的「性能-複雜度」平衡點？**

### 具體實驗設計

#### 特徵工程後的候選特徵
假設使用 2 次記錄（T₁, T₂）預測 T₃：

```python
候選特徵（約 30 個）：
1. sex (固定)
2. Age₂ (T₂ 年齡)

# T₁ 特徵（第一次檢查）
3. BMI₁, 4. SBP₁, 5. DBP₁, 6. FBG₁, 7. TC₁, 8. Cr₁, 9. GFR₁

# T₂ 特徵（第二次檢查）
10. BMI₂, 11. SBP₂, 12. DBP₂, 13. FBG₂, 14. TC₂, 15. Cr₂, 16. GFR₂

# Δ 變化量特徵（T₂ - T₁）
17. ΔBMI, 18. ΔSBP, 19. ΔDBP, 20. ΔFBG, 21. ΔTC, 22. ΔCr, 23. ΔGFR

# 時間特徵
24. days_T1_T2 (T₁→T₂ 間隔天數)
25. days_T2_T3 (T₂→T₃ 間隔天數)

# 衍生特徵
26. Age_BMI_interaction (年齡 × BMI)
27. SBP_DBP_ratio (收縮壓/舒張壓)
28. Cr_GFR_interaction (肌酸酐 × GFR)
29. ...
```

#### 實驗組設計

**目標**：測試使用 Top-K 個重要特徵的預測性能

| 組別 | 使用特徵數 | 特徵選擇方法 | 預期 AUC |
|------|-----------|-------------|---------|
| Group 1 | Top-3 | 最重要的 3 個特徵 | 0.75-0.78 |
| Group 2 | Top-5 | 最重要的 5 個特徵 | 0.78-0.82 |
| Group 3 | Top-7 | 最重要的 7 個特徵 | 0.80-0.84 |
| Group 4 | Top-10 | 最重要的 10 個特徵 | 0.82-0.85 |
| Group 5 | Top-15 | 最重要的 15 個特徵 | 0.83-0.85 |
| Group 6 | All (30) | 所有特徵 | 0.83-0.85（可能過擬合）|

---

## 預期結果圖示

### 1. 準確度 vs. 特徵數量

```
AUC-ROC
  0.85 |                _______________
       |            ___/
  0.80 |        ___/
       |    ___/
  0.75 | __/
       |/
  0.70 |
       +----------------------------------
         3    5    7    10   15   20   30  特徵數

         ↑         ↑              ↑
    Top 核心特徵  次要特徵      邊際貢獻低
```

### 2. 邊際收益（Marginal Gain）

```
△AUC
 0.04 | ██
      | ██
 0.03 | ███
      | ███
 0.02 | ████
      | ████
 0.01 | █████
      | ██████
 0.00 | ████████
      +----------------------------------
        3→5  5→7  7→10  10→15  15→20  20→30

         ↑                            ↑
    邊際收益高                  邊際收益趨近零
```

### 3. 模型複雜度 vs. 性能

```
準確度 ↑                      最佳點
       |                        ●
  0.84 |                    ●       過擬合風險
       |                ●               ●
  0.80 |            ●
       |        ●
  0.75 |    ●                              複雜度 →
       +--------------------------------
         3   5   7   10  15  20  25  30  特徵數
```

---

## 特徵重要性分析方法

### 1. Filter 方法（快速篩選）
```python
from sklearn.feature_selection import mutual_info_classif

# 計算每個特徵與目標的互信息
importance = mutual_info_classif(X, y)

# 選擇 Top-K
selected_features = np.argsort(importance)[-k:]
```

**優點**：
- 計算快速
- 與模型無關

**缺點**：
- 不考慮特徵間的交互作用

### 2. Wrapper 方法（遞迴特徵消除）
```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

# 使用 RFE 選擇 Top-K
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=k)
rfe.fit(X, y)
selected_features = rfe.support_
```

**優點**：
- 考慮特徵組合效果
- 針對特定模型優化

**缺點**：
- 計算成本高

### 3. Embedded 方法（模型內建）
```python
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb

# Random Forest 特徵重要性
rf = RandomForestClassifier()
rf.fit(X, y)
importance = rf.feature_importances_

# XGBoost 特徵重要性
xgb_model = xgb.XGBClassifier()
xgb_model.fit(X, y)
importance = xgb_model.feature_importances_
```

**優點**：
- 訓練過程中自動計算
- 兼顧準確度與效率

---

## 預期的 Top 特徵（假設）

根據文獻與臨床知識，預期最重要的特徵：

### 預測高血壓
1. **SBP₂**（最近一次收縮壓）← 直接相關
2. **DBP₂**（最近一次舒張壓）← 直接相關
3. **ΔSBP**（收縮壓變化）← 趨勢指標
4. **BMI₂**（最近一次 BMI）← 肥胖因子
5. **Age₂**（年齡）← 年齡越大風險越高

### 預測高血糖
1. **FBG₂**（最近一次空腹血糖）← 直接相關
2. **ΔFBG**（血糖變化）← 趨勢指標
3. **BMI₂**（最近一次 BMI）← 肥胖因子
4. **Age₂**（年齡）← 年齡越大風險越高
5. **TC₂**（總膽固醇）← 代謝症候群相關

### 預測高血脂
1. **TC₂**（最近一次總膽固醇）← 直接相關
2. **ΔTC**（膽固醇變化）← 趨勢指標
3. **BMI₂**（最近一次 BMI）← 肥胖因子
4. **Age₂**（年齡）← 年齡越大風險越高
5. **GFR₂**（腎功能）← 代謝相關

---

## 實驗流程

### Step 1: 計算所有特徵的重要性
```python
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# 訓練模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 取得特徵重要性
importance = rf.feature_importances_
feature_names = X_train.columns

# 排序
indices = np.argsort(importance)[::-1]
sorted_features = [(feature_names[i], importance[i]) for i in indices]

print("Top 10 重要特徵:")
for i, (name, score) in enumerate(sorted_features[:10], 1):
    print(f"{i}. {name}: {score:.4f}")
```

### Step 2: 測試不同特徵數量的性能
```python
results = []

for k in [3, 5, 7, 10, 15, 20, 30]:
    # 選擇 Top-K 特徵
    top_k_features = [feature_names[i] for i in indices[:k]]
    X_train_k = X_train[top_k_features]
    X_test_k = X_test[top_k_features]

    # 訓練與評估
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train_k, y_train)

    y_pred = rf.predict_proba(X_test_k)[:, 1]
    auc = roc_auc_score(y_test, y_pred)

    results.append({'k': k, 'auc': auc})
    print(f"Top-{k} 特徵 AUC: {auc:.4f}")

# 計算邊際收益
for i in range(1, len(results)):
    marginal_gain = results[i]['auc'] - results[i-1]['auc']
    print(f"從 Top-{results[i-1]['k']} 到 Top-{results[i]['k']} 的邊際收益: {marginal_gain:.4f}")
```

### Step 3: 視覺化結果
```python
import matplotlib.pyplot as plt

ks = [r['k'] for r in results]
aucs = [r['auc'] for r in results]

plt.figure(figsize=(10, 6))
plt.plot(ks, aucs, marker='o', linewidth=2)
plt.xlabel('特徵數量 (Top-K)', fontsize=12)
plt.ylabel('AUC-ROC', fontsize=12)
plt.title('特徵數量 vs. 預測準確度', fontsize=14)
plt.grid(True, alpha=0.3)
plt.axhline(y=max(aucs), color='r', linestyle='--', alpha=0.5, label='最高 AUC')
plt.legend()
plt.show()
```

---

## 研究意義

### 1. 臨床實用性
- **簡化檢測**：若 Top-5 特徵已達 80% 性能，可減少不必要的檢驗項目
- **成本效益**：減少檢驗項目 → 降低醫療成本
- **可解釋性**：少數核心特徵更易於臨床解釋與應用

### 2. 模型優化
- **避免過擬合**：使用過多特徵可能導致過擬合
- **訓練效率**：特徵少 → 訓練快 → 易於部署
- **泛化能力**：核心特徵通常更穩健

### 3. 理論貢獻
- **特徵飽和點**：證明超過某個數量後，額外特徵對預測的貢獻有限
- **80/20 法則**：少數核心特徵貢獻大部分預測力

---

## 與其他研究對比

| 研究 | 使用特徵數 | AUC | 核心特徵 |
|------|-----------|-----|---------|
| Liu et al. (2024) | 13 個 | 0.93 | HbA1c, FBG, Weight, fT4, TG |
| Taiwan MTL (2025) | 未明確說明 | 0.85-0.88 | 多疾病共享特徵 |
| 本研究 | 3-30（實驗比較）| TBD | 系統性探討最佳特徵數 |

**創新點**：
- 系統性比較不同特徵數量的影響
- 找出邊際效應遞減的臨界點
- 提供「最少但足夠」的特徵組合

---

## 可能的發現

### 情境 A：快速飽和（Top-5 即足夠）
```
Top-3: AUC 0.78
Top-5: AUC 0.82 (+0.04)
Top-7: AUC 0.83 (+0.01)  ← 邊際收益降低
Top-10: AUC 0.83 (+0.00) ← 飽和
```

**結論**：建議使用 Top-5 特徵，後續增加特徵無顯著改善

**臨床建議**：
```
最少但足夠的檢驗組合（以高血糖為例）：
1. 空腹血糖（FBG）
2. BMI
3. 年齡
4. 血糖變化量（ΔFBG）
5. 總膽固醇（TC）

→ 只需這 5 項指標即可達 82% AUC
```

### 情境 B：持續改善但遞減
```
Top-3: AUC 0.75
Top-5: AUC 0.78 (+0.03)
Top-7: AUC 0.81 (+0.03)
Top-10: AUC 0.83 (+0.02)
Top-15: AUC 0.84 (+0.01) ← 仍有貢獻但減少
Top-20: AUC 0.845 (+0.005) ← 邊際收益極低
```

**結論**：Top-10 是性能與複雜度的平衡點

### 情境 C：過擬合警訊
```
Top-5: Train AUC 0.80, Test AUC 0.79 (差距 0.01)
Top-10: Train AUC 0.85, Test AUC 0.82 (差距 0.03)
Top-20: Train AUC 0.92, Test AUC 0.80 (差距 0.12) ← 過擬合！
```

**結論**：使用過多特徵導致過擬合，需限制特徵數

---

## 多疾病預測的特殊考量

### 共享特徵 vs. 疾病專屬特徵

#### 高血壓專屬
- SBP₂, DBP₂, ΔSBP, ΔDBP

#### 高血糖專屬
- FBG₂, ΔFBG

#### 高血脂專屬
- TC₂, ΔTC, Cr₂, GFR₂

#### 共享特徵（三高共用）
- Age₂, BMI₂, ΔBMI, sex

### 實驗設計
**問題**：三高預測是否能共享同一組特徵？

| 實驗組 | 高血壓 Top-K | 高血糖 Top-K | 高血脂 Top-K | 方法 |
|--------|------------|------------|------------|------|
| Group 1 | 獨立 Top-5 | 獨立 Top-5 | 獨立 Top-5 | 每個疾病用專屬特徵 |
| Group 2 | 共享 Top-10 | 共享 Top-10 | 共享 Top-10 | 三高共用同一組特徵 |
| Group 3 | 共享 5 + 專屬 3 | 共享 5 + 專屬 3 | 共享 5 + 專屬 3 | 混合策略 |

**預期**：
- Group 3（混合策略）可能表現最佳
- 共享特徵提供基礎預測力，專屬特徵提升個別疾病準確度

---

## 實驗挑戰與解決方案

### 挑戰 1: 特徵間相關性
**問題**：SBP₂ 和 DBP₂ 高度相關（r > 0.8）

**解決方案**：
- 使用 VIF（Variance Inflation Factor）檢測多重共線性
- 移除高度相關的特徵之一
- 或使用 PCA 降維

### 挑戰 2: 缺失值影響特徵選擇
**問題**：
- FBG: 68.96% 缺失
- TC: 72.22% 缺失

**解決方案**：
- 先填補缺失值（mean/median/KNN imputation）
- 再進行特徵選擇
- 或在不同缺失值處理策略下分別實驗

### 挑戰 3: 類別不平衡
**問題**：三高陽性率可能僅 5-15%

**解決方案**：
- 使用 Stratified K-Fold 確保每個 fold 的類別分布一致
- 調整 class weight
- 使用 SMOTE 過採樣（謹慎使用）

---

## 論文撰寫重點

### 可能的章節標題
> **Feature Selection via Diminishing Marginal Returns: Identifying the Minimal Sufficient Feature Set for Multi-Disease Prediction**

### 關鍵圖表
1. **Figure 1**: 特徵重要性排序（Bar chart）
2. **Figure 2**: 準確度 vs. 特徵數量曲線（Line plot）
3. **Figure 3**: 邊際收益圖（Bar chart showing △AUC）
4. **Table 1**: 不同特徵數的性能比較（含 Train/Test AUC）
5. **Table 2**: Top-10 核心特徵與其重要性分數

### Discussion 要點
- 本研究發現 **Top-5 特徵已達 80% 性能**（假設）
- 與 Liu et al.（使用 13 個特徵）對比 → 更精簡
- 臨床建議：優先檢測這 5 項指標即可達有效預測
- 成本效益：減少 60% 檢驗項目，僅損失 5% 準確度

---

## 與「時間序列記錄數」的綜合實驗

### 二維探索：記錄數 × 特徵數

| 記錄數 \ 特徵數 | Top-3 | Top-5 | Top-7 | Top-10 | Top-15 |
|----------------|-------|-------|-------|--------|--------|
| **2 次** | 0.75 | 0.78 | 0.80 | 0.81 | 0.81 |
| **3 次** | 0.78 | 0.82 | 0.84 | 0.85 | 0.85 |
| **4 次** | 0.80 | 0.83 | 0.85 | 0.86 | 0.86 |
| **5 次** | 0.81 | 0.84 | 0.86 | 0.87 | 0.87 |

**熱圖視覺化**：
```
        Top-3  Top-5  Top-7  Top-10 Top-15
2 次    [0.75] [0.78] [0.80] [0.81] [0.81]
3 次    [0.78] [0.82] [0.84] [0.85] [0.85]
4 次    [0.80] [0.83] [0.85] [0.86] [0.86]
5 次    [0.81] [0.84] [0.86] [0.87] [0.87]

顏色: 深綠（高 AUC）→ 淺綠（低 AUC）
```

**發現最佳組合**：
- **性能優先**：5 次記錄 + Top-10 特徵（AUC 0.87）
- **平衡選擇**：3 次記錄 + Top-5 特徵（AUC 0.82，成本低）
- **最簡配置**：2 次記錄 + Top-3 特徵（AUC 0.75，快速篩檢）

---

## 會議討論紀錄

**日期**: 2025-01-14（推測）
**提出人**: 教授
**核心概念**: 邊際效應遞減也適用於**特徵選擇**
**實驗方向**: 測試 Top-3, 5, 7 個特徵對預測準確度的影響
**預期發現**: 少數核心特徵已能提供大部分預測力，後續增加特徵效益遞減
**臨床價值**: 找到「最少但足夠」的檢驗項目組合

---

## 後續工作

- [ ] 完成 Synthea 資料轉換與特徵工程
- [ ] 計算所有候選特徵的重要性
- [ ] 實驗不同特徵數量（3, 5, 7, 10, 15, 30）的性能
- [ ] 視覺化準確度-特徵數曲線與邊際收益圖
- [ ] 分析三高是否能共享特徵或需專屬特徵
- [ ] 撰寫論文章節：Feature Selection Experiments

---

## 標籤

`#特徵選擇` `#邊際效應遞減` `#特徵重要性` `#模型簡化` `#臨床實用性` `#成本效益` `#80-20法則` `#可解釋性`
