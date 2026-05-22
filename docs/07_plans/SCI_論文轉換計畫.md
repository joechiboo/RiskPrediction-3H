# SCI 期刊論文轉換計畫

> **建立日期**：2026-03-17
> **前提**：碩士論文口試通過後再正式啟動，目前先規劃架構
> **待確認**：週五 Meeting 與教授討論目標期刊

---

## 研究賣點

1. **同時預測三高**（HTN + HG + DL）— 多數研究僅預測單一疾病
2. **縱向 Delta 特徵** — 驗證時間變化量對預測的貢獻
3. **PySR symbolic regression** — 產出可解釋數學公式，臨床可用性高
4. **公開資料集**（Dryad）— 完全可重現

---

## 論文結構對應

| 碩論章節 | SCI 論文段落 | 預估頁數 | 備註 |
|----------|------------|:--------:|------|
| Ch1 緒論 | Introduction | 1.5-2 | 精簡動機，強化 novelty |
| Ch2 文獻探討 | Related Work | 1 | 大幅精簡，只留直接相關 |
| Ch3 研究方法 | Methods | 2-3 | 合併 Ch4/Ch5 |
| Ch4 資料集 | ↑ (併入 Methods) | — | Dataset & Preprocessing |
| Ch5 特徵工程 | ↑ (併入 Methods) | — | Feature Engineering |
| Ch6 實驗結果 | Results | 3-4 | 核心，保留最佳模型比較 |
| Ch7 討論 | Discussion | 1.5-2 | 聚焦臨床意義 + 限制 |
| Ch8 結論 | Conclusion | 0.5 | |
| — | Abstract | 0.5 | 250-300 words |
| **合計** | | **12-15** | |

---

## 主要工作項目

| # | 項目 | 工作量 | 狀態 |
|:-:|------|:------:|:----:|
| 1 | 與教授確認目標期刊 | 低 | ⬜ 3/21 Meeting |
| 2 | 查目標期刊投稿規範（字數、格式、模板） | 低 | ⬜ |
| 3 | 擬定英文標題與 Abstract | 中 | ⬜ |
| 4 | Introduction 撰寫（精簡 Ch1 + novelty 論述） | 中 | ⬜ |
| 5 | Methods 整合（Ch3 + Ch4 + Ch5 精華） | 高 | ⬜ |
| 6 | Results 精選（Ch6 核心表格/圖表） | 高 | ⬜ |
| 7 | Discussion 改寫（聚焦貢獻 + 臨床意義） | 中 | ⬜ |
| 8 | 全文英文潤稿 | 高 | ⬜ |
| 9 | 圖表重製（符合期刊規範） | 中 | ⬜ |
| 10 | Cover letter 撰寫 | 低 | ⬜ |
| 11 | 投稿 | — | ⬜ |

---

## 可能的目標期刊（待與教授討論）

| 期刊 | IF 範圍 | 領域 | 備註 |
|------|:------:|------|------|
| BMC Medical Informatics | ~3-4 | 醫學資訊 | OA，接受度較高 |
| JMIR Medical Informatics | ~3-4 | 數位健康 | OA |
| Computers in Biology and Medicine | ~7 | 生醫計算 | 競爭較高 |
| Artificial Intelligence in Medicine | ~7 | AI + 醫學 | |
| PLOS ONE | ~3 | 綜合 | 接受度高，審稿快 |
| Applied Sciences (MDPI) | ~2-3 | 應用科學 | OA，審稿較快 |

> 以上僅為初步參考，實際投稿目標以教授建議為準。

---

## 可複用的素材

### 直接沿用
- 實驗數據、表格數值（Ch6）
- 模型超參數設定（Ch3）
- 資料集描述統計（Ch4）
- PySR 公式（Ch6 表6-10）
- SHAP / Feature Importance 圖（Ch6）

### 需要改寫
- 文獻回顧（中→英，大幅精簡）
- 研究動機（加強 gap statement）
- 討論（加強與 SOTA 比較）

### 需要新增
- Graphical abstract（部分期刊要求）
- Highlights（3-5 bullet points）
- Author contributions statement
- Data availability statement（Dryad DOI）
- Conflict of interest statement

---

## PySR 追加實驗方向（SCI 加分項）

> PySR symbolic regression 是本研究最有特色的部分，碩論中為基礎實驗，投 SCI 可深化。

| # | 方向 | 說明 | 預估工作量 |
|:-:|------|------|:--------:|
| 1 | **Pareto front 分析** | 系統化測試不同 complexity 上限，畫複雜度 vs 準確度曲線 | 中 |
| 2 | **與 black-box 對比** | 同樣特徵下，PySR 公式 vs XGBoost/MLP 的表現差異量化 | 低 |
| 3 | **Operator set 實驗** | 測試加入 log、exp、sqrt、abs 等運算子的效果 | 中 |
| 4 | **Cross-validation 穩定性** | 不同 fold 是否收斂到相似公式結構，驗證公式穩定度 | 中 |
| 5 | **臨床可用性評估** | 找醫師/檢驗師評估公式是否符合臨床直覺 | 高（需外部合作） |
| 6 | **公式簡化 + 視覺化** | 最佳公式的數學展開、決策邊界圖 | 低 |

> 方向 1-4 可用程式批次跑，口試後暑假執行；方向 5 需教授協助聯繫臨床端。

---

## 時程規劃（暫定）

```
7 月：口試通過
7-8 月：英文初稿撰寫
9 月：教授審閱 + 修改
10 月：英文潤稿 + 投稿
```

---

## Q2/Q3 期刊策略補充（2026-05-18 規劃）

**目標定位**：Q2 中段（IF 3-4），不衝 Q1。理由是降低方法學門檻、縮短準備時程、與在職論文延伸的合理目標相稱。

### 推薦目標期刊

| 期刊 | Quartile | IF | 為何適合 |
|------|---------|---|---------|
| **BMC Medical Informatics and Decision Making** | Q2 | ~3.5 | 接受單一 cohort + limitation 寫清楚 |
| **JMIR Medical Informatics** | Q2 | ~3-4 | 重視臨床應用價值 |
| **Diagnostics (MDPI)** | Q2 | ~3-4 | 審稿快（2-3 個月），對方法寬鬆 |
| **PLOS ONE** | Q2 | ~3 | 不要求 novelty，要求方法 sound |

### 避免

- IEEE TPAMI/TKDE 等純 CS 期刊（不收醫學應用）
- Computers in Biology and Medicine（Q1，會 demand 外部驗證）
- 已被 WoS 除名的期刊（如 Computational Intelligence and Neuroscience，2023 被踢出）

### Q2/Q3 門檻重新分類

**🔴 必補（不補會被打槍）**：
- 全部 AUC 加 **Bootstrap 95% CI**（1-2 天）
- **個人 Demo (n=1) 拿掉**（n=1 在 SCI 是大忌，0 工時）
- 英文寫作（AI 草稿 + 人工潤稿，2-3 週）
- 資料/程式可重現性（Dryad ✓ + GitHub repo）

**🟡 強烈建議補（加分）**：
- Calibration plot + Brier score（3-5 天）
- TRIPOD 簡化版對照表（2 天）
- **時間切分驗證**（同資料前後切，1 週）—— 替代外部驗證的折衷

**🟢 寫進 limitation 即可**：
- 外部驗證資料集 → future work
- 與 Framingham 等臨床評分比較 → limitation
- DCA / Subgroup analysis → future work
- DeLong test → 用 CI 重疊與否替代

### 壓縮時程（目標 Q2/Q3）

| 階段 | 時間 |
|------|------|
| 教授確認目標期刊 | 1 週 |
| 補必補項（CI + 時間切分驗證 + 刪 demo）| 2-3 週 |
| 英文撰寫 | 4-6 週 |
| 圖表重製 + 格式調整 | 1-2 週 |
| 教授內審 + 修改 | 2-3 週 |
| **送投** | **總計 2.5-3.5 個月** |
| 第一輪審稿 + Revision | 2-3 個月 |
| **接受** | **6-8 個月內可期** |

### MVP 最小可行版本

1. 刪掉 n=1 demo
2. AUC 加 Bootstrap CI
3. 補 Calibration plot
4. 主動承認外部驗證缺失（Limitations 一段）
5. 教授過稿 → 送 BMC MIDM 或 Diagnostics

---

## 期刊 Survey 比較表（待填，建議 5/26 那週做完）

> **產出目標**：帶到 Meeting 1 / 2 跟教授討論決定目標期刊

| 期刊 | IF | Quartile | Scope 契合 | OA 費用 (USD) | 審稿時間 | 接受率 | 格式 | 是否強要求外部驗證 | 近期類似論文 |
|------|:--:|:--:|:--:|:--:|:--:|:--:|------|:--:|:--:|
| BMC Medical Informatics and Decision Making | ~3.5 | Q2 | | | | | | | |
| JMIR Medical Informatics | ~3-4 | Q2 | | | | | | | |
| Diagnostics (MDPI) | ~3-4 | Q2 | | | | | | | |
| PLOS ONE | ~3 | Q2 | | | | | | | |
| Healthcare (MDPI) | ~2-3 | Q2-Q3 | | | | | | | |
| Applied Sciences (MDPI) | ~2-3 | Q2-Q3 | | | | | | | |

**估時**：2-3 小時（網站可查）

---

## Paper 閱讀方向（教授指示「繼續看」）

| 方向 | 用途 | 數量 | 優先 |
|------|------|:--:|:--:|
| **目標期刊近期收的「ML 三高」論文** | 學寫作風格、找引用、確認 fit | 3-5 篇 | 🔴 高 |
| **2024-2026 縱向健檢 ML 新論文** | 補充文獻、口試應答 | 2-3 篇 | 🟡 中 |
| **Calibration / external validation 方法論文** | SCI 階段補實驗用 | 1-2 篇 | 🟢 低 |

**閱讀紀錄請寫到** [docs/02_literature/](../02_literature/) 既有結構。

---

**維護者**：紀伯喬
