# Memos 索引

> **最後更新**：2025-12-04
> **用途**：Meeting 討論重點、研究備忘、實驗設計

---

## 核心知識（必讀）

| 文件 | 主題 | 口試相關 |
|------|------|:--------:|
| [訓練集與測試集的切分方式](訓練集與測試集的切分方式.md) | 80/20 切分、分層抽樣、random_state=42 | ⭐ |
| [為何用T3而非T2作為預測目標](為何用T3而非T2作為預測目標.md) | Δ 特徵可用、避免資料洩漏、2年介入窗口 | ⭐ |

---

## 實驗設計（待執行）

| 文件 | 主題 | 優先級 |
|------|------|:------:|
| [class_weight消融實驗設計](class_weight消融實驗設計.md) | 有 vs 無 class_weight 比較 | 中 |
| [GP套件替代方案研究](GP套件替代方案研究.md) | PySR、DEAP、Operon 比較 | 中 |
| [時間點選擇與檢驗頻率的延伸研究](時間點選擇與檢驗頻率的延伸研究.md) | 前三次 vs 後三次、動態時間點 | 低 |

---

## 快速摘要

### 訓練集/測試集
- **比例**：80% 訓練（~4,845 人）/ 20% 測試（~1,211 人）
- **分層抽樣**：`stratify=y_hypertension`
- **隨機種子**：`random_state=42`

### 為何用 T3
- T2 作為目標 → 資料洩漏（Δ = T2 - T1，Y 也在 T2）
- T3 作為目標 → 真正的預測，給醫生 2 年介入時間

### class_weight
- LR、RF、SVM：`class_weight='balanced'`
- XGBoost：`scale_pos_weight = neg/pos`
- ANN：傳入 `fit(class_weight={...})`
- GP (gplearn)：❌ 不支援 → 失敗主因

### GP 替代方案
- **PySR**：最推薦，Julia 核心，支援 sample weights
- **DEAP**：高度客製化，需自訂適應度函數
- **Operon**：C++ 實作，效能最佳

---

## 待新增

- [ ] SHAP 可解釋性分析結果
- [ ] Δ 消融實驗結果（有 Δ vs 無 Δ）
- [ ] PR-AUC vs ROC-AUC 比較
- [ ] SMOTE 實驗結果

---

**相關資料夾**：
- [research_plans/](../research_plans/) - 研究計畫
- [meeting_notes/](../meeting_notes/) - 會議記錄
- [thesis_guidelines/](../thesis_guidelines/) - 學位論文規定
