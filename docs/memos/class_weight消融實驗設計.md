# class_weight 消融實驗設計

> **建立日期**：2025-12-04
> **來源**：Meeting 17 討論
> **狀態**：待執行實驗

---

## 背景

我們的資料集存在**嚴重類別不平衡**：

| 疾病 | 正樣本比例 | 負/正比例 |
|------|-----------|----------|
| 高血壓 | ~17% | ~5:1 |
| 高血糖 | ~6% | ~16:1 |
| 高血脂 | ~6% | ~16:1 |

為了處理這個問題，各模型使用了不同的 class_weight 機制。

---

## 各模型 class_weight 使用情況

| 模型 | 參數名稱 | 使用方式 | 備註 |
|------|----------|----------|------|
| **Logistic Regression** | `class_weight='balanced'` | ✅ 自動計算 | sklearn 內建 |
| **Random Forest** | `class_weight='balanced'` | ✅ 自動計算 | sklearn 內建 |
| **XGBoost** | `scale_pos_weight` | ✅ 手動計算 | neg/pos 比例 |
| **ANN (Keras)** | `class_weight` | ✅ 傳入 fit() | 字典格式 |
| **SVM** | `class_weight='balanced'` | ✅ 自動計算 | sklearn 內建 |
| **GP (gplearn)** | ❌ 不支援 | ❌ | **這是 GP 失敗的主因之一** |

---

## class_weight 計算方式

### sklearn balanced 模式

```python
# sklearn 自動計算公式
weight[class] = n_samples / (n_classes * n_samples_class)

# 範例：高血糖（6% 正樣本）
# 假設 n_samples = 6000, n_positive = 360, n_negative = 5640
weight[0] = 6000 / (2 * 5640) = 0.53  # 負樣本權重
weight[1] = 6000 / (2 * 360) = 8.33   # 正樣本權重
```

### XGBoost scale_pos_weight

```python
# XGBoost 計算公式
scale_pos_weight = n_negative / n_positive

# 範例：高血糖
scale_pos_weight = 5640 / 360 = 15.67
```

---

## 實驗設計

### 實驗目標

量化 class_weight 對模型效能的影響，證明其在不平衡資料中的重要性。

### 實驗矩陣

```
5 個模型 × 3 種疾病 × 2 種設定 = 30 組實驗
```

| 模型 | 有 class_weight | 無 class_weight |
|------|----------------|-----------------|
| LR | `class_weight='balanced'` | `class_weight=None` |
| RF | `class_weight='balanced'` | `class_weight=None` |
| XGBoost | `scale_pos_weight=計算值` | `scale_pos_weight=1` |
| ANN | `class_weight={0:w0, 1:w1}` | `class_weight=None` |
| SVM | `class_weight='balanced'` | `class_weight=None` |

### 評估指標

| 指標 | 說明 | 預期變化 |
|------|------|----------|
| **AUC** | 整體區分能力 | 可能小幅下降或持平 |
| **Recall** | 正樣本召回率 | **大幅下降** |
| **F1** | 精確率與召回率調和 | 下降 |
| **Precision** | 正樣本精確率 | 可能上升（因為預測更保守） |

---

## 程式碼範例

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, f1_score, recall_score

# 實驗結果儲存
results = []

diseases = ['高血壓', '高血糖', '高血脂']

for disease in diseases:
    y_train, y_test = get_disease_data(disease)

    # 計算 scale_pos_weight
    neg_count = (y_train == 0).sum()
    pos_count = (y_train == 1).sum()
    scale_weight = neg_count / pos_count

    # 定義模型（有 vs 無 class_weight）
    models = {
        'LR_balanced': LogisticRegression(class_weight='balanced', random_state=42),
        'LR_none': LogisticRegression(class_weight=None, random_state=42),

        'RF_balanced': RandomForestClassifier(class_weight='balanced', random_state=42),
        'RF_none': RandomForestClassifier(class_weight=None, random_state=42),

        'XGB_weighted': XGBClassifier(scale_pos_weight=scale_weight, random_state=42),
        'XGB_none': XGBClassifier(scale_pos_weight=1, random_state=42),

        'SVM_balanced': SVC(class_weight='balanced', probability=True, random_state=42),
        'SVM_none': SVC(class_weight=None, probability=True, random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_proba = model.predict_proba(X_test_scaled)[:, 1]

        results.append({
            '疾病': disease,
            '模型': name,
            'AUC': roc_auc_score(y_test, y_proba),
            'F1': f1_score(y_test, y_pred),
            'Recall': recall_score(y_test, y_pred),
        })

# 整理結果
df_results = pd.DataFrame(results)
```

---

## 預期結果

### 假設

1. **AUC 變化不大**：class_weight 主要影響決策閾值，不影響排序能力
2. **Recall 大幅下降**：沒有 class_weight 時，模型傾向預測多數類（健康）
3. **F1 明顯下降**：Recall 下降導致 F1 下降
4. **高血糖/高血脂影響更大**：因為不平衡程度更嚴重（16:1 vs 5:1）

### 預期數據範例

| 疾病 | 模型 | AUC (有) | AUC (無) | Recall (有) | Recall (無) |
|------|------|---------|---------|-------------|-------------|
| 高血壓 | LR | 0.749 | ~0.74 | 0.73 | **~0.20** |
| 高血糖 | LR | 0.931 | ~0.92 | 0.82 | **~0.10** |
| 高血脂 | LR | 0.888 | ~0.88 | 0.83 | **~0.10** |

---

## 論文價值

### 可寫入論文的內容

1. **方法論章節**：
   - 說明類別不平衡問題
   - 解釋 class_weight 機制
   - 各模型的具體實作方式

2. **實驗結果章節**：
   - 表格：有/無 class_weight 的效能比較
   - 圖表：Recall 變化柱狀圖
   - 討論：為什麼 GP 失敗（不支援 class_weight）

3. **討論章節**：
   - class_weight 在醫療預測的重要性
   - 少數類別（患病者）的識別是臨床核心需求
   - 推薦在不平衡資料中必須使用 class_weight

---

## 與 GP 失敗的關聯

這個實驗可以**直接解釋 GP 為何失敗**：

```
GP 失敗原因分析：
1. gplearn 不支援 class_weight 機制
2. 適應度函數（如 log loss）對多數類更敏感
3. GP 演化出的公式傾向預測「健康」以降低整體錯誤率
4. 結果：高血脂 AUC = 0.5（等同隨機猜測）
```

---

## 執行優先級

- **優先級**：中（核心實驗之一）
- **預估時間**：2-3 小時
- **相依性**：無，可獨立執行
- **產出**：1 張比較表格 + 1 張 Recall 變化圖

---

**相關文件**：
- [訓練集與測試集的切分方式.md](訓練集與測試集的切分方式.md)
- [Next_Steps_Research_Plan.md](../research_plans/Next_Steps_Research_Plan.md)
- [07_GeneticProgramming.ipynb](../../notebooks/experiments/07_GeneticProgramming.ipynb)
