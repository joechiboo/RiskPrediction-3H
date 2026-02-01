# MTL 計算效益補充程式碼

> **目的**：在各 notebook 補充 MTL vs Single-Task 的計算效益比較
> **日期**：2025-12-04

---

## 補充位置

| Notebook | 模型 | MTL 狀態 | 補充位置 |
|----------|------|----------|----------|
| **03_ModelBuilding** | LR, RF | ✅ 成功 | Section 9 之後 |
| **04_XGBoost** | XGBoost | ✅ 有 MTL | Section 6 之後 |
| **05_NeuralNetworks** | ANN | ⚠️ 部分失敗 | Section 7 之後 |

---

## 通用程式碼範本

```python
import time
import sys
import pickle

print("="*80)
print("計算效益分析：Single-Task vs MTL")
print("="*80)

# ===== 1. 訓練時間比較 =====
# (在訓練模型時就記錄 start/end time)

# ===== 2. 推論時間比較 =====
print("\n推論時間比較")
print("-"*80)

# Single-Task 推論
start = time.time()
for disease, model in single_task_models.items():
    _ = model.predict_proba(X_test_scaled)
single_predict_time = time.time() - start

# MTL 推論
start = time.time()
_ = mtl_model.predict_proba(X_test_scaled)
mtl_predict_time = time.time() - start

print(f"Single-Task 推論時間: {single_predict_time:.4f} 秒")
print(f"MTL 推論時間: {mtl_predict_time:.4f} 秒")
print(f"速度比: {(single_predict_time / mtl_predict_time):.2f}x")

# ===== 3. 模型大小比較 =====
print("\n模型大小比較")
print("-"*80)

single_size = sum(sys.getsizeof(pickle.dumps(m)) for m in single_task_models.values())
mtl_size = sys.getsizeof(pickle.dumps(mtl_model))

print(f"Single-Task (3 模型): {single_size / 1024:.2f} KB")
print(f"MTL (1 模型): {mtl_size / 1024:.2f} KB")
print(f"節省: {(single_size - mtl_size) / 1024:.2f} KB ({(1 - mtl_size/single_size)*100:.1f}%)")

# ===== 4. 綜合比較表 =====
print("\n" + "="*80)
print("綜合比較")
print("="*80)

results = pd.DataFrame([
    {
        '方法': 'Single-Task',
        '訓練時間 (秒)': single_train_time,
        '推論時間 (秒)': single_predict_time,
        '模型大小 (KB)': single_size / 1024,
        '模型數量': 3
    },
    {
        '方法': 'MTL',
        '訓練時間 (秒)': mtl_train_time,
        '推論時間 (秒)': mtl_predict_time,
        '模型大小 (KB)': mtl_size / 1024,
        '模型數量': 1
    }
])

print(results.to_string(index=False))
```

---

## 03_ModelBuilding.ipynb

**位置**：Section 9 (MTL with class_weight) 的最後

```python
# ============================================================
# 新增：MTL 計算效益分析
# ============================================================

import time
import sys
import pickle

print("\n" + "="*80)
print("MTL 計算效益分析")
print("="*80)

# 1. 訓練時間 (需要重新訓練來記錄時間)
print("\n1. 訓練時間比較")
print("-"*80)

# LR Single-Task
start = time.time()
lr_single = {}
for i, disease in enumerate(['高血壓', '高血糖', '高血脂']):
    model = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train_multi[:, i])
    lr_single[disease] = model
lr_single_time = time.time() - start

# LR MTL
start = time.time()
lr_mtl_temp = MultiOutputClassifier(
    LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
)
lr_mtl_temp.fit(X_train_scaled, y_train_multi)
lr_mtl_time = time.time() - start

print(f"LR Single-Task: {lr_single_time:.3f} 秒")
print(f"LR MTL: {lr_mtl_time:.3f} 秒")
print(f"MTL 相對速度: {(lr_single_time / lr_mtl_time):.2f}x")

# RF Single-Task
start = time.time()
rf_single = {}
for i, disease in enumerate(['高血壓', '高血糖', '高血脂']):
    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42, n_jobs=-1)
    model.fit(X_train_scaled, y_train_multi[:, i])
    rf_single[disease] = model
rf_single_time = time.time() - start

# RF MTL
start = time.time()
rf_mtl_temp = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42, n_jobs=-1)
rf_mtl_temp.fit(X_train_scaled, y_train_multi)
rf_mtl_time = time.time() - start

print(f"\nRF Single-Task: {rf_single_time:.3f} 秒")
print(f"RF MTL: {rf_mtl_time:.3f} 秒")
print(f"MTL 相對速度: {(rf_single_time / rf_mtl_time):.2f}x")

# 2. 推論時間
print("\n2. 推論時間比較")
print("-"*80)

# LR
start = time.time()
for model in lr_single.values():
    _ = model.predict_proba(X_test_scaled)
lr_single_pred = time.time() - start

start = time.time()
_ = lr_mtl_temp.predict_proba(X_test_scaled)
lr_mtl_pred = time.time() - start

print(f"LR Single-Task: {lr_single_pred:.4f} 秒")
print(f"LR MTL: {lr_mtl_pred:.4f} 秒")

# RF
start = time.time()
for model in rf_single.values():
    _ = model.predict_proba(X_test_scaled)
rf_single_pred = time.time() - start

start = time.time()
_ = rf_mtl_temp.predict_proba(X_test_scaled)
rf_mtl_pred = time.time() - start

print(f"\nRF Single-Task: {rf_single_pred:.4f} 秒")
print(f"RF MTL: {rf_mtl_pred:.4f} 秒")

# 3. 模型大小
print("\n3. 模型大小比較")
print("-"*80)

lr_single_size = sum(sys.getsizeof(pickle.dumps(m)) for m in lr_single.values())
lr_mtl_size = sys.getsizeof(pickle.dumps(lr_mtl_temp))

rf_single_size = sum(sys.getsizeof(pickle.dumps(m)) for m in rf_single.values())
rf_mtl_size = sys.getsizeof(pickle.dumps(rf_mtl_temp))

print(f"LR Single-Task: {lr_single_size / 1024:.2f} KB")
print(f"LR MTL: {lr_mtl_size / 1024:.2f} KB (節省 {(1 - lr_mtl_size/lr_single_size)*100:.1f}%)")

print(f"\nRF Single-Task: {rf_single_size / 1024:.2f} KB")
print(f"RF MTL: {rf_mtl_size / 1024:.2f} KB (節省 {(1 - rf_mtl_size/rf_single_size)*100:.1f}%)")

# 4. 綜合表格
print("\n" + "="*80)
print("綜合比較表")
print("="*80)

efficiency_df = pd.DataFrame([
    {
        '模型': 'LR',
        '方法': 'Single-Task',
        '訓練時間 (秒)': lr_single_time,
        '推論時間 (秒)': lr_single_pred,
        '模型大小 (KB)': lr_single_size / 1024
    },
    {
        '模型': 'LR',
        '方法': 'MTL',
        '訓練時間 (秒)': lr_mtl_time,
        '推論時間 (秒)': lr_mtl_pred,
        '模型大小 (KB)': lr_mtl_size / 1024
    },
    {
        '模型': 'RF',
        '方法': 'Single-Task',
        '訓練時間 (秒)': rf_single_time,
        '推論時間 (秒)': rf_single_pred,
        '模型大小 (KB)': rf_single_size / 1024
    },
    {
        '模型': 'RF',
        '方法': 'MTL',
        '訓練時間 (秒)': rf_mtl_time,
        '推論時間 (秒)': rf_mtl_pred,
        '模型大小 (KB)': rf_mtl_size / 1024
    }
])

print(efficiency_df.to_string(index=False))
```

---

## 04_XGBoost.ipynb

**位置**：Section 6 (MTL XGBoost) 的最後

```python
# ============================================================
# 新增：XGBoost MTL 計算效益分析
# ============================================================

print("\n" + "="*80)
print("XGBoost MTL 計算效益分析")
print("="*80)

# 需要重新訓練來記錄時間
# (參考上面的程式碼，調整成 XGBoost)
```

---

## 05_NeuralNetworks.ipynb

**位置**：Section 7 (ANN 效能比較) 的最後

```python
# ============================================================
# 新增：ANN MTL 計算效益分析
# ============================================================

print("\n" + "="*80)
print("ANN MTL 計算效益分析")
print("="*80)

# ANN 已經有部分比較了
# 補充：訓練時間、推論時間、模型大小
```

---

## 執行順序

1. **03_ModelBuilding.ipynb** - 先做這個（LR, RF 最簡單）
2. **05_NeuralNetworks.ipynb** - 你說的 9 秒應該在這
3. **04_XGBoost.ipynb** - 最後做這個

---

**相關文件**：
- [MTL實驗保留與分析.md](MTL實驗保留與分析.md)
