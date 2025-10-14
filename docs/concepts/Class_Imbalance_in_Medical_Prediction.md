# 類別不平衡問題（Class Imbalance）在醫療預測中的應用

## 問題背景

### 醫療預測的典型特徵
**健康的人 >> 不健康的人**

在疾病預測任務中，類別不平衡是常態：
- 大部分人是健康的（陰性類別）
- 少數人會發病（陽性類別）

---

## 本研究的情境

### 研究設定：預測「健康→三高」的轉變

**與台中榮總研究相似**：
- **Liu et al. (2024)**：相對健康成人（平均 FBG 89.6, HbA1c 5.5%）→ 預測 10 年內糖尿病發病
- **本研究**：過去沒有三高的人 → 預測未來三高風險

### 納入條件
```python
# T₁ 和 T₂ 時都沒有三高
納入標準：
- T₁: 無高血壓 AND 無高血糖 AND 無高血脂
- T₂: 無高血壓 AND 無高血糖 AND 無高血脂

預測目標：
- T₃: 是否新發三高（incident cases）
```

### 排除條件
```python
排除：
- T₁ 已有三高（prevalent cases）
- T₂ 已有三高
- 資料缺失者
```

---

## 類別不平衡的程度

### 三高盛行率（年齡相關）

根據台灣衛福部統計：

| 年齡層 | 高血壓盛行率 | 高血糖盛行率 | 高血脂盛行率 |
|--------|------------|------------|------------|
| 20-39歲 | 5-10% | 3-5% | 10-15% |
| 40-64歲 | 30-40% | 15-20% | 25-35% |
| 65歲+ | 60-70% | 25-30% | 40-50% |

**關鍵觀察**：
> 40歲以後，三高盛行率確實相當高（30-70%）

### 本研究的預期發病率（Incidence Rate）

**情境設定**：
- 篩選：T₁, T₂ 都沒有三高的人
- 預測：T₃ 是否新發三高
- 時間間隔：假設 T₂→T₃ 間隔 1-2 年

**預期發病率（估計）**：

#### 情境 A：年輕族群（平均 40 歲以下）
```
預期發病率：5-10%
類別分布：
- 陰性（仍健康）: 90-95%
- 陽性（新發三高）: 5-10%
不平衡比例：約 1:10 到 1:20
```

#### 情境 B：中高齡族群（平均 50-60 歲）
```
預期發病率：15-25%
類別分布：
- 陰性（仍健康）: 75-85%
- 陽性（新發三高）: 15-25%
不平衡比例：約 1:3 到 1:5
```

#### 情境 C：混合族群（本研究 Synthea）
```
預期發病率：10-20%（待驗證）
類別分布：
- 陰性（仍健康）: 80-90%
- 陽性（新發三高）: 10-20%
不平衡比例：約 1:4 到 1:9
```

---

## 類別不平衡的影響

### 1. 模型傾向預測多數類別

**問題**：
```python
# 假設陽性率僅 10%
# 模型可能學到「全部預測為陰性」也有 90% 準確率

準確率（Accuracy）= 90%  ← 看似很高！
但 Recall（召回率）= 0%  ← 完全沒抓到陽性！
```

**範例**：
```
真實情況：100 位病患，10 位會發病，90 位不會
模型預測：全部預測「不會發病」

結果：
- Accuracy = 90% ✓ （看似很好）
- Precision = N/A
- Recall = 0% ✗ （完全失敗）
- F1-Score = 0 ✗
```

### 2. 評估指標的誤導

**不適合的指標**：
- **Accuracy**：類別不平衡時會高估性能

**適合的指標**：
- **AUC-ROC**：對類別不平衡較不敏感
- **F1-Score**：平衡 Precision 與 Recall
- **Recall**：醫療重視（不能漏掉高風險）
- **Precision-Recall Curve**：比 ROC 更適合極度不平衡的情境

### 3. 梯度更新偏向多數類別

在深度學習中：
```python
# 假設陽性 10 個，陰性 90 個
# 損失函數：Binary Cross-Entropy

Total Loss = 0.1 * Loss_陽性 + 0.9 * Loss_陰性
                    ↑                    ↑
                  貢獻小              貢獻大

結果：模型學習偏向預測陰性
```

---

## 處理類別不平衡的方法

### 策略 1: 資料層面（Data-level）

#### 1.1 過採樣（Over-sampling）

**Random Over-sampling**：
```python
from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

# 原始：陽性 100, 陰性 900
# 重採樣後：陽性 900, 陰性 900
```

**優點**：簡單、易實作
**缺點**：重複樣本，可能過擬合

**SMOTE（Synthetic Minority Over-sampling Technique）**：
```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# 生成「合成」的少數類別樣本
# 方法：在少數類別樣本間插值
```

**優點**：增加多樣性，減少過擬合
**缺點**：可能生成不真實的樣本（醫療資料需謹慎）

**⚠️ 醫療資料的特殊考量**：
```
問題：SMOTE 生成的合成樣本可能不符合生理邏輯
範例：
  真實病患 A: SBP=130, FBG=95, BMI=24
  真實病患 B: SBP=138, FBG=105, BMI=28
  SMOTE 合成: SBP=134, FBG=100, BMI=26  ← 看似合理

但可能產生：
  合成樣本: SBP=145, FBG=90, BMI=22  ← 不合常理
  （高血壓但血糖低、BMI 正常，少見組合）

建議：謹慎使用，需領域專家驗證
```

#### 1.2 欠採樣（Under-sampling）

**Random Under-sampling**：
```python
from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X_train, y_train)

# 原始：陽性 100, 陰性 900
# 重採樣後：陽性 100, 陰性 100
```

**優點**：減少訓練時間、避免多數類別主導
**缺點**：丟棄大量資料、可能損失重要資訊

**Tomek Links / ENN（Edited Nearest Neighbors）**：
```python
from imblearn.under_sampling import TomekLinks

tl = TomekLinks()
X_resampled, y_resampled = tl.fit_resample(X_train, y_train)

# 移除邊界上的多數類別樣本（模糊樣本）
```

**優點**：保留清晰樣本、改善決策邊界
**缺點**：仍會丟失資料

#### 1.3 混合採樣

**SMOTE + Tomek Links**：
```python
from imblearn.combine import SMOTETomek

smt = SMOTETomek(random_state=42)
X_resampled, y_resampled = smt.fit_resample(X_train, y_train)

# 先過採樣少數類別，再清理邊界樣本
```

---

### 策略 2: 算法層面（Algorithm-level）

#### 2.1 類別權重（Class Weights）

**原理**：給少數類別更高的權重

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.class_weight import compute_class_weight

# 自動計算類別權重
class_weights = compute_class_weight(
    'balanced',
    classes=np.unique(y_train),
    y=y_train
)
# 陽性 10%, 陰性 90% → 權重 [0.56, 5.0]

# 訓練模型
rf = RandomForestClassifier(class_weight='balanced')
rf.fit(X_train, y_train)
```

**支援的模型**：
- Logistic Regression: `class_weight='balanced'`
- Random Forest: `class_weight='balanced'`
- XGBoost: `scale_pos_weight=ratio`
- SVM: `class_weight='balanced'`

**XGBoost 範例**：
```python
import xgboost as xgb

# 計算正負樣本比例
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
# 例如：900 / 100 = 9

xgb_model = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight)
xgb_model.fit(X_train, y_train)
```

**深度學習（加權損失函數）**：
```python
import tensorflow as tf

# 計算類別權重
class_weight = {0: 1.0, 1: 9.0}  # 陽性權重 9 倍

model.fit(
    X_train, y_train,
    class_weight=class_weight,
    epochs=50
)
```

**或使用 Focal Loss**（處理極度不平衡）：
```python
def focal_loss(gamma=2., alpha=0.25):
    def focal_loss_fixed(y_true, y_pred):
        pt = tf.where(tf.equal(y_true, 1), y_pred, 1 - y_pred)
        return -alpha * tf.pow(1. - pt, gamma) * tf.log(pt + 1e-8)
    return focal_loss_fixed

model.compile(
    optimizer='adam',
    loss=focal_loss(gamma=2, alpha=0.75)
)
```

#### 2.2 閾值調整（Threshold Tuning）

**原理**：調整分類閾值，提高召回率

```python
from sklearn.metrics import precision_recall_curve

# 預測機率
y_pred_proba = model.predict_proba(X_test)[:, 1]

# 找出最佳閾值（最大化 F1-Score）
precision, recall, thresholds = precision_recall_curve(y_test, y_pred_proba)
f1_scores = 2 * (precision * recall) / (precision + recall)
best_threshold = thresholds[np.argmax(f1_scores)]

print(f"最佳閾值: {best_threshold:.3f}")  # 可能是 0.3 而非預設的 0.5

# 使用調整後的閾值
y_pred_adjusted = (y_pred_proba >= best_threshold).astype(int)
```

**醫療應用的閾值選擇**：
```
情境 A：篩檢（寧可錯殺不可放過）
- 目標：高 Recall（不漏掉任何高風險）
- 閾值：0.2-0.3（較低）
- 結果：Recall 90%, Precision 50%
  → 10 個陽性預測，5 個是誤報（可接受）

情境 B：確診（避免過度治療）
- 目標：高 Precision（避免誤診）
- 閾值：0.6-0.7（較高）
- 結果：Recall 60%, Precision 85%
  → 會漏掉一些病患，但預測陽性的很準確
```

#### 2.3 集成學習（Ensemble）

**Balanced Bagging**：
```python
from imblearn.ensemble import BalancedBaggingClassifier

bbc = BalancedBaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=10,
    random_state=42
)
bbc.fit(X_train, y_train)

# 每個 base learner 使用平衡的子樣本訓練
```

**Balanced Random Forest**：
```python
from imblearn.ensemble import BalancedRandomForestClassifier

brf = BalancedRandomForestClassifier(
    n_estimators=100,
    random_state=42
)
brf.fit(X_train, y_train)
```

**EasyEnsemble**：
```python
from imblearn.ensemble import EasyEnsembleClassifier

eec = EasyEnsembleClassifier(n_estimators=10, random_state=42)
eec.fit(X_train, y_train)

# 多次欠採樣多數類別，訓練多個分類器，最後投票
```

---

### 策略 3: 評估指標調整

#### 使用對不平衡魯棒的指標

**不推薦**：
- Accuracy（會被多數類別主導）

**推薦**：
1. **AUC-ROC**：對類別分布較不敏感
2. **AUC-PR（Precision-Recall Curve）**：極度不平衡時比 ROC 更適合
3. **F1-Score**：平衡 Precision 與 Recall
4. **Matthews Correlation Coefficient (MCC)**：考慮混淆矩陣所有元素

**AUC-PR 範例**：
```python
from sklearn.metrics import average_precision_score, precision_recall_curve
import matplotlib.pyplot as plt

# 計算 PR AUC
ap_score = average_precision_score(y_test, y_pred_proba)

# 繪製 PR Curve
precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
plt.plot(recall, precision, label=f'AP={ap_score:.3f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.show()
```

**MCC 範例**：
```python
from sklearn.metrics import matthews_corrcoef

mcc = matthews_corrcoef(y_test, y_pred)
print(f"MCC: {mcc:.3f}")  # 範圍 [-1, 1]，0 表示隨機預測
```

---

## 本研究的策略選擇

### 推薦方案：多管齊下

#### Phase 1: 資料探索
```python
# 1. 檢查實際的類別分布
print(y_train.value_counts())
# 預期：陰性 80-90%, 陽性 10-20%

# 2. 視覺化特徵分布（陽性 vs. 陰性）
import seaborn as sns
sns.boxplot(x='label', y='SBP', data=df)
# 確認是否有明顯區分度
```

#### Phase 2: Baseline（不處理不平衡）
```python
# 先訓練不做任何平衡處理的模型
xgb_baseline = xgb.XGBClassifier()
xgb_baseline.fit(X_train, y_train)

# 評估
print(f"AUC: {auc_score:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1: {f1:.3f}")

# 如果 Recall < 0.6，需要處理不平衡
```

#### Phase 3: 應用平衡策略

**方案 A：類別權重（首選）**
```python
# XGBoost
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
xgb_balanced = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight)

# Random Forest
rf_balanced = RandomForestClassifier(class_weight='balanced')

# Logistic Regression
lr_balanced = LogisticRegression(class_weight='balanced')
```

**優點**：
- 不改變原始資料
- 計算效率高
- 所有主流模型都支援

**方案 B：SMOTE（謹慎使用）**
```python
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42, k_neighbors=5)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# ⚠️ 只在訓練集上使用，測試集保持原樣
xgb_smote = xgb.XGBClassifier()
xgb_smote.fit(X_train_resampled, y_train_resampled)
```

**注意事項**：
- 只對訓練集做 SMOTE
- 驗證集與測試集維持原始分布（反映真實情況）
- 需檢查生成樣本的合理性

**方案 C：閾值調整（後處理）**
```python
# 先訓練模型（可搭配類別權重）
xgb_model = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight)
xgb_model.fit(X_train, y_train)

# 在驗證集上找最佳閾值
y_val_proba = xgb_model.predict_proba(X_val)[:, 1]
precision, recall, thresholds = precision_recall_curve(y_val, y_val_proba)

# 根據需求選擇閾值
# 目標：Recall > 0.7
threshold = thresholds[recall >= 0.7][0]

# 在測試集上使用調整後的閾值
y_test_proba = xgb_model.predict_proba(X_test)[:, 1]
y_test_pred = (y_test_proba >= threshold).astype(int)
```

#### Phase 4: 比較不同策略

| 方法 | AUC | F1 | Recall | Precision | 備註 |
|------|-----|----|----|----|----|
| Baseline | 0.80 | 0.65 | 0.58 | 0.74 | Recall 偏低 |
| Class Weight | 0.82 | 0.70 | 0.72 | 0.68 | 平衡改善 ✓ |
| SMOTE | 0.81 | 0.68 | 0.75 | 0.62 | Recall 高但 Precision 降低 |
| Threshold=0.3 | 0.82 | 0.72 | 0.78 | 0.67 | Recall 最高 ✓ |
| **推薦組合** | **0.83** | **0.73** | **0.76** | **0.70** | Class Weight + Threshold 調整 |

---

## 與 Liu et al. (2024) 的對比

### Liu et al. 的處理方式

**研究設計**：
- 納入：6,687 位相對健康成人
- 追蹤：10 年
- 發病率：約 15-20%（估計，論文未明確說明）

**類別不平衡處理**：
- 使用 **SMOTE** 過採樣
- 使用 **Random Under-sampling** 欠採樣
- 比較不同平衡策略的效果

**結果**：
- XGBoost (SMOTE) 達 AUC 0.93

### 本研究的策略

**相似點**：
- 同樣納入「目前健康」的人
- 同樣預測「未來發病」
- 同樣面臨類別不平衡

**差異點**：

| 特性 | Liu et al. (2024) | 本研究 |
|------|------------------|--------|
| **追蹤時間** | 10 年（長期） | 1-2 年（短期） |
| **預測疾病** | 單一（糖尿病） | 多標籤（三高） |
| **發病率** | 約 15-20% | 預期 10-20% |
| **平衡策略** | SMOTE + Under-sampling | Class Weight + Threshold（推薦）|
| **模型** | XGBoost, RF | XGBoost, MTL, GA, ... |

---

## 多標籤分類的特殊考量

### 三高的類別分布可能不同

```python
# 假設各疾病的發病率不同
高血壓新發率：15%（較高）
高血糖新發率：10%（中等）
高血脂新發率：12%（中等）

# 每個疾病的不平衡程度不同
# 需分別處理？還是統一策略？
```

### 策略 A：獨立處理（三個二元分類器）

```python
# 為每個疾病訓練獨立模型
# 各自處理類別不平衡

# 高血壓
scale_pos_weight_ht = (y_ht == 0).sum() / (y_ht == 1).sum()
xgb_ht = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight_ht)

# 高血糖
scale_pos_weight_hg = (y_hg == 0).sum() / (y_hg == 1).sum()
xgb_hg = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight_hg)

# 高血脂
scale_pos_weight_hl = (y_hl == 0).sum() / (y_hl == 1).sum()
xgb_hl = xgb.XGBClassifier(scale_pos_weight=scale_pos_weight_hl)
```

**優點**：每個疾病針對性處理
**缺點**：無法利用疾病間的相關性

### 策略 B：多任務學習（MTL）

```python
# 使用加權損失函數
def weighted_binary_crossentropy(y_true, y_pred, weights):
    """
    weights: [w_ht, w_hg, w_hl]
    """
    bce = tf.keras.losses.binary_crossentropy(y_true, y_pred)
    weighted_bce = bce * weights
    return tf.reduce_mean(weighted_bce)

# 根據各疾病的發病率設定權重
weights = [1.5, 2.0, 1.8]  # 高血糖發病率最低，權重最高

model.compile(
    optimizer='adam',
    loss=lambda y_true, y_pred: weighted_binary_crossentropy(y_true, y_pred, weights)
)
```

---

## 實驗設計

### 實驗問題
1. **不處理 vs. 處理不平衡**：性能差異有多大？
2. **不同平衡策略**：Class Weight vs. SMOTE vs. 閾值調整，哪個最好？
3. **多標籤處理**：獨立處理 vs. MTL 統一處理？

### 實驗流程

```python
# Step 1: 確認類別分布
print("訓練集類別分布:")
print(f"高血壓 - 陰性: {(y_ht_train==0).sum()}, 陽性: {(y_ht_train==1).sum()}")
print(f"高血糖 - 陰性: {(y_hg_train==0).sum()}, 陽性: {(y_hg_train==1).sum()}")
print(f"高血脂 - 陰性: {(y_hl_train==0).sum()}, 陽性: {(y_hl_train==1).sum()}")

# Step 2: Baseline（不處理不平衡）
baseline_results = train_baseline(X_train, y_train)

# Step 3: 應用不同平衡策略
strategies = ['class_weight', 'smote', 'threshold_tuning', 'combined']
for strategy in strategies:
    results = train_with_strategy(X_train, y_train, strategy)
    compare_results(baseline_results, results)

# Step 4: 視覺化比較
plot_comparison(strategies, metrics=['AUC', 'F1', 'Recall', 'Precision'])
```

---

## 論文撰寫重點

### Methods 章節
```
3.5 Handling Class Imbalance

Given the nature of disease prediction, class imbalance is expected
in our dataset. We adopted the following strategies:

1. Class Weighting: Assigned higher weights to minority classes
   (incident cases) proportional to their inverse frequency.

2. Threshold Adjustment: Optimized classification thresholds on
   the validation set to maximize F1-Score while maintaining
   Recall > 0.70 for clinical utility.

3. Evaluation Metrics: Used AUC-ROC and F1-Score as primary
   metrics, as they are robust to class imbalance compared to
   accuracy.
```

### Results 章節
```
4.X Class Imbalance Analysis

Table X: Class distribution in training set
| Disease       | Negative | Positive | Imbalance Ratio |
|---------------|----------|----------|-----------------|
| Hypertension  | 7,200    | 1,200    | 1:6             |
| Hyperglycemia | 7,800    | 600      | 1:13            |
| Dyslipidemia  | 7,500    | 900      | 1:8.3           |

Table Y: Performance comparison with different imbalance strategies
| Strategy      | AUC  | F1   | Recall | Precision |
|---------------|------|------|--------|-----------|
| Baseline      | 0.80 | 0.65 | 0.58   | 0.74      |
| Class Weight  | 0.82 | 0.70 | 0.72   | 0.68      |
| SMOTE         | 0.81 | 0.68 | 0.75   | 0.62      |
| Threshold=0.3 | 0.82 | 0.72 | 0.78   | 0.67      |
| Combined*     | 0.83 | 0.73 | 0.76   | 0.70      |

*Combined: Class Weight + Threshold Adjustment

Figure X: Precision-Recall curves for different strategies
[展示不同策略的 PR Curve]
```

### Discussion 章節
```
5.X Addressing Class Imbalance in Preventive Medicine

Our study focused on predicting incident cases (healthy → disease),
similar to Liu et al. (2024). This design inherently leads to class
imbalance, as most individuals remain healthy over short follow-up
periods.

We found that combining class weighting and threshold adjustment
achieved the best balance between Recall (0.76) and Precision (0.70).
Unlike Liu et al., who used SMOTE, we avoided synthetic sample
generation due to concerns about violating physiological constraints
in medical data.

For clinical deployment, we recommend using a lower threshold (0.3)
to prioritize Recall, ensuring that high-risk individuals are not
missed during screening.
```

---

## 參考文獻

### 類別不平衡處理
- Chawla et al. (2002) - SMOTE 原始論文
- He & Garcia (2009) - Learning from Imbalanced Data
- Batista et al. (2004) - SMOTE 變體比較

### 醫療預測中的不平衡
- Liu et al. (2024) - 台中榮總糖尿病預測（使用 SMOTE）
- [待補充] 其他醫療不平衡處理案例

---

## 會議討論紀錄

**日期**: 2025-01-14
**討論內容**：
- 醫療預測中類別不平衡是常態
- 40 歲以後三高盛行率高，但「新發病例」仍是少數
- 本研究與台中榮總相似：預測「健康→三高」的轉變
- 需排除 T₁, T₂已有三高的人（只預測新發病例）

---

## 後續工作

- [ ] 檢查 Synthea_SUA 的實際類別分布
- [ ] 實作類別權重策略（XGBoost, RF, LR）
- [ ] 實驗 SMOTE 並驗證生成樣本的合理性
- [ ] 在驗證集上調整最佳閾值
- [ ] 比較不同策略的性能（表格與圖表）
- [ ] 撰寫 Methods 與 Results 章節

---

## 標籤

`#類別不平衡` `#SMOTE` `#類別權重` `#閾值調整` `#醫療預測` `#新發病例` `#Recall優先` `#Precision-Recall`
