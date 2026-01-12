# Archive - 舊版實驗 Notebooks

> **封存日期**：2026-01-13
> **原因**：採用滑動窗口資料 + GroupKFold 後，這些實驗結果已不適用

---

## 封存的 Notebooks

| Notebook | 內容 | 取代方案 |
|----------|------|----------|
| 03_ModelBuilding.ipynb | LR, RF 模型訓練 | → **17_SlidingWindow_5FoldCV.ipynb** |
| 04_XGBoost.ipynb | XGBoost 訓練 | → **17** |
| 05_NeuralNetworks.ipynb | MLP 訓練 | → **17** |
| 06_SVM.ipynb | SVM 訓練 | → **17** |
| 07_GeneticProgramming.ipynb | GP 實驗 | → **17** (或 PySR 系列) |
| 08_SHAP_Analysis.ipynb | SHAP 可解釋性分析 | → **19_SHAP_SlidingWindow.ipynb** |

---

## 為什麼封存？

1. **資料格式變更**：
   - 舊：固定窗口 (T1, T2 → T3)，6,056 樣本
   - 新：滑動窗口 (Ti, Ti+1 → Ti+2)，13,514 樣本

2. **CV 策略變更**：
   - 舊：StratifiedKFold（可能有資料洩漏）
   - 新：StratifiedGroupKFold（同患者不跨 fold）

3. **結果不可比較**：
   - 舊實驗的 AUC 可能偏高（資料洩漏）
   - 新實驗結果更保守但更可靠

---

## 新基準

所有論文數據請使用：
- **17_SlidingWindow_5FoldCV.ipynb** - 模型比較
- **19_SHAP_SlidingWindow.ipynb** - SHAP 分析

---

## 保留的 Notebooks

以下 notebooks 仍在主目錄，未封存：
- 01, 02：EDA 和資料預處理（參考用）
- 08-16：消融實驗、PySR（部分需更新）
- 17+：新實驗
