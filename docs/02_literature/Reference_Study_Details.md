# 相關研究實驗細節（從 PDF 提取）

**最後更新**：2026-02-27
**用途**：記錄從各篇 PDF 提取的模型、評估指標等實驗細節，供論文寫作查閱。

---

## 總覽

| 研究 | 模型數 | 評估指標數 | 最佳模型 | AUC |
|------|--------|-----------|---------|-----|
| Ye (2018) | 1 | 4 | XGBoost | 0.917 |
| Alaa (2019) | 9 | 4 | AutoPrognosis | 0.774 |
| Dinh (2019) | 5 | 6 | XGBoost | 0.862 |
| Kanegae (2020) | 3 | 3 | XGBoost | 0.881 |
| Hung (2021) | 4 | 7 | RF | 0.851 |
| Liu (2024) | 3 | 5 | XGBoost | 0.930 |
| Wang (2024) | 3 | 4 | XGBoost | 0.889 |
| Yang (2025) | 5 | 8 | XGBoost | — |
| Majcherek (2025) | 18 | 6 | Extra Trees | 0.99 |

---

## 各研究詳細

### Ye et al. (2018) — 高血壓預測

- **PDF**: `papers/Ye_JMIR_Hypertension_ML_2018.pdf`
- **模型 (1)**: XGBoost
- **評估指標 (4)**: AUC, Sensitivity, Specificity, PPV
- **備註**: 單一模型研究，未做模型間比較。前五名重要特徵均為降壓藥物，可能有資料洩漏。

### Alaa et al. (2019) — 心血管疾病預測

- **PDF**: `papers/Alaa_PLOSONE_CVD_AutoML_2019.pdf`
- **模型 (9)**: Framingham Risk Score, Cox PH (7 var), Cox PH (473 var), SVM, Random Forest, Neural Networks, AdaBoost, Gradient Boosting, AutoPrognosis
- **評估指標 (4)**: AUC, Brier Score, Sensitivity, PPV
- **備註**: AutoPrognosis 為自動化模型搜尋框架，會自動組合最佳 pipeline。

### Dinh et al. (2019) — 糖尿病/心血管疾病預測

- **PDF**: `papers/Dinh_BMC_Diabetes_CVD_2019.pdf`
- **模型 (5)**: Logistic Regression, SVM, Random Forest, XGBoost (GBT), Weighted Ensemble (WEM)
- **評估指標 (6)**: AUC, Precision, Recall, F1, Sensitivity, Specificity
- **備註**: 排除 Neural Networks（因 black-box）。10-fold CV。

### Kanegae et al. (2020) — 高血壓預測

- **PDF**: `papers/Kanegae_Hypertension_2020.pdf`
- **模型 (3)**: Logistic Regression, Ensemble (Bagging: LR + RF + XGBoost), XGBoost
- **評估指標 (3)**: AUC, Precision, Recall
- **備註**: 使用縱向 Δ 特徵（Year(-2) → Year(-1) → Year(0)）。

### Hung et al. (2021) — 隱匿性高血壓預測

- **PDF**: `papers/fcvm-08-778306.pdf`
- **模型 (4)**: Logistic Regression, Random Forest, XGBoost, ANN
- **評估指標 (7)**: AUC, Sensitivity, Specificity, PPV, NPV, Accuracy, F1
- **備註**: RF 僅用 6 個特徵即達最佳效能。

### Liu et al. (2024) — 糖尿病預測

- **PDF**: `papers/diagnostics-15-00072.pdf`
- **模型 (3)**: Logistic Regression, Random Forest, XGBoost
- **評估指標 (5)**: AUC, Accuracy, Precision, Recall, F1
- **備註**: 台中榮總 EHR，追蹤 10 年。

### Wang et al. (2024) — 高血壓預測

- **PDF**: `papers/Wang_PLOSONE_Hypertension_2024_correct.pdf`
- **模型 (3)**: XGBoost, LightGBM, Random Forest
- **評估指標 (4)**: AUC, Precision, Recall, F1
- **備註**: 台灣美兆資料，健檢次數越多預測越準（4 次以上最佳）。5-fold CV。

### Yang et al. (2025) — 前驅糖尿病預測

- **PDF**: `papers/diagnostics-15-02507.pdf`
- **模型 (5)**: Random Forest, Stochastic Gradient Boosting, XGBoost, Elastic Net, Multiple Linear Regression
- **評估指標 (8)**: AUC, Accuracy, Precision, Sensitivity, Specificity, F1, PR-AUC, Brier Score
- **備註**: 雙框架設計（迴歸預測 δ-FPG + 分類預測前驅糖尿病）。使用 SMOTE-Tomek。SHAP 可解釋性。

### Majcherek et al. (2025) — 糖尿病預測

- **PDF**: `papers/Majcherek_PLOSONE_Diabetes_BRFSS_2025.pdf`
- **模型 (18)**: AdaBoost, Extra Trees, C5.0, CatBoost, Decision Tree, Gradient Boosting, Hist-GBM, Isolation Forest, KNN, LightGBM, LDA, Logistic Regression, Naive Bayes, Nearest Centroid, QDA, Random Forest, Ridge, XGBoost
- **評估指標 (6)**: AUC, Accuracy, Precision, Recall, Sensitivity, Specificity
- **備註**: BRFSS 美國大規模調查資料。使用 ROS、SMOTE、ADASYN 處理不平衡。SHAP 可解釋性。
