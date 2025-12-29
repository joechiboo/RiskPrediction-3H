# Meeting 18 實驗進度簡報

> **報告人**：紀伯喬
> **日期**：[待定]
> **狀態**：大綱階段

---

## 簡報大綱（10 頁）

| Page | 標題 | 內容重點 |
|------|------|----------|
| 1 | 封面 | Meeting 18 實驗進度報告 |
| 2 | 本次進度總覽 | 4 項新實驗完成（消融 x2、SHAP、PySR） |
| 3 | 消融實驗：Δ 特徵 | Full vs No-Δ 效能比較 |
| 4 | 消融實驗：class_weight | balanced vs None 效能比較 |
| 5 | SHAP 分析：高血壓 | 特徵重要性、蜂群圖 |
| 6 | SHAP 分析：高血糖 & 高血脂 | 特徵重要性比較 |
| 7 | PySR 符號回歸 | 三種疾病的可解釋公式 |
| 8 | gplearn 參數調整 | 嘗試結果（仍失敗，已擱置） |
| 9 | 效能總整理 | 最佳模型 & AUC 彙整 |
| 10 | 下一步 | 5-fold CV、論文撰寫 |

---

## 與 Meeting 17 的差異

**Meeting 17 已報告**（不重複）：
- 6 種模型初步結果
- GP 失敗分析
- MTL 嘗試

**Meeting 18 新進度**：
- ✅ 消融實驗：Δ 特徵
- ✅ 消融實驗：class_weight
- ✅ SHAP 可解釋性分析
- ✅ PySR 符號回歸（新工具）
- ✅ gplearn 參數調整（最終擱置）

---

## 各頁內容草稿

### Page 1: 封面

```
Meeting 18 實驗進度報告

基於縱向健檢資料之三高風險預測

報告人：紀伯喬
日期：[待定]
```

---

### Page 2: 本次進度總覽

**完成的實驗**：

| # | 實驗 | 結果 |
|---|------|------|
| 1 | Δ 特徵消融 | Δ 對高血壓貢獻最大 |
| 2 | class_weight 消融 | balanced 對高血糖/高血脂改善明顯 |
| 3 | SHAP 分析 | 完成三種疾病特徵重要性 |
| 4 | PySR 符號回歸 | 產出可解釋公式 |

---

### Page 3: 消融實驗 - Δ 特徵

**實驗設計**：
- Full：T1 + T2 + Δ（26 特徵）
- No-Δ：T1 + T2（18 特徵）

**結果**（LR, class_weight=balanced）：

| 疾病 | Full AUC | No-Δ AUC | Δ 貢獻 |
|------|----------|----------|--------|
| 高血壓 | 0.749 | 0.720 | **+0.029** |
| 高血糖 | 0.931 | 0.925 | +0.006 |
| 高血脂 | 0.888 | 0.880 | +0.008 |

**結論**：Δ 特徵對高血壓預測貢獻最顯著

---

### Page 4: 消融實驗 - class_weight

**實驗設計**：
- balanced：自動調整權重
- None：不調整（原始分佈）

**結果**（LR）：

| 疾病 | balanced Recall | None Recall | 改善 |
|------|-----------------|-------------|------|
| 高血壓 | 68.3% | 45.0% | **+23.3%** |
| 高血糖 | 92.3% | 30.8% | **+61.5%** |
| 高血脂 | 87.5% | 43.1% | **+44.4%** |

**結論**：class_weight=balanced 大幅提升 Recall，對不平衡資料至關重要

---

### Page 5: SHAP 分析 - 高血壓

**Top 5 特徵重要性**：
1. SBP_T2（收縮壓 T2）
2. Age
3. DBP_T2（舒張壓 T2）
4. SBP_T1
5. Delta1_SBP

**蜂群圖**：[待插入圖片]

---

### Page 6: SHAP 分析 - 高血糖 & 高血脂

**高血糖 Top 5**：
1. FBG_T2
2. FBG_T1
3. Age
4. Delta1_FBG
5. BMI_T2

**高血脂 Top 5**：
1. TC_T2
2. TC_T1
3. Age
4. Delta1_TC
5. BMI_T2

---

### Page 7: PySR 符號回歸

**三種疾病的可解釋公式**：

| 疾病 | 公式 | AUC |
|------|------|-----|
| 高血壓 | `0.106 × exp(SBP_T1)` | 0.745 |
| 高血糖 | `0.116 × FBG_T2` | 0.943 |
| 高血脂 | `0.052 × exp(TC_T1)` | 0.801 |

**優勢**：完全透明、可直接臨床使用

---

### Page 8: gplearn 參數調整

**嘗試**：
- generations: 20 → 100
- tournament_size: 20 → 2

**結果**：
- 高血糖 AUC 0.938（超越 LR！）
- 高血壓、高血脂仍失敗

**決定**：擱置 gplearn，改用 PySR

---

### Page 9: 效能總整理

**最佳模型 by 疾病**：

| 疾病 | 最佳模型 | AUC | Recall |
|------|----------|-----|--------|
| 高血壓 | ANN | 0.803 | 59.8% |
| 高血糖 | LR | 0.931 | 92.3% |
| 高血脂 | LR | 0.888 | 87.5% |

**符號回歸（PySR）**：
- 高血糖 AUC 0.943（最高！）
- 完全可解釋

---

### Page 10: 下一步

1. **5-fold CV**：提高結果穩定性
2. **論文第三章**：研究方法撰寫
3. **論文第四章**：實驗結果整理
4. **特徵選擇實驗**（Optional）：前 N 個特徵

---

## 相關文件

- [09_Delta_Ablation_output.txt](../../results/09_Delta_Ablation_output.txt)
- [10_ClassWeight_Ablation_output.txt](../../results/10_ClassWeight_Ablation_output.txt)
- [08_SHAP_Analysis_output.txt](../../results/08_SHAP_Analysis_output.txt)
- [12_PySR_Experiment_output.txt](../../results/12_PySR_Experiment_output.txt)
- [11_GP_Parameter_Tuning_output.txt](../../results/11_GP_Parameter_Tuning_output.txt)
