# 實驗與假說清單

> **建立日期**：2026-01-10
> **狀態**：持續更新

---

## 已完成實驗

### 1. ✅ 5-Fold CV 模型比較
- **狀態**：已完成 (2026-01-07)
- **結果**：LR 和 RF 表現最佳
- **輸出**：[13_5FoldCV_Model_Comparison.ipynb](../../notebooks/experiments/13_5FoldCV_Model_Comparison.ipynb)

### 2. ✅ Delta 特徵消融實驗
- **狀態**：已完成
- **結果**：Δ 特徵顯著提升預測效能
- **輸出**：[Delta消融實驗分析.md](summaries/Delta消融實驗分析.md)

### 3. ✅ Class Weight 消融實驗
- **狀態**：已完成
- **結果**：class_weight='balanced' 有效
- **輸出**：[ClassWeight消融實驗分析.md](summaries/ClassWeight消融實驗分析.md)

---

## 待執行實驗

### 4. 📋 PySR 參數調整實驗（Grid Search 風格）

**假說**：透過系統性參數調整，可以找到讓 PySR 產生穩定且高效能公式的最佳參數組合。

**背景**：
- 目前 PySR 結果不穩定（有時 AUC=0.5，常數解）
- 參考 JMIR 2025 論文的 Grid Search 做法

**參數候選值**：

| 參數 | 說明 | 候選值 |
|------|------|--------|
| niterations | 遺傳演算法迭代次數 | [100, 200, 400] |
| populations | 族群數量 | [10, 15, 20] |
| maxsize | 公式最大複雜度 | [15, 25, 35] |
| timeout | 超時秒數 | [600, 1200, 1800] |

**評估指標**：
- AUC（主要）
- 公式複雜度（越簡單越好）
- 執行時間

**預期結果**：
- 找到一組「最佳參數」讓 PySR AUC > 0.75
- 公式簡潔可解釋
- 執行時間合理（< 30 分鐘/疾病）

---

### 5. 📋 評估指標選擇實驗

**假說**：對於類別不平衡的資料，PR-AUC 比 ROC-AUC 更能反映模型對少數類的預測能力。

**背景**：
- 參考 JMIR 2025 論文同時報告 ROC-AUC 和 PR-AUC
- 我們的類別不平衡嚴重（Hyperglycemia 1:17, Dyslipidemia 1:16）

**待加入的評估指標**：

| 指標 | 說明 | 適用情境 |
|------|------|----------|
| **ROC-AUC** | 目前主要指標 | 通用 |
| **PR-AUC** | Precision-Recall AUC | 類別極度不平衡 |
| **Calibration curves** | 校準曲線 | 評估預測機率準確性 |
| **DCA** | Decision Curve Analysis | 評估臨床效用 |
| **DeLong test** | AUC 統計比較 | 模型間差異顯著性檢定 |

**實驗設計**：
- 在現有 5-fold CV 框架中加入 PR-AUC
- 比較 ROC-AUC 和 PR-AUC 的排名是否一致
- 特別關注 Hyperglycemia 和 Dyslipidemia

---

### 6. 📋 CatBoost 模型加入

**假說**：CatBoost 可能比 XGBoost/LightGBM 表現更好（JMIR 2025 論文顯示 CatBoost 最佳）。

**背景**：
- JMIR 2025：CatBoost (0.819) > LightGBM (0.813) > XGBoost (0.811)
- 我們目前沒有 CatBoost

**實驗設計**：
- 加入 CatBoost 到 5-fold CV 比較
- 使用相同的特徵和資料分割

---

### 7. 📋 MTL vs STL 完整比較

**假說**：多任務學習（MTL）透過共享表示，可以提升整體預測效能。

**實驗設計**：
- STL：三個獨立模型分別預測三高
- MTL：單一模型同時預測三高
- 比較 AUC、訓練時間、泛化能力

---

### 8. 📋 外部驗證報告格式

**假說**：清楚報告 HRS → CLSA 的 AUC 變化，可以展示模型泛化能力。

**參考 JMIR 2025 做法**：
- 主要隊列 AUC: 0.819
- 外部驗證 AUC: 0.807
- 下降幅度: 1.2%

**我們的報告格式**：
- HRS (主要) AUC: X.XXX
- CLSA (外部) AUC: X.XXX
- 下降幅度: X.X%

---

## 評估指標總覽

### 目前使用

| 指標 | 類型 | 說明 |
|------|------|------|
| AUC-ROC | 區分能力 | 主要指標 |
| Sensitivity | 分類 | 召回率 |
| Specificity | 分類 | 特異度 |
| F1-Score | 分類 | 精確率與召回率的調和平均 |
| Balanced Accuracy | 分類 | 平衡準確率 |

### 待加入

| 指標 | 類型 | 說明 | 優先度 |
|------|------|------|--------|
| **PR-AUC** | 區分能力 | 適合不平衡資料 | 高 |
| **Calibration curves** | 校準能力 | 預測機率準確性 | 中 |
| **DCA** | 臨床效用 | 決策曲線分析 | 中 |
| **DeLong test** | 統計 | AUC 差異檢定 | 中 |
| **NPV/PPV** | 分類 | 陰性/陽性預測值 | 低 |

---

## 相關文件

- [Meeting_19_Notes.md](../04_meetings/Meeting_19_Notes.md)
- [Paper_China_Prediabetes_Diabetes_2025.md](../02_literature/summaries/Paper_China_Prediabetes_Diabetes_2025.md)
- [13_5FoldCV_Model_Comparison.ipynb](../../notebooks/experiments/13_5FoldCV_Model_Comparison.ipynb)
