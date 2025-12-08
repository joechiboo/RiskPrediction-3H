# class_weight 與 SMOTE 比較

> **建立日期**：2025-12-08
> **目的**：釐清兩種處理類別不平衡的方法差異
> **狀態**：待討論是否加入 SMOTE 實驗

---

## 背景：類別不平衡問題

我們的資料集存在嚴重的類別不平衡：

| 疾病 | 正樣本比例 | 負/正比例 |
|------|-----------|----------|
| 高血壓 | ~17% | ~5:1 |
| 高血糖 | ~6% | ~16:1 |
| 高血脂 | ~6% | ~16:1 |

**問題**：模型會傾向預測多數類（健康），導致患者被漏診。

---

## 解決方案比較

### 方法 1：class_weight（權重調整）⭐ 目前使用

#### 原理

**不改變資料，只調整損失函數的權重**

```python
# sklearn 自動計算
weight[class] = n_samples / (n_classes × n_samples_class)

# 範例：高血糖（6% 正樣本）
# n_samples = 6000, n_positive = 360, n_negative = 5640
weight[0] = 6000 / (2 × 5640) = 0.53  # 負樣本權重
weight[1] = 6000 / (2 × 360) = 8.33   # 正樣本權重 ← 高很多！

# 模型訓練時
loss = Σ weight[y_true] × error(y_pred, y_true)
```

**效果**：正樣本的錯誤會被放大 8.33 倍，迫使模型更重視少數類。

#### 使用方式

```python
# Logistic Regression / Random Forest / SVM
model = LogisticRegression(class_weight='balanced')

# XGBoost
scale_pos_weight = n_negative / n_positive  # 15.67
model = XGBClassifier(scale_pos_weight=scale_pos_weight)

# ANN (Keras)
class_weight = {0: 0.53, 1: 8.33}
model.fit(X_train, y_train, class_weight=class_weight)
```

#### 優點

- ✅ **不增加資料量**：訓練速度快，記憶體需求低
- ✅ **不產生假資料**：保持原始資料真實性
- ✅ **sklearn 內建**：大多數模型都支援
- ✅ **簡單有效**：一行程式碼就能解決

#### 缺點

- ⚠️ **過度關注少數類**：可能導致過擬合
- ⚠️ **不改變資料分布**：決策邊界可能不夠好
- ⚠️ **需要模型支援**：gplearn 不支援（這是 GP 失敗的主因）

---

### 方法 2：SMOTE（合成少數類過採樣）

#### 原理

**改變資料，生成新的合成樣本**

```text
原始資料：
  正樣本 (患病)：360 個
  負樣本 (健康)：5640 個
  比例：1:15.67

↓ 套用 SMOTE

新資料：
  正樣本：5640 個（360 原始 + 5280 合成）← 補齊！
  負樣本：5640 個
  比例：1:1
```

#### 合成方法

```python
# SMOTE 演算法
1. 選擇一個正樣本 A
2. 找到 A 的 k 個最近鄰居（k=5，預設）
3. 隨機選一個鄰居 B
4. 在 A 和 B 之間插值生成新樣本

新樣本 = A + λ × (B - A)  # λ ∈ [0, 1] 隨機

# 範例
A = [FPG=110, BMI=25, SBP=130]
B = [FPG=115, BMI=26, SBP=135]
λ = 0.6

新樣本 = [110, 25, 130] + 0.6 × ([115, 26, 135] - [110, 25, 130])
       = [110, 25, 130] + 0.6 × [5, 1, 5]
       = [113, 25.6, 133]  ← 合成的「虛擬患者」
```

#### 使用方式

```python
from imblearn.over_sampling import SMOTE

# 套用 SMOTE
smote = SMOTE(random_state=42, k_neighbors=5)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# 訓練模型
model = LogisticRegression()  # 不需要 class_weight
model.fit(X_train_resampled, y_train_resampled)
```

#### 優點

- ✅ **增加正樣本多樣性**：不只是重複樣本
- ✅ **改善決策邊界**：模型有更多正樣本學習
- ✅ **適用所有模型**：不需要模型支援 class_weight
- ✅ **對 SVM 特別有效**：決策邊界更清晰

#### 缺點

- ⚠️ **訓練資料暴增**：
  - 原始：6000 筆
  - SMOTE 後：11280 筆（幾乎翻倍）
  - 訓練時間 ↑、記憶體 ↑
- ⚠️ **產生不真實的資料**：合成的患者不存在
- ⚠️ **可能過擬合**：過度採樣雜訊樣本
- ⚠️ **不適合類別重疊**：如果正負樣本混在一起，會產生錯誤樣本

---

## 完整比較表

| 項目 | class_weight | SMOTE |
|------|--------------|-------|
| **方法類型** | Cost-Sensitive Learning | Over-Sampling |
| **原理** | 調整損失函數權重 | 生成合成樣本 |
| **改變資料嗎** | ❌ 否 | ✅ 是（增加樣本） |
| **訓練資料量** | 不變 | 暴增（可能翻倍） |
| **訓練時間** | 快 ⚡ | 慢 🐢 |
| **記憶體需求** | 低 | 高 |
| **實作難度** | 簡單（一行） | 簡單（需額外套件） |
| **適用模型** | 需模型支援 | 所有模型 |
| **資料真實性** | 保持真實 | 產生假資料 |
| **過擬合風險** | 中 | 高 |
| **決策邊界** | 可能不夠好 | 更清晰 |

---

## 我們目前的做法

### ✅ 已使用：class_weight

| 模型 | 參數名稱 | 使用方式 |
|------|----------|----------|
| **Logistic Regression** | `class_weight='balanced'` | ✅ |
| **Random Forest** | `class_weight='balanced'` | ✅ |
| **XGBoost** | `scale_pos_weight` | ✅ |
| **ANN (Keras)** | `class_weight` | ✅ |
| **SVM** | `class_weight='balanced'` | ✅ |
| **GP (gplearn)** | ❌ 不支援 | ❌ **這是 GP 失敗的主因** |

### ❓ 待評估：SMOTE

目前尚未使用 SMOTE。

---

## 實驗建議

### 策略 1：class_weight 消融實驗（優先）

**目的**：證明 class_weight 的重要性

```python
# 有 class_weight vs 無 class_weight
models = {
    'LR_balanced': LogisticRegression(class_weight='balanced'),
    'LR_none': LogisticRegression(class_weight=None)
}

# 預期：無 class_weight 時 Recall 大幅下降
```

**參考文件**：[class_weight消融實驗設計.md](class_weight消融實驗設計.md)

---

### 策略 2：SMOTE 實驗（可選）

**目的**：探索 SMOTE 能否進一步提升效能

```python
# 實驗組合
1. Baseline (無處理)
2. class_weight only
3. SMOTE only
4. SMOTE + class_weight
```

**預期結果**：

| 組合 | AUC | Recall | 訓練時間 |
|------|-----|--------|----------|
| Baseline | 低 | **極低** | 快 |
| class_weight | 高 | 高 | 快 |
| SMOTE | 中 | 中 | **慢** |
| SMOTE + class_weight | **最高?** | **最高?** | **最慢** |

**論文價值**：
- ✅ 可寫入方法論章節
- ✅ 展示對不平衡問題的深入理解
- ✅ 比較不同方法的優缺點

---

### 策略 3：兩者結合（進階）

```python
from imblearn.over_sampling import SMOTE

# Step 1: 先用 SMOTE 增加正樣本
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Step 2: 仍然使用 class_weight（雙重保險）
model = LogisticRegression(class_weight='balanced')
model.fit(X_train_smote, y_train_smote)
```

**優點**：結合兩者優勢
**缺點**：可能過度調整，導致過擬合

---

## 相關文件

- [class_weight消融實驗設計.md](class_weight消融實驗設計.md)
- [訓練集與測試集的切分方式.md](訓練集與測試集的切分方式.md)
- [論文候選清單_從Dual2025延伸.md](論文候選清單_從Dual2025延伸.md) - #9 SMOTE + SHAP 論文

---

## 結論

### 當前建議

1. **保持 class_weight**：簡單、快速、有效
2. **執行 class_weight 消融實驗**：證明其重要性
3. **考慮加入 SMOTE 實驗**：如果時間允許，可豐富論文

### 優先順序

1. 🔥🔥 class_weight 消融實驗（必做）
2. 🔥 閱讀 SMOTE + SHAP 論文（#9）
3. 🟡 SMOTE 實驗（時間允許）

---

**下一步**：討論是否要加入 SMOTE 實驗到 Meeting 18 的任務清單。
