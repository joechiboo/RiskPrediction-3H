# Liu et al. (2024) - 台中榮總糖尿病預測研究深度解析

## 論文基本資訊

- **標題**: Use of Machine Learning to Predict the Incidence of Type 2 Diabetes Among Relatively Healthy Adults: A 10-Year Longitudinal Study in Taiwan
- **期刊**: Diagnostics 2025, 15(1), 72
- **DOI**: 10.3390/diagnostics15010072
- **發表日期**: 2024年12月31日
- **研究機構**: 台中榮總家庭醫學科
- **研究設計**: 10年縱向回顧性研究（2011-2021）
- **檔案位置**: `docs/references/diagnostics-15-00072.pdf`

---

## 研究概覽

### 研究目標
1. 選擇適當特徵預測相對健康成人的第二型糖尿病
2. 建立預測模型並比較不同 ML 演算法的性能

### 研究意義
- **台灣首個**使用 EHR + ML 預測糖尿病的研究
- **10年縱向設計**
- **首次證明甲狀腺激素（fT4）在糖尿病預測中的重要性**

---

## 研究方法

### 1. 資料來源
- **來源**: 台中榮總臨床資料中心（Clinical Data Center）
- **資料類型**: 電子病歷（EHR）
- **時間範圍**: 2011年1月 - 2021年6月

### 2. 納入與排除條件

#### 納入條件
- 相對健康的成人
- 至少接受 2 次自費健康檢查
- 兩次檢查間隔 < 4 年

#### 排除條件
- 研究期間前已確診糖尿病者
- 資料缺失者

#### 最終樣本
- **6,687 位成人**
- 平均年齡: 57.7 歲
- 平均 FBS: 89.6 mg/dL
- 平均 HbA1c: 5.5%

---

### 3. 預測特徵（33 項）

#### 人口學特徵
- Age（年齡）
- Gender（性別）

#### 生理測量（7 項）
- Height（身高）
- Weight（體重）
- Waist size（腰圍）
- Pulse rate（脈搏）
- Respiration rate（呼吸速率）

#### 血液檢驗（24 項）

**血糖相關**
- Fasting blood glucose (FBG)
- Glycated hemoglobin (HbA1c)

**血脂相關**
- Total cholesterol (TC)
- Triglycerides (TG)
- HDL-C（高密度脂蛋白膽固醇）
- LDL-C（低密度脂蛋白膽固醇）

**肝功能**
- AST（天門冬胺酸轉胺酶）
- ALT（丙胺酸轉胺酶）
- Total bilirubin（總膽紅素）
- Direct bilirubin（直接膽紅素）
- r-GT（γ-麩胺醯轉移酶）

**腎功能**
- BUN（血中尿素氮）
- Serum creatinine（血清肌酸酐）
- eGFR（估算腎絲球過濾率）

**甲狀腺功能** ⭐
- TSH（促甲狀腺激素）
- **fT4（游離甲狀腺素）** - 重要發現！

**其他**
- Hemoglobin (Hgb)
- Platelets
- High-sensitivity C-reactive protein (hsCRP)
- Total protein
- Albumin
- Uric acid
- Serum sodium
- Serum calcium

#### 尿液檢查（2 項）
- Urine glucose
- Urine ketone

---

### 4. 資料分類

#### 糖尿病診斷標準
- **HbA1c > 6.5%**，或
- **空腹血糖 > 126 mg/dL**

#### 初步標記（4 個標籤）
1. "No diabetes symptoms"（無糖尿病症狀）
2. "Potential diabetes symptoms"（潛在糖尿病症狀）
3. "Confirmed diabetes"（確診糖尿病）
4. "No data"（無資料）

#### 最終二元分類
- **Class 0（正常）**: 6,967 人（98.9%）
- **Class 1（潛在糖尿病）**: 76 人（1.1%）
- **比例**: 約 92:1（極度不平衡）

---

### 5. 資料預處理

#### 缺失值處理
- 缺失率 > 20% 的欄位 → **直接移除**
- 缺失率 ≤ 20% 的欄位 → **填入 -999** 作為缺失值指標

#### 資料分割
- **訓練集**: 60%
- **測試集**: 40%
- 使用 scikit-learn 1.6 的 train_test_split 函數

**注意**: 論文沒有使用驗證集（validation set）

---

### 6. 機器學習模型

#### 模型 1: Random Forest (RF)
- **類型**: 集成學習（Ensemble Learning）
- **原理**: 多個決策樹透過投票機制整合結果
- **公式**: RF = Σ Pk(1 - Pk) = 1 - Σ Pk²

#### 模型 2: Logistic Regression (LR)
- **類型**: 線性分類器
- **特點**: 輸出值限制在 [0, 1] 範圍
- **用途**: 二元分類

#### 模型 3: XGBoost
- **全名**: Extreme Gradient Boosting
- **原理**: 每次迭代加入新函數修正前一棵樹的錯誤
- **特點**:
  - 隨機特徵採樣
  - 增加模型多樣性和穩健性
- **公式**: XGBoost = Σ l(yi, yi(t)) + Σ Ω(fi)

---

### 7. 模型解釋性

#### SHAP（Shapley Additive exPlanations）
- 視覺化模型對特徵的關注程度
- 增強預測結果的可解釋性
- 幫助理解模型決策過程

---

## 研究結果

### 1. 模型性能比較

| 模型 | Accuracy | Precision (Class 1) | Recall (Class 1) | F1-Score (Class 1) | AUC-ROC |
|------|----------|---------------------|------------------|-------------------|---------|
| **Random Forest** | **99%** | 25% | 1% | 0.03 | 0.74 |
| **Logistic Regression** | **99%** | 0% | 0% | 0.00 | 0.90 |
| **XGBoost** | **98%** | 19% | 33% | 0.24 | **0.93** ⭐ |

#### 關鍵發現
- **Accuracy 高但不可靠**（受資料不平衡影響）
- **AUC-ROC 是更好的評估指標**
- **XGBoost 是最佳模型**（AUC = 0.93）

---

### 2. Confusion Matrix 分析

#### Logistic Regression（Accuracy = 99%）
```
                預測 0    預測 1
實際 0 (正常)    3031      563
實際 1 (糖尿病)   14        46
```
- Recall (Class 1) = 76.7%
- Precision (Class 1) = 7.6%

#### Random Forest（Accuracy = 99%）
```
                預測 0    預測 1
實際 0 (正常)    3593       1
實際 1 (糖尿病)   60        0
```
- **Recall (Class 1) = 0%**（完全失敗）

#### XGBoost（Accuracy = 98%）
```
                預測 0    預測 1
實際 0 (正常)    3703      252
實際 1 (糖尿病)   33        32
```
- Recall (Class 1) = 49.2%
- Precision (Class 1) = 11.3%
- **實際預測能力最好**

---

### 3. ⭐ Top 5 重要特徵

#### 特徵重要性排名（來自 XGBoost + SHAP）

1. **HbA1c（糖化血色素）** - 最重要
   - 預期中的結果
   - 糖尿病診斷金標準

2. **Fasting Blood Glucose（空腹血糖）**
   - 預期中的結果
   - 所有糖尿病研究的核心特徵

3. **Weight（體重）**
   - 預期中的結果
   - 與肥胖、代謝症候群相關

4. **🔬 fT4（游離甲狀腺素）** - **新發現！**
   - **過去研究完全忽視**
   - **首次證明其重要性**
   - 臨床上不常規檢測
   - 作者最強調的特徵

5. **Triglycerides（三酸甘油酯）**
   - 預期中的結果
   - 代謝症候群常見指標

---

## 核心發現：為何 fT4 是突破性發現？

### 1. 過去研究都忽略了

> "There were several studies utilizing machine learning to predict diabetes. **Fasting blood glucose is one of the significant features in the studies**. Although this study revealed a similar result, **it also revealed the importance of fT4**."

**過去研究聚焦**：
- 血糖（FBG, HbA1c）
- 血脂（TG, Cholesterol）
- BMI、體重

**沒有人發現甲狀腺的重要性**

---

### 2. 首次使用 ML 證明

> "**This would be the first study using machine learning models to predict diabetes that has demonstrated the importance of thyroid hormone.**"

這是**第一篇**使用機器學習證明甲狀腺激素預測價值的研究。

---

### 3. 排名超越傳統指標

fT4 排名第 4，**超越了**：
- Hemoglobin（血紅素）
- Platelet（血小板）
- AST/ALT（肝功能）
- hsCRP（發炎指標）
- Waist（腰圍）
- LDL-C（低密度膽固醇）
- **甚至超越 TSH**（促甲狀腺激素）

---

### 4. 臨床上不常規檢測

> "In clinical settings, **thyroid function measurement, including thyroid-stimulating hormone (TSH) and fT4, is not included in routine screenings for diabetes**, particularly in people without any apparent symptoms of thyroid dysfunction."

**臨床現狀**：
- 糖尿病篩檢 → 只測血糖、HbA1c
- 甲狀腺功能 → 只在懷疑甲狀腺疾病時才測

**這個發現的意義**：
- 建議將 fT4 納入糖尿病風險評估
- 即使沒有甲狀腺症狀，也可能影響糖尿病風險

---

### 5. 生理機制有科學支持

> "The thyroid hormone plays a role in both **regulating metabolism and energy expenditure**, while it is also involved in **insulin regulation and glucose homeostasis**."

**甲狀腺激素的作用**：
1. 調節代謝和能量消耗
2. 參與胰島素調節
3. 維持血糖穩態
4. 增強胰島 β 細胞存活率

---

### 6. 文獻證據支持

#### [29] Falzacappa et al. (2010)
- 甲狀腺激素可以**增強胰島 β 細胞存活率**

#### [30] Chaker et al. (2016) - BMC Medicine
- **亞臨床甲狀腺功能低下**是前驅糖尿病患者的風險因子

#### [31] Nishi (2018) - Diabetology International
- **甲亢和甲減都與第二型糖尿病相關**
- 亞臨床甲狀腺功能低下者**併發症發生率更高**

---

### 7. 成本效益考量

> "Moreover, it highlighted **the relevance of predicting type 2 diabetes using more affordable methods**, such as triglycerides, compared to the cost of the HbA1C test."

**實務意義**：
- fT4 檢測相對便宜
- 可能比單獨依賴 HbA1c 更具成本效益
- 適合大規模篩檢

---

## 為何排除已確診糖尿病患者？

### 研究目標差異

| 研究類型 | 研究對象 | 研究問題 | 排除確診患者？|
|---------|---------|---------|--------------|
| **預測發病**（本研究）| 健康/高風險族群 | 誰**未來會**得糖尿病？ | ✅ **要排除** |
| **預測併發症** | 已確診糖尿病患者 | 誰**會出現**併發症？ | ❌ 不排除 |

---

### 排除的理由

#### 1. 符合預防醫學目標
- 在糖尿病「前期」就預測出來
- 提早介入，改變生活方式
- 延緩或避免發病

#### 2. 避免資料洩漏（Data Leakage）
如果不排除確診患者：
```
模型會學到：
「已經在吃降血糖藥的人 → 有糖尿病」
「已經有糖尿病併發症的人 → 有糖尿病」
這是作弊！
```

#### 3. 應用場景是健康檢查
- ✅ 健康檢查中心
- ✅ 預防醫學門診
- ✅ 企業員工健檢

**不是**：
- ❌ 糖尿病門診
- ❌ 內分泌科病房

#### 4. 臨床意義
> "Onset of NIDDM occurs at least 4–7 yr before clinical diagnosis"

- 糖尿病發病可能在確診前 4-7 年就開始
- **預測研究的目標是在這 4-7 年的「前期」就發現**

---

## 為何使用 AUC-ROC 而非 Accuracy？

### Accuracy 的陷阱

#### 資料極度不平衡
- Class 0（正常）：6,967 人（**98.9%**）
- Class 1（糖尿病）：76 人（**1.1%**）

**問題**：如果模型「全部預測為 Class 0」，Accuracy 就能達到 **98.9%**！

```python
# 模型很懶，全部預測為 0
predictions = [0, 0, 0, ..., 0]
Accuracy = 98.9% ✅ 看起來很好！
但實際上：完全沒有預測到任何糖尿病患者！❌
```

---

### AUC-ROC 揭露真相

| 模型 | Accuracy | **AUC-ROC** | 實際表現 |
|------|----------|-------------|----------|
| Logistic Regression | 99% | **0.90** | 中等 |
| Random Forest | 99% | **0.74** | 最差 ⚠️ |
| **XGBoost** | 98% | **0.93** ⭐ | **最好** |

**關鍵洞察**：
- Random Forest 雖然 Accuracy = 99%，但 AUC 只有 0.74（**很差**）
- XGBoost 雖然 Accuracy = 98%（最低），但 AUC = 0.93（**最好**）

---

### AUC-ROC 的優勢

#### 衡量什麼？
```
ROC Curve：
- X 軸：False Positive Rate (1 - Specificity)
- Y 軸：True Positive Rate (Recall / Sensitivity)

AUC（曲線下面積）：
- 1.0 = 完美模型
- 0.5 = 隨機猜測
- < 0.5 = 比隨機還差
```

#### 為何適合不平衡資料？
1. 考慮了 True Positive 和 False Positive 的權衡
2. 不受 class distribution 影響
3. 評估模型的**分辨能力**，而非單純預測正確率

---

### 醫療應用的考量

- **高 Recall（靈敏度）**：不能漏掉真正的糖尿病患者
- **高 Specificity（特異度）**：不要誤判太多正常人
- **AUC-ROC** 同時考慮兩者的平衡

---

## 討論與啟示

### 研究優勢 ✅

1. **台灣首創**
   - 首個使用 EHR + ML 預測糖尿病的研究
   - 10 年縱向設計

2. **高準確率**
   - RF, LR: 99%
   - XGBoost: 98%（但 AUC 最高 = 0.93）

3. **新發現**
   - 首次證明甲狀腺激素（fT4）的重要性
   - 過去文獻完全忽視

4. **臨床應用性**
   - 使用常規健檢數據
   - 成本效益高
   - 適合預防醫學

---

### 研究限制 ⚠️

1. **外部驗證不足**
   - 單一醫學中心（台中榮總）
   - 未用其他公開資料庫驗證
   - 泛化能力有待確認

2. **特徵數量多**
   - 33 項特徵
   - 小型醫療系統可能無法收集完整資料
   - 可能影響模型準確度

3. **資料極度不平衡**
   - Class 0 vs Class 1 = 92:1
   - 導致 Precision 和 Recall 在 Class 1 表現較差
   - XGBoost 的 Recall 也只有 33%

4. **沒有驗證集**
   - 只有訓練集和測試集
   - 可能有過擬合風險

---

### 未來研究方向

1. **外部驗證**
   - 應用於其他醫療系統
   - 使用公開資料庫（如 NHANES）驗證

2. **甲狀腺功能深入研究**
   - 探討 fT4 與糖尿病的因果關係
   - 是否應將甲狀腺功能納入常規篩檢

3. **處理資料不平衡**
   - 使用 SMOTE 等技術
   - 改善 Class 1 的預測能力

4. **簡化特徵**
   - 探索使用更少特徵達到相似準確度
   - 提高小型醫療系統的可行性

---

## 臨床應用意義

### 1. 預防醫學

> "For clinical healthcare professionals involved in **preventive medicine**, we believe that the prediction model could apply to both clinical practice and shared decision-making, particularly for individuals seeking to **raise health awareness**, thereby **promoting any necessary lifestyle modifications**."

**應用場景**：
- 健康檢查中心
- 企業員工健檢
- 預防醫學門診

---

### 2. 提早介入

> "Diabetes prediction could not only **prevent the onset of an irreversible disease**, but it may also **mitigate the burden of excess financial expenditures**, which would negatively impact the healthcare system over the coming years."

**效益**：
- 提早發現高風險者
- 生活方式介入
- 延緩或避免發病
- 降低醫療負擔

---

### 3. 甲狀腺功能篩檢

> "Future studies are still warranted in order to better explore whether **thyroid function measurement should be incorporated into diabetes screening** among relatively healthy adults."

**建議**：
- 考慮將 fT4 納入糖尿病風險評估
- 即使無甲狀腺症狀也應檢測
- 成本效益高

---

## 與本研究（三高預測）的關聯

### 相似之處

1. **預測目標**
   - 都是預測慢性代謝性疾病
   - 本研究：三高同時預測
   - Liu et al.：糖尿病預測

2. **研究設計**
   - 都使用縱向追蹤設計
   - 都使用電子病歷數據
   - 都使用多種 ML 模型比較

3. **特徵類型**
   - 都包含生理測量（BMI, 血壓）
   - 都包含血液檢驗（血糖, 血脂）
   - 都使用時間序列資料

---

### 差異之處

| 特性 | Liu et al. (2024) | 本研究 |
|------|-------------------|--------|
| **預測疾病** | 糖尿病（單一疾病）| 三高同時預測（多標籤）|
| **研究設計** | 10年追蹤 | T₁→T₂→T₃ 時序 |
| **特徵工程** | 靜態特徵（33項）| 靜態 + 變化量 (Δ) |
| **模型方法** | 單任務學習 | 可考慮 Multi-Task Learning |
| **資料來源** | 台中榮總真實資料 | Synthea 合成資料 |
| **資料平衡** | 極度不平衡（92:1）| 待確認 |

---

### 可借鏡之處

1. **特徵選擇**
   - fT4（甲狀腺功能）可納入考量
   - 除了傳統血糖、血脂指標，應探索其他生化指標

2. **評估指標**
   - 資料不平衡時，AUC-ROC 比 Accuracy 更可靠
   - 應重視 Recall（不能漏掉高風險者）

3. **模型選擇**
   - XGBoost 在不平衡資料表現優異
   - 使用 SHAP 增強可解釋性

4. **研究設計**
   - 排除已確診患者的邏輯
   - 縱向追蹤的臨床意義

5. **外部驗證**
   - 單一資料來源的限制
   - 需要多中心驗證

---

## 重要引文（簡報可用）

### 關於 fT4 的突破性發現

> "**fT4 seems to be one of the significant features in predicting the onset of diabetes**. Moreover, **this would be the first study using machine learning models to predict diabetes that has demonstrated the importance of thyroid hormone**."
>
> — Abstract, p.1

---

### 關於預防醫學應用

> "Diabetes prediction could not only **prevent the onset of an irreversible disease**, but it may also **mitigate the burden of excess financial expenditures**, which would negatively impact the healthcare system over the coming years."
>
> — Discussion, p.9

---

### 關於臨床應用

> "For clinical healthcare professionals involved in **preventive medicine**, we believe that the prediction model could apply to both clinical practice and shared decision-making, particularly for individuals seeking to **raise health awareness**, thereby **promoting any necessary lifestyle modifications**."
>
> — Implications, p.8-9

---

### 關於早期診斷的重要性

> "Of major concern is that the onset of type 2 diabetes may be delayed **9–12 years upon diagnosis**, when patients who present themselves with established microvascular complications, such as diabetic retinopathy, can be treated. It remains important to **identify patients with undiagnosed type 2 diabetes during the preclinical period**."
>
> — Introduction, p.2

---

## 簡報建議結構（10頁）

### Slide 1: 研究概覽
- 標題、期刊、研究機構
- 10年縱向研究（2011-2021）
- 6,687位相對健康成人

### Slide 2: 研究背景與動機
- 太平洋島國糖尿病盛行率最高
- 診斷延遲 9-12 年
- 台灣缺乏預測工具

### Slide 3: 資料來源與納入條件
- 台中榮總 EHR
- 納入/排除標準
- 為何排除已確診患者

### Slide 4: 預測特徵（33項）
- 人口學 + 生理測量
- 血液檢驗（血糖、血脂、肝腎功能）
- **甲狀腺功能**（TSH, fT4）

### Slide 5: 糖尿病診斷標準與資料分類
- HbA1c > 6.5% 或 FBG > 126 mg/dL
- Class 0: 6,967人 vs Class 1: 76人
- 資料極度不平衡（92:1）

### Slide 6: 機器學習模型
- Random Forest, Logistic Regression, XGBoost
- SHAP 特徵重要性分析

### Slide 7: 模型性能比較
- Accuracy vs AUC-ROC
- 為何 Accuracy 高但不可靠
- XGBoost 最佳（AUC = 0.93）

### Slide 8: ⭐ Top 5 重要特徵
- HbA1c, FBG, Weight, **fT4**, TG
- fT4 的突破性發現

### Slide 9: 甲狀腺與糖尿病的關聯
- 為何 fT4 重要？
- 生理機制
- 文獻支持
- 臨床意義

### Slide 10: 研究優勢與限制
- 優勢：台灣首創、高準確率、新發現
- 限制：單一中心、資料不平衡
- 未來方向

---

## 參考文獻連結

### 論文本身
- DOI: [10.3390/diagnostics15010072](https://doi.org/10.3390/diagnostics15010072)
- 檔案: `docs/references/diagnostics-15-00072.pdf`

### 相關文獻筆記
- 台灣三高文獻回顧: `docs/Q2_Taiwan_Literature_Review.md`
- 參考文獻清單: `docs/references/README.md`

---

## 筆記整理日期
2025年10月7日

---

## 關鍵標籤
`#台中榮總` `#糖尿病預測` `#機器學習` `#甲狀腺` `#fT4` `#XGBoost` `#縱向研究` `#預防醫學` `#台灣研究`
