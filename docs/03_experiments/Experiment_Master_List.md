# 實驗總清單（Master List）

> **建立日期**：2026-01-10
> **更新日期**：2026-01-14
> **用途**：追蹤所有實驗的假說、狀態、結果

---

## 快速導覽

| 狀態 | 數量 |
|------|------|
| ✅ 已完成 | 14 |
| 🔄 進行中 | 1 |
| 📋 待執行 | 1 |
| 🗄️ 已封存 | 6 |

---

## Notebook 狀態總覽

### 目前使用中

| Notebook | 用途 | 狀態 |
|----------|------|------|
| 10_ClassWeight_Ablation | 假說 H5 驗證 | ✅ |
| 14_Checkup_Frequency | 假說 H1 驗證 | ✅ |
| 16_PySR_Parameter_Tuning | PySR 參數參考 | ✅ |
| **17_SlidingWindow_5FoldCV** | **主要結果：基準模型比較** | ✅ |
| 19_SHAP_SlidingWindow | SHAP 可解釋性分析 | ✅ |
| 20_MTL_vs_STL | MTL vs STL 比較 | ✅ |
| 21_Delta_Ablation | Delta 特徵消融 | ✅ |
| 22_Feature_Selection_Ablation | 特徵選擇消融 | ✅ |
| 23_PySR_SlidingWindow | PySR 滑動窗口版本 | ✅ |
| 24_SMOTE_vs_ClassWeight | SMOTE vs class_weight 比較 | 📋 待執行 |
| 25_PySR_Depth_Experiment | PySR 樹深度實驗 | 🔄 進行中 |

### 已封存（archive/）

| Notebook | 封存原因 | 取代版本 |
|----------|----------|----------|
| 03-09 | 舊資料格式（wide_format） | → Nb17 |
| 11_GP_Parameter_Tuning | gplearn 失敗 | → PySR |
| 12_PySR_Experiment | 已有更新版 | → Nb16, Nb23 |
| 13_5FoldCV_Model_Comparison | 舊資料格式 | → Nb17 |
| 14_DecisionTree | 已整合到 Nb17 | → Nb17 |
| 15_PySR_Depth_Experiment | 參數已優化 | → Nb16 |
| 18_PySR_Complex_Formulas | 高血壓退化為常數 | → Nb23 |

---

## ✅ 已完成實驗

### E01. 基礎模型比較（5-Fold CV）⭐ 主要結果

| 項目 | 內容 |
|------|------|
| **假說** | 不同 ML 模型在三高預測上有顯著差異 |
| **完成日期** | 2026-01-12 |
| **Notebook** | [17_SlidingWindow_5FoldCV.ipynb](../../notebooks/experiments/17_SlidingWindow_5FoldCV.ipynb) |
| **資料** | 滑動窗口（13,514 筆），StratifiedGroupKFold |
| **結論** | RF 在高血壓最佳(0.743)；LR 在高血糖(0.938)、高血脂(0.867)最佳 |

**最終結果**：

| 疾病 | 最佳模型 | AUC | 95% CI |
|------|----------|-----|--------|
| 高血壓 | RF | 0.743 | (0.725, 0.762) |
| 高血糖 | LR | 0.938 | (0.924, 0.951) |
| 高血脂 | LR | 0.867 | (0.850, 0.884) |

---

### E02. Delta 特徵消融實驗

| 項目 | 內容 |
|------|------|
| **假說** | H2：變化量特徵（Δ）能提升預測效能 |
| **完成日期** | 2026-01-13 |
| **Notebook** | [21_Delta_Ablation.ipynb](../../notebooks/experiments/21_Delta_Ablation.ipynb) |
| **摘要** | [Delta_Ablation_完整分析.md](summaries/Delta_Ablation_完整分析.md) |
| **結論** | ✅ **已驗證**：Delta 特徵對高血壓貢獻 +7%，對高血糖/高血脂貢獻 +2% |

---

### E03. Class Weight 消融實驗

| 項目 | 內容 |
|------|------|
| **假說** | H5：class_weight='balanced' 能提升 Sensitivity |
| **完成日期** | 2025-12 |
| **Notebook** | [10_ClassWeight_Ablation.ipynb](../../notebooks/experiments/10_ClassWeight_Ablation.ipynb) |
| **結論** | ✅ **已驗證**：balanced 權重大幅提升 Sensitivity（+35%），AUC 幾乎不變 |

---

### E04. SHAP 可解釋性分析

| 項目 | 內容 |
|------|------|
| **假說** | SHAP 能驗證模型學到臨床合理的特徵關係 |
| **完成日期** | 2026-01-13 |
| **Notebook** | [19_SHAP_SlidingWindow.ipynb](../../notebooks/experiments/19_SHAP_SlidingWindow.ipynb) |
| **結論** | 各疾病由核心指標主導（SBP→高血壓、FBG→高血糖、TC→高血脂） |

---

### E05. 健檢次數與預測準確度

| 項目 | 內容 |
|------|------|
| **假說** | H1：使用更多次健檢資料，能提升預測準確度 |
| **完成日期** | 2026-01-10 |
| **Notebook** | [14_Checkup_Frequency_Experiment.ipynb](../../notebooks/experiments/14_Checkup_Frequency_Experiment.ipynb) |
| **結論** | ✅ **已驗證**：但 1 次健檢已有很高 AUC（HG=0.931），高血壓受益最大 |

**結果**：

| 健檢次數 | HTN | HG | DL | 平均 |
|----------|-----|----|----|------|
| 1 次 | 0.666 | 0.931 | 0.867 | 0.821 |
| 4 次 | **0.835** | **0.945** | 0.882 | **0.887** |

---

### E06. MTL vs STL 比較

| 項目 | 內容 |
|------|------|
| **假說** | H3：多任務學習優於單任務學習 |
| **完成日期** | 2026-01-13 |
| **Notebook** | [20_MTL_vs_STL.ipynb](../../notebooks/experiments/20_MTL_vs_STL.ipynb) |
| **摘要** | [MTL_vs_STL_完整分析.md](summaries/MTL_vs_STL_完整分析.md) |
| **結論** | ❌ **未驗證**：MTL 與 STL 效能幾乎相同（差異 < 1%），因三高相關性弱 |

---

### E07. 可解釋性 vs 效能比較

| 項目 | 內容 |
|------|------|
| **假說** | H4：可解釋模型（LR）能達到接近黑盒模型的效能 |
| **完成日期** | 2026-01-12 |
| **Notebook** | [17_SlidingWindow_5FoldCV.ipynb](../../notebooks/experiments/17_SlidingWindow_5FoldCV.ipynb) |
| **結論** | ✅ **已驗證**：LR 在 2/3 疾病上表現最佳 |

---

### E08. 特徵選擇消融

| 項目 | 內容 |
|------|------|
| **假說** | 前 N 個重要特徵可能已足夠達到相近效能 |
| **完成日期** | 2026-01-13 |
| **Notebook** | [22_Feature_Selection_Ablation.ipynb](../../notebooks/experiments/22_Feature_Selection_Ablation.ipynb) |
| **結論** | Top 10 特徵可達到約 95% 的完整模型效能 |

---

### E09. 外部驗證（Synthea）

| 項目 | 內容 |
|------|------|
| **假說** | 模型在外部資料集上仍有良好泛化能力 |
| **完成日期** | 2026-01-13 |
| **摘要** | [External_Validation_Analysis.md](summaries/External_Validation_Analysis.md) |
| **結論** | ⚠️ 僅高血壓可驗證，AUC 下降約 12%（0.72→0.60），可能是族群差異所致 |

**可行性**：

| 疾病 | 可行性 | 原因 |
|------|--------|------|
| 高血壓 | ✅ 有限度 | 資料完整，但年齡分佈差異大 |
| 高血糖 | ❌ 不可行 | 極端選擇偏差（99.4% 陽性）|
| 高血脂 | ⚠️ 有限度 | 中度檢測偏差 |

---

### E10. 共病效應分析

| 項目 | 內容 |
|------|------|
| **假說** | 三高之間有顯著共病效應 |
| **完成日期** | 2026-01-13 |
| **摘要** | [Comorbidity_Analysis.md](summaries/Comorbidity_Analysis.md) |
| **結論** | 三高相關性弱（Phi < 0.1），解釋了 MTL 無優勢的原因 |

---

### E11. PySR 參數調整

| 項目 | 內容 |
|------|------|
| **假說** | H6：符號回歸能找到有臨床意義的數學公式 |
| **完成日期** | 2026-01-10 |
| **Notebook** | [16_PySR_Parameter_Tuning.ipynb](../../notebooks/experiments/16_PySR_Parameter_Tuning.ipynb) |
| **結論** | 最佳參數：parsimony=0.0001, maxsize=35；公式 AUC 接近 LR |

**最佳公式示例**：
- 高血壓：`abs((|Delta_SBP| + SBP_T1 + 1.46) * 0.15)`（AUC=0.780）
- 高血糖：`0.12 * FBG_T2`
- 高血脂：`0.04 * exp(TC_T1)`

---

### E12. gplearn 實驗（已放棄）

| 項目 | 內容 |
|------|------|
| **假說** | gplearn 可用於符號回歸 |
| **完成日期** | 2026-01-10 |
| **Notebook** | archive/11_GP_Parameter_Tuning.ipynb |
| **結論** | ❌ **失敗**：gplearn 不支援 class_weight，在不平衡資料上退化為常數解 |

---

## ✅ 已完成實驗（續）

### E13. PySR 滑動窗口版本

| 項目 | 內容 |
|------|------|
| **假說** | PySR 在滑動窗口資料上可產生穩定的公式 |
| **完成日期** | 2026-01-13 |
| **Notebook** | [23_PySR_SlidingWindow.ipynb](../../notebooks/experiments/23_PySR_SlidingWindow.ipynb) |
| **執行時間** | 161 分鐘（約 2.7 小時） |
| **結論** | 高血糖成功（AUC 0.918，公式 `0.12*FBG_T2`）；高血壓/高血脂不穩定（3/5 fold 退化常數） |

**結果**：

| 疾病 | AUC | 公式穩定性 | 代表公式 |
|------|-----|-----------|----------|
| 高血壓 | 0.580 ± 0.110 | ❌ 3/5 常數 | `0.09*SBP_T2 + 0.19` |
| 高血糖 | 0.918 ± 0.016 | ✅ 5/5 穩定 | `0.12*FBG_T2` |
| 高血脂 | 0.640 ± 0.192 | ❌ 3/5 常數 | `0.09*TC_T2 + 0.08` |

---

## 🔄 進行中實驗

### E14. PySR 樹深度實驗

| 項目 | 內容 |
|------|------|
| **假說** | 使用 Top 5 特徵可產生更深（depth ≥ 2）的公式 |
| **狀態** | 🔄 進行中 |
| **Notebook** | [24_PySR_Depth_Experiment.ipynb](../../notebooks/experiments/24_PySR_Depth_Experiment.ipynb) |
| **設計** | 對比：Top 5 特徵 vs 全部特徵，parsimony=0.0001 vs 0 |
| **預估時間** | 約 3 小時 |

---

## ✅ 已完成實驗（續）

### E15. SMOTE vs class_weight 比較

| 項目 | 內容 |
|------|------|
| **假說** | SMOTE 是否比 class_weight 更好？ |
| **完成日期** | 2026-01-14 |
| **Notebook** | [24_SMOTE_Comparison.ipynb](../../notebooks/experiments/24_SMOTE_Comparison.ipynb) |
| **結論** | ✅ **已驗證**：SMOTE 不比 class_weight 更好，所有方法效果幾乎相同（差異 < 2%） |

**結果**：

| 方法 | 高血壓 Sens | 高血糖 Sens | 高血脂 Sens |
|------|------------|------------|------------|
| Baseline | 0.041 | 0.335 | 0.135 |
| class_weight | 0.698 | 0.861 | 0.791 |
| SMOTE | 0.698 | 0.852 | 0.785 |
| ADASYN | 0.696 | 0.877 | 0.794 |

**推薦**：使用 `class_weight='balanced'`（最簡單有效）

---

## 假說驗證總表

| ID | 假說 | 狀態 | 結論 |
|----|------|------|------|
| H1 | 健檢次數越多，預測越準 | ✅ 已驗證 | 確認，但 1 次已很準 |
| H2 | Delta 特徵能提升效能 | ✅ 已驗證 | 高血壓 +7%，其他 +2% |
| H3 | MTL 優於 STL | ❌ 未驗證 | 無顯著差異（三高相關性弱）|
| H4 | LR 效能接近黑盒模型 | ✅ 已驗證 | LR 在 2/3 疾病最佳 |
| H5 | class_weight 提升 Sensitivity | ✅ 已驗證 | balanced +35% Sensitivity |
| H6 | 符號回歸能找到有意義公式 | ✅ 已驗證 | PySR 可行，公式有臨床意義 |

---

## 相關文件

- [Experiment_Overview.md](Experiment_Overview.md) - 實驗概覽
- [hypothesis_list.md](../07_plans/hypothesis_list.md) - 假說列表
- [Meeting_19_教授問題回覆.md](../04_meetings/Meeting_19_教授問題回覆.md) - 教授問題總整理

---

**最後更新**：2026-01-13
