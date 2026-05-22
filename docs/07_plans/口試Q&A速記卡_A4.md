# 口試 Q&A 速記卡（A4 雙面版）

> 2026-05-18｜每題 ≤ 5 行｜路上反覆背｜詳版見 [口試Q&A答案卡.md](口試Q&A答案卡.md)

---

## 概念

**Q1. 泛化 (Generalization)** = 模型在沒見過資料上的表現能力。比喻：學生背考古題 vs 考新題型。

**Q2. CV 不防過擬合？** 對。CV 是**體溫計**（測過擬合）、不是**退燒藥**（防過擬合）。要防靠正則化/剪枝/early stopping。

**Q3. 過擬合分析怎麼做、為什麼？** 5-fold CV 同時記錄 Train/Test AUC 並列比較。三理由：① CV 不防過擬合 ② 支持選 LR（Gap ≤ 0.01 最穩） ③ 學術誠信。

**Q4. 為什麼選 LR 當主模型？** §6.1.5 表 6-5：樹模型 Gap 0.06-0.25 過擬合明顯；LR 泛化最穩。

---

## 方法選擇

**Q5. SHAP 為什麼用 XGBoost 不用 LR？** 分工：**XGBoost+SHAP 找特徵、LR 部署**。SHAP 在樹模型有 TreeExplainer 精確快速；LR 係數本就可解釋。

**Q6. Logistic vs Linear Regression** Logistic = **分類**（sigmoid 壓成機率）；Linear = 連續值回歸。本研究是分類用 Logistic。⚠️ **口語別說「線性回歸」**。係數解讀：exp(β) = Odds Ratio。

---

## 結果解釋

**Q7. 高血壓 AUC 為何比血糖血脂低？** 血壓是**瞬時訊號**（24h 變動 30-40 mmHg）；血糖經 8h 禁食標準化、血脂慢變化。ABPM 存在就是因為單次門診血壓不可靠。

**Q8. 全部都是 5-fold 平均嗎？** 主實驗是。例外：① PySR 表 6-17 單次跑 ② Slide 17 (§6.7.3) 用 StratifiedKFold（無 Group，每人 1 筆）。

---

## 評估指標

**Q9. 為什麼選 AUC 當主指標？** ① 閾值無關 ② 抗類別不平衡 ③ 跨研究可比較（表 2-1 全用 AUC） ④ TRIPOD 標準。詮釋：隨機抽正負樣本，模型把正排前的機率。

**Q10. Accuracy ≠ Recall！** Accuracy = 全部答對 % (TP+TN)/all；Recall = Sens = TP/(TP+FN) = 真病人抓到 %。陽性率 17% 時全預測健康，Accuracy 83% 但 **Recall = 0**——這就是不用 Accuracy 的理由。

**Q11. Sens / Spec / Precision 對照**
- **Sens = Recall**：TP/(TP+FN) — 真病人中抓出 %（篩檢核心）
- **Spec**：TN/(TN+FP) — 真健康中排除 %
- **Precision**：TP/(TP+FP) — 預測病人中真病人 %

**Q12. Sens 低有什麼影響？** 漏診率高。Slide 19 高血壓無處理 Sens 0.041 → 1000 病人只抓 41 個、漏 959 個；`class_weight='balanced'` 拉到 0.698。AUC 沒變，整體鑑別力沒損失。

---

## 限制與部署

**Q13. 個人 Demo 算效度分析？** **不算**，是個案 sanity check (n=1)。正式 calibration plot + 外部驗證屬 SCI 階段，§8 已列 limitation。

**Q14. 效度分析還差什麼？** 5 面向：鑑別力✅、校準度❌、外部效度❌、臨床效用(DCA)❌、面向效度⚠️。SCI 階段優先補 **calibration + 時間切分驗證**（替代外部）。

**Q15. UA 不是公費健檢項目，模型能用？** Slide 15 顯示 **Top 2 特徵已達 95% 全特徵效能**，這 2 個都是公費必含（SBP/FBG/TC）。UA 移除不影響核心可用性。

**Q16. Slide 11 寫 6 大實驗、論文寫 10 項？** Slide 11 是主敘事 6 項；另 4 項分到 Slide 15 (SHAP)、Slide 17 (各時間點)、Slide 21 (符號回歸)；資料篩選策略 §6.6 內含。

---

## 醫學基礎

**Q17. SBP / DBP** **SBP = Systolic = 收縮**壓（高，120）；**DBP = Diastolic = 舒張**壓（低，80）。記憶：**S**queeze = 收縮。論文高血壓主驅動是 SBP_Y-1/SBP_Y-2。

**Q18. 代糖 → 糖尿病？** 不直接升血糖 ✓，但可能透過 **腸道菌相改變、葡萄糖耐受性下降** 對代謝不利（Suez 2014 Nature；WHO 2023 反對；DGA 2025-2030 反對阿斯巴甜）。⚠️ **別講「胰島素過度分泌」**——人類證據弱。

---

**口試前一週至少跑 3 遍｜現場若忘詞抓粗體字記憶句**