# Zhang et al. (2020) PLOS One — 視網膜照片預測三高深度解析

> **論文**：Prediction of hypertension, hyperglycemia and dyslipidemia from retinal fundus photographs via deep learning: A cross-sectional study of chronic diseases in central China
> **期刊**：PLOS One, 2020-05-14
> **作者**：Li Zhang, Mengya Yuan, Zhen An, et al.（共 13 位作者，通訊 Pan Li & Weidong Wu）
> **機構**：新鄉醫學院公共衛生學院（中國河南）
> **DOI**：[10.1371/journal.pone.0233166](https://doi.org/10.1371/journal.pone.0233166)
> **PDF 直連**：<https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0233166&type=printable>
> **PMC**：<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7224473/>
> **與本研究關聯度**：⭐⭐⭐⭐⭐（Tier 1 — **目前文獻中唯一同時預測三高的論文**，但 modality 不同）

---

## 一句話摘要

**使用 625 位中國河南鄉村居民的 1,222 張視網膜眼底照片，以 Inception-v3 深度學習同時預測高血壓（AUC 0.766）、高血糖（0.880）、高血脂（0.703），證實視網膜微血管影像可作為三高同時篩檢工具，但屬 cross-sectional 設計、樣本小、無外部驗證。**

---

## 基本資訊

| 項目 | 內容 |
| --- | --- |
| **研究主題** | 三高（HTN + HG + DL）同時預測 |
| **研究設計** | Cross-sectional（單時間點）|
| **資料來源** | 中國河南新鄉縣鄉村慢性病篩檢 |
| **時間範圍** | 2017 年 4-6 月（單次收集）|
| **樣本數** | 625 位、1,222 張照片（28 位僅單眼）|
| **年齡** | 54.70 ± 11.67 歲 |
| **慢性病自報率** | 55.86% |
| **Input** | 視網膜眼底照片（2736×1824 → 800×800）|
| **Method** | Inception-v3 transfer learning（ImageNet 預訓練）|
| **Framework** | TensorFlow |
| **Data split** | 80% train / 10% val / 10% test |
| **Regularization** | L2 + Augmentor（少數類 oversampling）|

---

## 疾病定義（cutoffs）

| 疾病 | 定義 |
| --- | --- |
| **高血壓** | SBP ≥ 130 OR DBP ≥ 85 mmHg OR 服降壓藥 |
| **高血糖** | 空腹血糖閾值（詳見 S1 Table）|
| **高血脂** | 三酸甘油酯閾值（詳見 S1 Table）|

⚠️ **注意**：HTN 用 130/85 cutoff（JNC 7 寬鬆版本），跟本研究用 140/90 不同 — 可能解釋為何 Zhang HTN AUC 較低（0.766 vs 本研究 0.743，但 cutoff 不同無法直接比）。

---

## 主要結果

### AUC 對照

| 疾病 | Zhang 2020 AUC | Accuracy | 本研究 (LR) AUC |
| --- | :---: | :---: | :---: |
| 高血糖 | **0.880** | 78.7% | **0.938** |
| 高血壓 | **0.766** | 68.8% | 0.721（最佳 RF 0.743）|
| 高血脂 | **0.703** | 66.7% | **0.867** |

→ **本研究在高血糖、高血脂明顯較強；高血壓 cutoff 不同無法直接比**

### 附加預測

CNN 同時預測（AUC > 0.7）：
- HCT（血容比）
- MCHC（紅血球平均血色素濃度）
- 年齡、BMI
- 心血管疾病風險因子

---

## 作者明確列出的限制

- 「相對小」的樣本（n=625）
- Cross-sectional 限制普及性
- **缺乏外部驗證**
- 建議未來用更大樣本、更多事件數研究

---

## 跟本研究的關鍵差異

| 維度 | Zhang 2020 | 本研究 |
| --- | --- | --- |
| **樣本數** | 625（小）| **6,056（10 倍）** |
| **設定** | 鄉村單一縣（河南）| 城市多年代（杭州 2010-2018）|
| **時間維度** | Cross-sectional 單時間點 | **Longitudinal 縱向 + Δ** |
| **Input modality** | 視網膜照片 | **健檢血液+生理指標** |
| **Method** | CNN（black-box）| **11 模型 + 符號回歸（可解釋）** |
| **可解釋性** | Saliency map | **LR 係數 + SHAP + 公式** |
| **Deployment cost** | 需眼底相機 | **一般健檢即可** |
| **疾病 cutoff** | HTN 130/85（寬鬆）| **HTN 140/90（標準）** |
| **AUC HG** | 0.880 | **0.938（更強）** |
| **AUC DL** | 0.703 | **0.867（更強）** |

→ **5 個明確差異維度**，reviewer 問「跟 Zhang 差在哪」可以答出來

---

## 對本研究 SCI 投稿的影響

### ❌ 不能再寫「首次」

論文 Ch1/Ch2/Ch7/Ch8 中所有「**首次三高同時預測**」用語要校正。

### ✅ 替代 framing

| 舊 | 新 |
| --- | --- |
| 「首次三高同時預測」 | 「**首次基於縱向健檢資料 + Δ + 11 模型整合的三高同時預測**」 |
| 「視覺化三高綜合風險」 | 「視覺化『**血液生理指標路徑**』下的三高綜合風險」 |

### ✅ Discussion 加段對比 Zhang 2020

建議在 Discussion / Related Work 加一段：

> "Zhang et al. (2020) demonstrated the feasibility of simultaneous three-condition prediction (hypertension, hyperglycemia, dyslipidemia) using retinal fundus photographs and CNN. However, their work was limited by (a) cross-sectional design without temporal feature, (b) small sample size (n=625), (c) lack of model interpretability, and (d) requirement of specialized fundus camera. Our study addresses these gaps by using longitudinal health checkup data (n=6,056, 8-year follow-up) with Δ features capturing temporal trajectories, achieving substantially higher AUC for hyperglycemia (0.938 vs 0.880) and dyslipidemia (0.867 vs 0.703), while providing interpretable models (LR, SHAP, symbolic regression formulas) deployable with standard blood test workflows."

### ✅ Cite 進論文

- 加入 Ch9 [編號 28 新增]
- Ch2 §2.1 文獻探討時提及
- Ch7 §討論時 differentiation 對比

---

## 對 SCI 期刊選擇的影響

| 期刊 | 是否合適 |
| --- | :---: |
| Diagnostics (MDPI) | ✓ 接受 cross-cohort 對比文章 |
| IEEE Access | ✓ scope 廣，方法論對比 OK |
| **IJMI**（Elsevier）| ✓✓ 健檢/EMR-based ML 是 scope 核心 |

→ Zhang 2020 在 PLOS One，**本研究投 IJMI 反而有利**（differentiation 強：clinical informatics vs general open access）

---

## 評分

| 維度 | 評分 |
| --- | :---: |
| **方法新穎度** | ⭐⭐⭐⭐（2020 視網膜深度學習）|
| **臨床實用性** | ⭐⭐（需眼底相機，部署成本高）|
| **方法論嚴謹** | ⭐⭐⭐（小樣本、無外部驗證）|
| **可解釋性** | ⭐（CNN black-box）|
| **跟本研究的威脅度** | ⭐⭐⭐（同 task 但 modality 差很多）|

---

## 待補

- [ ] PDF 下載閱讀全文（驗證 cutoff、確認 supplementary tables）
- [ ] 校正本論文 Ch1/Ch2/Ch7/Ch8 的「首次」用語
- [ ] Ch2 加入 Zhang 2020 引用
- [ ] Ch9 加入 reference

---

**建立日期**：2026-06-05
**維護者**：紀伯喬