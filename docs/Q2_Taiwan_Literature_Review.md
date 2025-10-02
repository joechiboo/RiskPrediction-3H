# Q2：台灣三高預測相關文獻回顧

## 摘要
本文獻回顧整理了台灣及華人地區關於高血壓、高血糖、高血脂預測的機器學習研究，特別聚焦於使用縱向資料（longitudinal data）和時序特徵的預測模型。

---

## 一、高血壓預測（Hypertension Prediction）

### 1.1 台灣研究

#### 研究 1：隱匿性高血壓的機器學習預測

- **作者**：Hung et al. (2021)
- **資料來源**：台灣六家醫學中心（2004-2005）+ 台北榮總（2012-2020）
- **樣本數**：Cohort 1: 970 位高血壓患者；Cohort 2: 416 位患者
- **研究目標**：預測隱匿性高血壓（Masked Hypertension, MH）和隱匿性未控制高血壓（MUCH）
- **方法**：
  - 使用 33 個臨床特徵（人口統計、血壓參數、降壓藥物、生化指標）
  - 四種模型：Logistic Regression、Random Forest、XGBoost、ANN
  - 使用 SMOTE-NC 處理類別不平衡問題

- **主要發現**：
  - Random Forest 表現最佳（Internal AUC = 0.851, External AUC = 0.837）
  - 僅需 6 個預測變數：office DBP, MAP, SBP, PP, beta-blocker, HDL-C
  - Sensitivity = 1.000, NPV = 1.000（高敏感度和陰性預測值）

- **重要特徵**：舒張壓、平均動脈壓、收縮壓、脈壓、Beta-blocker、HDL-C
- **與本研究的關聯**：
  - 同樣使用台灣資料
  - 驗證了機器學習在高血壓預測的有效性
  - 但專注於單次就診預測，而非縱向預測

#### 研究 2：台灣高血壓風險預測模型

- **作者**：Chien KL et al. (2011)
- **期刊**：Journal of Human Hypertension
- **研究目標**：為台灣華人族群建立新發高血壓的風險預測模型
- **資料來源**：提到但未在本次搜尋中詳細獲取
- **與本研究的關聯**：早期台灣高血壓預測研究，可作為基準比較

---

## 二、糖尿病預測（Diabetes Prediction）

### 2.1 台灣研究

#### 研究 3：台灣第二型糖尿病發病預測

- **作者**：Liu et al. (2024)
- **資料來源**：台中榮民總醫院電子病歷（2003-2022）
- **樣本數**：6,687 位相對健康的成年人
- **追蹤時間**：10 年縱向研究
- **方法**：
  - 33 個臨床特徵
  - 三種模型：Logistic Regression、Random Forest、XGBoost

- **主要發現**：
  - Random Forest 準確率 99%
  - Logistic Regression 準確率 99%
  - XGBoost 準確率 98%

- **重要特徵**：
  - HbA1c（糖化血色素）
  - Fasting Blood Glucose（空腹血糖）
  - Weight（體重）
  - Free Thyroxine (fT4)（游離甲狀腺素）— 首次發現甲狀腺激素的重要性
  - Triglycerides（三酸甘油酯）

- **與本研究的關聯**：
  - 台灣本土資料，人口特性相近
  - 縱向研究設計（10年追蹤）
  - 高準確率可作為 benchmark
  - 特徵選擇可供參考

#### 研究 4：台灣青年男性血糖變化與前驅糖尿病預測

- **作者**：Dual Machine Learning Framework (2025)
- **資料來源**：Taiwan Biobank
- **樣本數**：6,247 位 18-35 歲台灣男性
- **追蹤時間**：平均 5.9 年
- **方法**：
  - 雙機器學習框架：(1) 預測血糖變化量（δ-FPG）(2) 分類前驅糖尿病風險
  - 模型：Random Forest、Stochastic Gradient Boosting、XGBoost、Elastic Net
  - 使用 SHAP 進行模型解釋
  - 10 次重複訓練測試以評估穩定性

- **主要發現**：
  - δ-FPG 預測：XGBoost 和 Random Forest 表現最佳
  - 前驅糖尿病分類：AUC 男性 0.76, 女性 0.80
  - 強調年齡和性別差異的重要性

- **與本研究的關聯**：
  - **高度相關**：同樣使用縱向資料預測未來疾病風險
  - 雙框架設計（連續值預測 + 二元分類）可借鏡
  - SHAP 解釋性方法可應用
  - 重複訓練評估穩定性的做法值得採用

#### 研究 5：台灣糖尿病發病預測（神經網路）

- **作者**：Chen & Huang (2023)
- **期刊**：Journal of Personalized Medicine
- **資料來源**：台灣患者資料
- **方法**：
  - Microsoft Machine Learning Studio
  - 多種神經網路模型比較

- **主要發現**：
  - Two-class Boosted Decision Tree 表現最佳
  - AUC = 0.991

- **與本研究的關聯**：
  - 證實深度學習在台灣糖尿病預測的有效性
  - 極高的 AUC 值顯示問題可行性

---

## 三、高血脂預測（Dyslipidemia/Hyperlipidemia Prediction）

### 3.1 國際研究（台灣研究較少）

#### 研究 6：血脂異常預測（伊朗）

- **作者**：Lifestyle Promotion Project (2024)
- **資料來源**：伊朗 East Azerbaijan Province
- **方法**：
  - Multilayer Perceptron (MLP) 表現最佳
  - Random Forest 準確率 80%

- **重要發現**：IR（胰島素阻抗）相關指標如 TyG index 是重要預測因子

#### 研究 7：LDL-C 預測（機器學習 vs 傳統公式）

- **作者**：韓國研究 (2024)
- **資料來源**：KNHANES 資料
- **方法**：
  - 比較 ML 模型（Linear Regression, KNN, Decision Tree, Random Forest, XGBoost, MLP）與傳統公式（Friedewald, Martin, Sampson）

- **主要發現**：
  - Random Forest 和 XGBoost 準確率最高（R² = 0.94）
  - ML 在高三酸甘油酯情況下仍保持高準確率
  - 兩步驟預測模型 concordance rate = 85.1%

### 3.2 台灣血脂相關指引

- 2022 Taiwan Lipid Guidelines for Primary Prevention
- 2017 Taiwan Lipid Guidelines for High Risk Patients
- 這些指引可作為臨床標準和評估基準

---

## 四、代謝症候群預測（Metabolic Syndrome）

### 4.1 台灣研究

#### 研究 8：台灣成人代謝症候群嚴重度評分

- **作者**：An Application of MS Severity Scores (2020)
- **資料來源**：Major Health Screening Center, Taiwan
- **樣本數**：71,108 位 20-64 歲參與者
- **方法**：
  - 使用 Principal Component Analysis (PCA) 建立 MetS-Z score
  - 依性別和年齡分組（20-34, 35-49, 50-64 歲）

- **主要發現**：
  - MetS 盛行率在台灣 12 年內從 13.6% 成長至 25.5%
  - 連續評分比二元診斷更能反映風險程度
  - 與生活方式因素（運動、飲酒、吸菸）高度相關

#### 研究 9：台灣成人代謝症候群風險因子評估

- **作者**：Data-Driven Assessment (2019)
- **方法**：Decision Tree Algorithm
- **主要發現**：
  - Triglycerides (TG) 是最重要的 root node
  - Waist Circumference (WC) 是次要關鍵因子
  - 中高齡族群的 TG 和 WC 是預防 MetS 的關鍵

#### 研究 10：台灣人工神經網路預測代謝症候群

- **資料來源**：台灣健檢機構（2006-2014）
- **樣本數**：27,415 位受試者
- **追蹤**：三個階段的重複測量
- **方法**：
  - Artificial Neural Network (ANN)
  - Over-sampling technique (SMOTE)

- **主要發現**：
  - AUC 達 0.93
  - Over-sampling 提升敏感度和 F2 measure
  - MetS 盛行率：Stage 1 (18.3%), Stage 2 (24.6%), Stage 3 (30.1%)

---

## 五、綜合比較與總結

### 5.1 文獻特點比較表

| 研究 | 國家/地區 | 疾病 | 樣本數 | 追蹤時間 | 最佳模型 | AUC/準確率 | 關鍵特徵 |
|------|----------|------|--------|---------|---------|-----------|---------|
| Hung et al. 2021 | 台灣 | 隱匿性高血壓 | 970+416 | 橫斷面 | Random Forest | 0.851/0.837 | DBP, MAP, SBP, PP, beta-blocker, HDL-C |
| Liu et al. 2024 | 台灣 | 第二型糖尿病 | 6,687 | 10年 | Random Forest | 99% | HbA1c, FBG, Weight, fT4, TG |
| Dual Framework 2025 | 台灣 | 前驅糖尿病 | 6,247 | 5.9年 | XGBoost/RF | 0.76-0.80 | FPG, Age, BMI |
| Chen & Huang 2023 | 台灣 | 糖尿病 | N/A | N/A | Boosted Decision Tree | 0.991 | N/A |
| MS Severity 2020 | 台灣 | 代謝症候群 | 71,108 | 橫斷面 | PCA (MetS-Z) | N/A | WC, FPG, BP, TG, HDL-C |
| ANN MetS 2006-14 | 台灣 | 代謝症候群 | 27,415 | 3 stages | ANN | 0.93 | 社經地位+生活方式 |

### 5.2 與本研究的關聯性

#### 高度相關的研究：

1. **Liu et al. 2024（台灣糖尿病預測）**
   - 同為台灣本土資料
   - 10年縱向追蹤
   - 可作為糖尿病預測的 baseline

2. **Dual Framework 2025（台灣前驅糖尿病）**
   - 縱向血糖變化預測
   - 雙機器學習框架設計
   - SHAP 解釋性方法
   - 重複實驗評估穩定性

3. **Hung et al. 2021（台灣隱匿性高血壓）**
   - 台灣多中心資料
   - 外部驗證設計
   - Random Forest 優異表現

#### 可借鑑的研究設計：

1. **特徵工程**：
   - 變化量特徵（Δ特徵）的重要性
   - 時間間隔特徵
   - 藥物使用特徵

2. **模型選擇**：
   - Random Forest、XGBoost 在台灣資料表現穩定
   - Ensemble 方法普遍優於單一模型
   - ANN/MLP 在處理非線性關係時有優勢

3. **評估指標**：
   - AUC-ROC 作為主要指標
   - Sensitivity/Specificity/NPV/PPV 全面評估
   - 外部驗證的必要性

### 5.3 研究缺口（Research Gap）

本研究填補的缺口：

1. **多標籤同時預測**：現有文獻多為單一疾病預測，缺乏同時預測三高的研究
2. **縱向時序特徵**：結合 T₁ 和 T₂ 的變化量進行 T₃ 預測
3. **台灣本土三高綜合研究**：整合三種代謝疾病的預測模型

### 5.4 模型性能基準（Benchmark）

根據文獻，台灣相關研究的性能基準：

- **高血壓預測**：AUC 0.75-0.85
- **糖尿病預測**：AUC 0.76-0.99, Accuracy 98-99%
- **代謝症候群**：AUC 0.90-0.93

**本研究目標**：

- AUC-ROC > 0.75
- F1-Score > 0.65
- Recall > 0.65

這些目標與文獻基準一致，具有可達成性。

---

## 六、方法論啟示

### 6.1 資料處理

- 缺失值處理：Mean imputation
- 類別不平衡：SMOTE、SMOTE-NC、Over-sampling
- 標準化：Z-score normalization（特別在 LR 和 ANN）

### 6.2 特徵選擇

- LASSO regression
- Random Forest feature importance
- SHAP values（可解釋性）
- Mutual Information

### 6.3 模型驗證

- 內部驗證：訓練集/驗證集/測試集分割（70/15/15）
- 外部驗證：不同時期或不同醫院的資料
- 交叉驗證：10-fold cross-validation
- 重複實驗：多次隨機種子確保穩定性

### 6.4 可解釋性

- SHAP (SHapley Additive exPlanations)：全局和局部解釋
- Feature Importance Ranking
- Decision Tree Visualization

---

## 七、建議與下一步

### 7.1 文獻參考優先級

**高優先級（必讀並詳細引用）**：

- Liu et al. 2024 - 台灣糖尿病 10 年追蹤
- Hung et al. 2021 - 台灣隱匿性高血壓預測
- Dual Framework 2025 - 台灣前驅糖尿病雙框架

**中優先級（引用作為對比）**：

- Chen & Huang 2023 - 台灣糖尿病神經網路
- MS Severity 2020 - 台灣代謝症候群評分
- ANN MetS 2006-14 - 台灣代謝症候群 ANN

**低優先級（背景資訊）**：

- 2022 Taiwan Lipid Guidelines
- 國際血脂預測研究（作為對比）

### 7.2 論文撰寫建議

**文獻回顧章節結構**：

1. 引言：三高的流行病學和健康影響
2. 機器學習在疾病預測的應用
3. 台灣三高相關研究回顧
   - 3.1 高血壓預測
   - 3.2 糖尿病預測
   - 3.3 高血脂預測
   - 3.4 代謝症候群綜合研究
4. 縱向資料在疾病預測的優勢
5. 研究缺口與本研究貢獻

**引用策略**：

- 台灣研究作為主要對比基準
- 國際研究提供方法論支持
- 強調本研究的創新性：多標籤 + 縱向預測

---

## 八、參考文獻清單

### 台灣高血壓研究

1. Hung, M.-H., et al. (2021). Prediction of Masked Hypertension and Masked Uncontrolled Hypertension Using Machine Learning. *Frontiers in Cardiovascular Medicine*, 8:778306.
2. Chien, K.L., et al. (2011). Prediction Models for the Risk of New Onset Hypertension in Ethnic Chinese in Taiwan. *Journal of Human Hypertension*, 25, 294–303.

### 台灣糖尿病研究

3. Liu, Y.-Q., et al. (2024). Use of Machine Learning to Predict the Incidence of Type 2 Diabetes Among Relatively Healthy Adults: A 10-Year Longitudinal Study in Taiwan. *Diagnostics*, 15(1), 72.
4. Dual Machine Learning Framework (2025). Dual Machine Learning Framework for Predicting Long-Term Glycemic Change and Prediabetes Risk in Young Taiwanese Men. *Diagnostics*, 15(19), 2507.
5. Chen, C.-Y., & Huang, D.-Y. (2023). Predicting the Onset of Diabetes with Machine Learning Methods. *Journal of Personalized Medicine*, 13(3), 406.

### 台灣代謝症候群研究

6. An Application of Metabolic Syndrome Severity Scores in the Lifestyle Risk Assessment of Taiwanese Adults (2020). *International Journal of Environmental Research and Public Health*, 17(10), 3348.
7. A Data-Driven Assessment of the Metabolic Syndrome Criteria for Adult Health Management in Taiwan (2019). *International Journal of Environmental Research and Public Health*, 16(1), 92.

### 台灣血脂指引

8. Huang, P.-H., et al. (2022). 2022 Taiwan lipid guidelines for primary prevention. *Journal of the Formosan Medical Association*, 121(12), 2393-2407.

### 國際研究（方法論參考）

9. Predicting dyslipidemia incidence: unleashing machine learning algorithms on Lifestyle Promotion Project data (2024). *BMC Public Health*.
10. Machine learning-based prediction of LDL cholesterol (2025). Various international studies.
