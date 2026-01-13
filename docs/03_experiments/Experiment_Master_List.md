# 實驗總清單（Master List）

> **建立日期**：2026-01-10
> **狀態**：持續更新
> **用途**：追蹤所有實驗的假說、狀態、結果

---

## 快速導覽

| 狀態 | 數量 |
|------|------|
| ✅ 已完成 | 7 |
| 🔄 進行中 | 2 |
| 📋 待執行 | 7 |
| 💡 未來構想 | 3 |

---

## ✅ 已完成實驗

### E01. 基礎模型比較（5-Fold CV）

| 項目 | 內容 |
|------|------|
| **假說** | 不同 ML 模型在三高預測上有顯著差異 |
| **完成日期** | 2026-01-07 |
| **Notebook** | [13_5FoldCV_Model_Comparison.ipynb](../../notebooks/experiments/13_5FoldCV_Model_Comparison.ipynb) |
| **結論** | LR 在高血糖(0.932)、高血脂(0.867)最佳；RF 在高血壓(0.788)最佳 |

### E02. Delta 特徵消融實驗

| 項目 | 內容 |
|------|------|
| **假說** | H2：變化量特徵（Δ）能提升預測效能 |
| **完成日期** | 2025-12 |
| **Notebook** | [09_Delta_Ablation.ipynb](../../notebooks/experiments/09_Delta_Ablation.ipynb) |
| **摘要** | [Delta消融實驗分析.md](summaries/Delta消融實驗分析.md) |
| **結論** | ✅ **已驗證**：T2+Delta 組合表現最佳 |

### E03. Class Weight 消融實驗

| 項目 | 內容 |
|------|------|
| **假說** | H5：class_weight='balanced' 能提升 Sensitivity |
| **完成日期** | 2025-12 |
| **Notebook** | [10_ClassWeight_Ablation.ipynb](../../notebooks/experiments/10_ClassWeight_Ablation.ipynb) |
| **摘要** | [ClassWeight消融實驗分析.md](summaries/ClassWeight消融實驗分析.md) |
| **結論** | ✅ **已驗證**：balanced 權重大幅提升 Sensitivity，AUC 幾乎不變 |

### E04. SHAP 可解釋性分析

| 項目 | 內容 |
|------|------|
| **假說** | SHAP 能驗證模型學到臨床合理的特徵關係 |
| **完成日期** | 2025-12 |
| **Notebook** | [08_SHAP_Analysis.ipynb](../../notebooks/experiments/08_SHAP_Analysis.ipynb) |
| **摘要** | [SHAP可解釋性分析.md](summaries/SHAP可解釋性分析.md) |
| **結論** | 各疾病由核心指標主導（SBP→高血壓、FBG→高血糖、TC→高血脂） |

### E05. GP 符號回歸實驗

| 項目 | 內容 |
|------|------|
| **假說** | H6：符號回歸能找到有臨床意義的數學公式 |
| **完成日期** | 2026-01 |
| **Notebook** | [11_GP_Experiment.ipynb](../../notebooks/experiments/11_GP_Experiment.ipynb), [12_PySR_Experiment.ipynb](../../notebooks/experiments/12_PySR_Experiment.ipynb) |
| **摘要** | [GP符號回歸實驗總結.md](summaries/GP符號回歸實驗總結.md) |
| **結論** | gplearn 不支援 class_weight；PySR 可學到公式但 AUC 低於 LR/XGB |

### E06. MTL 計算效益分析

| 項目 | 內容 |
|------|------|
| **假說** | MTL 比 STL 訓練效率更高 |
| **完成日期** | 2025-12 |
| **摘要** | [MTL實驗保留與分析.md](summaries/MTL實驗保留與分析.md) |
| **結論** | MTL 訓練時間約為 STL 的 1/3 |

### E07. 可解釋性 vs 效能比較

| 項目 | 內容 |
|------|------|
| **假說** | H4：可解釋模型（LR）能達到接近黑盒模型的效能 |
| **完成日期** | 2026-01-07 |
| **結論** | ✅ **已驗證**：LR 在 2/3 疾病上表現最佳 |

---

## 🔄 進行中實驗

### E08. PySR 參數調整 + 5-Fold CV

| 項目 | 內容 |
|------|------|
| **假說** | 系統性參數調整可讓 PySR 產生穩定高效能公式 |
| **狀態** | 進行中 |
| **待完成** | Grid Search 參數組合、5-fold CV 驗證 |

---

## 📋 待執行實驗

### E09. 健檢次數與預測準確度（H1）

| 項目 | 內容 |
|------|------|
| **假說** | H1：使用更多次健檢資料，能提升預測準確度 |
| **優先度** | 🔥🔥🔥 高 |
| **設計** | T1→T2 vs T1+T2→T3 vs T1+T2+T3→T4 |
| **預期** | AUC 隨健檢次數增加而上升，但有邊際遞減 |
| **詳細** | [Future_Experiment_Ideas.md](Future_Experiment_Ideas.md) 實驗構想 2 |

### E10. MTL vs STL 完整比較（H3）

| 項目 | 內容 |
|------|------|
| **假說** | H3：多任務學習優於單任務學習 |
| **優先度** | 🔥🔥 中高 |
| **設計** | STL（3獨立模型）vs MTL（共享層+3輸出頭）|
| **指標** | 各疾病 AUC、macro-AUC、訓練時間 |

### E11. CatBoost 模型加入

| 項目 | 內容 |
|------|------|
| **假說** | CatBoost 可能比 XGBoost 表現更好（JMIR 2025 顯示） |
| **優先度** | 🔥 中 |
| **參考** | JMIR 2025：CatBoost(0.819) > LightGBM(0.813) > XGBoost(0.811) |

### E12. PR-AUC 評估指標補充

| 項目 | 內容 |
|------|------|
| **假說** | PR-AUC 比 ROC-AUC 更能反映不平衡資料的預測能力 |
| **優先度** | 🔥 中 |
| **設計** | 在 5-fold CV 框架中加入 PR-AUC，比較排名是否一致 |

### E13. Calibration Curves + DCA

| 項目 | 內容 |
|------|------|
| **假說** | 校準曲線和 DCA 能評估臨床效用 |
| **優先度** | 中 |
| **參考** | JMIR 2025 論文做法 |

### E14. 不平衡處理方法消融

| 項目 | 內容 |
|------|------|
| **假說** | 不同不平衡處理方法效果有顯著差異 |
| **優先度** | 中 |
| **設計** | Baseline / class_weight / SMOTE / ADASYN / UnderSampling |

### E15. 特徵選擇消融實驗

| 項目 | 內容 |
|------|------|
| **假說** | 前 N 個重要特徵可能已足夠達到相近效能 |
| **狀態** | 🔄 進行中 |
| **Notebook** | [22_Feature_Selection_Ablation.ipynb](../../notebooks/experiments/22_Feature_Selection_Ablation.ipynb) |
| **設計** | Top 5/10/15/20/全部(26) 特徵的 AUC 比較，使用 SHAP 排序 |
| **模型** | LR + XGBoost, 5-Fold CV |

### E16. 外部驗證（Synthea）

| 項目 | 內容 |
|------|------|
| **假說** | 模型在外部資料集上仍有良好泛化能力 |
| **優先度** | 🔥🔥 中高 |
| **設計** | SUA 訓練 → Synthea 測試，報告 AUC 變化 |

---

## 💡 未來構想（Future Work）

### F01. 時間點選擇策略

| 項目 | 內容 |
|------|------|
| **問題** | 前三次 vs 後三次檢驗，哪個策略更好？ |
| **詳細** | [Future_Experiment_Ideas.md](Future_Experiment_Ideas.md) 實驗構想 1 |

### F02. 時間序列模型（LSTM/GRU）

| 項目 | 內容 |
|------|------|
| **問題** | 時間序列模型能否更好地捕捉健康軌跡？ |
| **挑戰** | 需要可變長度輸入、新模型架構 |

### F03. 健檢頻率優化

| 項目 | 內容 |
|------|------|
| **問題** | 最佳健檢間隔是多久？1年/2年/3年？ |
| **需求** | 需要有精確時間戳記的資料集 |

---

## 📚 文獻補充（待研究）

### L01. 高血壓與糖尿病雙向關聯

| 項目 | 內容 |
|------|------|
| **背景** | SHAP 顯示各疾病由核心指標主導，缺乏跨疾病關聯文獻 |
| **優先度** | 🔥 高 |
| **目的** | 為 MTL 架構提供理論依據 |

### L02. 代謝症候群共病性文獻

| 項目 | 內容 |
|------|------|
| **背景** | 需要文獻支持三高之間的共享風險因子 |
| **目的** | Discussion 章節素材 |

### L03. 跨疾病共享特徵分析

| 項目 | 內容 |
|------|------|
| **背景** | Age, BMI, UA, GFR 在三種疾病中都有貢獻 |
| **目的** | 深入分析 SHAP 結果的臨床意義 |

---

## 假說總表

| ID | 假說 | 狀態 | 結論 |
|----|------|------|------|
| H1 | 健檢次數越多，預測越準 | 📋 待執行 | - |
| H2 | Delta 特徵能提升效能 | ✅ 已驗證 | T2+Delta 最佳 |
| H3 | MTL 優於 STL | 📋 待執行 | - |
| H4 | LR 效能接近黑盒模型 | ✅ 已驗證 | LR 在 2/3 疾病最佳 |
| H5 | class_weight 提升 Sensitivity | ✅ 已驗證 | balanced 有效 |
| H6 | 符號回歸能找到有意義公式 | 🔄 進行中 | PySR 可行但 AUC 較低 |

---

## 相關文件

- [todo.md](../../todo.md) - 總待辦事項
- [hypothesis_list.md](../07_plans/hypothesis_list.md) - 舊版假說列表（可合併）
- [Future_Experiment_Ideas.md](Future_Experiment_Ideas.md) - 詳細未來構想

---

**最後更新**：2026-01-10
