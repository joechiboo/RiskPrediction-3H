# Meeting 16 簡報大綱 - Taiwan MTL (2025) 論文閱讀

**論文標題**: Multitask learning multimodal network for chronic disease prediction
**期刊**: Scientific Reports (2025年5月) - **SCI 期刊** (IF ~4.0, Q2)
**DOI**: https://doi.org/10.1038/s41598-025-99554-z
**連結**: https://www.nature.com/articles/s41598-025-99554-z

**作者群**:
- **Hsinhan Tsai¹** (第一作者 & 通訊作者) - 台大資工系
- **Ta-Wei Yang²** - 台大網路與多媒體研究所
- **Tien-Yi Wu²** - 台大網路與多媒體研究所
- **Ya-Chi Tu¹,³** - 台大資工系 & 林口長庚醫院檢驗醫學科
- **Cheng-Lung Chen⁴** - 國家太空中心
- **Cheng-Fu Chou¹,²** (通訊作者) - 台大資工系 & 網路與多媒體研究所

**機構**:
1. 國立台灣大學 資訊工程學系
2. 國立台灣大學 網路與多媒體研究所
3. 林口長庚紀念醫院 檢驗醫學科
4. 國家太空中心

**研究特色**: 跨領域合作（資工 × 醫學 × 太空科技）

---

## 簡報架構（10 頁）

### Slide 1: 封面
- 論文標題：Multitask learning multimodal network for chronic disease prediction
- 期刊：Scientific Reports (2025年5月) - **SCI 期刊** (IF ~4.0)
- **作者群**：
  - **第一作者**: Hsinhan Tsai (台大資工系)
  - **通訊作者**: Cheng-Fu Chou (台大資工系)
  - **合作團隊**: 台大 × 長庚醫院 × 國家太空中心
- 報告人：紀伯喬
- 日期：Meeting 16

**亮點**: 跨領域合作（資工 × 臨床醫學 × 太空科技）

---

### Slide 2: 研究動機與背景

**問題點**：
- 傳統方法：預測不同疾病需要建立獨立模型
  - 耗時、耗計算資源
  - 未考慮疾病間相關性
- 慢性病之間存在強相關性
  - 西班牙：30% 多重慢性病盛行率
  - 馬德里：25% 的 14 歲以上人口患有多種慢性病

**研究目標**：
- 使用 Multi-Task Learning (MTL) 同時預測 4 種慢性病
- 捕捉疾病間相關性
- 減少計算資源與訓練時間
- 提高模型可解釋性

---

### Slide 3: 研究方法 - 問題定義

**預測任務**：
- 同時預測未來 5 年內發生以下疾病的風險：
  - 糖尿病 (Diabetes Mellitus)
  - 心臟病 (Heart Disease)
  - 中風 (Stroke)
  - 高血壓 (Hypertension)

**輸入資料**：
- **醫療紀錄**：過去 10 年的 ICD codes
- **個人資訊**：
  - 年齡 (Age)
  - 性別 (Gender)
  - 居住地區 (Residential Area)
  - 是否偏遠地區 (Remote Area)
  - 職業類別 (Occupation)

**資料來源**：
- 台灣 Health and Welfare Data Science Center (HWDC)
- 200 萬人隨機樣本的醫療紀錄

---

### Slide 4: 研究方法 - 資料處理

**特徵建構方式**：
- 每 2 個月選取最常出現的 3 個疾病（ICD codes）
- 10 年 × 每年 6 個雙月 × 3 個疾病 = **180 個疾病特徵**
- 缺失值使用 `<PAD>` token 填補

**ICD Code Embedding**：
- 使用 Word2Vec-based Skip-gram model
- 將 ICD codes 轉換為語義向量
- 相似疾病在特徵空間中距離更近

**資料集規模**：
- 總樣本數：555,124
- 訓練集：64% / 驗證集：16% / 測試集：20%

**疾病發生率**：
- 糖尿病：22.4%
- 心臟病：24.6%
- 中風：8.7%
- 高血壓：39.0%
- 無疾病組：51.3%

**排除條件**：
- 排除過去 10 年內已被診斷目標疾病的患者

---

### Slide 5: 研究方法 - 模型架構

**核心創新：Multi-Task Learning**
- **Single-Task Learning (STL)**：
  - 每個疾病獨立訓練一個模型
  - 4 種疾病需要 4 個模型

- **Multi-Task Learning (MTL)**：
  - 使用 Hard Parameter Sharing
  - 共享隱藏層（Shared Layers）
  - 各疾病有獨立預測層（Task-specific Layers）

**模型組成部分**：
1. **ICD Embedding Layer**：Word2Vec-based embedding
2. **ICD Extraction Module**（可選擇以下之一）：
   - Logistic Regression (LR)
   - Multi-Layer Perceptron (MLP)
   - Long Short-Term Memory (LSTM)
   - Multi-Head Self-Attention (MHSA)
3. **Numerical & Categorical Modules**：處理個人資訊
4. **Concatenation Layer**：整合所有特徵
5. **Prediction Layers**：4 個獨立輸出（MTL）或 1 個輸出（STL）

**對比模型**：
- CTR (Click-Through Rate) 模型：
  - Factorization Machine (FM)
  - Deep & Cross Network (DCN)

---

### Slide 6: 研究結果 - 模型效能比較

**主要發現**：
- ✅ MTL 與 STL 效能相當
- ✅ 部分 MTL 結果甚至優於 STL（說明疾病間存在共享資訊）
- ✅ **最佳模型**：MAND-LSTM（時間序列資訊重要）

**各疾病 AUC 表現**（以 MAND-LSTM 為例）：
| 疾病 | STL AUC | MTL AUC |
|------|---------|---------|
| 心臟病 | 0.8774 | 0.8787 |
| 糖尿病 | 0.8926 | 0.8912 |
| 中風 | 0.8700 | 0.8625 |
| 高血壓 | 0.9346 | 0.9346 |

**挑戰**：
- ⚠️ 高 False Negative Rate (FNR)
  - 心臟病、糖尿病、中風的 FNR 較高
  - 主因：資料不平衡（中風發生率僅 8.7%）
  - 模型傾向預測為陰性案例

**結論**：
- MTL 可在不犧牲效能的情況下同時預測多種疾病
- LSTM 模組能有效捕捉時序資訊

---

### Slide 7: 研究結果 - MTL 參數效率優勢

**參數數量比較**（以 MAND-MLP 為例）：

| 模型類型 | 參數數量 | 說明 |
|---------|---------|------|
| 單一 STL 模型 | 402,117 | 預測 1 種疾病 |
| 4 個 STL 模型 | 1,608,468 | 預測 4 種疾病需要 4 個獨立模型 |
| 1 個 MTL 模型 | 419,784 | 同時預測 4 種疾病 |

**MTL 優勢**：
- 僅需 **1/4 參數量**（相較於 4 個 STL 模型）
- 共享層可學習疾病間的共同特徵
- 有助於發現共病關係（comorbidities）

**實務應用價值**：
- ✅ 節省儲存空間
- ✅ 減少計算資源需求
- ✅ 適合部署於資源受限的邊緣裝置 (Edge devices)
- ✅ 降低模型載入延遲
- ✅ 適用於臨床決策支援系統 (Clinical Decision Support)

---

### Slide 8: 研究結果 - 特徵重要性分析

**個人資訊特徵重要性**（Permutation Feature Importance）：

| 特徵 | AUC (無擾動) | AUC (擾動後) | 下降幅度 | 重要性排名 |
|------|-------------|-------------|---------|-----------|
| 基準 | 0.8908 | - | - | - |
| **Age** | - | **0.8364** | **-0.0544** | **1** |
| Gender | - | 0.8899 | -0.0009 | 2 |
| Residential Area | - | 0.8890 | -0.0018 | 3 |
| Remote Area | - | 0.8907 | -0.0001 | 4 |
| Occupation | - | 0.8904 | -0.0004 | 5 |

**關鍵發現**：
- **年齡 (Age)** 是最重要的預測因子
  - 符合醫學文獻：年齡是慢性病的關鍵非可修改風險因子
  - 隨著年齡增長，生理功能下降，疾病風險顯著上升
- 性別、居住地區也有潛在影響（符合文獻）

**醫療紀錄重要性**（隨機遮蔽實驗）：

| 遮蔽比例 | Log Loss | AUC |
|---------|---------|-----|
| 0% (完整) | 0.2829 | 0.8918 |
| 50% | 0.2946 | 0.8856 |
| 60% | 0.3009 | 0.8825 |
| 100% (僅個人資訊) | 0.5348 | 0.8031 |

**結論**：
- 完整醫療紀錄 → AUC 提升 9 個百分點
- 即使遮蔽 60% 紀錄，AUC 僅下降約 1%
- 顯示模型具有**高穩健性**，能有效利用醫療紀錄間的交互作用

---

### Slide 9: 研究結果 - 風險因子與共病分析

**Attention Score 分析方法**：
- 選取各疾病預測分數最高的前 2000 名患者
- 分析 Self-Attention 機制中注意力分數最高的 ICD code pairs
- 識別模型認為最重要的疾病關聯

**發現的關鍵 ICD Codes**（分為三類）：

**1. 可修改風險因子 (Modifiable Risk Factors)**
- 純高膽固醇血症 (Pure hypercholesterolemia, 272.0)
- 混合型高血脂 (Mixed hyperlipidemia, 272.2)
- 其他未明示高血脂 (Other and unspecified hyperlipidemia, 272.4)
- ➡️ 與文獻一致：高血脂是三高的重要可修改風險因子

**2. 多重慢性病共病 (Multimorbidity)**
- 痛風 (Gout, unspecified, 274.9)
- 老年性白內障 (Senile cataract, unspecified, 366.10)
- 慢性肝炎 (Chronic hepatitis, unspecified, 571.40)
- 慢性腎衰竭 (Chronic renal failure, 585)
- 骨關節炎 - 下肢 (Osteoarthrosis, lower leg, 715.36)
- 骨關節炎 - 未明示部位 (Osteoarthrosis, unspecified site, 715.90)
- 腰薦椎脊椎病 (Lumbosacral spondylosis without myelopathy, 721.3)
- ➡️ 高齡患者常見的慢性病，文獻證實慢性病患者易發展多重慢性病

**3. 新興風險因子 (Emerging Factors)**
- 焦慮症 (Anxiety state, unspecified, 300.00)
- 神經性憂鬱 (Neurotic depression, 300.4)
- ➡️ 近期研究顯示：焦慮和憂鬱可能增加慢性病風險

**醫學意義**：
- 模型識別的風險因子與文獻高度一致
- 證明 MTL 模型具有良好的可解釋性
- 可協助臨床醫師識別高風險患者

---

### Slide 10: 研究貢獻、限制與未來方向

**研究貢獻** ✅
1. **證明 MTL 可行性**：
   - MTL 效能與 STL 相當，部分甚至更優
   - 同時預測多種慢性病，捕捉疾病間相關性

2. **Word2Vec Embedding 有效性**：
   - 比 Label Encoding 和 Multi-hot Encoding 更好
   - 能有效捕捉疾病間語義關聯

3. **參數效率高**：
   - MTL 僅需 STL 的 1/4 參數（4 個疾病）
   - 適合實際臨床應用與邊緣裝置部署

4. **高可解釋性**：
   - Attention Score 分析識別的風險因子與文獻一致
   - 年齡是最重要預測因子
   - 發現高血脂、多重慢性病、焦慮憂鬱的關聯

5. **模型穩健性**：
   - 即使 60% 醫療紀錄遮蔽，AUC 仍維持 0.88

---

**研究限制** ⚠️
1. **資料不平衡**：
   - 中風發生率僅 8.7% → FNR 高達 70%+
   - 模型傾向預測陰性案例

2. **依賴敏感醫療紀錄**：
   - 需要患者過去 10 年完整醫療紀錄
   - 隱私與資料取得可能是實際應用挑戰

3. **年齡依賴性強**：
   - 需要進一步研究年輕族群的風險因子
   - 有助於早期預防

4. **Balanced Accuracy 60-80%**：
   - 未達 90% 不適合獨立診斷
   - 但適合作為臨床決策輔助工具

---

**未來研究方向** 🔮

1. **簡化模型輸入**：
   - 模型蒸餾 (Model Distillation)
   - 僅需關鍵特徵，提升實用性

2. **年齡分層分析**：
   - 探索不同年齡層的風險因子
   - 提供個人化預測

3. **長期疾病預測**：
   - 使用 5 年紀錄預測 10 年風險
   - 實現更早期介入

4. **解決資料不平衡**：
   - 採樣技術 (Sampling)
   - 成本敏感學習 (Cost-sensitive Learning)

5. **年度疾病發生率預測**：
   - 預測每年疾病發生風險
   - 識別加速疾病發生的風險因子

---

## 視覺化建議

- **Slide 2**: 多重慢性病統計圖表、傳統 STL vs MTL 對比圖
- **Slide 4**: 資料處理流程圖、ICD code 時間序列示意圖
- **Slide 5**: MTL 模型架構圖（Figure 1b from paper）
- **Slide 6**: 各疾病 AUC 比較長條圖、STL vs MTL 對比表
- **Slide 7**: 參數數量對比圖（強調 1/4 優勢）
- **Slide 8**: 特徵重要性橫條圖、遮蔽實驗曲線圖
- **Slide 9**: Attention Score Heatmap、風險因子分類表
- **Slide 10**: 研究貢獻總結表、未來方向路線圖

---

## 時間分配建議（20 分鐘）

- Slide 1-2: 2 分鐘（開場與動機）
- Slide 3-5: 6 分鐘（研究方法）
- Slide 6-7: 5 分鐘（效能與效率）
- Slide 8-9: 5 分鐘（可解釋性分析）
- Slide 10: 2 分鐘（總結與展望）

---

## 重點強調

1. **MTL 創新性**：首次應用於台灣慢性病多任務預測
2. **參數效率**：1/4 參數達到相同效能
3. **可解釋性**：Attention Score 識別的風險因子符合醫學文獻
4. **與本研究的關聯**：
   - 本研究預測三高（高血壓、高血糖、高血脂）
   - Taiwan MTL 預測四病（糖尿病、高血壓、心臟病、中風）
   - 都使用 MTL + 時序特徵
   - 可參考其 ICD embedding 與 Attention 機制

---

## 參考資料

**論文位置**: `docs/references/s41598-025-99554-z.pdf`
**會議紀錄**: Meeting 15 - `docs/meeting_notes/meeting15_presentation_outline.md`
**任務清單**: `todo.md`
