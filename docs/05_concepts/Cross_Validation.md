# Cross-Validation（交叉驗證）

## 基本概念

Cross-validation 是一種評估模型泛化能力的統計方法，透過將資料分成多份並輪流作為訓練集與驗證集，來獲得更可靠的性能估計。

---

## K-Fold Cross-Validation

### 原理
將資料分成 K 份（通常 K=5 或 10），輪流使用其中 1 份作為驗證集，其餘 K-1 份作為訓練集，重複 K 次。

### 示例（K=5）

```
第1輪: [驗證] [訓練] [訓練] [訓練] [訓練]
第2輪: [訓練] [驗證] [訓練] [訓練] [訓練]
第3輪: [訓練] [訓練] [驗證] [訓練] [訓練]
第4輪: [訓練] [訓練] [訓練] [驗證] [訓練]
第5輪: [訓練] [訓練] [訓練] [訓練] [驗證]

最終結果 = 5 次驗證結果的平均值
```

### 優點
- **充分利用資料**：每筆資料都會被用於訓練和驗證
- **減少偶然性**：避免單次分割造成的偏差
- **更可靠的性能估計**：多次驗證的平均更穩定

### 缺點
- **計算成本高**：需要訓練 K 次模型
- **時間消耗**：對大型資料集或複雜模型較慢

---

## 常見變體

### 1. Stratified K-Fold
- **適用情境**：類別不平衡資料
- **特點**：確保每個 fold 的類別分布與整體資料一致
- **範例**：若整體資料有 10% 陽性樣本，每個 fold 也維持 10%

### 2. Group K-Fold
- **適用情境**：有群組結構的資料（如同一病患的多次記錄）
- **特點**：同一群組的資料不會被分散到訓練集與驗證集
- **重要性**：避免資料洩漏（data leakage）

**範例**：
```
病患 A 的所有記錄 → 全部放在訓練集或全部放在驗證集
病患 B 的所有記錄 → 全部放在訓練集或全部放在驗證集
...
```

### 3. Time Series Split
- **適用情境**：時間序列資料
- **特點**：只使用過去資料訓練，未來資料驗證
- **重要性**：符合實際應用情境（無法用未來預測過去）

**範例**：
```
第1輪: [訓練] | [驗證] - - -
第2輪: [訓練] [訓練] | [驗證] - -
第3輪: [訓練] [訓練] [訓練] | [驗證] -
第4輪: [訓練] [訓練] [訓練] [訓練] | [驗證]
```

### 4. Leave-One-Out Cross-Validation (LOOCV)
- **特點**：K = N（資料總數），每次只留 1 筆作為驗證集
- **優點**：最大化訓練資料
- **缺點**：計算成本極高，適合小資料集

---

## 本研究的應用

### 資料特性
- 1,155 位病患，每位有 3+ 次記錄
- 同一病患的多次記錄具有相關性

### 推薦方法：Group K-Fold

**為什麼？**
1. **避免資料洩漏**：同一病患的 T₁、T₂ 不能分散在訓練集與驗證集
2. **真實泛化能力**：測試模型對「新病患」的預測能力，而非對「同一病患不同時間點」的預測

**實作方式**：
```python
from sklearn.model_selection import GroupKFold

gkf = GroupKFold(n_splits=5)
for train_idx, val_idx in gkf.split(X, y, groups=patient_ids):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
    # 訓練與評估模型
```

### 與 Train-Val-Test Split 的關係

**標準流程**：
1. 先按病患分割出 **Test Set**（15%，完全不參與訓練）
2. 剩餘資料（85%）用 **Group K-Fold** 進行訓練與驗證
3. 最終在 Test Set 上報告性能

**好處**：
- Cross-validation 用於模型選擇與超參數調優
- Test Set 提供最終的無偏估計

---

## 評估指標

Cross-validation 可以計算：
- **平均性能**：K 次驗證的 AUC、F1-Score、Recall 等的平均
- **標準差**：評估模型穩定性
- **95% 信賴區間**：提供統計顯著性

**範例**：
```
5-Fold CV Results:
- AUC: 0.82 ± 0.03 (mean ± std)
- F1-Score: 0.68 ± 0.05
- Recall: 0.71 ± 0.04
```

---

## 常見誤區

### ❌ 錯誤做法
```python
# 在整個資料集上做特徵標準化，再進行 CV
scaler.fit(X)  # ← 資料洩漏！
X_scaled = scaler.transform(X)
cross_val_score(model, X_scaled, y, cv=5)
```

### ✅ 正確做法
```python
# 在每個 fold 內部分別做特徵處理
for train_idx, val_idx in kf.split(X):
    X_train, X_val = X[train_idx], X[val_idx]

    scaler.fit(X_train)  # ← 只用訓練集統計量
    X_train_scaled = scaler.transform(X_train)
    X_val_scaled = scaler.transform(X_val)

    model.fit(X_train_scaled, y_train)
    score = model.score(X_val_scaled, y_val)
```

---

## 延伸閱讀

- [Sklearn Cross-Validation Documentation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Time Series Split 詳解](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)
- [Group K-Fold 範例](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html)

---

## 標籤

`#交叉驗證` `#模型評估` `#資料分割` `#泛化能力` `#Group-K-Fold` `#避免資料洩漏`
