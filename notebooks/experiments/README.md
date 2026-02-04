# Notebook 實驗索引

> 最後更新：2026-02-04

## 使用中的 Notebooks

| Nb# | 檔名 | 實驗 | 對應章節 | 說明 |
|-----|------|------|----------|------|
| 01 | ExploratoryDataAnalysis_Chinese_Dataset | - | §3.2 | EDA：25,744 筆紀錄、6,119 人 |
| 02 | DataPreprocessing | - | §3.2 | 長轉寬、建立 T1/T2/T3 + Delta 特徵 |
| 10 | ClassWeight_Ablation | E03 | §4.5 | class_weight 五種設定比較（None/balanced/1:3/1:5/1:10） |
| 14 | Checkup_Frequency_Experiment | E05 | §4.6 | 健檢次數 1~4 次 vs AUC，固定預測 T5 |
| 16 | PySR_Parameter_Tuning | E11 | §4.7 | PySR 超參數調整（parsimony、maxsize） |
| 17 | SlidingWindow_5FoldCV | E01 | §4.1 | **主實驗**：8 模型 × 3 疾病，StratifiedGroupKFold |
| 19 | SHAP_SlidingWindow | E04 | §4.2 | SHAP 特徵重要性（XGBoost） |
| 20 | MTL_vs_STL | E06 | - | MTL vs STL 比較（結論：無顯著差異） |
| 21 | Delta_Ablation | E02 | - | Delta 消融（早期版本，已由 Nb27 取代） |
| 22 | Feature_Selection_Ablation | E08 | §4.4 | Top-N 特徵選擇消融 |
| 23 | PySR_SlidingWindow | E13 | §4.7 | PySR 滑動窗口（5-Fold，161 分鐘） |
| 24 | SMOTE_Comparison | E15 | §4.5 | SMOTE vs class_weight（結論：無差異 <2%） |
| 25 | PySR_Depth_Experiment | E14 | §4.7 | PySR 樹深度實驗（結論：簡單公式最佳） |
| 27 | Delta_Ablation_Comprehensive | E02 | §4.3 | **Delta 消融完整版**：兩組框架（Full vs No-Δ、Y-1+Δ vs Y-1 Only） |

## 已封存的 Notebooks（archive/）

| Nb# | 檔名 | 封存原因 | 取代者 |
|-----|------|----------|--------|
| 03 | ModelBuilding | 舊資料格式（wide_format） | Nb17 |
| 04 | XGBoost | 舊資料格式 | Nb17 |
| 05 | NeuralNetworks | 舊資料格式 | Nb17 |
| 06 | SVM | 舊資料格式 | Nb17 |
| 07 | GeneticProgramming | gplearn 實驗失敗 | 放棄 |
| 08 | SHAP_Analysis | 舊資料格式 | Nb19 |
| 09 | Delta_Ablation | 舊資料格式 | Nb21 → Nb27 |
| 11 | GP_Parameter_Tuning | gplearn 不支援 class_weight | 改用 PySR（Nb16） |
| 12 | PySR_Experiment | 初期 PySR 實驗 | Nb16、Nb23 |
| 13 | 5FoldCV_Model_Comparison | 舊 CV（6,056 筆） | Nb17（GroupKFold） |
| 14 | DecisionTree | 獨立 DT 實驗 | 整合入 Nb17 |
| 15 | PySR_Depth_Experiment | 早期深度實驗 | Nb25 |
| 18 | PySR_Complex_Formulas | HTN 退化為常數 | Nb23 |

## 資料格式演進

```
Phase 1 (Nb01-02)：原始資料 → Wide format (T1, T2, T3)
Phase 2 (Nb03-15)：Wide format 實驗 → 已封存
Phase 3 (Nb17+)  ：滑動窗口（13,514 筆）+ StratifiedGroupKFold
```

## 缺少的 Notebooks

- Nb26：不存在（跳號）
- NB/LDA 實驗：尚未建立（需新增，對應 Ch3 §3.4.1 與 Ch4 §4.1）
