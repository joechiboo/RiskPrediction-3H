# 論文筆記：5-Year Prediabetes→Diabetes Prediction (2025)

> **建立日期**：2026-01-09
> **論文編號**：候選清單 #2
> **狀態**：已完整閱讀
> **評估**：⭐⭐⭐⭐⭐ 與本研究高度相關

---

## 一句話摘要

**用機器學習預測「前驅糖尿病患者在 5 年內是否會進展為糖尿病」，CatBoost 表現最佳 (AUC=0.819)。**

---

## 研究問題

| 問題 | 回答 |
|------|------|
| **研究什麼？** | 前驅糖尿病 → 糖尿病的 5 年進展風險預測 |
| **對象是誰？** | 中國成年人（已確診前驅糖尿病，HbA1c 5.7%-6.4%）|
| **預測什麼？** | 5 年內是否會進展為糖尿病（HbA1c ≥6.5%）|
| **用什麼方法？** | 7 種機器學習模型 + SHAP 可解釋性分析 |
| **最佳模型？** | CatBoost（AUC 0.819 內部 / 0.807 外部驗證）|
| **關鍵發現？** | FBG、HDL、ALT/AST、BMI、Age、MONO 是最重要的預測因子 |

---

## 基本資訊

| 欄位 | 內容 |
|------|------|
| **標題** | Development of a 5-Year Risk Prediction Model for Transition From Prediabetes to Diabetes Using Machine Learning: Retrospective Cohort Study |
| **期刊** | Journal of Medical Internet Research (JMIR) |
| **年份** | 2025 (May 9) |
| **DOI** | [10.2196/73190](https://doi.org/10.2196/73190) |
| **PMID** | 40344663 |
| **PDF位置** | [JMIR_Prediabetes_Diabetes_2025.pdf](../references/JMIR_Prediabetes_Diabetes_2025.pdf) |

---

## 作者與機構

- Yongsheng Zhang, Hongyu Zhang, Dawei Wang, Na Li, Haoyue Lv, **Guang Zhang** (通訊)
- 機構：
  - 山東第一醫科大學附屬醫院（主要隊列）
  - 濱州醫學院附屬醫院（外部驗證）
  - 山東健康管理工程研究中心

---

## 研究目標

1. 開發針對**中國人群**的 5 年 Prediabetes → Diabetes 風險預測模型
2. 比較 7 種機器學習算法的效能
3. 建立互動式網頁平台供臨床使用

---

## 資料集 ⭐⭐⭐⭐⭐

| 項目 | 主要隊列 | 外部驗證隊列 |
|------|----------|-------------|
| **來源** | 山東第一醫科大學附屬醫院 | 濱州醫學院附屬醫院 |
| **樣本數** | 6,270 人 | 2,157 人 |
| **追蹤期** | 2019-2024（5 年） | 2019-2024（5 年） |
| **健檢頻率** | **每年一次** | **每年一次** |
| **進展率** | 41.6%（2,610 人） | 35.2%（760 人） |
| **年均進展率** | 8.33% | 7.04% |
| **失訪率** | 7.5% | 5.2% |

### 納入/排除標準

**納入**：
- 2019 年基線確診為前驅糖尿病（HbA1c 5.7%-6.4%）

**排除**：
- 已有糖尿病（HbA1c ≥6.5% 或使用降糖藥）
- 妊娠糖尿病史
- 使用影響血糖代謝的藥物
- 惡性腫瘤史
- 2019 年後無第二次健檢

---

## 方法論 ⭐⭐⭐⭐⭐

### 1. 特徵工程

**原始特徵**：42 個變數
- 人口統計：性別、年齡、身高、體重、BMI
- 血壓：SBP、DBP
- 血液學：WBC、中性粒細胞、淋巴細胞、單核細胞(MONO)、血紅蛋白、RBC、血小板、血細胞比容
- 肝功能：ALT、AST、ALT/AST、GGT、ALP、總膽紅素、直接膽紅素、間接膽紅素
- 蛋白：總蛋白、白蛋白、球蛋白、白蛋白/球蛋白
- 血脂：TG、TC、HDL、LDL、HDL/TC
- 腎功能：BUN、肌酐、尿酸、eGFR、BUN/肌酐
- 血糖：FBG
- 其他：TyG 指數、MONO/HDL、中性粒細胞/HDL

**特徵選擇**：RFE-Logistic（遞迴特徵消除）
- 最終選出 **14 個特徵**：
  1. FBG（空腹血糖）
  2. HDL
  3. ALT/AST
  4. BMI
  5. Age
  6. MONO（單核細胞）
  7. Creatinine
  8. Height
  9. Weight
  10. LDL
  11. Hemoglobin
  12. HDL/TC
  13. RBC
  14. Hematocrit

### 2. 機器學習模型（7 種）

| 模型 | 類型 |
|------|------|
| Logistic Regression | 線性 |
| Random Forest | 集成（Bagging）|
| SVM | 核方法 |
| MLP | 神經網路 |
| XGBoost | 集成（Boosting）|
| LightGBM | 集成（Boosting）|
| **CatBoost** ⭐ | 集成（Boosting）|

### 3. 訓練與驗證

| 步驟 | 方法 |
|------|------|
| **資料分割** | 訓練 70% / 測試 30% |
| **超參數優化** | Grid Search + 5-fold CV |
| **內部驗證** | Test set (30%) |
| **外部驗證** | 獨立醫院隊列 |

### 4. 評估指標

- **區分能力**：AUC-ROC、PR-AUC
- **分類指標**：Accuracy、Sensitivity、Specificity、PPV、NPV、F1-score
- **校準能力**：Calibration curves
- **臨床效用**：Decision Curve Analysis (DCA)
- **可解釋性**：SHAP

---

## 結果 ⭐⭐⭐⭐⭐

### 最佳模型：CatBoost

| 指標 | Test Set | External Set |
|------|----------|--------------|
| **AUC** | **0.819** | **0.807** |
| Accuracy | 74.6% | 75.9% |
| Sensitivity | 64.8% | 57.2% |
| Specificity | 81.6% | 86.0% |
| PPV | 71.5% | 69.0% |
| NPV | 76.5% | 78.7% |
| F1-score | 0.68 | 0.626 |

### 7 模型比較（Test Set AUC）

| 模型 | AUC |
|------|-----|
| **CatBoost** | **0.819** ⭐ |
| LightGBM | 0.813 |
| XGBoost | 0.811 |
| SVM | 0.809 |
| LR | 0.801 |
| RF | 0.790 |
| MLP | 0.707 |

### SHAP 特徵重要性（Top 6）

| 排名 | 特徵 | 方向 | 臨床意義 |
|------|------|------|----------|
| 1 | **FBG** | ↑ 風險 | 核心診斷指標 |
| 2 | **HDL** | ↓ 保護 | 脂質代謝 |
| 3 | **ALT/AST** | ↓ 保護 | 肝功能 |
| 4 | **BMI** | ↑ 風險 | 肥胖指標 |
| 5 | **Age** | ↑ 風險 | 年齡 |
| 6 | **MONO** | ↑ 風險 | 發炎指標 |

---

## 與本研究的關聯 ⭐⭐⭐⭐⭐

### 相似點

| 項目 | 本論文 | 我們的研究 |
|------|--------|-----------|
| **資料規模** | 6,270 + 2,157 | ~6,000 + ~1,000 |
| **追蹤設計** | 縱向 5 年，每年健檢 | T1 → T2 → T3 |
| **外部驗證** | ✅ 有 | ✅ 有 (CLSA) |
| **特徵類型** | 血液檢驗 + 生理測量 | 血液檢驗 + 生理測量 |
| **SHAP** | ✅ 使用 | ✅ 使用 |
| **多模型比較** | 7 種 | 6 種 |

### 差異點

| 項目 | 本論文 | 我們的研究 |
|------|--------|-----------|
| **預測目標** | 單一疾病（糖尿病） | 三高（多任務）|
| **Δ 特徵** | ❌ 未使用 | ✅ 核心創新 |
| **CatBoost** | ✅ 最佳模型 | ❌ 未嘗試 |
| **診斷標準** | HbA1c（單一） | 多指標 |
| **人群** | 中國（前驅糖尿病） | 美國+加拿大（一般人群）|

---

## 可借鏡之處 ⭐⭐⭐⭐⭐

### 1. CatBoost 模型
- **考慮加入我們的模型比較**
- 論文顯示 CatBoost > LightGBM > XGBoost > RF
- 適合處理類別特徵，不需要 one-hot encoding

### 2. RFE-Logistic 特徵選擇
- 從 42 個特徵選出 14 個
- 可參考其特徵選擇流程

### 3. 完整的評估框架
- **Calibration curves**：我們可以加入
- **Decision Curve Analysis**：評估臨床效用
- **DeLong test**：模型間 AUC 比較的統計檢定

### 4. 外部驗證設計
- 使用獨立醫院資料驗證
- AUC 僅下降 0.012（0.819 → 0.807），穩定性佳

### 5. Web 介面
- 建立了互動式預測工具
- 可整合到電子病歷系統

---

## 限制

1. **回顧性研究**：缺少吸菸、飲酒、家族史等風險因子
2. **單一診斷標準**：僅用 HbA1c，未用 FBG + OGTT
3. **單一族群**：僅中國人，未驗證其他種族
4. **無縱向特徵追蹤**：未使用 Δ 特徵（這是我們的優勢！）

---

## 對 Meeting 19 簡報的建議

### 報告重點

1. **為什麼選這篇**
   - 資料規模與我們相近（~6,000 人）
   - 縱向多次健檢設計
   - 有外部驗證（我們也有 CLSA）
   - CatBoost 是我們沒用過的新模型

2. **方法論亮點**
   - 7 種模型比較 + 統計檢定
   - RFE 特徵選擇
   - 完整評估框架（校準、DCA）

3. **與我們研究的比較**
   - 他們：單一疾病、無 Δ 特徵
   - 我們：三高同時預測、Δ 特徵是核心創新

4. **可借鏡**
   - 考慮加入 CatBoost
   - 加入 Calibration curves 和 DCA

---

## 關鍵字

prediabetes, diabetes progression, CatBoost, SHAP, longitudinal study, external validation, 5-year prediction, Chinese population

---

**相關文件**：
- [論文候選清單](論文候選清單_從Dual2025延伸.md)
- [Literature_Master_Index.md](../literature_notes/Literature_Master_Index.md)
- [Meeting_19_Notes.md](../meeting_notes/Meeting_19_Notes.md)
