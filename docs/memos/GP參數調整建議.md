# GP 參數調整建議

> **建立日期**：2025-12-04
> **來源**：Meeting 17 教授建議
> **狀態**：待執行實驗

---

## 目前參數設定

```python
gp_params = {
    'generations': 20,           # ← 教授：太少
    'tournament_size': 20,       # ← 教授：太多
    'population_size': 500,
    'function_set': ('add', 'sub', 'mul', 'div', 'log', 'sqrt', 'abs', 'neg', 'max', 'min'),
    'parsimony_coefficient': 0.01,
    # max_depth 未明確設定（預設值）
}
```

---

## 教授建議的調整

### 1. 世代數（generations）

| 參數 | 目前 | 建議 | 說明 |
|------|------|------|------|
| `generations` | 20 | 100 / 200 / 300 | 給 GP 更多時間演化 |

**實驗設計**：
```python
generations_to_test = [20, 100, 200, 300]
```

**預期**：更多世代 → 公式更精緻，但訓練時間更長

---

### 2. 錦標賽大小（tournament_size）

| 參數 | 目前 | 建議 | 說明 |
|------|------|------|------|
| `tournament_size` | 20 | 2 | 降低選擇壓力 |

**實驗設計**：
```python
tournament_sizes_to_test = [1, 2, 3, 5, 20]
```

**原理**：
- `tournament_size` 大 → 選擇壓力大 → 快速收斂，但容易陷入局部最優
- `tournament_size` 小 → 選擇壓力小 → 保持多樣性，探索更多解空間

**教授觀點**：20 太大，導致過早收斂，應該用 2 左右

---

### 3. 函數集（function_set）

| 參數 | 目前 | 建議 |
|------|------|------|
| `function_set` | 基本運算 | 增加更多函數 |

**目前函數集**：
```python
('add', 'sub', 'mul', 'div', 'log', 'sqrt', 'abs', 'neg', 'max', 'min')
```

**可新增的函數**：
```python
# gplearn 支援的額外函數
'sin'      # 正弦
'cos'      # 餘弦
'tan'      # 正切
'inv'      # 1/x（倒數）
```

**建議擴展**：
```python
function_set_extended = (
    # 基本運算
    'add', 'sub', 'mul', 'div',
    # 數學函數
    'log', 'sqrt', 'abs', 'neg',
    # 比較函數
    'max', 'min',
    # 三角函數（新增）
    'sin', 'cos',
    # 倒數（新增）
    'inv'
)
```

---

### 4. 樹深度（max_depth / init_depth）

| 參數 | 目前 | 建議 |
|------|------|------|
| `max_depth` | 未設定（預設） | 嘗試不同深度 |
| `init_depth` | 未設定（預設） | 配合 max_depth |

**gplearn 預設值**：
- `init_depth = (2, 6)` - 初始樹深度範圍
- `max_depth` 無明確預設，但受 init_depth 影響

**實驗設計**：
```python
max_depths_to_test = [5, 10, 15, 20]
init_depths_to_test = [(2, 6), (3, 8), (4, 10)]
```

**原理**：
- 深度小 → 公式簡單，可能欠擬合
- 深度大 → 公式複雜，可能過擬合

---

## 完整實驗設計

### 策略一：逐一調整（推薦）

```python
# 基準參數
base_params = {
    'population_size': 500,
    'parsimony_coefficient': 0.01,
    'random_state': 42,
}

# 實驗 1：調整世代數
for gen in [20, 100, 200, 300]:
    params = {**base_params, 'generations': gen, 'tournament_size': 2}
    run_experiment(params)

# 實驗 2：調整錦標賽大小
for ts in [1, 2, 3, 5]:
    params = {**base_params, 'generations': 100, 'tournament_size': ts}
    run_experiment(params)

# 實驗 3：調整函數集
for fs in [basic_functions, extended_functions]:
    params = {**base_params, 'generations': 100, 'tournament_size': 2, 'function_set': fs}
    run_experiment(params)

# 實驗 4：調整樹深度
for depth in [5, 10, 15]:
    params = {**base_params, 'generations': 100, 'tournament_size': 2, 'max_depth': depth}
    run_experiment(params)
```

### 策略二：網格搜尋（全面但耗時）

```python
from itertools import product

param_grid = {
    'generations': [100, 200],
    'tournament_size': [2, 3],
    'max_depth': [10, 15],
    'function_set': [basic, extended],
}

# 2 × 2 × 2 × 2 = 16 組實驗 × 3 疾病 = 48 次訓練
```

---

## 預期改善

| 調整 | 預期效果 |
|------|----------|
| 增加世代 | 公式更精緻，AUC 可能提升 |
| 降低錦標賽 | 保持多樣性，避免局部最優 |
| 擴展函數集 | 更多表達能力，可能找到更好的公式 |
| 增加樹深度 | 更複雜的關係，但要注意過擬合 |

---

## 實驗優先級

1. **第一優先**：`tournament_size = 2` + `generations = 100`
   - 教授明確建議，最容易驗證效果

2. **第二優先**：擴展 `function_set`
   - 低成本嘗試，可能有意外收穫

3. **第三優先**：調整 `max_depth`
   - 需要更多實驗來找到最佳值

---

## 預估時間

| 實驗 | 組數 | 時間/組 | 總時間 |
|------|------|---------|--------|
| 世代調整 | 4 | ~10-30 min | 1-2 小時 |
| 錦標賽調整 | 4 | ~10 min | 40 min |
| 函數集調整 | 2 | ~10 min | 20 min |
| 樹深度調整 | 3 | ~10 min | 30 min |

**總計**：約 3-4 小時（單疾病）

---

## 注意事項

1. **仍然沒有 class_weight**：參數調整可能改善，但根本問題未解決
2. **建議搭配 PySR**：同時用 PySR 做對照實驗
3. **記錄演化公式**：每次實驗都保存最終公式，分析差異

---

**相關文件**：
- [GP套件替代方案研究.md](GP套件替代方案研究.md)
- [class_weight消融實驗設計.md](class_weight消融實驗設計.md)
- [07_GeneticProgramming.ipynb](../../notebooks/experiments/07_GeneticProgramming.ipynb)
