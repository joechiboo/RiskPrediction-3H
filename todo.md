# TODO - 1/8 前完整 Meeting 準備

> ⚠️ **重要**：教授 1/8 後不在 10 天，之前需完成完整 Meeting

---

## 📖 Meeting 18 論文閱讀

- [x] 🔥🔥 #5 Taiwan MJ 高血壓預測（最優先）
- [ ] 🔥 #1 Dual 2025 前作
- [ ] 🔥 #9 SMOTE + SHAP Framework

---

## 🧪 核心實驗

- [x] SHAP 可解釋性分析
- [x] Δ 消融實驗（有 Δ vs 無 Δ）
- [x] class_weight 消融實驗
- [x] 混淆矩陣評估指標補充（教授建議）
- [x] GP 參數調整（generations=100, tournament=2）+ PySR 替代方案實驗
- [x] MTL 計算效益（訓練時間比較）

> ✅ **GP/PySR 結論**：非 bug，是方法本身限制。gplearn 不支援 class_weight，PySR 雖可學到公式但 AUC 仍低於 LR/XGBoost。建議：論文以 LR/XGBoost 為主，PySR 公式作為附錄補充。

---

## 🔬 待做實驗（Future Work）

**短期（Meeting 18 後）**：
- [ ] 5-fold CV：提高結果穩定性
- [ ] 特徵選擇實驗：前 N 個特徵是否足夠？（參考 Wang et al.）
- [ ] 不平衡處理方法消融實驗：比較 Baseline / class_weight / SMOTE / ADASYN / UnderSampling（驗證方法選擇依據，看 SMOTE 能否改善 RF）

**中期（論文撰寫期間）**：
- [ ] 健檢頻率分析：用年齡差（Age_T2 - Age_T1）分組比較 1/2/3 年間隔
- [ ] 外部驗證：尋找其他健檢資料集測試泛化能力

---

## 📚 文獻補充（三高關聯性）

> **背景**：目前 SHAP 分析顯示各疾病由「核心指標」主導（血壓→高血壓、血糖→糖尿病、TC→高血脂），但缺乏跨疾病關聯的文獻支持。

- [ ] 🔥 搜尋高血壓與糖尿病雙向關聯的文獻（流行病學研究）
- [ ] 分析 SHAP 結果中的跨疾病共享特徵（Age, BMI, UA, GFR）
- [ ] 補充代謝症候群共病性的文獻支持（為 MTL 架構提供理論依據）
- [ ] 論述「核心指標主導」vs「共享風險因子」現象（Discussion 章節素材）

**長期（未來展望）**：
- [ ] 健檢頻率優化實驗（需要有時間戳記的資料集）
- [ ] 虛擬健檢概念（參考 Wang et al.）

---

## ✍️ 論文撰寫

- [ ] 第三章：研究方法初稿

---

## 📊 Meeting 18 簡報

- [ ] 撰寫簡報 page 0 / 20
- [ ] 演練簡報
- [ ] 約教授 meeting

---

## 📝 完成的 Memos

01. ✅ 為何用T3而非T2作為預測目標
02. ✅ 時間點選擇與檢驗頻率的延伸研究
03. ✅ 訓練集與測試集的切分方式 ⭐
04. ✅ class_weight消融實驗設計
05. ✅ GP套件替代方案研究（PySR 推薦）
06. ✅ GP參數調整建議（教授建議）
07. ✅ MTL實驗保留與分析
08. ✅ 論文候選清單_從Dual2025延伸
09. ✅ 1月8日前完整Meeting準備
10. ✅ 混淆矩陣評估指標補充（教授建議）
11. ✅ MTL計算效益補充程式碼
12. ✅ Taiwan MJ 高血壓預測論文深度解析
13. ✅ class_weight與SMOTE比較
14. ✅ MTL真偽辨析
15. ✅ SHAP可解釋性分析
16. ✅ Delta消融實驗分析
17. ✅ ClassWeight消融實驗分析
18. ✅ GP符號回歸實驗總結（gplearn + PySR）
19. ✅ 統計顯著性檢驗方法（5-fold CV + Paired t-test）
