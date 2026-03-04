# Saito & Rehmsmeier (2015) PLoS ONE — PR 曲線 vs ROC 曲線深度解析

> **論文**：The Precision-Recall Plot Is More Informative than the ROC Plot When Evaluating Binary Classifiers on Imbalanced Datasets
> **期刊**：PLoS ONE, 2015; 10(3): e0118432
> **作者**：Takaya Saito, Marc Rehmsmeier
> **機構**：Computational Biology Unit, Department of Informatics, University of Bergen, Norway
> **DOI**：[10.1371/journal.pone.0118432](https://doi.org/10.1371/journal.pone.0118432)
> **PDF**：[Saito_PLOSONE_PRAUC_2015.pdf](../papers/Saito_PLOSONE_PRAUC_2015.pdf)
> **與本研究關聯度**：⭐⭐⭐⭐（Tier 2 — 為本研究同時報告 ROC-AUC 與 PR-AUC 的評估策略提供理論依據）

---

## 一句話摘要

**通過模擬實驗、文獻分析與 MiRFinder 再分析，系統證明 Precision-Recall (PRC) 曲線在不平衡資料集上比 ROC 曲線更具資訊量——ROC/CROC/CC 在平衡與不平衡間完全不變，唯 PRC 能反映類別比例變化對分類器實際表現的影響，且 66.7% 的不平衡資料研究僅用 ROC 而忽略 PRC。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **論文類型** | 方法論／比較研究（評估指標比較） |
| **核心貢獻** | 證明 PRC 在不平衡資料上比 ROC 更具資訊量 |
| **比較方法** | ROC、PRC、Concentrated ROC (CROC)、Cost Curves (CC) |
| **驗證方式** | 模擬實驗 + PubMed 文獻分析 + MiRFinder 再分析 |
| **模擬設定** | 平衡 1000:1000 vs 不平衡 1000:10000（1:10） |
| **文獻分析** | 58 篇 PubMed SVM + Genome-wide 研究 |
| **引用量** | >3,000 引用（評估指標領域高被引） |

---

## 理論背景

### 混淆矩陣基本指標（Table 1）

| 指標 | 公式 | 說明 |
|------|------|------|
| **ACC** | (TP + TN) / (TP + TN + FN + FP) | 準確率 |
| **ERR** | (FP + FN) / (TP + TN + FN + FP) | 錯誤率 |
| **SN / TPR / REC** | TP / (TP + FN) | 敏感度 / 召回率 |
| **SP** | TN / (TN + FP) | 特異度 |
| **FPR** | FP / (TN + FP) | 偽陽性率 |
| **PREC / PPV** | TP / (TP + FP) | 精確率 / 陽性預測值 |
| **MCC** | (TP·TN − FP·FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN)) | Matthews 相關係數 |
| **F₁** | 2·PREC·REC / (PREC + REC) | F1 分數 |

### 四種模型全域評估方法

| 方法 | X 軸 | Y 軸 | 基線 | 不平衡時 |
|------|------|------|------|----------|
| **ROC** | FPR | TPR | 對角線（AUC=0.5） | **不變** |
| **CROC** | f(FPR) 變換 | TPR | 變換後對角線 | **不變** |
| **CC** | PCF(+) | NE[C] | 最大三角 | **不變** |
| **PRC** | Recall | Precision | y = P/(P+N) | **改變** ✓ |

**關鍵差異**：只有 PRC 的基線隨類別比例移動（y = P/(P+N)），因此能反映不平衡對性能的真實影響。

---

## 核心發現

### 1. 基本指標在平衡 vs 不平衡下的行為（Table 2）

| 指標 | 平衡 (10P:10N) | 不平衡 (5P:15N) | 是否改變 |
|------|----------------|-----------------|----------|
| ACC | 0.60 | 0.60 | ✗ |
| ERR | 0.40 | 0.40 | ✗ |
| SN (TPR, REC) | 0.60 | 0.60 | ✗ |
| SP | 0.60 | 0.60 | ✗ |
| FPR | 0.40 | 0.40 | ✗ |
| **PREC (PPV)** | **0.60** | **0.33** | **✓** |
| **MCC** | **0.20** | **0.17** | **✓** |
| **F₀.₅** | **0.60** | **0.37** | **✓** |
| **F₁** | **0.60** | **0.43** | **✓** |
| **F₂** | **0.60** | **0.52** | **✓** |

**關鍵洞見**：ACC、SN、SP、FPR 在不平衡時完全不變 → 無法捕捉性能下降。**Precision 直接反映「正預測中有多少是對的」**，在不平衡時從 0.60 降到 0.33，最直覺。

### 2. 模擬實驗：五個性能等級 × 平衡/不平衡

**模擬設定**（Table 3）：

| 等級 | 正樣本分佈 | 負樣本分佈 |
|------|------------|------------|
| Random (Rand) | N(0, 1) | N(0, 1) |
| Poor ER (ER−) | Beta(4, 1) | Beta(1, 1) |
| Good ER (ER+) | Beta(1, 1) | Beta(1, 4) |
| Excellent (Excel) | N(3, 1) | N(0, 1) |
| Perfect (Perf) | 固定值 1 | 固定值 0 |

**平衡**：1000P : 1000N → **不平衡**：1000P : 10000N，迭代 1000 次

**核心結果**：
- **ROC、CROC、CC**：平衡 vs 不平衡的曲線**完全一致**，AUC 完全不變
- **PRC**：不平衡時曲線**明顯下移**，AUC 顯著降低
- ER− 在 ROC 上看起來不錯（FPR=0.16 時 TPR=0.5），但在不平衡情境下代表 **1600 個 FP**（而非平衡時的 160 個）——ROC 曲線無法顯示此差異
- ER+ vs ER− 的 AUC(ROC) 均為 0.8，ROC 無法區分早期檢索性能差異；PRC 可以

### 3. 文獻分析：ROC 的壓倒性使用

**PubMed 搜索**：58 篇 SVM + Genome-wide 研究

| 篩選條件 | 使用 ROC | 使用 PRC | 僅用單閾值指標 |
|----------|----------|----------|----------------|
| 全部 58 篇 | 35 (60.3%) | 4 (6.9%) | 其餘 |
| BS + IB（33 篇） | **22 (66.7%)** | **4 (12.1%)** | 10 |

**結論**：在不平衡資料集上，**66.7% 的研究使用 ROC 作為主要評估方法，僅 6-12% 使用 PRC** → 大量研究可能對分類器性能做了過度樂觀的解讀。

### 4. MiRFinder 再分析（Table 5）

| 工具 | T1 ROC | T1 PRC | T2 ROC | T2 PRC |
|------|--------|--------|--------|--------|
| **MiRFinder** | 0.992* | 0.945 | 0.772 | **0.106*** |
| **miPred** | 0.991 | 0.976* | 0.707 | 0.024 |
| **RNAmicro** | 0.858 | 0.559 | 0.886* | 0.054 |
| **ProMiR** | 0.974 | 0.801 | 0.711 | 0.035 |
| **RNAfold** | 0.964 | 0.670 | 0.706 | 0.015 |

*\* = 該列最佳*

**戲劇性對比**：
- T2 資料集（111P : 13444N，1:121 不平衡）上：
  - ROC-AUC 看起來「還不錯」（0.706–0.886）
  - **PRC-AUC 暴露真相**（0.015–0.106），幾乎所有工具近乎隨機
- RNAmicro 在 T2 上 AUC(ROC) = 0.886（最佳），但 AUC(PRC) = 0.054（接近隨機基線 0.008）

---

## PRC 的關鍵特性

### 為什麼 PRC 更有資訊量

1. **基線隨不平衡度移動**：y = P/(P+N)，不平衡越嚴重基線越低 → 直觀顯示分類難度
2. **Precision 直接可解釋**：「正預測中 X% 是正確的」→ 直接對應實際應用價值
3. **暴露 ROC 的盲點**：FPR 的分母是全部負樣本，當負樣本極多時，即使 FPR 看起來很低，FP 的絕對數量可能極大

### PRC vs ROC 插值差異

- **ROC**：使用線性插值
- **PRC**：必須使用**非線性插值** y = (TP_A + x) / {TP_A + x + FP_A + ((FP_B − FP_A)/(TP_B − TP_A))·x}
- 使用線性插值計算 PRC 會得到錯誤結果

### 推薦工具

| 工具 | 語言 | ROC | PRC | 非線性插值 |
|------|------|-----|-----|-----------|
| **ROCR** | R | ✓ | ✓ | ✗ |
| **AUCCalculator** | Java | ✓ | ✓ | ✓ |
| **CROC** | Python | ✓ | ✗ | - |
| **scikit-learn** | Python | ✓ | ✓ | ✓（後續版本） |

---

## 與本研究的比較

### 不平衡程度對照

| 項目 | Saito 模擬 | 本研究 |
|------|------------|--------|
| **不平衡比** | 1:10 (1000P:10000N) | 約 1:4 ~ 1:8（視疾病而定） |
| **正樣本數** | 1000 | ~700-1500（視疾病） |
| **處理方式** | 無（直接評估） | SMOTE 過採樣 |

### 本研究的評估策略對應

| Saito 建議 | 本研究做法 | 對應程度 |
|------------|-----------|----------|
| 應報告 PRC/PR-AUC | ✅ 報告 PR-AUC（與 ROC-AUC 並列） | 完全對應 |
| ROC 在不平衡時易誤導 | ✅ 使用 SMOTE 緩解 + 雙指標驗證 | 超越建議 |
| Precision 比 ACC 重要 | ✅ 報告 Precision、Recall、F1 | 完全對應 |
| 應注意 FPR 的分母效應 | ✅ 分析 Specificity 在不同疾病間的差異 | 部分對應 |

### 本研究可引用的理論支撐

1. **為何同時報告 ROC-AUC 與 PR-AUC**：Saito 證明 ROC-AUC 在不平衡時不變 → 僅 ROC-AUC 不足以評估
2. **為何使用 SMOTE**：Saito 展示不平衡對 Precision 的劇烈影響 → 需要類別平衡技術
3. **為何 PR-AUC 比 ROC-AUC 低**：本研究觀察到 PR-AUC 普遍低於 ROC-AUC → Saito 解釋這是正常現象（PRC 基線 = P/(P+N) << 0.5）
4. **為何不能只看 Accuracy**：Table 2 直接證明 ACC 在不平衡時完全無用

---

## 局限性

1. **模擬偏簡化**：僅用正態/Beta 分佈生成分數，未涵蓋真實 ML 模型的分數分佈特性
2. **不平衡比例固定**：僅測試 1:10，未系統探討不同不平衡程度的影響梯度
3. **文獻分析窄**：僅限 SVM + Genome-wide 研究，不代表所有 ML 應用領域
4. **未討論 SMOTE 等平衡技術**：只比較評估指標，未討論平衡技術對 ROC vs PRC 差異的影響
5. **未考慮校準**：未討論分類器機率校準對 PRC 的影響
6. **PRC 的 AUC 計算複雜**：需非線性插值，許多工具實作不正確
7. **發表年代**：2015 年，後續有 F1-AUC、Matthews 相關係數等替代方案被提出

---

## 各章節引用建議

| 章節 | 引用方式 | 具體內容 |
|------|----------|----------|
| **第二章（文獻回顧）** | 評估指標理論 | 說明 ROC-AUC vs PR-AUC 在不平衡資料上的差異 |
| **第五章（模型方法）** | 指標選擇依據 | 引用 Saito 作為同時報告 ROC-AUC 和 PR-AUC 的理論依據 |
| **第六章（結果）** | 結果解讀 | 解釋為何 PR-AUC 系統性低於 ROC-AUC |
| **第七章（討論）** | 方法論辯護 | 討論本研究採用雙指標策略的合理性，引 Table 2 說明單一指標不足 |

---

## 關鍵引文

> "The visual interpretability of ROC plots in the context of imbalanced datasets can be deceptive with respect to conclusions about the reliability of classification performance, owing to an intuitive but wrong interpretation of specificity."

> "PRC plots, on the other hand, can provide the viewer with an accurate prediction of future classification performance due to the fact that they evaluate the fraction of true positives among positive predictions."

> "Only precision, MCC, and the three Fβ scores vary between the two datasets, while the majority of measures stay unchanged."

> "PRC is the most informative and powerful plot for imbalanced cases and is able to explicitly reveal differences in early-retrieval performance."

> "The results of our study strongly recommend PRC plots as the most informative visual analysis tool."

> "Fig. 7D dramatically demonstrates that classifier performance deteriorates strongly under this test set... the PRC plot reveals the bitter truth."

---

## 延伸閱讀

- **He & Garcia (2009)** — 不平衡學習全面綜述（本研究 Ref [5]），涵蓋 SMOTE、成本敏感方法
- **Chawla et al. (2002)** — SMOTE 原始論文（本研究 Ref [7]）
- **Davis & Goadrich (2006)** — PRC 與 ROC 的一對一對應關係（本研究 Ref [26]），AUCCalculator 工具
- **Swets (1988)** — ROC 的經典理論基礎（本研究 Ref [24]）
