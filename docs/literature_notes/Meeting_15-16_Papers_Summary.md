# Meeting 15-16 論文總結

**整理日期**：2025-11-13
**用途**：總結 Meeting 15 和 Meeting 16 報告的重點論文

---

## 📑 文獻總覽

| 編號 | 論文 | 期刊 | 年份 | 疾病 | 狀態 | Meeting |
|------|------|------|------|------|------|---------|
| 15 | 台灣第二型糖尿病發病預測 | Diagnostics, 15(1), 72 | 2024 | 糖尿病 | ✅ 已深度解析 | Meeting 15 |
| 16 | 台灣多慢性病同時預測 (Taiwan MTL) | Scientific Reports | 2025 | 糖尿病、高血壓、心臟病、中風 | ✅ 已深度解析 | Meeting 16 |

---

## 論文 15：台灣第二型糖尿病發病預測 (Liu et al. 2024)

### 基本資訊

| 項目 | 內容 |
|------|------|
| **標題** | Use of Machine Learning to Predict the Incidence of Type 2 Diabetes Among Relatively Healthy Adults: A 10-Year Longitudinal Study in Taiwan |
| **作者** | Liu et al. (2024) |
| **期刊** | Diagnostics, 15(1), 72 |
| **DOI** | [10.3390/diagnostics15010072](https://doi.org/10.3390/diagnostics15010072) |
| **PDF位置** | [diagnostics-15-00072.pdf](../references/diagnostics-15-00072.pdf) |
| **研究類型** | 縱向回顧性研究 (Longitudinal retrospective study) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | 臺中榮民總醫院電子病歷 (EHR) |
| **資料集** | 不可下載 |
| **樣本數** | 6,687 位相對健康的成年人 |
| **追蹤時間** | 10 年 (2003-2022) |
| **資料不平衡** | Class 0 (98.9%) vs Class 1 (1.1%)，比例 92:1 |

### 輸入特徵

**處理問題**：罹患疾病前預測糖尿病機率

**輸入資料類型**：
- 人口特徵 (Demographics)
- 生理測量 (Physical measurements)
- 血液檢驗 (Blood tests)

**特徵數量**：33 個臨床特徵

### 方法

**前處理**：
- 資料篩選
- 欄位轉換
- 資料分割

**機器學習方法**：
- Logistic Regression (LR)
- Random Forest (RF)
- XGBoost

### 評估準則

- Accuracy
- Precision
- Recall
- F1-Score
- AUC

### 主要結果

**模型性能**：
| 模型 | Accuracy | AUC |
|------|----------|-----|
| Random Forest | 99% | 0.74 |
| Logistic Regression | 99% | 0.90 |
| **XGBoost** | 98% | **0.93** ⭐ (最佳) |

**關鍵特徵** (Feature Importance):
1. **HbA1c**（糖化血色素）
2. **Fasting Blood Glucose**（空腹血糖）
3. **Weight**（體重）
4. **Free Thyroxine (fT4)**（游離甲狀腺素）⭐ 首次發現
5. **Triglycerides**（三酸甘油酯）

### 輸出

- **預測糖尿病風險**（二元分類：Yes/No）

### 提出解決方案

- 無特定名稱，但證明 XGBoost 在台灣資料上表現優異

### 與本研究的關聯

✅ **高度相關**
- 台灣本土資料，人口特性相近
- 10 年縱向追蹤設計
- 高準確率可作為 benchmark (AUC > 0.90)
- 特徵選擇可供參考
- 處理極度不平衡資料的經驗

### 相關文檔

- [Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md](Liu_2024_TCVGH_Diabetes_Prediction_深度解析.md)
- 簡報檔：[meeting15_21138X006_紀伯喬_wVBA.pptm](../meeting_notes/meeting15_21138X006_紀伯喬_wVBA.pptm) (已報告完成)

---

## 論文 16：台灣多慢性病同時預測 (Taiwan MTL 2025)

### 基本資訊

| 項目 | 內容 |
|------|------|
| **標題** | Multitask learning multimodal network for chronic disease prediction |
| **作者** | Hsinhan Tsai, Ta-Wei Yang, Tien-Yi Wu, Ya-Chi Tu, Cheng-Lung Chen, Cheng-Fu Chou |
| **期刊** | Scientific Reports (2025年5月) |
| **期刊分級** | **SCI 期刊** (IF ~4.0, Q2) |
| **DOI** | [10.1038/s41598-025-99554-z](https://doi.org/10.1038/s41598-025-99554-z) |
| **PDF位置** | [s41598-025-99554-z.pdf](../references/s41598-025-99554-z.pdf) |
| **研究機構** | 台大資工系 × 林口長庚醫院 × 國家太空中心 |
| **研究類型** | 多任務學習 (Multi-Task Learning) |

### 研究設計

| 項目 | 內容 |
|------|------|
| **資料來源** | 台灣衛生福利資料科學中心 (HWDC) |
| **資料集** | 不可下載（台灣健保資料庫） |
| **樣本數** | 555,124 位 |
| **追蹤時間** | 過去 10 年醫療紀錄 → 預測未來 5 年風險 |
| **資料分割** | 訓練集：64% / 驗證集：16% / 測試集：20% |

### 輸入特徵

**處理問題**：同時預測多種慢性病並探索疾病共病關係

**輸入資料類型**：
- **ICD 診斷代碼序列**（過去 10 年）
- **個人資訊**：
  - 年齡 (Age)
  - 性別 (Gender)
  - 居住地區 (Residential Area)
  - 是否偏遠地區 (Remote Area)
  - 職業類別 (Occupation)

**特徵建構方式**：
- 每 2 個月選取最常出現的 3 個疾病（ICD codes）
- 10 年 × 每年 6 個雙月 × 3 個疾病 = **180 個疾病特徵**
- 缺失值使用 `<PAD>` token 填補

**❌ 無血液檢驗數據**（與論文 15 的主要差異）

### 方法

**前處理**：
- **Word2Vec Embedding**：將 ICD codes 轉換為語義向量
- **特徵選取**：每 2 個月選 3 個最常見疾病
- **缺失值處理**：使用 `<PAD>` token
- **排除已患病者**：排除過去 10 年內已診斷目標疾病的患者

**機器學習方法**：
- **MAND 系列** (Multi-Task Learning):
  - MAND-LR (Logistic Regression)
  - MAND-MLP (Multi-Layer Perceptron)
  - MAND-LSTM (Long Short-Term Memory)
  - MAND-MHSA (Multi-Head Self-Attention)
- **CTR 模型** (Click-Through Rate):
  - FM (Factorization Machine)
  - DCN (Deep & Cross Network)

**核心架構**：
- Hard Parameter Sharing (共享隱藏層)
- Task-specific Layers (各疾病獨立預測層)

### 評估準則

- Log Loss
- AUC
- BAC (Balanced Accuracy)
- Precision
- Recall
- F1-Score
- FPR (False Positive Rate)
- FNR (False Negative Rate)

### 主要結果

**最佳模型**：MAND-LSTM

**各疾病 AUC 表現** (MTL):
| 疾病 | 發生率 | AUC (MAND-LSTM) |
|------|--------|-----------------|
| 心臟病 | 24.6% | 0.8787 |
| 糖尿病 | 22.4% | 0.8912 |
| 中風 | 8.7% | 0.8625 |
| 高血壓 | 39.0% | 0.9346 |
| 無疾病 | 51.3% | - |

**參數效率優勢**：
| 模型類型 | 參數數量 |
|---------|---------|
| 4 個 STL 模型 | 1,608,468 |
| 1 個 MTL 模型 | 419,784 |
| **參數減少** | **僅需 1/4 參數量** ⭐ |

**關鍵特徵** (Permutation Feature Importance):
1. **Age**（年齡）⭐ 最重要預測因子（AUC 下降 0.0544）
2. Gender（性別）
3. Residential Area（居住地區）
4. Remote Area（偏遠地區）
5. Occupation（職業）

**Attention Score 分析** - 關鍵疾病關聯：
- **可修改風險因子**：
  - 純高膽固醇血症 (272.0)
  - 混合型高血脂 (272.2)
  - 其他未明示高血脂 (272.4)
- **多重慢性病共病**：
  - 痛風 (274.9)
  - 老年性白內障 (366.10)
  - 慢性肝炎 (571.40)
  - 慢性腎衰竭 (585)
  - 骨關節炎 (715.36, 715.90)
  - 腰薦椎脊椎病 (721.3)
- **新興風險因子**：
  - 焦慮症 (300.00)
  - 神經性憂鬱 (300.4)

### 輸出

- **同時預測 4 種疾病的風險**：
  - 糖尿病 (Diabetes)
  - 心臟病 (Heart Disease)
  - 中風 (Stroke)
  - 高血壓 (Hypertension)

### 提出解決方案

**MAND (Multi-task learning multimodal network)**

**創新點**：
1. ✅ **Multi-Task Learning (MTL)** - 同時預測多種慢性病
2. ✅ **Hard Parameter Sharing** - 共享隱藏層，捕捉疾病間相關性
3. ✅ **Word2Vec Embedding** - 將 ICD codes 轉換為語義向量
4. ✅ **Attention 機制 (MHSA)** - 識別關鍵疾病關聯
5. ✅ **參數效率高** - 僅需 STL 的 1/4 參數
6. ✅ **高可解釋性** - Attention Score 分析與文獻一致

### 研究貢獻

1. **證明 MTL 可行性**：MTL 效能與 STL 相當，部分甚至更優
2. **參數效率高**：MTL 僅需 STL 的 1/4 參數
3. **高可解釋性**：Attention Score 識別的風險因子與文獻一致
4. **模型穩健性**：即使 60% 醫療紀錄遮蔽，AUC 仍維持 0.88
5. **首次應用**：首次將 MTL 應用於台灣慢性病預測

### 研究限制

1. ⚠️ **資料不平衡**：中風發生率僅 8.7%，FNR 高達 70%+
2. ⚠️ **依賴敏感醫療紀錄**：需要過去 10 年完整醫療紀錄
3. ⚠️ **年齡依賴性強**：需進一步研究年輕族群風險因子
4. ⚠️ **Balanced Accuracy 60-80%**：不適合獨立診斷，僅適合輔助工具

### 與本研究的關聯

⭐⭐⭐ **中等關聯**（教授評估：因輸入資料差異大）

**相似點**：
- ✅ 同樣預測多種慢性病（Taiwan MTL: 4 種 | 本研究: 3 種三高）
- ✅ 都使用 Multi-Task Learning 架構
- ✅ 都使用台灣本土資料
- ✅ 都關注疾病間的共病關係
- ✅ **多疾病同時預測的論文較少** ⭐

**關鍵差異** ⚠️：
| 項目 | Taiwan MTL (2025) | 本研究 (RiskPrediction-3H) |
|------|-------------------|---------------------------|
| **輸入資料** | **ICD 診斷代碼** + 個人資訊 ❌ | **血液檢驗 + 生理測量** ✅ |
| **資料性質** | 過去疾病史（已發生） | 生理指標（連續值） |
| **預測疾病** | 糖尿病、高血壓、心臟病、中風 | 高血壓、高血糖、高血脂 |
| **時序特徵** | 10 年 ICD 序列 | T₁ → T₂ → T₃ 縱向變化 (Δ 特徵) |
| **追蹤時間** | 10 年紀錄 → 5 年預測 | 短期追蹤（3 次健檢）|
| **特徵工程** | Word2Vec Embedding | Δ 變化量特徵 |
| **可解釋性** | Attention Score 分析 | SHAP (計畫中) |

**教授觀點**：
- ⚠️ **輸入資料類型差異大**：ICD 診斷代碼 vs. 血液檢驗數值
- ⚠️ Taiwan MTL 依賴過去疾病史，本研究使用生理指標預測
- ⚠️ 特徵工程方法不可直接遷移（Word2Vec vs. Δ特徵）

**本研究觀點**：
- ✅ **多疾病同時預測的論文相對稀少**，Taiwan MTL 仍有重要參考價值
- ✅ MTL 架構設計思路可借鑑
- ✅ 可解釋性分析方法可參考

**可借鑑之處**（方法論層面）：
1. MTL 架構設計 (Hard Parameter Sharing)
2. Attention 機制識別疾病關聯的思路
3. 特徵重要性分析方法（Permutation Feature Importance）
4. 處理資料不平衡的策略
5. 可解釋性分析框架

**不可直接應用**：
- ❌ Word2Vec Embedding（僅適用於類別型 ICD codes）
- ❌ 10 年 ICD 序列處理方法
- ❌ 特定的特徵工程技術

### 相關文檔

- [meeting16_taiwan_mtl_presentation_outline.md](../meeting_notes/meeting16_taiwan_mtl_presentation_outline.md)
- [meeting16_taiwan_mtl_presentation_outline_10min.md](../meeting_notes/meeting16_taiwan_mtl_presentation_outline_10min.md)

---

## 兩篇論文的比較總結

### 相似點

| 項目 | 論文 15 (Liu 2024) | 論文 16 (Taiwan MTL 2025) |
|------|-------------------|--------------------------|
| **資料來源** | ✅ 台灣本土資料 | ✅ 台灣本土資料 |
| **研究類型** | ✅ 縱向追蹤研究 | ✅ 縱向追蹤研究 |
| **資料集狀態** | ❌ 不可下載 | ❌ 不可下載 |
| **目標疾病** | 糖尿病 | 糖尿病、高血壓、心臟病、中風 |
| **預測時間** | 10 年風險 | 5 年風險 |

### 差異點

| 項目 | 論文 15 (Liu 2024) | 論文 16 (Taiwan MTL 2025) |
|------|-------------------|--------------------------|
| **輸入資料** | 血液檢驗 + 生理測量 | ICD 診斷代碼 + 個人資訊 |
| **特徵數量** | 33 個臨床特徵 | 180 個 ICD 特徵 + 5 個個人資訊 |
| **預測目標** | 單一疾病（糖尿病） | 多疾病同時預測（4 種） |
| **模型架構** | 傳統 ML (LR, RF, XGBoost) | Multi-Task Learning (MAND) |
| **最佳模型** | XGBoost (AUC 0.93) | MAND-LSTM (AUC 0.87-0.93) |
| **可解釋性** | Feature Importance | Attention Score 分析 |
| **關鍵創新** | fT4 首次被發現為重要特徵 | MTL 參數僅需 STL 的 1/4 |

### 與本研究的關聯度比較

| 項目 | 論文 15 (Liu 2024) | 論文 16 (Taiwan MTL 2025) |
|------|-------------------|--------------------------|
| **資料類型相似度** | ⭐⭐⭐⭐⭐ (血液檢驗) | ⭐⭐ (ICD 代碼，差異大) |
| **預測目標相似度** | ⭐⭐⭐ (單一疾病) | ⭐⭐⭐⭐ (多疾病同時預測) |
| **方法論相似度** | ⭐⭐⭐ (傳統 ML) | ⭐⭐⭐⭐ (MTL 架構可借鑑) |
| **特徵工程相似度** | ⭐⭐⭐⭐ (臨床指標) | ⭐ (Word2Vec 不適用) |
| **總體關聯度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

**教授評估**：論文 15 (Liu 2024) 因資料類型相同（血液檢驗 + 生理測量），關聯度較高
**研究觀點**：論文 16 (Taiwan MTL 2025) 雖輸入資料差異大，但多疾病預測論文稀少，方法論仍有參考價值

---

## 對本研究的啟示

### 從論文 15 (Liu 2024) 學到：

1. ✅ **XGBoost 在台灣資料表現優異**（AUC 0.93）
2. ✅ **關鍵特徵選擇**：HbA1c, FBG, Weight, fT4, TG
3. ✅ **處理極度不平衡資料**的策略（92:1）
4. ✅ **性能基準**：AUC > 0.90 是可達成目標

### 從論文 16 (Taiwan MTL 2025) 學到：

**方法論層面**（可借鑑）：
1. ✅ **Multi-Task Learning 可行性**：MTL 效能與 STL 相當，值得嘗試
2. ✅ **參數效率**：共享層減少 75% 參數量的架構設計思路
3. ✅ **可解釋性框架**：Attention Score + Permutation Feature Importance 的分析流程
4. ✅ **時序模型優勢**：LSTM 能有效捕捉時間序列資訊
5. ✅ **處理資料不平衡**：針對低發生率疾病的策略

**局限性**（不可直接應用）：
- ⚠️ Word2Vec Embedding 僅適用於 ICD codes，無法用於連續數值
- ⚠️ 10 年 ICD 序列處理方法與健檢資料特性不同
- ⚠️ 教授評估：**輸入資料差異大**，降低直接參考價值

### 本研究的優勢與定位

**結合兩篇論文的優點**：
1. **血液檢驗 + 生理測量**（如論文 15）← 教授認為關聯度更高 ⭐
2. **多疾病同時預測**（如論文 16）← 此類研究較少，有創新性 ⭐
3. **MTL 架構**（如論文 16）← 方法論可借鑑
4. **縱向時序特徵 (Δ 特徵)**（本研究創新點）← 與論文 15 更契合

**本研究的獨特貢獻**：
- ✅ 使用**血液檢驗數值**預測多種疾病（結合論文 15 + 16 優勢）
- ✅ **Δ 特徵**捕捉生理指標變化（更貼近臨床實務）
- ✅ 短期健檢追蹤（更實用於預防醫學）
- ✅ 填補研究缺口：**血液檢驗 + 多疾病同時預測**的論文稀少

---

## 📌 快速導航

- 📂 [返回 Literature Notes 目錄](.)
- 📊 [查看文獻總覽索引](Literature_Master_Index.md)
- 📋 [查看 Q2 台灣文獻回顧](../research_plans/Q2_Taiwan_Literature_Review.md)
- 🎯 [查看 Meeting 17 準備計畫](../meeting_notes/Meeting_17_Preparation_Plan.md)

---

**文檔建立日期**：2025-11-13
**維護者**：紀伯喬
