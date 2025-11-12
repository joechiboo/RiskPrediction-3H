# Meeting 17 準備計畫

**預計時間**：2-3週後（約 2025-11-25 ~ 2025-12-02）
**主題**：Dual Framework 2025 論文分析 + 模型實驗初步成果
**準備日期**：2025-11-11

---

## 📋 Meeting 17 目標

### 1. 文獻報告：Dual Framework 2025 深度解析（10頁簡報）
### 2. 論文進度報告：Anaconda 模型實驗初步成果（8頁簡報）

**總共**：18頁簡報

---

## 📚 Part 1: Dual Framework 2025 論文分析（10頁）

### 論文基本資訊

**標題**：Dual Machine Learning Framework for Predicting Long-Term Glycemic Change and Prediabetes Risk in Young Taiwanese Men

**期刊**：Diagnostics, 15(19), 2507 (2025)

**DOI**：https://doi.org/10.3390/diagnostics15192507

**PDF位置**：[docs/references/diagnostics-15-02507.pdf](../references/diagnostics-15-02507.pdf) (3.5 MB)

**下載日期**：2025-11-11

---

### 選擇理由 ⭐⭐⭐⭐⭐

#### 與本研究高度相關的5大原因：

1. **血液檢驗項目最完整** ✅✅
   - 血脂 3 項（HDL, LDL, TG）
   - 肝功能 4 項（GPT, GOT, γ-GT, ALP）
   - 腎功能（肌酐）
   - 尿酸 ⭐
   - 血球相關（白血球、血小板、血紅素）
   - 甲狀腺功能

2. **縱向變化量特徵（δ-FPG）** ✅✅
   - 與我們的 Δ 特徵概念完全相同
   - T₁ → T₂ 的血糖變化量

3. **台灣本土資料** ✅
   - 6,247位台灣年輕男性（18-35歲）
   - 平均追蹤 5.9 年
   - 台灣 MJ 健康篩檢中心

4. **SHAP 可解釋性分析** ✅
   - 特徵重要性視覺化
   - 可學習如何應用 SHAP

5. **雙框架設計** ✅
   - 連續值預測（δ-FPG）
   - 二元分類（前驅糖尿病風險）

---

### 簡報架構（10頁）

#### Slide 1: 封面
- 論文標題與基本資訊
- 為何選擇這篇論文

#### Slide 2: 研究動機與問題
- 前驅糖尿病的重要性
- 現有研究的不足
- 本研究的創新點

#### Slide 3: 研究設計
- 資料來源：台灣 MJ 健康篩檢中心
- 樣本數：6,247位年輕男性
- 追蹤時間：5.9年
- 預測目標：δ-FPG + 前驅糖尿病風險

#### Slide 4: 輸入特徵（Input Features）
- **重點**：完整血液檢驗項目列表
- 與我們研究的 11 項指標比較
- 特徵類別分組

#### Slide 5: 雙機器學習框架
- Framework 1：預測 δ-FPG（連續值）
- Framework 2：分類前驅糖尿病風險（二元）
- 模型：RF, SGB, XGBoost, Elastic Net

#### Slide 6: δ-FPG 特徵工程 ⭐
- **重點**：如何計算血糖變化量
- 與我們的 Δ 特徵設計對比
- 時間間隔處理方法

#### Slide 7: 模型性能結果
- 各模型的 SMAPE, RMSE, RAE, RRSE
- AUC 結果（分類任務）
- 最佳模型：XGBoost / RF

#### Slide 8: SHAP 特徵重要性分析
- **重點**：SHAP 圖解讀
- 最重要的特徵排名
- 年齡、HDL-C、追蹤時間等的影響

#### Slide 9: 對本研究的啟發
- **特徵工程**：如何計算 Δ 特徵
- **模型選擇**：RF, XGBoost 的優勢
- **可解釋性**：SHAP 應用方法
- **雙框架**：連續值預測 + 分類的組合

#### Slide 10: 與本研究的異同
- **相同點**：
  - 血液檢驗數據
  - 縱向變化量特徵
  - 台灣資料
  - 可解釋性重視
- **相異點**：
  - 單一疾病 vs 多疾病（三高）
  - 年輕男性 vs 一般成人
- **下一步**：開始模型實驗

---

## 💻 Part 2: 論文進度報告 - Anaconda 模型實驗（8頁）

### 簡報架構（8頁）

#### Slide 1: 研究進度概覽
- 目前進度：實驗環境建置 + 初步模型訓練
- 本次報告重點：資料集處理 + 基礎模型結果

#### Slide 2: 實驗環境建置
- **開發環境**：Anaconda
- **主要套件**：
  - scikit-learn（LR, RF, DT, SVM）
  - XGBoost
  - pandas, numpy
  - matplotlib, seaborn（視覺化）
- **版本資訊**

#### Slide 3: 資料集選擇與狀態
- **中國東南部資料集**（2010-2018）
  - 樣本數：25,744 筆
  - 11 項血液檢驗指標（含尿酸）
  - 資料完整度：高
  - 狀態：✅ 已處理完成

- **加拿大 HRS 資料集**
  - 樣本數：待確認
  - 特徵：⚠️ 缺失值較多、無尿酸
  - 狀態：⚠️ 資料清理中

#### Slide 4: 資料前處理
- **缺失值處理**：方法與比例
- **類別不平衡處理**：SMOTE / Under-sampling
- **特徵標準化**：Z-score normalization
- **資料分割**：Train (70%) / Validation (15%) / Test (15%)

#### Slide 5: 特徵工程
- **基本特徵**（T₂ 時刻的 11 項血液檢驗）
- **變化量特徵（Δ）**：T₂ - T₁
- **時間特徵**：追蹤間隔
- 總特徵數：？項

#### Slide 6: 初步模型訓練結果（中國資料集）
- **模型**：
  1. Logistic Regression (LR)
  2. Decision Tree (DT)
  3. Random Forest (RF)
  4. XGBoost
  5. Support Vector Machine (SVM)

- **評估指標**：
  - Accuracy
  - Precision, Recall, F1-Score
  - AUC-ROC

- **結果表格**：各模型性能比較

#### Slide 7: 模型性能分析
- **最佳模型**：？
- **Confusion Matrix**
- **ROC Curve**
- **特徵重要性排名**（RF / XGBoost）

#### Slide 8: 遇到的挑戰與下一步
- **當前挑戰**：
  - 資料不平衡問題
  - 特徵選擇策略
  - 模型調優
  - GP (Genetic Programming) 實現

- **下一步計畫**：
  1. 完成 HRS 資料集處理與比較
  2. 實作 Genetic Programming
  3. 超參數調優
  4. SHAP 可解釋性分析
  5. 多資料集交叉驗證

---

## ✅ 準備任務清單（優先順序）

### 第一週（Week 1：2025-11-11 ~ 2025-11-17）

#### 📚 文獻分析任務

- [ ] **深度閱讀 Dual Framework 2025 論文**
  - [ ] 完整閱讀論文
  - [ ] 整理研究設計、方法、結果
  - [ ] 標註重點：δ-FPG 計算方法、SHAP 應用

- [ ] **製作 Dual Framework 2025 深度解析文檔**
  - [ ] 參考 Liu 2024 的深度解析格式
  - [ ] 建立：`docs/literature_notes/Dual_2025_深度解析.md`
  - [ ] 重點：δ 特徵工程方法、SHAP 圖解讀

- [ ] **準備 Dual 2025 簡報（10頁）**
  - [ ] 按照上述架構製作
  - [ ] 重點突出與本研究的關聯性

#### 💻 實驗任務

- [ ] **Anaconda 環境建置與測試**
  - [ ] 安裝所需套件
  - [ ] 測試基本功能

- [ ] **中國東南部資料集處理**
  - [ ] 資料載入與探索
  - [ ] 缺失值處理
  - [ ] 特徵工程（Δ 特徵）
  - [ ] 資料分割

### 第二週（Week 2：2025-11-18 ~ 2025-11-24）

#### 💻 模型訓練任務

- [ ] **基礎模型訓練（中國資料集）**
  - [ ] Logistic Regression
  - [ ] Decision Tree
  - [ ] Random Forest
  - [ ] XGBoost
  - [ ] SVM

- [ ] **模型評估與分析**
  - [ ] 計算所有評估指標
  - [ ] 繪製 ROC Curve
  - [ ] Confusion Matrix
  - [ ] 特徵重要性分析

- [ ] **HRS 資料集處理（如果時間允許）**
  - [ ] 資料清理
  - [ ] 特徵對齊

#### 📊 簡報製作

- [ ] **製作論文進度簡報（8頁）**
  - [ ] 整理實驗結果
  - [ ] 製作圖表
  - [ ] 分析遇到的挑戰

### 第三週（Week 3：2025-11-25 ~ Meeting 17）

- [ ] **簡報整合與練習**
  - [ ] 合併兩部分簡報（18頁）
  - [ ] 調整順序與邏輯
  - [ ] 練習報告流程

- [ ] **最後檢查**
  - [ ] 確認所有數據正確
  - [ ] 準備可能的問題回答
  - [ ] 備份所有資料與程式碼

---

## 📂 需要建立的文檔

### 文獻分析文檔
1. `docs/literature_notes/Dual_2025_深度解析.md`
2. `docs/literature_notes/Dual_2025_演講稿_10頁.md`

### 實驗記錄文檔
1. `docs/experiments/experiment_log.md` - 實驗日誌
2. `docs/experiments/dataset_preprocessing.md` - 資料前處理記錄
3. `docs/experiments/model_training_results.md` - 模型訓練結果

### 程式碼文檔
1. `src/preprocessing/` - 資料前處理腳本
2. `src/models/` - 模型訓練腳本
3. `src/evaluation/` - 評估指標計算
4. `notebooks/` - Jupyter notebooks（探索性分析）

---

## 🎯 Meeting 17 預期成果

### Part 1: 文獻分析
- ✅ 完整理解 Dual Framework 2025 的方法
- ✅ 掌握 δ 特徵工程方法
- ✅ 了解 SHAP 應用技巧
- ✅ 10頁高品質簡報

### Part 2: 實驗成果
- ✅ Anaconda 環境建置完成
- ✅ 中國資料集完整處理
- ✅ 至少 5 個基礎模型的訓練結果
- ✅ 初步性能比較與分析
- ✅ 8頁實驗進度簡報

### 總體目標
- ✅ 18頁完整簡報
- ✅ 證明可以開始實際模型開發
- ✅ 為後續 GP 實作打基礎

---

## 📌 重要提醒

### 時間管理
- **文獻分析**：1週
- **模型實驗**：1週
- **簡報製作**：3-4天
- **緩衝時間**：2-3天

### 優先順序
1. **最高優先級**：Dual 2025 論文深度閱讀與簡報
2. **高優先級**：基礎模型訓練（LR, RF, XGBoost）
3. **中優先級**：特徵重要性分析
4. **低優先級**：HRS 資料集（如果時間不夠可以延後）

### 風險管理
- 如果模型訓練遇到問題，至少要有資料探索分析（EDA）的結果
- 如果時間不夠，可以先專注在中國資料集，HRS 留到下次
- GP 實作可以留到 Meeting 18

---

**文檔建立日期**：2025-11-11
**下次更新**：Meeting 17 後
**負責人**：紀伯喬

---

## 📌 快速導航

- 📂 [返回 Meeting Notes 目錄](.)
- 📖 [查看 Dual 2025 論文](../references/diagnostics-15-02507.pdf)
- 📊 [查看 Meeting 1-16 總結](Meeting_Summary_1-16.md)
- 📚 [查看 Q2 文獻回顧](../research_plans/Q2_Taiwan_Literature_Review.md)
