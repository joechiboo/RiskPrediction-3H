# 實驗記錄：資料前處理完成

**日期**：2025-11-13
**任務**：資料重組與特徵工程（Long Format → Wide Format）
**狀態**：✅ 成功完成

---

## 📋 今日完成項目

### 1. ✅ 完成 EDA Notebook（11/11延續）
- 檔案：`01_ExploratoryDataAnalysis_Chinese_Dataset.ipynb`
- 解決中文字型顯示問題（設定為 DFKai-SB）
- 解決 VS Code 輸出截斷問題
- 完整探索 25,744 筆資料的特性

### 2. ✅ 資料前處理 Notebook 開發與執行
- 檔案：`02_DataPreprocessing.ipynb`
- 完整的資料重組流程
- 計算 Δ 變化量特徵
- 生成建模用的資料集

### 3. ✅ 時間點選擇策略討論
- 決定採用「前3次檢查」（T1, T2, T3）方案
- 符合早期預測目標
- 記錄未來實驗想法（後3次 vs 分層比較）

---

## 🔍 資料前處理關鍵成果

### 輸入資料
- **原始資料**：25,744 筆記錄，15 個欄位
- **參與人數**：6,119 人
- **平均檢查次數**：4.2 次

### 資料篩選
- **篩選條件**：保留 ≥3 次檢查的參與者
- **篩選結果**：6,056 人（保留率 98.97%）
- **被排除**：63 人（僅 1-2 次檢查）

### 檢查次數分佈（篩選後）
```
3 次檢查: 1,754 人 (28.96%)
4 次檢查: 1,776 人 (29.33%)
5 次檢查: 1,935 人 (31.95%)
6 次檢查: 556 人 (9.18%)
7 次檢查: 31 人 (0.51%)
8 次檢查: 4 人 (0.07%)
```

### Wide Format 資料集
- **參與人數**：6,056 人
- **總欄位數**：107 個
- **檔案大小**：2,483.74 KB
- **處理時間**：約 5.4 秒

### 欄位結構
```
- ID + 人口統計: 3 個 (ID, sex, Age)
- T1 特徵: 8 個 (5 血液 + 3 身體測量)
- T2 特徵: 8 個
- T3 特徵: 8 個
- T4-T8 特徵: 最多到 T8（部分參與者）
- Δ1 特徵 (T2-T1): 8 個
- Δ2 特徵 (T3-T2): 8 個
- 目標變數: 3 x 多個時間點
```

### Δ 特徵清單
**Δ1 (T2 - T1)**：
- Delta1_FBG（血糖變化）
- Delta1_TC（總膽固醇變化）
- Delta1_Cr（肌酐酸變化）
- Delta1_UA（尿酸變化）
- Delta1_GFR（腎絲球過濾率變化）
- Delta1_BMI（BMI 變化）
- Delta1_SBP（收縮壓變化）
- Delta1_DBP（舒張壓變化）

**Δ2 (T3 - T2)**：同上 8 項

---

## 💡 關鍵決策與討論

### 時間點選擇策略

#### 最終決定：採用「前3次」（T1, T2, T3）⭐
**理由**：
1. ✅ 符合研究目標：預測「健康→生病」的過程
2. ✅ 臨床意義：早期預測、預防醫學
3. ✅ 資料一致性：所有人從相同起點（首次檢查）開始
4. ✅ 避免資料洩漏：每人只產生 1 筆記錄

#### 討論的替代方案
1. **方案 B**：取「後3次」（T2-T4 或 T3-T5）
   - 適用：疾病進展研究
   - 缺點：可能已經生病，失去「預測」意義

2. **方案 C**：滑動窗口（每人產生多筆）
   - 嚴重資料洩漏風險
   - 不採用

3. **未來實驗**：分層比較
   - 比較「只有3次」vs「有4次以上」的人
   - Subgroup analysis
   - 優先級：低（記錄在 memo）

---

## 📊 視覺化產出

### 生成的圖表
1. **delta1_features_distribution.png**
   - Δ1 (T2-T1) 的 8 個特徵分佈
   - 紅色虛線標示「無變化」基準

2. **delta2_features_distribution.png**
   - Δ2 (T3-T2) 的 8 個特徵分佈
   - 用於測試集驗證

---

## 🎯 建模策略

### 訓練/測試分割
```
訓練階段：T1 + Δ1 → 預測 T2 的疾病狀態
測試階段：T2 + Δ2 → 預測 T3 的疾病狀態
```

### 特徵組合方案
1. **基礎模型**：只用 T1 特徵（8項）
2. **加入變化量**：T1 + Δ1（16項）
3. **完整時序**：T1 + T2 + Δ1（24項）

### 目標變數
- hypertension（高血壓）
- hyperglycemia（高血糖）
- dyslipidemia（高血脂）

每個疾病都要建立獨立的二元分類模型

---

## 📂 檔案結構

### 新增的檔案
```
data/processed/
└── SUA_CVDs_wide_format.csv (2.48 MB)

notebooks/experiments/
├── 01_ExploratoryDataAnalysis_Chinese_Dataset.ipynb ✅
└── 02_DataPreprocessing.ipynb ✅

docs/experiments/
├── 2025-11-11_EDA_Session_Memo.md ✅
├── delta1_features_distribution.png ✅
├── delta2_features_distribution.png ✅
├── blood_test_distributions.png ✅
└── correlation_matrix.png ✅
```

---

## 🛠️ 技術細節

### 資料重組方法
```python
# 將 long format 轉 wide format
for participant_id in df_sorted['ID'].unique():
    participant_data = df_sorted[df_sorted['ID'] == participant_id]
    participant_data = participant_data.head(3)  # 只取前3次

    # 為每個時間點建立欄位
    # T1: FBG_T1, TC_T1, ...
    # T2: FBG_T2, TC_T2, ...
    # T3: FBG_T3, TC_T3, ...
```

### Δ 特徵計算
```python
# Δ1 = T2 - T1
df_wide['Delta1_FBG'] = df_wide['FBG_T2'] - df_wide['FBG_T1']

# Δ2 = T3 - T2
df_wide['Delta2_FBG'] = df_wide['FBG_T3'] - df_wide['FBG_T2']
```

---

## 📈 與 Meeting 17 準備進度

### 已完成 ✅
- [x] EDA 完整分析
- [x] 資料前處理與重組
- [x] 特徵工程（Δ 特徵）
- [x] 建模用資料集產出

### 進行中 🔄
- [ ] 建立 Baseline 模型
- [ ] 閱讀 Dual Framework 2025 論文

### 距離 Meeting 17
- **預計日期**：2025-11-24
- **剩餘時間**：約 11 天
- **當前進度**：資料準備完成，準備開始建模

---

## 💭 研究者筆記

### 重要洞察

1. **資料品質優異**
   - 保留率接近 99%
   - 只排除 63 人（檢查次數不足）
   - Wide format 轉換順利

2. **時間點選擇的重要性**
   - 「前3次」vs「後3次」影響研究目標定位
   - 決定採用「前3次」符合早期預測目標
   - 記錄未來可做的對比實驗

3. **Δ 特徵的價值**
   - 捕捉縱向變化趨勢
   - 與 Dual Framework 2025 的 δ-FPG 概念相同
   - 同時計算 Δ1 和 Δ2 以支援訓練/測試分割

4. **資料結構清晰**
   - Wide format 適合傳統 ML 模型
   - 每人一筆記錄，避免資料洩漏
   - 欄位命名規則統一（feature_T1, feature_T2...）

### 潛在挑戰

1. **類別不平衡**
   - 需要在建模時確認各疾病的比例
   - 可能需要 SMOTE 或類別權重調整

2. **缺失值處理**
   - T4-T8 有大量 NaN（正常，因為不是所有人都有）
   - 建模時只使用 T1, T2, T3

3. **多任務學習（MTL）**
   - 三個疾病可以獨立建模
   - 也可以嘗試 MTL 同時預測
   - 需要比較兩種方法的效果

---

## 🔗 相關文檔

### 資料集文檔
- [SUA_Dataset_Documentation.md](../datasets/SUA_Dataset_Documentation.md)

### 實驗 Notebooks
- [01_ExploratoryDataAnalysis_Chinese_Dataset.ipynb](../../notebooks/experiments/01_ExploratoryDataAnalysis_Chinese_Dataset.ipynb)
- [02_DataPreprocessing.ipynb](../../notebooks/experiments/02_DataPreprocessing.ipynb)

### 會議文檔
- [Meeting_17_Preparation_Plan.md](../meeting_notes/Meeting_17_Preparation_Plan.md)
- [Meeting_Summary_1-16.md](../meeting_notes/Meeting_Summary_1-16.md)

### 實驗記錄
- [2025-11-11_EDA_Session_Memo.md](2025-11-11_EDA_Session_Memo.md)

---

## ⏰ 時間記錄

- **日期**：2025-11-13（接續 11/11 的工作）
- **完成項目**：
  - 資料前處理 Notebook 開發
  - Long → Wide format 轉換
  - Δ 特徵計算
  - 視覺化產出
- **耗時**：資料處理執行約 5.4 秒，開發與討論約 2-3 小時
- **下次計畫**：建立 Baseline 模型（Logistic Regression）

---

## ✅ 今日成就

1. ✅ 完成資料前處理完整流程
2. ✅ 成功將 long format 轉為 wide format
3. ✅ 計算 Δ1 和 Δ2 特徵
4. ✅ 產出建模用資料集（6,056人 x 107欄位）
5. ✅ 確立建模策略（訓練/測試分割）
6. ✅ 討論並決定時間點選擇策略
7. ✅ 視覺化 Δ 特徵分佈
8. ✅ 記錄未來實驗想法

---

## 📌 快速回顧

**Q: 資料前處理後有多少人？**
**A**: 6,056 人（保留率 98.97%）

**Q: Wide format 有多少欄位？**
**A**: 107 個欄位（包含基礎特徵、時間點特徵、Δ 特徵）

**Q: 為什麼選擇「前3次」而不是「後3次」？**
**A**: 符合早期預測目標，觀察「健康→生病」的過程

**Q: Δ 特徵有幾個？**
**A**: 16 個（Δ1 有 8 個，Δ2 有 8 個）

**Q: 建模策略是什麼？**
**A**: 訓練用 T1+Δ1 預測 T2，測試用 T2+Δ2 預測 T3

**Q: 下一步要做什麼？**
**A**: 建立 Baseline 模型（Logistic Regression）

---

**記錄者**：紀伯喬
**狀態**：資料準備完成
**下次目標**：建立第一個預測模型

---

## 🎯 Meeting 17 準備狀態

### 可報告的成果（截至 11/13）

#### Part 2: 實驗進度（已完成部分）
- ✅ 環境建置（Anaconda + VS Code Jupyter）
- ✅ 資料集完整 EDA
- ✅ 資料前處理與重組
- ✅ 特徵工程（Δ 特徵）
- ✅ 建模用資料集產出

#### 待完成（剩餘 11 天）
- [ ] Baseline 模型訓練（LR, RF, XGBoost）
- [ ] 模型評估與比較
- [ ] 閱讀 Dual Framework 2025 論文
- [ ] 製作 18 頁簡報

**進度評估**：約完成 30%，進度良好 ✅
