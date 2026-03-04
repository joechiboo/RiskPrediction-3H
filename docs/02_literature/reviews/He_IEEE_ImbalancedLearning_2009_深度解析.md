# He & Garcia (2009) IEEE TKDE — 不平衡資料學習綜述深度解析

> **論文**：Learning from Imbalanced Data
> **期刊**：IEEE Transactions on Knowledge and Data Engineering, 2009; 21(9): 1263–1284
> **作者**：Haibo He, Edwardo A. Garcia
> **機構**：Stevens Institute of Technology, Hoboken, NJ
> **DOI**：[10.1109/TKDE.2008.239](https://doi.org/10.1109/TKDE.2008.239)
> **PDF**：[He_IEEE_Imbalanced_2009.pdf](../papers/He_IEEE_Imbalanced_2009.pdf)
> **與本研究關聯度**：⭐⭐⭐（Tier 2 — 不平衡學習的經典綜述，支撐本研究 SMOTE 使用的理論基礎）

---

## 一句話摘要

**全面回顧不平衡資料學習的問題本質、四大類解決方案（採樣法、成本敏感法、核方法、主動學習）和評估指標（Accuracy→F-measure→G-mean→ROC→PR 曲線→Cost 曲線），強調不平衡度並非唯一因素，資料複雜度（類別重疊、小分離群、維度災難）才是分類退化的根本原因。**

---

## 基本資訊

| 項目 | 內容 |
|------|------|
| **論文類型** | 綜述論文（Survey / Review） |
| **研究主題** | 不平衡資料學習（Imbalanced Learning） |
| **涵蓋範圍** | 問題本質 + 解決方案 + 評估指標 + 未來方向 |
| **引用量** | 截至 2025 年為不平衡學習領域最高被引論文之一（>10,000 引用） |
| **關鍵字** | Imbalanced learning, sampling methods, cost-sensitive learning, kernel-based learning, active learning, assessment metrics |

---

## 問題本質（Section 2）

### 不平衡的類型

| 類型 | 說明 | 例子 |
|------|------|------|
| **類間不平衡（Between-class）** | 一個類別嚴重多於另一個 | 100:1, 1000:1, 10000:1 |
| **類內不平衡（Within-class）** | 同一類別中子概念分佈不均 | 多數概念 vs 稀有子概念 |
| **相對不平衡（Relative）** | 少數類並非稀有，但相對於多數類人數少 | 2000 vs 20000 |
| **稀有實例不平衡** | 少數類本身數量極少 | 10 vs 10000 |

### 關鍵洞察：不平衡度 ≠ 分類困難度

**資料複雜度才是根本因素**：
1. **類別重疊（Overlapping）**：類別邊界模糊，分類器無法清晰區分
2. **小分離群（Small Disjuncts）**：少數類的子概念被分成多個小群組，學習規則過於具體
3. **缺乏代表性資料**：少數類的某些子概念樣本極少
4. **高維度 + 小樣本**：特徵空間大但訓練資料少，導致過擬合

> 簡單的不平衡資料（類別分離清楚）不一定難以學習；複雜的不平衡資料（重疊 + 小分離群 + 稀有實例）才真正困難

### 以決策樹為例的直接影響

1. 遞迴分割使少數類樣本越來越少 → 葉節點信心估計弱
2. 依賴特徵空間交叉的概念被稀疏性淹沒 → 學不到
3. 最終規則偏向多數類 → 少數類 recall 極低

---

## 四大類解決方案（Section 3）

### 3.1 採樣方法（Sampling Methods）

#### 基礎方法

| 方法 | 原理 | 優點 | 缺點 |
|------|------|------|------|
| **隨機欠採樣** | 刪除多數類樣本 | 簡單、減少訓練時間 | **資訊損失**（可能刪除重要概念） |
| **隨機過採樣** | 複製少數類樣本 | 簡單、保留所有資訊 | **過擬合**（"tied" 問題，規則過於具體） |

#### 進階採樣

| 方法 | 原理 | 特點 |
|------|------|------|
| **EasyEnsemble** | 從多數類獨立抽取多個子集 + 集成 | 無監督探索多數類 |
| **BalanceCascade** | 級聯式去除已被正確分類的多數類樣本 | 有監督逐步精煉 |
| **NearMiss-1/2/3** | 基於 KNN 距離的智慧欠採樣 | 保留邊界附近樣本 |
| **SMOTE** | 在少數類樣本間內插合成新樣本 | **本研究使用** |
| **Borderline-SMOTE** | 僅對邊界少數類樣本生成合成資料 | 聚焦最易誤分的區域 |
| **ADASYN** | 根據 KNN 中多數類比例自適應生成合成數量 | 困難樣本生成更多 |
| **SMOTE + Tomek Links** | SMOTE 後清除類別重疊的 Tomek 連結 | 更清晰的類別邊界 |
| **SMOTE + ENN** | SMOTE 後用 Edited Nearest Neighbor 清除 | Wilson editing 清理 |
| **CBO** | K-means 聚類後分別過採樣各群組 | 解決類內不平衡 |

#### SMOTE 的核心公式

對每個少數類樣本 $x_i$，從其 K 近鄰中隨機選一個 $\hat{x}_i$，生成：

$$x_{new} = x_i + (\ \hat{x}_i - x_i) \times \delta, \quad \delta \in [0,1]$$

**SMOTE 的已知缺點**：
- **過度泛化（Over-generalization）**：為每個少數樣本生成相同數量的合成樣本，不考慮鄰域
- **增加類別重疊**：合成樣本可能落入多數類區域
- **對雜訊敏感**：雜訊樣本也會被擴增

#### 採樣 + 集成整合

| 方法 | 組合 | 特點 |
|------|------|------|
| **SMOTEBoost** | SMOTE + AdaBoost.M2 | 每次提升迭代中加入合成採樣 |
| **DataBoost-IM** | 針對難學樣本合成 + AdaBoost.M1 | 根據錯誤率動態生成 |
| **JOUS-Boost** | 過/欠採樣 + 抖動(jittering) + Boosting | 簡單擾動打破 ties |

### 3.2 成本敏感方法（Cost-Sensitive Methods）

#### 風險最小化框架

分類的條件風險：
$$R(j|x) = \sum_i P(i|x) \cdot C(i,j)$$

其中 $C(i,j)$ 為將類 $i$ 預測為類 $j$ 的成本

#### 三種實現方式

| 方式 | 說明 |
|------|------|
| **成本敏感加權** | 用誤分類成本重新加權資料/分佈 |
| **集成 Metacost** | 將成本整合到集成方法的組合機制 |
| **算法內嵌** | 直接修改學習算法的損失函數/結構 |

#### 代表性方法

- **AdaC1/C2/C3**：將成本因子以不同方式嵌入 AdaBoost 的權重更新
- **成本敏感決策樹**：調整分割準則（DKM > Gini/Entropy）、決策閾值、剪枝策略
- **成本敏感神經網路**：修改輸出層、學習率、或用期望成本最小化替代 MSE

### 3.3 核方法 + 主動學習

- **SVM + 不平衡**：軟邊界最大化偏向多數類 → 邊界偏移
- **GSVM-RU**：用 SVM 逐步辨識和移除多數類支撐向量 → 智慧欠採樣
- **核修改法（KBA, CBA）**：修改核矩陣或邊界對齊
- **主動學習**：選擇最有資訊量的樣本（邊界附近），逐步重訓 SVM

### 3.4 其他方法

- **單類學習/新奇偵測**：僅用目標類建模（適合極端不平衡）
- **Mahalanobis-Taguchi System**：用單類資料建立連續測量尺度
- **多任務學習**：共享表徵擴大有效訓練規模

---

## 評估指標（Section 4）

### 為什麼 Accuracy 不適用

以 99:1 不平衡為例：
- 全部預測為多數類 → Accuracy = 99%
- 但少數類 Recall = 0%（完全漏診）

**根本問題**：Accuracy 同時使用混淆矩陣兩欄資訊，對類別分佈敏感

### 推薦指標層級

| 層級 | 指標 | 公式/說明 | 特點 |
|------|------|---------|------|
| 1 | **Precision** | TP/(TP+FP) | 精確度，對分佈敏感 |
| 1 | **Recall** | TP/(TP+FN) | 召回率，**不受分佈影響** |
| 2 | **F-measure** | (1+β²)·P·R/(β²·P+R) | 綜合，仍對分佈敏感 |
| 2 | **G-mean** | √(Recall · TNR) | 正負類準確率的幾何平均 |
| 3 | **ROC 曲線 + AUC** | TPR vs FPR | 跨閾值全面比較，**對分佈不敏感** |
| 4 | **PR 曲線 + PR-AUC** | Precision vs Recall | 高度不平衡時比 ROC 更informative |
| 5 | **Cost 曲線** | 歸一化期望成本 vs 操作點 | 視覺化不同成本條件下的表現 |

### ROC 的局限（→ PR 曲線的優勢）

- 當負類極多時（Nc >> Pc），FP 的大幅增加只造成 FPR 微小變化
- ROC 可能給出**過於樂觀的評估**
- **PR 曲線在高度不平衡時更具鑑別力**

---

## 與本研究的關聯

### 本研究的不平衡狀況

本研究的三個預測目標不平衡程度不同：
- 高血壓新發率：~25–40%（中度不平衡）
- 高血糖新發率：~15–25%（中度不平衡）
- 血脂異常新發率：~20–35%（中度不平衡）

### 本研究採用的策略（對應 He & Garcia 的分類）

| He & Garcia 方法類別 | 本研究使用 |
|---------------------|-----------|
| SMOTE（合成少數類過採樣） | ✅ 主要不平衡處理方法 |
| 成本敏感方法 | ❌ 未使用（可作為 future work） |
| 核方法 (SVM) | ✅ SVM 是 8 模型之一 |
| 評估指標：AUC | ✅ 主要評估指標 |
| 評估指標：F1 | ✅ 輔助指標 |
| 評估指標：PR-AUC | ✅ 輔助指標（引用 Saito 2015） |

### 本研究可引用的論證

1. **SMOTE 的理論基礎**：He & Garcia 全面回顧了 SMOTE 及其變體，支持本研究使用 SMOTE 的合理性
2. **Accuracy 的不適用性**：引用此文說明為何本研究選用 AUC/F1/PR-AUC 而非 Accuracy
3. **資料複雜度 > 不平衡度**：即使本研究的不平衡不算極端，類別重疊和小分離群仍可能影響學習
4. **採樣 vs 成本敏感**：討論為何選擇 SMOTE 而非成本敏感方法
5. **ROC 的局限→PR 曲線**：引用此文（及 Saito 2015）支持本研究同時報告 ROC-AUC 和 PR-AUC

### 可引用的理論框架

- **Between-class vs Within-class 不平衡**：解釋本研究資料的不平衡特性
- **SMOTE 的過度泛化風險**：作為 limitation 討論（Borderline-SMOTE 或 ADASYN 可能更好）
- **集成 + 採樣的組合優勢**：支持本研究使用 RF/XGBoost（本身為集成方法）+ SMOTE 的設計

---

## 研究限制與評析

1. **發表於 2009 年**：未涵蓋 2010 年後的進展（如 GAN-based 過採樣、深度學習不平衡處理）
2. **主要討論二分類**：多類不平衡僅簡要提及
3. **未提供 benchmark 實驗**：僅為綜述，無新實驗比較
4. **SMOTE 變體的演進**：2009 年後出現更多改良版（SMOTE-NC、SVM-SMOTE、K-Means-SMOTE 等）
5. **未討論深度學習場景**：CNN/RNN/Transformer 的不平衡處理（focal loss、class-weighted loss 等）

---

## 對本論文寫作的引用建議

### 第三章（研究方法）
- 引用 He & Garcia (2009) 作為使用 SMOTE 的理論依據
- 簡述不平衡學習的四大類方法，說明本研究選擇 SMOTE 的原因
- 引用 Accuracy 不適用的論證，說明為何使用 AUC/F1/PR-AUC

### 第七章（討論）
- 討論 SMOTE 的已知限制（過度泛化、類別重疊增加），作為本研究的 limitation
- 引用「資料複雜度 > 不平衡度」的觀點，分析本研究資料的特性
- 建議未來可嘗試 Borderline-SMOTE、ADASYN 或成本敏感方法

---

## 關鍵引述

> "The fundamental issue with the imbalanced learning problem is the ability of imbalanced data to significantly compromise the performance of most standard learning algorithms."

> "The degree of imbalance is not the only factor that hinders learning. As it turns out, data set complexity is the primary determining factor of classification deterioration, which, in turn, is amplified by the addition of a relative imbalance."

> "In the case of highly skewed data sets, it is observed that the ROC curve may provide an overly optimistic view of an algorithm's performance. Under such situations, the PR curves can provide a more informative representation of performance assessment."

> "Since oversampling simply appends replicated data to the original data set, multiple instances of certain examples become 'tied,' leading to overfitting."