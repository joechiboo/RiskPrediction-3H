# Archive - 已封存的 Notebooks

> **封存日期**：2026-01-13
> **原因**：採用滑動窗口資料 + GroupKFold 後，這些實驗結果已不適用

---

## 封存的 Notebooks

| Notebook | 內容 | 封存原因 | 取代方案 |
|----------|------|----------|----------|
| 03_ModelBuilding | LR, RF 模型訓練 | 舊資料格式 | → Nb17 |
| 04_XGBoost | XGBoost 訓練 | 舊資料格式 | → Nb17 |
| 05_NeuralNetworks | MLP 訓練 | 舊資料格式 | → Nb17 |
| 06_SVM | SVM 訓練 | 舊資料格式 | → Nb17 |
| 07_GeneticProgramming | gplearn 實驗 | 失敗（常數解） | → PySR |
| 08_SHAP_Analysis | SHAP 分析 | 舊資料格式 | → Nb19 |
| 09_Delta_Ablation | Delta 消融（舊） | 舊資料格式 | → Nb21 |
| 11_GP_Parameter_Tuning | gplearn 參數調整 | gplearn 放棄 | → PySR |
| 12_PySR_Experiment | PySR 基礎版 | 已有更新版 | → Nb16, Nb23 |
| 13_5FoldCV_Model_Comparison | 5-Fold CV | 舊資料格式 | → Nb17 |
| 14_DecisionTree | DT 實驗 | 已整合到 Nb17 | → Nb17 |
| 15_PySR_Depth_Experiment | PySR 深度測試 | 參數已優化 | → Nb16 |
| 18_PySR_Complex_Formulas | PySR 複雜公式 | 高血壓退化 | → Nb23 |

---

## 為什麼封存？

1. **資料格式變更**：
   - 舊：固定窗口 (T1, T2 → T3)，6,056 樣本
   - 新：滑動窗口 (Ti, Ti+1 → Ti+2)，13,514 樣本

2. **CV 策略變更**：
   - 舊：StratifiedKFold（可能有資料洩漏）
   - 新：StratifiedGroupKFold（同患者不跨 fold）

3. **gplearn 放棄，改用 PySR**：
   - gplearn 不支援 class_weight，在不平衡資料上退化為常數解
   - PySR 5-Fold CV 結果：高血壓 0.684、高血糖 0.899、高血脂 0.795
   - PySR 公式深度低（depth=1），但符合醫學直覺
   - **結論**：論文以 LR/XGBoost 為主，PySR 公式作為可解釋性補充

---

## 目前使用的 Notebooks

| Notebook | 用途 |
|----------|------|
| 10_ClassWeight_Ablation | 假說驗證：balanced 提升 Sensitivity |
| 14_Checkup_Frequency | 假說驗證：健檢次數 vs 準確度 |
| 16_PySR_Parameter_Tuning | PySR 最佳參數參考 |
| **17_SlidingWindow_5FoldCV** | **主要結果：基準模型比較** |
| 19_SHAP_SlidingWindow | 特徵重要性 SHAP 分析 |
| 20_MTL_vs_STL | MTL vs STL 比較 |
| 21_Delta_Ablation | Delta 特徵消融 |
| 22_Feature_Selection_Ablation | 特徵選擇消融 |
| 23_PySR_SlidingWindow | PySR 滑動窗口版本 |

---

## 論文數據來源

所有論文數據請使用：
- **17_SlidingWindow_5FoldCV.ipynb** - 模型比較
- **19_SHAP_SlidingWindow.ipynb** - SHAP 分析
- **21_Delta_Ablation.ipynb** - Delta 消融
- **23_PySR_SlidingWindow.ipynb** - PySR 可解釋公式
