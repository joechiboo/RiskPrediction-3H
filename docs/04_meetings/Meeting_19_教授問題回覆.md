# Meeting 19 - 教授問題回覆總整理

**日期**：2026-01-13
**目的**：回覆 Meeting 18 教授提出的所有問題與任務

---

## 任務完成總覽

| # | 任務 | 狀態 | 對應文件/Notebook |
|---|------|------|-------------------|
| 1 | MJ Health 資料申請 | ⏳ 待處理 | - |
| 2 | Problem Definition | ✅ 完成 | [Problem_Definition.md](../07_plans/Problem_Definition.md) |
| 3 | 選讀論文 | ⏳ 待確認 | 第二章文獻探討 |
| 4 | 實驗/假說列表 | ✅ 完成 | [hypothesis_list.md](../07_plans/hypothesis_list.md) |
| 5 | Decision Tree 模型 | ✅ 完成 | Notebook 17 |
| 6 | MTL vs STL 比較 | ✅ 完成 | Notebook 20 |
| 7 | PySR 深度實驗 | ⏳ 低優先 | 待重做 |
| 8 | 健檢次數實驗 | ✅ 完成 | Notebook 14 |
| 9 | 5-Fold CV | ✅ 完成 | Notebook 17 |

---

## 1. MJ Health 資料申請

**狀態**：⏳ 待處理

**行動項目**：
- 聯繫 MJ Health 研究基金會
- 詢問學術單位資料申請流程
- 參考聯絡人：朱大維（Taiwan MJ 論文作者）

---

## 2. Problem Definition（已完成）

**文件位置**：[Problem_Definition.md](../07_plans/Problem_Definition.md)

### 數學定義

**輸入（Input）**：
$$X = [X_{base}, X_{T_1}, X_{T_2}, \Delta X]$$

其中：
- $X_{base}$：基本資訊（性別、年齡）
- $X_{T_1}$：第一次健檢指標
- $X_{T_2}$：第二次健檢指標
- $\Delta X = X_{T_2} - X_{T_1}$：變化量

**模型（Model）**：
$$f: \mathbb{R}^{26} \rightarrow [0,1]^3$$

**輸出（Output）**：
$$\hat{Y} = [\hat{y}_{HTN}, \hat{y}_{HG}, \hat{y}_{DL}]$$

三高風險機率，經閾值轉換為二元分類。

---

## 3. 選讀論文

**狀態**：⏳ 待確認

**已讀論文**：
- Taiwan MJ 2024 (PLoS ONE) - 高血壓預測
- Dual 2025 - 深度學習糖尿病預測
- Liu 2024 TCVGH - 糖尿病預測
- SMOTE SHAP 2025 - 類別不平衡處理

**建議**：確認第二章文獻探討是否需要補充更多論文。

---

## 4. 實驗/假說列表（已完成）

**文件位置**：
- [hypothesis_list.md](../07_plans/hypothesis_list.md)
- [Experiment_Overview.md](../03_experiments/Experiment_Overview.md)

### 假說驗證總結

| 假說 | 內容 | 結果 |
|------|------|------|
| **H1** | 健檢次數越多越準 | ✅ 確認（但 1 次已很準） |
| **H2** | Delta 特徵有價值 | ✅ 確認（+2~7% AUC） |
| **H3** | MTL 優於 STL | ❌ 否定（無顯著差異） |
| **H4** | LR 效能接近黑盒 | ✅ 確認（2/3 疾病最佳） |
| **H5** | balanced 提升 Sensitivity | ✅ 確認（+35%） |
| **H6** | PySR 找到有意義公式 | ⏳ 待完成 |

---

## 5. Decision Tree 模型（已完成）

**Notebook**：17_SlidingWindow_5FoldCV.ipynb

### DT 實驗結果

| 疾病 | DT AUC | 最佳模型 | 最佳 AUC | 差距 |
|------|--------|----------|----------|------|
| 高血壓 | 0.658 | RF | 0.743 | -0.085 |
| 高血糖 | 0.835 | LR | 0.938 | -0.103 |
| 高血脂 | 0.744 | LR | 0.867 | -0.123 |

**結論**：DT 是所有模型中表現最差的，符合預期。RF 作為多棵 DT 的集成，效能顯著提升（+8~10%）。

---

## 6. MTL vs STL 比較（已完成）

**Notebook**：20_MTL_vs_STL.ipynb
**完整分析**：[MTL_vs_STL_完整分析.md](../03_experiments/summaries/MTL_vs_STL_完整分析.md)

### 實驗結果

| 方法 | HTN | HG | DL | 平均 | 訓練時間 |
|------|-----|----|----|------|----------|
| MTL | 0.734 | 0.932 | 0.868 | 0.845 | 9.0s |
| STL | 0.742 | 0.933 | 0.869 | 0.848 | 10.9s |
| **差異** | -0.008 | -0.001 | -0.001 | -0.003 | 1.21x 快 |

**結論**：MTL 與 STL 效能幾乎相同（差異 < 1%）。

**原因分析**：三高之間相關性弱（Phi 係數 < 0.1），MTL 難以從共享學習中獲益。

**論文價值**：這是「有價值的負面結果」，說明 MTL 不一定優於 STL。

---

## 7. PySR 深度實驗

**狀態**：⏳ 低優先

**需要做的事**：
- 使用滑動窗口資料重跑 PySR
- 測試不同深度設定（depth = 3, 5, 7, 10）
- 比較公式可解釋性 vs 效能

**初步發現**（舊資料）：
- 高血壓：SBP 是主要因子
- 高血糖：FBG 是主要因子
- 高血脂：TC 是主要因子

---

## 8. 健檢次數實驗（已完成）

**Notebook**：14_Checkup_Frequency_Experiment.ipynb

### 實驗結果

| 健檢次數 | HTN | HG | DL | 平均 AUC |
|----------|-----|----|----|----------|
| 1 次 | 0.666 | 0.931 | 0.867 | 0.821 |
| 2 次 | 0.679 | 0.940 | 0.879 | 0.832 |
| 3 次 | 0.676 | 0.942 | 0.883 | 0.834 |
| 4 次 | **0.835** | **0.945** | 0.882 | **0.887** |

**結論**：
- ✅ 假說成立：健檢次數越多，預測越準
- 🔍 **意外發現**：只看 1 次健檢已有很高 AUC（HG=0.931, DL=0.867）
- 高血壓受益最大：4 次 vs 1 次提升 **+0.170**

---

## 9. 5-Fold CV（已完成）

**Notebook**：17_SlidingWindow_5FoldCV.ipynb

### CV 策略

- **方法**：StratifiedGroupKFold
- **分組**：patient_id
- **防止資料洩漏**：同一病患永遠不會同時出現在訓練集和測試集

### 最終結果

| 疾病 | 最佳模型 | AUC | 95% CI |
|------|----------|-----|--------|
| 高血壓 | RF | 0.743 | (0.725, 0.762) |
| 高血糖 | LR | 0.938 | (0.924, 0.951) |
| 高血脂 | LR | 0.867 | (0.850, 0.884) |

---

## 額外完成項目

### 外部驗證評估

**結論**：Synthea 外部驗證 **不可行**

**原因**：
- FBG、TC 缺失率高達 70%
- 完整記錄僅 2,862 筆（19.8%）
- 高血糖佔 99.1%（嚴重選擇偏差）

**論文處理**：在「研究限制」章節說明。

### 新增文檔

| 文檔 | 說明 |
|------|------|
| [Experiment_Overview.md](../03_experiments/Experiment_Overview.md) | 實驗總覽 |
| [MTL_vs_STL_完整分析.md](../03_experiments/summaries/MTL_vs_STL_完整分析.md) | MTL 完整分析 |
| [Delta_Ablation_完整分析.md](../03_experiments/summaries/Delta_Ablation_完整分析.md) | Delta 消融分析 |
| [external_data_sources.md](../01_data/external_data_sources.md) | 外部資料來源 |

---

## 待處理事項

| 優先級 | 項目 | 負責人 |
|--------|------|--------|
| 高 | MJ Health 資料申請 | 學生 |
| 中 | 確認第二章文獻是否足夠 | 學生 |
| 低 | PySR 滑動窗口資料重做 | 可選 |

---

## 相關文件索引

### 核心文件
- [Problem_Definition.md](../07_plans/Problem_Definition.md)
- [hypothesis_list.md](../07_plans/hypothesis_list.md)
- [Experiment_Overview.md](../03_experiments/Experiment_Overview.md)

### 實驗分析
- [MTL_vs_STL_完整分析.md](../03_experiments/summaries/MTL_vs_STL_完整分析.md)
- [Delta_Ablation_完整分析.md](../03_experiments/summaries/Delta_Ablation_完整分析.md)
- [Comorbidity_Analysis.md](../03_experiments/summaries/Comorbidity_Analysis.md)

### Notebooks
- `14_Checkup_Frequency_Experiment.ipynb` - 健檢次數
- `17_SlidingWindow_5FoldCV.ipynb` - 基準模型比較
- `19_SHAP_SlidingWindow.ipynb` - SHAP 分析
- `20_MTL_vs_STL.ipynb` - MTL 比較
- `21_Delta_Ablation.ipynb` - Delta 消融
