# GP 套件替代方案研究

> **建立日期**：2025-12-04
> **來源**：Meeting 17 討論
> **狀態**：待評估

---

## 背景

目前使用 **gplearn** 進行 Genetic Programming 實驗，但遇到以下問題：

1. **不支援 class_weight** → 導致高血脂 AUC=0.5（隨機猜測）
2. **parsimony coefficient** 過度簡化公式
3. **效能較慢**（純 Python 實作）

---

## 替代套件比較

| 套件 | 語言 | 速度 | class_weight 支援 | 特點 |
|------|------|------|-------------------|------|
| **gplearn** | Python | 慢 | ❌ 不支援 | 目前使用，sklearn 風格 |
| **PySR** | Julia+Python | 🚀 快 | ⚠️ 可用 sample weights | 最推薦替代方案 |
| **DEAP** | Python | 中 | ⚠️ 需自訂 | 高度客製化 |
| **Operon** | C++ | 🚀🚀 極快 | ⚠️ 需自訂 | 效能最佳 |
| **TurboGP** | Python | 快 | ⚠️ 需自訂 | GPU 加速 |

---

## 推薦方案：PySR

### 基本資訊

- **GitHub**：[MilesCranmer/PySR](https://github.com/MilesCranmer/PySR)
- **論文**：[Interpretable Machine Learning for Science with PySR](https://arxiv.org/abs/2305.01582)
- **特點**：Julia 核心 + Python API，sklearn 相容

### 優點

1. **效能優異**：Julia 核心，比 gplearn 快 10-100 倍
2. **sklearn 相容**：`PySRClassifier` 直接替換
3. **支援 sample weights**：可處理不平衡資料
4. **自訂損失函數**：可用 Julia 語法定義加權損失
5. **常數優化**：內建模擬退火優化常數

### 處理不平衡資料的方式

```python
from pysr import PySRClassifier

# 方式一：使用 sample weights
weights = compute_sample_weight('balanced', y_train)
model = PySRClassifier(
    niterations=100,
    binary_operators=["+", "-", "*", "/"],
    unary_operators=["exp", "log", "sqrt"]
)
model.fit(X_train, y_train, weights=weights)

# 方式二：自訂損失函數（Julia 語法）
model = PySRClassifier(
    elementwise_loss="""
    function loss(prediction, target, weight)
        if target == 1
            return 16.0 * (prediction - target)^2  # 正樣本權重 16 倍
        else
            return (prediction - target)^2
        end
    end
    """
)
```

### 安裝

```bash
pip install pysr

# 首次使用會自動安裝 Julia 依賴
```

---

## 其他選項詳細說明

### DEAP（Distributed Evolutionary Algorithms in Python）

- **GitHub**：https://github.com/DEAP/deap
- **優點**：高度客製化，可完全控制演化過程
- **缺點**：需要更多程式碼，學習曲線陡峭
- **適用**：需要實驗不同演化策略時

```python
from deap import base, creator, tools, algorithms, gp

# 可自訂適應度函數，加入 class_weight
def evalSymbReg(individual, X, y, class_weights):
    func = toolbox.compile(expr=individual)
    predictions = [func(*x) for x in X]
    # 加權損失計算
    weighted_errors = [
        class_weights[yi] * (pred - yi)**2
        for pred, yi in zip(predictions, y)
    ]
    return sum(weighted_errors),
```

### Operon（C++ 實作）

- **GitHub**：https://github.com/heal-research/operon
- **論文**：GECCO 2020
- **優點**：單核效能最佳，比 gplearn 快 ~8 倍
- **缺點**：需要 C++ 編譯環境
- **適用**：追求極致效能時

### TurboGP

- **GitHub**：[TurboGP](https://github.com/l1n0b1/TurboGP)
- **優點**：GPU 加速、支援線上學習
- **缺點**：文件較少
- **適用**：大規模資料集

---

## 實驗建議

### 短期（可快速嘗試）

```python
# 用 PySR 替換 gplearn，比較結果
from pysr import PySRClassifier
from sklearn.utils.class_weight import compute_sample_weight

# 計算權重
weights = compute_sample_weight('balanced', y_train)

# PySR 分類器
model = PySRClassifier(
    niterations=40,
    populations=15,
    binary_operators=["+", "-", "*", "/"],
    unary_operators=["exp", "log", "sqrt", "abs"],
    maxsize=20,
    timeout_in_seconds=300,
)

# 訓練（使用權重）
model.fit(X_train_scaled, y_train, weights=weights)

# 預測
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]
```

### 比較實驗設計

| 實驗 | 套件 | class_weight | 預期 AUC |
|------|------|-------------|----------|
| A | gplearn | ❌ | 0.500（高血脂） |
| B | PySR + weights | ✅ | > 0.7（預期） |
| C | DEAP + 自訂適應度 | ✅ | > 0.7（預期） |

---

## 論文價值

### 可寫入論文的內容

1. **方法論**：比較不同 GP 實作的特性
2. **實驗結果**：gplearn vs PySR 效能比較
3. **討論**：GP 在不平衡資料的挑戰與解法

### 參考文獻

1. Cranmer, M. (2023). [Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl](https://arxiv.org/abs/2305.01582). arXiv.
2. Burlacu, B., et al. (2020). Operon C++: An Efficient Genetic Programming Framework for Symbolic Regression. GECCO.
3. La Cava, W., et al. (2024). [A Comparison of Recent Algorithms for Symbolic Regression to Genetic Programming](https://arxiv.org/html/2406.03585v1). arXiv.

---

## 優先級

- **建議**：先用 PySR 快速驗證是否能改善 GP 結果
- **預估時間**：2-4 小時（含安裝、實驗、比較）
- **產出**：1 張 gplearn vs PySR 比較表

---

**相關文件**：
- [class_weight消融實驗設計.md](class_weight消融實驗設計.md)
- [07_GeneticProgramming.ipynb](../../notebooks/experiments/07_GeneticProgramming.ipynb)

---

**Sources**：
- [PySR GitHub](https://github.com/MilesCranmer/PySR)
- [PySR API Reference](https://astroautomata.com/PySR/api/)
- [TurboGP GitHub](https://github.com/l1n0b1/TurboGP)
- [Symbolic Regression Comparison](https://m2lines.github.io/L96_demo/notebooks/symbolic_methods_comparison.html)
