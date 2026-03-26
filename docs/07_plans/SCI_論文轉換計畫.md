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

**維護者**：紀伯喬
