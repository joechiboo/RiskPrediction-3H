# MTL 實驗保留與分析

> **建立日期**：2025-12-04
> **來源**：Meeting 17 教授建議
> **狀態**：保留實驗，補充分析

---

## 背景

原本考慮移除 MTL（Multi-Task Learning）實驗，因為：
- 效能提升有限
- Single-Task 已經足夠好
- 資料量小，效率優勢不存在

**教授建議**：保留 MTL，可以豐富論文內容，並補充計算效益與精確時間比較。

---

## 目前 MTL 結果回顧

### AUC 比較

| 模型 | 高血壓 | 高血糖 | 高血脂 |
|------|--------|--------|--------|
| **RF Single-Task** | 0.796 | 0.892 | 0.868 |
| **RF MTL** | 0.787 | **0.914** ⬆️ | 0.873 |
| **差異** | -0.009 | **+0.022** | +0.005 |

| 模型 | 高血壓 | 高血糖 | 高血脂 |
|------|--------|--------|--------|
| **ANN Single-Task** | 0.803 | 0.899 | 0.861 |
| **ANN MTL** | 失敗 | 失敗 | 失敗 |

### 結論
- RF MTL 在高血糖上有明顯提升（+0.022）
- ANN MTL 完全失敗
- 整體而言提升有限

---

## 需要補充的分析

### 1. 精確訓練時間比較

```python
import time

# Single-Task 訓練時間
start = time.time()
for disease in ['高血壓', '高血糖', '高血脂']:
    model = train_single_task(disease)
single_task_time = time.time() - start

# MTL 訓練時間
start = time.time()
model = train_mtl(['高血壓', '高血糖', '高血脂'])
mtl_time = time.time() - start

print(f"Single-Task 總時間: {single_task_time:.2f} 秒")
print(f"MTL 訓練時間: {mtl_time:.2f} 秒")
print(f"時間節省: {(single_task_time - mtl_time) / single_task_time * 100:.1f}%")
```

### 2. 計算效益表格

| 指標 | Single-Task (×3) | MTL | 比較 |
|------|------------------|-----|------|
| **訓練時間** | ? 秒 | ? 秒 | ? |
| **模型大小** | 3 個模型 | 1 個模型 | MTL 更小 |
| **推論時間** | ? 秒 | ? 秒 | ? |
| **記憶體使用** | ? MB | ? MB | ? |

### 3. 論文可寫的內容

#### 正面發現
- RF MTL 在高血糖提升 0.022
- 單一模型同時預測三種疾病
- 理論上更適合臨床部署（一次推論）

#### 負面發現（同樣有價值）
- ANN MTL 失敗 → 分析原因
- 效率優勢在小資料集不明顯
- Single-Task 仍是更好選擇

---

## 實驗設計：計算效益分析

```python
import time
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

results = {
    'method': [],
    'train_time': [],
    'predict_time': [],
    'model_size': [],
}

# ===== Single-Task =====
start = time.time()
models = {}
for i, disease in enumerate(['高血壓', '高血糖', '高血脂']):
    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    model.fit(X_train_scaled, y_train_multi[:, i])
    models[disease] = model
single_train_time = time.time() - start

# Single-Task 推論時間
start = time.time()
for disease, model in models.items():
    _ = model.predict_proba(X_test_scaled)
single_predict_time = time.time() - start

# Single-Task 模型大小（估計）
single_model_size = sum(sys.getsizeof(m) for m in models.values())

# ===== MTL =====
start = time.time()
mtl_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
mtl_model.fit(X_train_scaled, y_train_multi)  # RF 原生支援多輸出
mtl_train_time = time.time() - start

# MTL 推論時間
start = time.time()
_ = mtl_model.predict_proba(X_test_scaled)
mtl_predict_time = time.time() - start

# MTL 模型大小
mtl_model_size = sys.getsizeof(mtl_model)

# ===== 結果 =====
print("=" * 50)
print("計算效益比較")
print("=" * 50)
print(f"{'指標':<15} {'Single-Task':<15} {'MTL':<15} {'差異':<15}")
print("-" * 50)
print(f"{'訓練時間':<15} {single_train_time:.3f} 秒{'':<6} {mtl_train_time:.3f} 秒{'':<6} {(mtl_train_time/single_train_time-1)*100:+.1f}%")
print(f"{'推論時間':<15} {single_predict_time:.3f} 秒{'':<6} {mtl_predict_time:.3f} 秒{'':<6} {(mtl_predict_time/single_predict_time-1)*100:+.1f}%")
print(f"{'模型數量':<15} {'3 個':<15} {'1 個':<15} {'-66.7%':<15}")
```

---

## 預期結果表格（論文用）

| 指標 | Single-Task | MTL | 結論 |
|------|-------------|-----|------|
| **平均 AUC** | 0.852 | 0.858 | 相近 |
| **訓練時間** | ~X.XX 秒 | ~Y.YY 秒 | 待測 |
| **推論時間** | ~X.XX 秒 | ~Y.YY 秒 | 待測 |
| **模型數量** | 3 個 | 1 個 | MTL 更精簡 |
| **部署複雜度** | 高 | 低 | MTL 更簡單 |

---

## 論文撰寫建議

### 可寫入的段落

> Multi-Task Learning (MTL) 實驗顯示，RF MTL 在高血糖預測上達到 0.914 的 AUC，
> 比 Single-Task 版本提升了 0.022。然而，整體而言 MTL 的優勢有限：
>
> 1. **效能提升微小**：僅高血糖有明顯改善
> 2. **效率優勢不存在**：資料量僅 6,056 筆，所有模型訓練時間皆在秒級
> 3. **ANN MTL 失敗**：多任務共享層架構導致各任務相互干擾
>
> 儘管如此，MTL 仍具有實務價值：單一模型同時預測三種疾病，
> 簡化了臨床部署的複雜度。未來研究可探索更大規模資料集上的 MTL 效益。

---

## 優先級

- **優先級**：中（論文豐富性）
- **預估時間**：30 分鐘（補充計時實驗）
- **產出**：1 張計算效益比較表

---

**相關文件**：
- [訓練集與測試集的切分方式.md](訓練集與測試集的切分方式.md)
- [03_ModelBuilding.ipynb](../../notebooks/experiments/03_ModelBuilding.ipynb)
