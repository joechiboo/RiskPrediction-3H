# Attention 機制應用指南

## 概述

Attention 機制是深度學習中用於提升模型可解釋性的重要技術，讓模型能夠「專注」在輸入特徵中最重要的部分。本文件說明如何在三高預測研究中應用 Attention 機制。

---

## 什麼是 Attention Score？

**Attention Score（注意力分數）** 是模型對每個輸入特徵的重要性評估：
- 數值範圍：通常在 0-1 之間（經過 softmax 標準化）
- 數值越高：表示模型認為該特徵對預測結果越重要
- 可解釋性：幫助理解模型的決策依據

### 數學定義

```
Attention(Q, K, V) = softmax(Q × K^T / √d_k) × V
```

其中：
- Q (Query): 查詢向量
- K (Key): 鍵向量
- V (Value): 值向量
- d_k: 鍵向量的維度

---

## Attention vs SHAP 比較

| 比較項目 | Attention Score | SHAP Value |
|---------|----------------|------------|
| **計算時機** | 模型訓練時學習 | 模型訓練後計算 |
| **理論基礎** | 神經網路可學習權重 | 賽局理論 (Shapley Value) |
| **適用模型** | 僅神經網路 | 所有模型（model-agnostic） |
| **輸出含義** | 相對重要性 (0-1) | 特徵貢獻值（可正可負） |
| **計算成本** | 低（推論時直接得到） | 高（需重複計算） |
| **理論保證** | 無 | 有（滿足公平性等公理） |
| **視覺化** | 熱力圖、條形圖 | 瀑布圖、蜂群圖、力圖 |

### 何時使用？

**Attention Score**
- ✅ 想要展示神經網路的「內建可解釋性」
- ✅ 需要即時解釋（推論時直接輸出）
- ✅ 分析不同任務關注的特徵差異

**SHAP Value**
- ✅ 需要公平比較不同模型（LR, RF, NN）
- ✅ 要求理論保證和數學嚴謹性
- ✅ 分析單一樣本的詳細貢獻

**建議：兩者都用**
- 用 SHAP 比較所有模型（Interpretable vs Black-box）
- 用 Attention 展示神經網路的額外優勢

---

## Taiwan MTL 論文中的應用

### 研究背景
- **論文**：Multitask learning multimodal network for chronic disease prediction (2025)
- **作者**：Hsinhan Tsai et al., National Taiwan University
- **期刊**：Scientific Reports

### Attention 使用方式

#### 1. Multi-Head Self-Attention (MHSA) 層
```
輸入：180 個 ICD 代碼 embedding
↓
MHSA 計算疾病之間的相關性
↓
輸出：加權後的疾病特徵表示
```

**超參數設定**（論文 Page 4）：
- Number of heads: 1
- Key dimension: 16
- Value dimension: 8

#### 2. Attention Score 分析（論文 Page 9-10）

**方法**：
1. 選取預測分數最高的 2000 位患者
2. 識別 attention score 最高的 ICD 代碼配對
3. 分類為三類風險因子

**發現的關鍵疾病**：

| 類別 | ICD 代碼 | 疾病名稱 | 醫學意義 |
|------|----------|----------|----------|
| **可修改風險因子** | 272.0 | Pure hypercholesterolemia | 純高膽固醇血症 |
| | 272.2 | Mixed hyperlipidemia | 混合型高脂血症 |
| | 272.4 | Other hyperlipidemia | 其他高脂血症 |
| **多重慢性病** | 274.9 | Gout, unspecified | 痛風 |
| | 366.10 | Senile cataract | 老年性白內障 |
| | 571.40 | Chronic hepatitis | 慢性肝炎 |
| | 585 | Chronic renal failure | 慢性腎衰竭 |
| | 715.36 | Osteoarthrosis, lower leg | 下肢骨關節炎 |
| **新興因子** | 300.00 | Anxiety state | 焦慮症 |
| | 300.4 | Neurotic depression | 神經性憂鬱症 |

**結論**：
- Attention scores 與醫學文獻一致
- 驗證了模型的可解釋性和可信度

---

## 在三高預測研究中的應用

### 我們的研究 vs Taiwan MTL 論文

| 項目 | Taiwan MTL (2025) | 我們的研究 |
|------|-------------------|-----------|
| **預測目標** | 糖尿病、心臟病、中風、高血壓 | 高血糖、高血壓、高血脂 |
| **輸入資料** | ICD 診斷代碼序列（10年） | HRS 調查資料 |
| **特徵類型** | 醫療紀錄 + 個人資訊 | 人口統計 + 生活方式 + 生物指標 |
| **資料來源** | 台灣健保資料庫 | Health and Retirement Study |
| **樣本數** | 555,124 | 待確認 |

### 關鍵差異：不能直接使用 ICD Embedding

**原因**：
- 他們：有 ICD 診斷代碼序列 → 可用 Word2Vec 做 ICD embedding
- 我們：沒有 ICD 代碼，只有問卷調查變數 → 不適用 ICD embedding

**但可以借鑑**：
- ✅ Multi-Task Learning 架構
- ✅ Attention 機制的可解釋性分析方法
- ✅ 特徵重要性評估框架

---

## 建議的模型架構

### 方案 1：Feature-level Attention

適用於我們的 HRS 資料（無序列結構）

```python
import torch
import torch.nn as nn

class FeatureAttention(nn.Module):
    """特徵層級的 Attention 機制"""
    def __init__(self, input_dim):
        super().__init__()
        self.attention_weights = nn.Linear(input_dim, 1)

    def forward(self, x):
        # x: [batch_size, num_features]
        scores = self.attention_weights(x)  # [batch_size, 1]
        attention = torch.softmax(scores, dim=1)
        weighted_features = x * attention
        return weighted_features, attention

class MTL_3H_Model(nn.Module):
    """三高預測的多任務學習模型"""
    def __init__(self, input_dim, hidden_dim=128):
        super().__init__()

        # 共享層
        self.shared_layer = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3)
        )

        # Attention 層
        self.attention = FeatureAttention(hidden_dim)

        # 任務特定層
        self.task_hypertension = nn.Linear(hidden_dim, 1)      # 高血壓
        self.task_hyperglycemia = nn.Linear(hidden_dim, 1)     # 高血糖
        self.task_dyslipidemia = nn.Linear(hidden_dim, 1)      # 高血脂

    def forward(self, x):
        # 共享特徵提取
        shared_features = self.shared_layer(x)

        # Attention 加權
        weighted_features, attention_scores = self.attention(shared_features)

        # 各任務預測
        pred_hypertension = torch.sigmoid(self.task_hypertension(weighted_features))
        pred_hyperglycemia = torch.sigmoid(self.task_hyperglycemia(weighted_features))
        pred_dyslipidemia = torch.sigmoid(self.task_dyslipidemia(weighted_features))

        return {
            'predictions': {
                'hypertension': pred_hypertension,
                'hyperglycemia': pred_hyperglycemia,
                'dyslipidemia': pred_dyslipidemia
            },
            'attention_scores': attention_scores
        }
```

### 方案 2：Task-specific Attention

每個任務有自己的 Attention 機制

```python
class TaskSpecificAttention(nn.Module):
    """任務特定的 Attention 機制"""
    def __init__(self, input_dim, num_tasks=3):
        super().__init__()
        self.num_tasks = num_tasks

        # 為每個任務建立獨立的 attention
        self.attention_layers = nn.ModuleList([
            nn.Linear(input_dim, 1) for _ in range(num_tasks)
        ])

    def forward(self, x, task_id):
        scores = self.attention_layers[task_id](x)
        attention = torch.softmax(scores, dim=1)
        return x * attention, attention

class MTL_TaskAttention_Model(nn.Module):
    """帶任務特定 Attention 的多任務模型"""
    def __init__(self, input_dim, hidden_dim=128):
        super().__init__()

        self.shared_layer = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU()
        )

        # 任務特定 Attention
        self.task_attention = TaskSpecificAttention(hidden_dim, num_tasks=3)

        # 預測層
        self.task_heads = nn.ModuleList([
            nn.Linear(hidden_dim, 1) for _ in range(3)
        ])

    def forward(self, x):
        shared = self.shared_layer(x)

        predictions = []
        attention_scores = []

        for task_id in range(3):
            weighted, attn = self.task_attention(shared, task_id)
            pred = torch.sigmoid(self.task_heads[task_id](weighted))
            predictions.append(pred)
            attention_scores.append(attn)

        return {
            'predictions': {
                'hypertension': predictions[0],
                'hyperglycemia': predictions[1],
                'dyslipidemia': predictions[2]
            },
            'attention_scores': {
                'hypertension': attention_scores[0],
                'hyperglycemia': attention_scores[1],
                'dyslipidemia': attention_scores[2]
            }
        }
```

---

## Attention Score 分析流程

### 1. 訓練模型並提取 Attention Scores

```python
# 訓練模型
model = MTL_3H_Model(input_dim=X_train.shape[1])
model.fit(X_train, y_train)

# 預測並提取 attention scores
with torch.no_grad():
    outputs = model(X_test)
    attention_scores = outputs['attention_scores']
```

### 2. 計算全局特徵重要性

```python
import numpy as np

# 平均所有樣本的 attention scores
mean_attention = attention_scores.mean(dim=0)

# 與特徵名稱配對
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'attention_score': mean_attention.cpu().numpy()
}).sort_values('attention_score', ascending=False)

print(feature_importance.head(10))
```

### 3. 任務特定的特徵重要性

```python
# 如果使用 Task-specific Attention
task_names = ['Hypertension', 'Hyperglycemia', 'Dyslipidemia']

for task_name in task_names:
    task_attention = outputs['attention_scores'][task_name.lower()]
    mean_attention = task_attention.mean(dim=0)

    print(f"\n{task_name} - Top 5 重要特徵:")
    top_features = pd.DataFrame({
        'feature': feature_names,
        'score': mean_attention.cpu().numpy()
    }).nlargest(5, 'score')
    print(top_features)
```

### 4. 視覺化

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 條形圖
plt.figure(figsize=(10, 6))
top_10 = feature_importance.head(10)
sns.barplot(data=top_10, x='attention_score', y='feature')
plt.title('Top 10 Features by Attention Score')
plt.xlabel('Attention Score')
plt.tight_layout()
plt.savefig('attention_scores.png')

# 熱力圖（任務 × 特徵）
if using_task_specific_attention:
    attention_matrix = np.array([
        outputs['attention_scores']['hypertension'].mean(0),
        outputs['attention_scores']['hyperglycemia'].mean(0),
        outputs['attention_scores']['dyslipidemia'].mean(0)
    ])

    plt.figure(figsize=(12, 4))
    sns.heatmap(attention_matrix,
                xticklabels=feature_names,
                yticklabels=task_names,
                cmap='YlOrRd',
                annot=True, fmt='.3f')
    plt.title('Task-specific Feature Attention')
    plt.tight_layout()
    plt.savefig('task_attention_heatmap.png')
```

---

## 預期結果範例

### 全局特徵重要性（所有任務平均）

```
特徵                  Attention Score    視覺化
─────────────────────────────────────────────────
收縮壓 (SBP)          0.28              ████████████
年齡 (Age)            0.22              ██████████
BMI                   0.18              ████████
舒張壓 (DBP)          0.15              ██████
吸菸史 (Smoking)      0.08              ███
飲酒 (Alcohol)        0.05              ██
運動 (Exercise)       0.04              █
```

### 任務特定特徵重要性

**高血壓 (Hypertension)**
```
1. 收縮壓 (SBP):     0.35
2. 舒張壓 (DBP):     0.28
3. 年齡 (Age):       0.18
4. BMI:              0.12
5. 家族史 (FH_HTN):  0.07
```

**高血糖 (Hyperglycemia)**
```
1. BMI:              0.32
2. 年齡 (Age):       0.26
3. 腰圍 (Waist):     0.20
4. 家族史 (FH_DM):   0.15
5. 運動 (Exercise):  0.07
```

**高血脂 (Dyslipidemia)**
```
1. BMI:              0.30
2. 飲酒 (Alcohol):   0.24
3. 年齡 (Age):       0.18
4. 飲食 (Diet):      0.16
5. 運動 (Exercise):  0.12
```

---

## 與醫學知識的驗證

### 驗證標準

參考 Taiwan MTL 論文的做法（Page 10）：

1. **與文獻一致性**：Attention scores 識別的風險因子應與醫學文獻一致
2. **臨床合理性**：不同任務關注的特徵應符合臨床認知
3. **可修改因子**：能識別出可干預的風險因子（如 BMI、吸菸、運動）

### 預期驗證結果

| 任務 | Attention 高分特徵 | 醫學文獻支持 |
|------|-------------------|-------------|
| 高血壓 | 收縮壓、舒張壓、年齡 | ✓ (AHA Guidelines) |
| 高血糖 | BMI、年齡、家族史 | ✓ (ADA Standards) |
| 高血脂 | BMI、飲酒、飲食 | ✓ (NCEP ATP III) |

---

## 論文中的應用建議

### 章節結構

**3. 方法論 (Methodology)**
- 3.4 模型架構
  - 3.4.1 多任務學習框架
  - 3.4.2 Attention 機制設計
  - 3.4.3 損失函數

**4. 實驗結果 (Results)**
- 4.3 模型可解釋性分析
  - 4.3.1 SHAP 值分析（所有模型）
  - 4.3.2 Attention Score 分析（神經網路）
  - 4.3.3 特徵重要性比較

**5. 討論 (Discussion)**
- 5.2 Attention vs SHAP 的比較
- 5.3 與臨床知識的一致性驗證

### 實驗設計

1. **Baseline 模型**（使用 SHAP）
   - Logistic Regression
   - Decision Tree
   - Random Forest

2. **Advanced 模型**（使用 Attention + SHAP）
   - Multi-Task Neural Network (單一 Attention)
   - Multi-Task Neural Network (任務特定 Attention)

3. **比較指標**
   - 預測效能：AUC, F1-score, Balanced Accuracy
   - 可解釋性：特徵重要性排序的一致性
   - 計算效率：推論時間、訓練時間

---

## 參考文獻

### 關鍵論文

1. **Taiwan MTL (2025)**
   - Tsai, H. et al. (2025). Multitask learning multimodal network for chronic disease prediction. *Scientific Reports*, 15:15468.
   - DOI: 10.1038/s41598-025-99554-z

2. **Attention 機制原始論文**
   - Vaswani, A. et al. (2017). Attention is all you need. *NeurIPS*.
   - Bahdanau, D. et al. (2015). Neural machine translation by jointly learning to align and translate. *ICLR*.

3. **SHAP**
   - Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *NeurIPS*.

4. **Multi-Task Learning**
   - Ruder, S. (2017). An overview of multi-task learning in deep neural networks. *arXiv:1706.05098*.

---

## 附錄：完整實作範例

```python
# 完整訓練與分析流程
import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 載入資料
X_train, X_test, y_train, y_test = load_hrs_data()
feature_names = X_train.columns.tolist()

# 2. 建立模型
model = MTL_3H_Model(
    input_dim=len(feature_names),
    hidden_dim=128
)

# 3. 訓練
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = nn.BCELoss()

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_train)

    # 計算三個任務的損失
    loss = (
        criterion(outputs['predictions']['hypertension'], y_train['hypertension']) +
        criterion(outputs['predictions']['hyperglycemia'], y_train['hyperglycemia']) +
        criterion(outputs['predictions']['dyslipidemia'], y_train['dyslipidemia'])
    ) / 3

    loss.backward()
    optimizer.step()

# 4. 提取 Attention Scores
model.eval()
with torch.no_grad():
    test_outputs = model(X_test)
    attention_scores = test_outputs['attention_scores'].cpu().numpy()

# 5. 分析與視覺化
mean_attention = attention_scores.mean(axis=0)
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'attention_score': mean_attention
}).sort_values('attention_score', ascending=False)

# 6. 繪圖
plt.figure(figsize=(10, 6))
top_10 = feature_importance.head(10)
sns.barplot(data=top_10, x='attention_score', y='feature')
plt.title('Feature Importance by Attention Score')
plt.xlabel('Attention Score')
plt.tight_layout()
plt.savefig('results/attention_analysis.png')

# 7. 儲存結果
feature_importance.to_csv('results/attention_scores.csv', index=False)
print("\n分析完成！結果已儲存至 results/")
```

---

**最後更新**：2025-01-05
**作者**：紀伯喬
**指導教授**：許揚 教授
**學校**：國立臺北教育大學 資訊科學系
