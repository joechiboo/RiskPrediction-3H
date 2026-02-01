# 多資料集驗證（Multi-Dataset Validation）

## 概念定義

### 外部驗證（External Validation）
使用與訓練資料**完全獨立**的資料集，測試模型的泛化能力。

**重要性**：
- 避免過擬合（僅在單一資料集表現好）
- 證明模型的跨人群、跨地區適用性
- 提升研究可信度與臨床應用價值

---

## 本研究的資料集

### Dataset 1: SUA_CVDs_risk_factors（中國東南社區）
- **來源**：中國東南地區社區研究
- **時間**：約 2010-2018
- **人群**：華人社區居民
- **樣本數**：TBD（需確認）
- **特徵**：三高相關指標
- **標籤**：心血管疾病風險因子

**檔案位置**：
```
data/raw/SUA_CVDs_risk_factors.csv
```

### Dataset 2: Synthea_SUA_format（加拿大合成資料）
- **來源**：Synthea 合成電子病歷（模擬加拿大/北美人群）
- **時間**：2010-2024
- **人群**：合成病患（反映北美人口特徵）
- **樣本數**：
  - 原始：100,000 或 1,000 病患
  - 轉換後：1,158 病患，14,466 筆記錄
- **特徵**：完整三高相關指標（SBP, DBP, BMI, FBG, TC, Cr, GFR...）
- **標籤**：三高診斷結果

**檔案位置**：
```
data/raw/100_synthea_sample_data/  或  data/raw/1000_synthea_sample_data/
data/processed/Synthea_SUA_format.csv
```

---

## 兩資料集的對比

| 特性 | SUA_CVDs (中國) | Synthea_SUA (加拿大/合成) |
|------|----------------|-------------------------|
| **資料類型** | 真實臨床資料 | 合成資料 |
| **地區** | 中國東南社區 | 北美（合成） |
| **人種** | 華人 | 多種族（合成） |
| **樣本數** | TBD | 1,158 病患 |
| **記錄數** | TBD | 14,466 筆 |
| **時間跨度** | 2010-2018（推測）| 2010-2024 |
| **資料完整度** | 需確認 | 較完整（但 UA 100% 缺失）|
| **缺失值** | 需確認 | FBG/TC 約 70%, BMI 20% |
| **優勢** | 真實資料、華人特徵 | 完整時序、無隱私問題 |
| **劣勢** | 可能缺失值多、樣本數少？ | 合成資料、可能過於理想化 |

---

## 驗證策略

### 策略 A：單一資料集訓練 + 外部驗證

#### 方案 A1：Synthea 訓練 → SUA 驗證
```python
# 在 Synthea 上訓練模型
X_train, y_train = load_synthea_data()
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

# 在 SUA 上測試（外部驗證）
X_external, y_external = load_sua_data()
y_pred = model.predict(X_external)
auc_external = roc_auc_score(y_external, y_pred)

print(f"Synthea (訓練集) AUC: {auc_internal:.3f}")
print(f"SUA (外部驗證) AUC: {auc_external:.3f}")
```

**預期情境**：
```
Synthea 內部驗證 AUC: 0.85
SUA 外部驗證 AUC: 0.72  ← 下降（正常現象）

原因：
1. 人群差異（合成 vs. 真實、北美 vs. 華人）
2. 資料收集方式不同
3. 缺失值模式不同
```

#### 方案 A2：SUA 訓練 → Synthea 驗證
```python
# 在 SUA 上訓練模型
X_train, y_train = load_sua_data()
model = xgb.XGBClassifier()
model.fit(X_train, y_train)

# 在 Synthea 上測試
X_external, y_external = load_synthea_data()
y_pred = model.predict(X_external)
auc_external = roc_auc_score(y_external, y_pred)
```

**問題**：
- SUA 樣本數可能不足（需確認）
- 若 SUA < 1,000 樣本，可能訓練不穩定

---

### 策略 B：雙向驗證（Bi-directional Validation）

**完整實驗**：
```python
# 實驗 1：Synthea → SUA
model_s2c = train_on_synthea()
auc_s2c = test_on_sua(model_s2c)

# 實驗 2：SUA → Synthea
model_c2s = train_on_sua()
auc_c2s = test_on_synthea(model_c2s)

# 報告雙向結果
print(f"Synthea → SUA: {auc_s2c:.3f}")
print(f"SUA → Synthea: {auc_c2s:.3f}")
```

**結果解讀**：
```
情境 A：雙向性能接近
Synthea → SUA: 0.78
SUA → Synthea: 0.76
→ 模型泛化能力強，跨資料集穩健

情境 B：單向性能差
Synthea → SUA: 0.72
SUA → Synthea: 0.65
→ 資料集差異大，需分析原因

情境 C：不對稱
Synthea → SUA: 0.80  ← 較好
SUA → Synthea: 0.65  ← 較差
→ 可能 SUA 樣本數太少，訓練不足
```

---

### 策略 C：資料集合併（Pooled Training）

**方法**：合併兩個資料集訓練，測試泛化能力

```python
# 合併資料
X_combined = pd.concat([X_synthea, X_sua])
y_combined = pd.concat([y_synthea, y_sua])

# 加入資料來源特徵（可選）
X_combined['dataset_source'] = ['synthea']*len(X_synthea) + ['sua']*len(X_sua)

# 訓練
model = xgb.XGBClassifier()
model.fit(X_combined, y_combined)

# 分別在兩個資料集上評估
auc_synthea = test_on_synthea(model)
auc_sua = test_on_sua(model)
```

**優點**：
- 增加訓練樣本數
- 學習更泛化的模式

**缺點**：
- 可能學習資料集偏差（dataset shift）
- 需檢查特徵分布是否一致

---

### 策略 D：遷移學習（Transfer Learning）

**情境**：Synthea 樣本多，SUA 樣本少

**方法**：
```python
# Step 1: 在 Synthea（大資料）上預訓練
model = xgb.XGBClassifier(n_estimators=100)
model.fit(X_synthea_train, y_synthea_train)

# Step 2: 在 SUA（小資料）上微調（Fine-tuning）
# XGBoost 的微調方法：繼續訓練
model.fit(X_sua_train, y_sua_train, xgb_model=model.get_booster())

# Step 3: 在 SUA 測試集上評估
auc = test_on_sua(model)
```

**適用情境**：
- SUA 樣本數 < 500
- 想利用 Synthea 的大量資料

**深度學習的遷移學習**：
```python
# Step 1: 在 Synthea 上預訓練 MLP
mlp = build_mlp()
mlp.fit(X_synthea, y_synthea, epochs=50)

# Step 2: 凍結底層，只訓練頂層（微調）
for layer in mlp.layers[:-2]:
    layer.trainable = False

mlp.fit(X_sua, y_sua, epochs=20)

# Step 3: 評估
auc = test_on_sua(mlp)
```

---

## 特徵對齊問題

### 問題：兩資料集的特徵可能不完全一致

#### 情境 A：特徵名稱不同
```python
# Synthea: ['SBP', 'DBP', 'FBG', 'TC', ...]
# SUA: ['收縮壓', '舒張壓', '空腹血糖', '總膽固醇', ...]

# 解決方案：特徵映射
feature_mapping = {
    '收縮壓': 'SBP',
    '舒張壓': 'DBP',
    '空腹血糖': 'FBG',
    '總膽固醇': 'TC'
}
sua_data.rename(columns=feature_mapping, inplace=True)
```

#### 情境 B：特徵缺失
```python
# Synthea 有：SBP, DBP, FBG, TC, Cr, GFR, BMI
# SUA 缺少：Cr, GFR

# 解決方案 1：只使用共同特徵
common_features = ['SBP', 'DBP', 'FBG', 'TC', 'BMI']
X_synthea_common = X_synthea[common_features]
X_sua_common = X_sua[common_features]

# 解決方案 2：填補缺失特徵（不推薦）
X_sua['Cr'] = X_sua['Cr'].fillna(X_synthea['Cr'].mean())
```

#### 情境 C：特徵範圍不同
```python
# Synthea: SBP 單位 mmHg（正常）
# SUA: SBP 單位可能不同或有異常值

# 解決方案：標準化
from sklearn.preprocessing import StandardScaler

scaler_synthea = StandardScaler()
X_synthea_scaled = scaler_synthea.fit_transform(X_synthea)

scaler_sua = StandardScaler()
X_sua_scaled = scaler_sua.fit_transform(X_sua)

# 或使用相同的 scaler（需謹慎）
scaler = StandardScaler().fit(X_synthea)  # 在訓練集 fit
X_synthea_scaled = scaler.transform(X_synthea)
X_sua_scaled = scaler.transform(X_sua)  # 在驗證集 transform
```

---

## 實驗設計

### 實驗問題
1. **泛化能力**：模型在外部資料集上的性能如何？
2. **資料集差異**：Synthea（合成）vs. SUA（真實）的性能差距有多大？
3. **最佳策略**：單獨訓練、合併訓練、遷移學習，哪個最好？
4. **特徵穩健性**：哪些特徵在兩個資料集上都重要？

### 實驗流程

#### Phase 1: 資料探索與對齊
```python
# 1. 載入兩個資料集
synthea = pd.read_csv('data/processed/Synthea_SUA_format.csv')
sua = pd.read_csv('data/raw/SUA_CVDs_risk_factors.csv')

# 2. 檢查特徵一致性
print("Synthea 特徵:", synthea.columns.tolist())
print("SUA 特徵:", sua.columns.tolist())

# 3. 檢查標籤定義是否一致
print("Synthea 三高診斷標準:", ...)
print("SUA 三高診斷標準:", ...)

# 4. 統計描述
print(synthea.describe())
print(sua.describe())

# 5. 視覺化特徵分布對比
import seaborn as sns
sns.boxplot(data=[synthea['SBP'], sua['SBP']], labels=['Synthea', 'SUA'])
```

#### Phase 2: Baseline（內部驗證）
```python
# 先在各自資料集上建立 baseline
# 了解各自的「天花板」性能

# Synthea 內部驗證（5-Fold CV）
auc_synthea_internal = train_and_evaluate_on_synthea()
print(f"Synthea 內部 AUC: {auc_synthea_internal:.3f}")

# SUA 內部驗證（5-Fold CV）
auc_sua_internal = train_and_evaluate_on_sua()
print(f"SUA 內部 AUC: {auc_sua_internal:.3f}")
```

#### Phase 3: 外部驗證
```python
# 實驗 1：Synthea 訓練 → SUA 驗證
model_s2c = train_on_entire_synthea()
auc_s2c = test_on_entire_sua(model_s2c)

# 實驗 2：SUA 訓練 → Synthea 驗證
model_c2s = train_on_entire_sua()
auc_c2s = test_on_entire_synthea(model_c2s)

# 實驗 3：合併訓練
model_combined = train_on_combined_data()
auc_synthea_test = test_on_synthea_testset(model_combined)
auc_sua_test = test_on_sua_testset(model_combined)
```

#### Phase 4: 結果比較
```python
results = {
    'Synthea 內部驗證': auc_synthea_internal,
    'SUA 內部驗證': auc_sua_internal,
    'Synthea → SUA': auc_s2c,
    'SUA → Synthea': auc_c2s,
    'Combined (Synthea test)': auc_synthea_test,
    'Combined (SUA test)': auc_sua_test
}

plot_comparison(results)
```

---

## 預期結果

### 情境 A：理想情況
```
內部驗證：
- Synthea 內部 AUC: 0.85
- SUA 內部 AUC: 0.83

外部驗證：
- Synthea → SUA: 0.78 (下降 7%)
- SUA → Synthea: 0.80 (下降 3%)

合併訓練：
- Combined (Synthea test): 0.84
- Combined (SUA test): 0.82

結論：模型泛化能力良好，外部驗證性能下降可接受
```

### 情境 B：合成資料偏差
```
內部驗證：
- Synthea 內部 AUC: 0.88 ← 過高（合成資料太理想）
- SUA 內部 AUC: 0.78 ← 真實資料較難

外部驗證：
- Synthea → SUA: 0.65 ← 大幅下降！
- SUA → Synthea: 0.85 ← 反而上升（合成資料簡單）

結論：Synthea 合成資料與真實資料差異大，需謹慎解釋
```

### 情境 C：樣本數不足
```
內部驗證：
- Synthea 內部 AUC: 0.85
- SUA 內部 AUC: 0.72 ← 可能樣本數少，訓練不穩定

外部驗證：
- Synthea → SUA: 0.80 ← 表現反而比 SUA 內部好！
- SUA → Synthea: 0.70 ← 樣本數少，泛化差

結論：SUA 需更多樣本，或使用遷移學習
```

---

## 分析維度

### 1. 整體性能比較
```
Table: 多資料集驗證結果

| 訓練集 | 驗證集 | AUC | F1 | Recall | Precision |
|--------|--------|-----|----|----|-------|
| Synthea | Synthea (內部) | 0.85 | 0.73 | 0.75 | 0.71 |
| Synthea | SUA (外部) | 0.78 | 0.68 | 0.70 | 0.66 |
| SUA | SUA (內部) | 0.83 | 0.71 | 0.73 | 0.69 |
| SUA | Synthea (外部) | 0.80 | 0.70 | 0.72 | 0.68 |
| Combined | Synthea (測試) | 0.84 | 0.72 | 0.74 | 0.70 |
| Combined | SUA (測試) | 0.82 | 0.71 | 0.73 | 0.69 |
```

### 2. 特徵重要性對比
```python
# 在兩個資料集上訓練模型，比較特徵重要性

# Synthea 模型的 Top-5 特徵
synthea_top5 = ['SBP₂', 'FBG₂', 'BMI₂', 'ΔSBP', 'Age']

# SUA 模型的 Top-5 特徵
sua_top5 = ['SBP₂', 'Age', 'BMI₂', 'TC₂', 'ΔFBG']

# 共同重要特徵
common = ['SBP₂', 'BMI₂', 'Age']  ← 穩健特徵

# 差異特徵
synthea_unique = ['FBG₂', 'ΔSBP']
sua_unique = ['TC₂', 'ΔFBG']
```

**結論**：
- 共同重要特徵（SBP₂, BMI₂, Age）是穩健的預測因子
- 差異特徵可能反映資料集特性或人群差異

### 3. 亞組分析（Subgroup Analysis）
```python
# 按年齡分層驗證
age_groups = ['<40', '40-60', '>60']

for age_group in age_groups:
    auc_synthea = evaluate_on_age_group(model, synthea, age_group)
    auc_sua = evaluate_on_age_group(model, sua, age_group)
    print(f"{age_group}: Synthea AUC={auc_synthea:.3f}, SUA AUC={auc_sua:.3f}")

# 可能發現
<40: Synthea 0.80, SUA 0.75 ← 年輕族群表現接近
40-60: Synthea 0.85, SUA 0.80
>60: Synthea 0.82, SUA 0.70 ← 老年族群差異大
```

### 4. 預測失敗案例分析（Error Analysis）
```python
# 在外部驗證中，哪些樣本預測錯誤？

# Synthea → SUA 的預測錯誤
errors_s2c = find_prediction_errors(model_s2c, X_sua, y_sua)

# 分析錯誤樣本的特徵
print("False Negatives（漏診）特徵:")
print(X_sua[errors_s2c['FN']].describe())

print("False Positives（誤診）特徵:")
print(X_sua[errors_s2c['FP']].describe())

# 可能發現
漏診案例：SBP 在 130-139 之間（邊界值）
誤診案例：BMI > 30 但其他指標正常（肥胖但健康）
```

---

## 與文獻的對比

### Liu et al. (2024) 的驗證方式
- **單一資料集**：台中榮總 EHR
- **內部驗證**：5-Fold Cross-Validation
- **無外部驗證**：僅在單一醫學中心

**局限性（論文中提到）**：
> "Our study was conducted at a single medical center, limiting the generalizability of our findings to other populations."

### Taiwan MTL (2025) 的驗證方式
- **單一資料集**：台灣健保資料
- **內部驗證**：Train-Test Split
- **無外部驗證**

### 本研究的優勢
- **雙資料集**：Synthea（合成）+ SUA（真實）
- **跨人群**：北美（合成）+ 華人社區
- **外部驗證**：雙向驗證，測試泛化能力

**創新點**：
> "To our knowledge, this is the first study to validate a multi-disease prediction model across both synthetic (Synthea) and real-world (SUA) datasets, demonstrating cross-population generalizability."

---

## 論文撰寫重點

### Methods 章節
```
3.6 Multi-Dataset Validation

To assess the generalizability of our models, we performed external
validation using two independent datasets:

1. Synthea_SUA (N=1,158 patients, 14,466 records): Synthetic EHR
   data simulating North American population characteristics.

2. SUA_CVDs (N=TBD): Real-world data from a Southeast Chinese
   community-based cohort study (2010-2018).

We conducted bi-directional validation:
- Train on Synthea → Test on SUA (cross-dataset validation)
- Train on SUA → Test on Synthea (reverse validation)
- Train on Combined → Test on both (pooled approach)

Feature alignment was performed to ensure consistency across datasets,
using only common features: [SBP, DBP, FBG, TC, BMI, Age, Sex].
```

### Results 章節
```
4.X Multi-Dataset Validation Results

Table X: Internal vs. External Validation Performance

| Training Set | Test Set | AUC | F1 | △AUC* |
|--------------|----------|-----|-------|-------|
| Synthea | Synthea (internal) | 0.85 | 0.73 | - |
| Synthea | SUA (external) | 0.78 | 0.68 | -0.07 |
| SUA | SUA (internal) | 0.83 | 0.71 | - |
| SUA | Synthea (external) | 0.80 | 0.70 | -0.03 |
| Combined | Synthea (test) | 0.84 | 0.72 | - |
| Combined | SUA (test) | 0.82 | 0.71 | - |

*△AUC: Performance drop in external validation

Figure X: Feature Importance Comparison Across Datasets
[展示兩個資料集上的特徵重要性對比圖]

Key Findings:
1. External validation AUC decreased by 3-7%, indicating acceptable
   generalizability.
2. Core features (SBP, BMI, Age) remained important across both
   datasets, suggesting robustness.
3. Pooled training improved performance on both datasets, leveraging
   the strengths of each data source.
```

### Discussion 章節
```
5.X Generalizability Across Datasets

Our multi-dataset validation revealed both strengths and limitations:

Strengths:
- External validation AUC (0.78-0.80) remained competitive, indicating
  that the model captured generalizable patterns rather than
  dataset-specific artifacts.
- Core features (SBP, Age, BMI) were consistently important across
  synthetic (Synthea) and real-world (SUA) data, supporting their
  clinical relevance.

Limitations:
- The 3-7% AUC drop in external validation suggests some dataset-specific
  patterns were learned. This is expected given population differences
  (North American synthetic vs. Chinese community).
- Synthea's synthetic nature may introduce biases (e.g., idealized
  data distribution), limiting direct comparison with real-world
  datasets.

Comparison with Literature:
- Most prior studies (Liu et al., Taiwan MTL) lacked external
  validation, limiting generalizability claims.
- Our dual-dataset approach provides stronger evidence for model
  robustness across populations.

Clinical Implications:
- For deployment in Chinese populations, models trained on SUA may
  be preferred.
- For broader applications, pooled training offers a balanced approach.
```

---

## 挑戰與解決方案

### 挑戰 1: SUA 資料集資訊不明確
**問題**：
- 不確定 SUA 的樣本數、特徵定義、標籤定義
- 可能需要大量資料清理

**解決方案**：
- 先讀取 SUA 資料，探索其結構
- 查閱相關文獻（2010-2018 中國東南社區研究）
- 必要時聯繫資料提供者確認

### 挑戰 2: 特徵不一致
**問題**：
- Synthea 有完整特徵，SUA 可能缺少某些欄位
- 特徵名稱、單位可能不同

**解決方案**：
- 只使用**共同特徵**進行外部驗證
- 建立特徵映射表（feature mapping）
- 標準化數值範圍

### 挑戰 3: 標籤定義不同
**問題**：
- Synthea 使用自定義診斷標準（SBP≥140, FBG≥126...）
- SUA 可能使用不同的診斷標準

**解決方案**：
- 統一使用台灣/國際診斷標準
- 重新標註標籤（如果原始數值可用）
- 在論文中明確說明標籤定義

### 挑戰 4: 外部驗證性能過低
**問題**：
- 若 Synthea → SUA AUC < 0.65，難以說服審稿人

**解決方案**：
- 分析原因（人群差異、資料品質、特徵缺失）
- 強調「性能下降是預期的」（合成 vs. 真實、不同人群）
- 使用遷移學習或領域自適應技術
- 退而求其次：報告共同特徵的穩健性（而非整體性能）

---

## 後續工作

### 短期（1-2 週）
- [ ] 探索 SUA_CVDs_risk_factors.csv 的資料結構
- [ ] 確認 SUA 的樣本數、特徵、標籤定義
- [ ] 比較 Synthea 與 SUA 的特徵分布
- [ ] 建立特徵對齊策略

### 中期（3-4 週）
- [ ] 實作 Baseline（內部驗證）
- [ ] 實作外部驗證（Synthea → SUA, SUA → Synthea）
- [ ] 實作合併訓練
- [ ] 比較不同策略的性能

### 長期（5-8 週）
- [ ] 特徵重要性對比分析
- [ ] 亞組分析（年齡、性別）
- [ ] 預測失敗案例分析
- [ ] 撰寫 Methods 與 Results 章節

---

## 參考文獻

### 外部驗證相關
- [待補充] External Validation of Clinical Prediction Models
- [待補充] Cross-Population Validation in Medical AI
- Collins et al. (2015) - Transparent Reporting of External Validation

### 合成資料驗證
- [待補充] Validating Models on Synthetic vs. Real Data
- Synthea: An Approach for Generating Synthetic Healthcare Data

---

## 會議討論紀錄

**日期**: 2025-01-14
**討論內容**：
- 本研究有兩個資料集可用
  1. SUA_CVDs_risk_factors（中國東南社區，真實資料）
  2. Synthea_SUA_format（加拿大/北美，合成資料）
- 可進行多資料集驗證，測試模型泛化能力
- 這是相對於 Liu et al. 和 Taiwan MTL 的優勢（他們僅單一資料集）

---

## 標籤

`#外部驗證` `#多資料集` `#泛化能力` `#跨人群驗證` `#Synthea` `#SUA` `#雙向驗證` `#模型穩健性`
