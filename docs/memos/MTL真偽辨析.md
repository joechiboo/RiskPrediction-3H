# MTL 真偽辨析

> **建立日期**：2025-12-08
> **目的**：釐清哪些是真正的 MTL，哪些是假的
> **狀態**：已確認

---

## 問題：什麼是真正的 MTL？

在我們的實驗中，並非所有標示為 "MTL" 的方法都是真正的 Multi-Task Learning。

---

## 真 MTL vs 假 MTL

### ✅ 真 MTL：共享參數的多任務學習

**定義**：
- 模型底層參數在多個任務之間**共享**
- 只有最後的輸出層針對不同任務分開
- **訓練一次**，同時學習所有任務

**範例**：ANN (Artificial Neural Network)

```python
# 真 MTL：共享隱藏層的神經網路
model = Sequential([
    Dense(64, activation='relu'),  # ← 共享層（3 個任務共用）
    Dense(32, activation='relu'),  # ← 共享層（3 個任務共用）
    Dense(3, activation='sigmoid') # ← 輸出層（3 個輸出節點）
])

# 一次訓練，同時學習 3 個任務
model.fit(X_train, y_train_multi)  # y_train_multi: (n_samples, 3)
```

**結構圖**：

```text
輸入層 (特徵)
    ↓
共享隱藏層 1 (64 neurons) ← 3 個任務共用
    ↓
共享隱藏層 2 (32 neurons) ← 3 個任務共用
    ↓
    ├─→ 輸出 1 (高血壓)
    ├─→ 輸出 2 (高血糖)
    └─→ 輸出 3 (高血脂)
```

**優點**：
- ✅ 真正共享知識
- ✅ 任務間可以互相幫助（transfer learning）
- ✅ 參數數量少（節省記憶體）
- ✅ 訓練時間短（一次訓練）

---

### ⚠️ 假 MTL：MultiOutputClassifier 包裝器

**定義**：
- 使用 `sklearn.multioutput.MultiOutputClassifier`
- **實際上還是訓練 3 個獨立模型**
- 沒有參數共享
- 只是包裝成一個介面而已

**範例**：LR, RF, SVM, XGBoost, GP

```python
# 假 MTL：包裝器
from sklearn.multioutput import MultiOutputClassifier

mtl_model = MultiOutputClassifier(
    LogisticRegression(class_weight='balanced')
)
mtl_model.fit(X_train, y_train_multi)

# 等價於（內部實作）
models = []
for i in range(3):  # 3 個疾病
    model = LogisticRegression(class_weight='balanced')
    model.fit(X_train, y_train_multi[:, i])  # 訓練 3 次！
    models.append(model)
```

**結構圖**：

```text
輸入層 (特徵)
    ↓
    ├─→ 模型 1 (LR) → 輸出 1 (高血壓)
    ├─→ 模型 2 (LR) → 輸出 2 (高血糖)
    └─→ 模型 3 (LR) → 輸出 3 (高血脂)

3 個完全獨立的模型！
```

**缺點**：
- ❌ 沒有參數共享
- ❌ 任務間無法互相學習
- ❌ 訓練時間 ≈ Single-Task × 3
- ❌ 模型大小 ≈ Single-Task × 3

**為什麼還叫 MTL？**
- 只是 sklearn 提供的統一介面
- 方便一次預測多個輸出
- **但本質上不是真正的 MTL**

---

## 我們的實驗分類

### ✅ 真 MTL

| Notebook | 模型 | 共享參數 | 真/假 |
|----------|------|----------|:-----:|
| **05_NeuralNetworks** | ANN | ✅ 共享隱藏層 | ✅ **真** |

---

### ⚠️ 假 MTL（MultiOutputClassifier 包裝器）

| Notebook | 模型 | 共享參數 | 真/假 |
|----------|------|----------|:-----:|
| **03_ModelBuilding** | Logistic Regression | ❌ 3 個獨立模型 | ❌ **假** |
| **03_ModelBuilding** | Random Forest | ❌ 3 個獨立模型 | ❌ **假** |
| **04_XGBoost** | XGBoost | ❌ 3 個獨立模型 | ❌ **假** |
| **06_SVM** | SVM | ❌ 3 個獨立模型 | ❌ **假** |
| **07_GeneticProgramming** | GP | ❌ 3 個獨立模型 | ❌ **假** |

---

## 為什麼保留「假 MTL」？

雖然 LR、RF、SVM、XGBoost、GP 的 "MTL" 是假的，但仍有價值：

### 1. 推論時間優勢

```python
# Single-Task：需要呼叫 3 次
pred1 = model1.predict_proba(X_test)  # 0.01 秒
pred2 = model2.predict_proba(X_test)  # 0.01 秒
pred3 = model3.predict_proba(X_test)  # 0.01 秒
# 總計：0.03 秒

# MultiOutputClassifier：只需呼叫 1 次
preds = mtl_model.predict_proba(X_test)  # 0.02 秒
# 加速：1.5x
```

**原因**：
- 避免重複的資料預處理
- 單次函式呼叫開銷
- 內部可能有平行化優化

### 2. 模型大小優勢

```python
# Single-Task：3 個獨立物件
pickle.dump(model1, f1)  # 15 KB
pickle.dump(model2, f2)  # 15 KB
pickle.dump(model3, f3)  # 15 KB
# 總計：45 KB

# MultiOutputClassifier：1 個包裝物件
pickle.dump(mtl_model, f)  # 38 KB
# 節省：7 KB (15%)
```

**原因**：
- 共享包裝器的 metadata
- 序列化開銷減少

### 3. 介面一致性

```python
# 統一介面，方便比較
models = {
    'LR_MTL': MultiOutputClassifier(LogisticRegression(...)),
    'RF_MTL': MultiOutputClassifier(RandomForestClassifier(...)),
    'ANN_MTL': ann_model  # 真 MTL
}

# 都用相同方式預測
for name, model in models.items():
    preds = model.predict_proba(X_test)
```

---

## 論文中如何呈現

### 建議寫法

#### 方法論章節

> 我們實驗了兩種多任務學習（MTL）方法：
>
> 1. **真 MTL (Parameter Sharing)**：使用神經網路的共享隱藏層，同時學習三種疾病的預測。底層參數在任務間共享，只有最後的輸出層分開。
>
> 2. **Multi-Output Wrapper**：使用 `MultiOutputClassifier` 包裝傳統機器學習模型（LR、RF、XGBoost、SVM），提供統一的多輸出介面。雖然內部仍訓練獨立模型，但在推論時可一次預測所有任務。

#### 結果章節

> 表 X 展示了不同方法的計算效益。真 MTL (ANN) 在訓練時間上有顯著優勢（加速 2.5x），因為只需訓練一次。Multi-Output Wrapper 方法在推論時間上也有小幅提升（1.5x），主要來自單次函式呼叫的開銷減少。

#### 討論章節

> 值得注意的是，MultiOutputClassifier 並非真正的參數共享 MTL，而是將多個獨立模型包裝成統一介面。真正的 MTL（如本研究使用的神經網路）能夠透過共享表徵（shared representation）在任務間傳遞知識，這在理論上可能帶來效能提升。然而，在我們的實驗中，ANN MTL 的效能並未超越傳統方法（表 Y），這可能與資料量有關...

---

## 實驗建議

### 保留「假 MTL」的理由

1. **計算效益有實際價值**：
   - 推論時間加速 1.5x
   - 模型大小節省 15%
   - 對生產環境有意義

2. **論文豐富性**：
   - 展示對 MTL 的深入理解
   - 比較真假 MTL 的差異
   - 討論 wrapper 方法的實用性

3. **已經完成實驗**：
   - 不需要額外工作
   - 結果可直接使用

### 論文撰寫重點

✅ **要做**：
- 清楚說明真 MTL vs wrapper 的差異
- 強調 ANN 是唯一真正的 MTL
- 討論 wrapper 的實用價值（推論加速）

❌ **避免**：
- 不要把 wrapper 當成真 MTL
- 不要誇大 wrapper 的效能提升
- 不要混淆兩種方法的原理

---

## 總結表

| 模型 | MTL 類型 | 參數共享 | 訓練時間 | 推論時間 | 模型大小 |
|------|----------|----------|----------|----------|----------|
| **ANN** | 真 MTL | ✅ | **快** (1x) | **快** (1x) | **小** (1x) |
| **LR/RF/XGB/SVM/GP** | Wrapper | ❌ | 慢 (≈3x) | 中 (≈2x) | 大 (≈3x) |

---

## 相關文件

- [MTL實驗保留與分析.md](MTL實驗保留與分析.md)
- [MTL計算效益補充程式碼.md](MTL計算效益補充程式碼.md)

---

**結論**：只有 ANN 是真 MTL，其他都是假的。但「假 MTL」仍有實用價值，可保留在論文中，只需清楚說明差異。
