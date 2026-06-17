# 論文補強 TODO

> **建立日期**：2026-06-08
> **用途**：追蹤論文 / 簡報 / SCI manuscript 待補強項目
> **緊急度判斷**：📕 6/28 印刷死線前 / 📘 SCI 投稿前（口試後）

---

## 📕 印刷死線前（6/28 前）— 可選

### 1. 共病性分析 補 Ch6 §6.7

**現況**：
- 共病/Phi 係數實驗**之前已做過**，結果發現「沒什麼關連」（Phi < 0.1）
- 但**沒寫進論文 Ch6 實驗結果章節**
- 論文 Ch7 §6 Discussion 提及 Phi < 0.1 作為 MTL 沒贏的原因 ①

**問題**：
- 口委可能問「Phi < 0.1 出自哪個實驗？」
- 目前只能答「Discussion 推測」，缺實驗章節支撐

**補做動作**（≈ 1.5 hr）：
- [ ] 找出舊共病分析 notebook
- [ ] 重跑 Phi 係數矩陣（HTN×HG / HG×DL / HTN×DL）
- [ ] 加 §6.7 共病分析章節（≈ 1 頁）
  - 表：Phi 係數矩陣 + 文獻共病率對比
  - 段落：低相關性的解釋（縱向 binary 預測場景）
  - 連結 §7.6 MTL Discussion
- [ ] 更新 §2.X 文獻定位表 2-2，「實驗涵蓋」欄位再加 1
- [ ] 簡報 Slide 18 把「Phi < 0.1（Discussion 推測）」改成「Phi < 0.1（§6.7 實驗證據）」

**影響面**：
- 論文 Ch2、Ch6、Ch7 互相對應更紮實
- 簡報 Slide 18 / Slide 19 surprise narrative 更有實驗證據

**是否一定要做**：
- ❌ 印刷前不一定要 — 口試時可用「Discussion 推測」回答
- ✅ 若想論文 publication-ready、強烈建議補

---

## 📘 SCI 投稿前（口試後）— 必補

### 2. Calibration 三件套

詳見 [Calibration_三件套.md](../05_concepts/Calibration_三件套.md)

- [ ] Reliability diagram（reliability_curve）
- [ ] Brier score（all models × 3 diseases）
- [ ] Hosmer-Lemeshow test
- [ ] 寫 §3.5 新章節
- [ ] 加 Figure 7（reliability diagram, 3 panels）

預估 4-5 天

### 3. Bootstrap 95% CI

所有 AUC 報告值加 95% CI（取代目前 ± SD）

- [ ] 重跑 5-fold CV + bootstrap（n=1000）
- [ ] 更新 Table 2、3
- [ ] 更新 Figure 3（加 error bars）

預估 1-2 天

### 4. 時間切分驗證（外部驗證替代）

- [ ] 用 2010-2014 train、2015-2018 test
- [ ] 對照 in-sample 結果
- [ ] 寫 §3.X 新章節

預估 1 週

### 5. 美國合成資料 negative finding 寫進 Discussion

- [ ] §4 Discussion 補一段
- [ ] Strong framing：distribution shift challenge

預估 0.5 天

### 6. Subgroup analysis（性別 / 年齡 / BMI）

- [ ] 5-fold CV per subgroup
- [ ] 加 Figure（subgroup forest plot）

預估 1-2 天

---

## 📘 SCI 補強 — 高 priority 但可選

### 7. LR 係數臨床解讀

把 SHAP「重要性」進階到「方向」（係數 + Odds Ratio）

- [ ] 算 LR 係數 → exp(β) = OR
- [ ] 加 Table：每疾病 Top 10 特徵 + OR
- [ ] Discussion 加一段「臨床決策可念給病人聽」

預估 0.5 天

### 8. AUC → 真實機率非線性偏差分析（深化 Calibration）

詳見 Slide 22 Calibration

- [ ] Reliability diagram per model class（樹 vs LR vs MLP）
- [ ] 展示 S 形 / 反 S 形 / 平移偏差
- [ ] Platt scaling vs Isotonic regression 對比

預估 1 天

---

## 對應 SCI manuscript（manuscript_v1.md）的開頭 todo list

- [ ] 作者列表 / ORCID / 通訊作者
- [ ] Bootstrap 95% CI（**項目 3**）
- [ ] Temporal-split validation（**項目 4**）
- [ ] Calibration plot + Brier score（**項目 2**）
- [ ] 圖表 re-export 期刊規格
- [ ] 專業英文潤稿
- [ ] TRIPOD checklist
- [ ] Cover letter

---

**最後更新**：2026-06-08
**維護者**：紀伯喬
