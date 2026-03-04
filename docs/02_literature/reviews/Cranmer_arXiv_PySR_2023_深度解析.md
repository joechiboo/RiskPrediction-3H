# Cranmer (2023) arXiv — PySR 符號回歸工具深度解析

> **論文**：Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl
> **發表**：arXiv:2305.01582v3, 2023 年 5 月 2 日
> **作者**：Miles Cranmer
> **機構**：Princeton University / Flatiron Institute, New York
> **DOI**：[10.48550/arXiv.2305.01582](https://doi.org/10.48550/arXiv.2305.01582)
> **PDF**：[Cranmer_arXiv_PySR_2023.pdf](../papers/Cranmer_arXiv_PySR_2023.pdf)
> **與本研究關聯度**：⭐⭐⭐（Tier 2 — 本研究使用 PySR 進行符號回歸，此為工具論文）

---

## 一句話摘要

**PySR 是一個開源的 Python/Julia 符號回歸（SR）庫，核心為多族群演化算法 + 獨特的 evolve-simplify-optimize 循環，支援自定義算子、自定義損失函數、深度學習接口和分散式運算；在新提出的 EmpiricalBench 基準測試中，PySR 在 9 個歷史經驗方程的重新發現任務中表現最佳（35/45 次成功）。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **論文類型** | 軟體工具論文（Software Paper） |
| **核心軟體** | PySR (Python 前端) + SymbolicRegression.jl (Julia 後端) |
| **GitHub** | github.com/MilesCranmer/PySR |
| **首次公開** | 2020 年 |
| **程式語言** | Python 前端 + Julia 後端（JIT 編譯） |
| **授權** | 開源 |
| **scikit-learn 接口** | ✅ PySRRegressor 完全相容 |
| **引用量** | 截至 2025 年已被廣泛引用（天文、氣候、經濟、材料科學等） |

---

## 核心方法：符號回歸（Symbolic Regression）

### 什麼是符號回歸

- **定義**：在分析表達式（analytic expressions）空間中搜尋模型的監督式學習任務
- **目標**：發現**可被人類理解的符號模型**（數學公式），而非黑箱預測
- **多目標優化**：同時最小化預測誤差和模型複雜度
- **科學歷史**：Kepler 第三定律、Planck 黑體輻射定律都是「手動符號回歸」的成果

### SR 的挑戰（作者列出 9 項）

1. **搜尋空間巨大**：含實數常數時，方程空間不可數無窮
2. **需提供科學洞察**：最準的不一定最有用，需平衡準確性與簡潔性
3. **雜訊資料**：真實資料含異質性雜訊
4. **不可微分表達式**：分段函數、條件表達式
5. **已知約束**：如守恆律
6. **自定義算子**：不同領域有獨特的數學函數
7. **高維資料**：需整合特徵選擇
8. **非表格資料**：序列、網格、圖等
9. **開源、跨平台、易用**

---

## PySR 演算法

### 架構概覽

```
外層循環：多族群島模型（Island Model）
├── Population 1 ──→ 獨立演化 ──→ 遷移
├── Population 2 ──→ 獨立演化 ──→ 遷移
├── ...
└── Population np ──→ 獨立演化 ──→ 遷移
                                     ↓
                              全域名人堂（Hall of Fame）
                              保存各複雜度最佳表達式

內層循環：Evolve-Simplify-Optimize
├── Evolve：錦標賽選擇 + 突變/交叉（nc=300,000 次）
├── Simplify：代數簡化（等價變換）
└── Optimize：BFGS 優化表達式中的實數常數
```

### 三大關鍵改進

| 改進 | 說明 |
|------|------|
| **1. 模擬退火** | 溫度 T 從 1 遞減到 0，高溫階段增加多樣性，低溫階段聚焦最佳個體 |
| **2. Evolve-Simplify-Optimize 循環** | 多次突變後才簡化+優化常數，允許冗餘中間態（如 x−x→xx→x−y） |
| **3. 自適應簡約性（Adaptive Parsimony）** | 懲罰過度出現的複雜度等級，確保搜尋均衡探索不同複雜度層級 |

### 演化操作（8 種突變）

| 突變類型 | 說明 |
|---------|------|
| 1. 突變常數 | 隨機擾動表達式中的數值常數 |
| 2. 突變算子 | 替換同維度的算子（如 + → −） |
| 3. 附加節點 | 在根或葉添加隨機節點 |
| 4. 插入節點 | 在表達式內部插入隨機節點 |
| 5. 刪除子樹 | 用常數或變數替換子樹 |
| 6. 簡化樹 | 代數簡化 |
| 7. 全新樹 | 完全隨機的新表達式 |
| 8. 不突變 | 保持不變 |

### 年齡正則化（Age-Regularized Evolution）

- 替換族群中**最老的**個體（而非最差的）
- 防止族群過早特化，避免局部最優
- 靈感來自神經架構搜尋（NAS）的成功經驗

---

## 軟體實現

### Python API（scikit-learn 風格）

```python
from pysr import PySRRegressor
model = PySRRegressor(
    model_selection="best",
    unary_operators=["cos", "sin"],
    binary_operators=["+", "-", "/", "*"],
)
model.fit(X, y)
print(model)
y_predicted = model.predict(X, 5)  # 用 Pareto 前沿第 5 個表達式
```

### 關鍵功能

| 功能 | 說明 |
|------|------|
| **自定義算子** | 任意 R→R 或 R²→R 函數 |
| **自定義損失** | 任意損失函數（含加權、分類） |
| **特徵選擇** | 梯度提升樹預篩選重要特徵 |
| **去噪** | 高斯過程預處理 |
| **約束** | 最大表達式大小、深度、算子嵌套限制 |
| **多節點平行** | 跨千核集群分散式搜尋 |
| **SIMD 核融合** | JIT 編譯自動融合算子組合為 SIMD 核心 |
| **匯出** | SymPy, NumPy, PyTorch, JAX |
| **Pareto 前沿** | 輸出不同複雜度-準確度的完整 Pareto 前沿 |

### 與深度學習的接口

- 支援 **PyTorch** 和 **JAX** 匯出
- 常數可作為可訓練參數（nn.Parameter）
- 可與「符號蒸餾」（Symbolic Distillation）結合：先訓練神經網路，再用 PySR 提取符號表達式

---

## 基準測試：EmpiricalBench

### 設計理念

- 現有基準（Feynman、Nguyen、SRBench）多為合成資料或已知物理常數
- **EmpiricalBench 使用真實歷史經驗方程 + 原始/合成資料**
- 9 個方程，每個 5 次試驗，共 45 次

### 9 個經驗方程

| 方程 | 領域 | 複雜度 |
|------|------|--------|
| Hubble 定律 v = H₀D | 天文（線性） | 低 |
| Kepler 第三定律 P² ∝ a³ | 天文 | 低 |
| Newton 萬有引力 | 物理 | 中 |
| Planck 黑體輻射 | 物理 | 高 |
| Leavitt 定律 | 天文 | 低 |
| Schechter 函數 | 天文 | 高 |
| Bode 定律 | 天文 | 中 |
| 理想氣體方程 | 物理 | 中 |
| Rydberg 公式 | 物理 | 中 |

### 結果（6 種 SR 算法比較）

| 算法 | 正確恢復次數 /45 | 類型 |
|------|----------------|------|
| **PySR** | **35/45** | 演化算法 |
| Operon | 9/45 | 演化算法 |
| DSR | 17/45 | 強化學習 |
| QLattice | 5/45 | 演化算法 |
| EQL | 0/45 | 深度學習 |
| SR-Transformer | 0/45 | 深度學習（預訓練） |

### 關鍵發現

1. **PySR 大幅領先**：35/45 正確，遠超第二名 DSR（17/45）
2. **純深度學習方法最差**：EQL 和 SR-Transformer 均為 0/45
3. **傳統演化算法 > 深度學習**：面對真實雜訊資料，手工設計的啟發式算法仍優於預訓練模型
4. **Planck 和 Rydberg 最難**：所有算法在此兩方程上均失敗或接近失敗

### SR 工具全面比較（Table 1）

| 特性 | PySR | Eureqa | GPLearn | Operon | DSR | EQL |
|------|------|--------|---------|--------|-----|-----|
| 編譯型 | ✅ | ✅ | - | ✅ | - | ✅ |
| 多核心 | ✅ | ✅ | ✅ | ✅ | - | ✅ |
| 多節點 | ✅ | - | - | - | - | - |
| 開源 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| 自定義算子 | ✅ | - | ✅ | - | - | - |
| 自定義損失 | ✅ | ✅ | ✅ | - | ✅ | - |
| 深度學習匯出 | ✅ | - | - | - | - | - |
| 表達力分數 | 4 | 5 | 4 | 3 | 3 | 2 |

→ PySR 是功能最全面的開源 SR 工具

---

## 與本研究的關聯

### 本研究如何使用 PySR

本研究在 8 種傳統 ML 模型之外，額外使用 PySR 進行符號回歸，目標是：

1. **從黑箱到白箱**：將 ML 模型的預測知識提煉為可讀的數學公式
2. **臨床可解釋性**：醫療人員可直接理解、驗證公式的生理意義
3. **簡約模型**：發現「用最少變數達到足夠準確度」的精簡預測公式
4. **Pareto 前沿分析**：在複雜度與準確度之間找到最佳平衡點

### 本研究可引用的論證

1. **PySR 是目前最全面的開源 SR 工具**：Table 1 的全面比較支持工具選擇的合理性
2. **EmpiricalBench 中的最佳表現**：35/45 正確率遠超其他方法，證明 PySR 在真實資料上的可靠性
3. **evolve-simplify-optimize 循環的創新**：BFGS 優化實數常數是實際應用的關鍵
4. **scikit-learn 接口**：易於整合到現有 ML 管線
5. **多目標 Pareto 前沿**：可同時獲得不同複雜度的多個公式，供臨床選擇
6. **跨領域成功應用**：天文、氣候、經濟、材料科學等，本研究為醫療健康領域的新應用

### 為什麼符號回歸適合本研究

| 需求 | PySR 的回應 |
|------|-----------|
| 臨床可解釋性 | 輸出人類可讀的數學公式 |
| 精簡模型 | 自動搜尋簡約表達式 |
| 自定義算子 | 可加入醫學相關函數（如 log、exp） |
| 特徵選擇 | 內建梯度提升樹特徵篩選 |
| 與 ML 互補 | SHAP 解釋黑箱，PySR 提供白箱替代 |

---

## 研究限制

1. **本文為工具論文**：未直接應用於醫療領域（主要在物理和天文）
2. **EmpiricalBench 偏向物理/天文**：9 個方程全來自自然科學
3. **作者為 PySR 開發者**：基準測試中可能對自己的工具更熟悉
4. **SR 本身的限制**：
   - 搜尋空間隨維度指數增長
   - 對高維資料（>10 特徵）需要配合特徵選擇
   - 對雜訊敏感度高於黑箱模型
   - 收斂時間長，非確定性結果
5. **未比較 SR 在醫療領域的效能**：缺乏醫學 benchmark
6. **arXiv 預印本**：尚未經同儕審查（但工具本身已被廣泛使用和引用）

---

## 對本論文寫作的引用建議

### 第三章（研究方法）
- 作為 PySR 工具的引用來源，說明演算法原理
- 引用 evolve-simplify-optimize 循環和自適應簡約性
- 引用 scikit-learn 接口和 Pareto 前沿分析
- 說明為何選擇 PySR：最全面的開源 SR 工具、EmpiricalBench 最佳表現

### 第六章（實驗結果）
- 在報告 PySR 發現的公式時，引用其 Pareto 前沿概念
- 說明公式的複雜度-準確度權衡

### 第七章（討論）
- 討論 SR 在醫療領域的創新性：「多數慢性病預測研究使用黑箱 ML，本研究首次引入 SR 提供可讀公式」
- 引用 Cranmer 的觀點：「最有洞察力的方程不一定是最準確的，而是平衡準確性與簡潔性的」
- 討論 SR 在臨床決策支援中的潛力

---

## 關鍵引述

> "In this family of algorithms, instead of fitting concrete parameters in some overparameterized general model, one searches the space of simple analytic expressions for accurate and interpretable models."

> "The equation which often holds the most insight, and is therefore adopted by scientists, is not always the most accurate, but is instead an equation which balances accuracy with simplicity."

> "PySR was developed to democratize and popularize symbolic regression for the sciences."

> "The two pure deep learning approaches, EQL and SR-Transformer, recovered the fewest expressions out of all tested algorithms... handwritten standard algorithms will often perform just as well on unexpected examples."