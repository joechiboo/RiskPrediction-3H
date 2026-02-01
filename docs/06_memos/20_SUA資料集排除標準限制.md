# Memo 20：SUA 資料集排除標準限制

> **建立日期**：2026-01-14
> **更新日期**：2026-01-19（新增 Y-2 患病比例分析）
> **來源**：Kanegae 2020 論文比較
> **狀態**：已確認 / 待寫入 Limitations

---

## 問題描述

Kanegae 2020 的排除標準：

| 排除條件 | 目的 |
|----------|------|
| 已有高血壓診斷 | 預測「新發」高血壓 |
| 正在使用降壓藥物 | 避免藥物干擾血壓值 |
| 數據缺失嚴重 | 資料品質 |

**我們的 SUA 資料集可能缺乏這些資訊。**

---

## SUA 資料集現況

| 資訊 | 是否有 | 說明 |
|------|--------|------|
| 血壓數值 | ✅ 有 | SBP, DBP |
| 診斷標籤 | ✅ 有 | hypertension, hyperglycemia, dyslipidemia（基於測量值閾值） |
| 藥物使用紀錄 | ❌ 無 | 健檢資料沒有用藥紀錄 |
| 病史問卷 | ❌ 無 | 無「過去是否診斷」的問卷 |

---

## 重要發現：首次健檢已排除患病者（2026-01-19 確認）

分析發現 **Times=1（首次健檢）幾乎沒有患病者**：

| Times | 高血壓 | 高血糖 | 高血脂 | 樣本數 |
|-------|--------|--------|--------|--------|
| **1** | **0.0%** | **0.0%** | **0.1%** | 6,056 |
| 2 | 19.1% | 4.5% | 8.1% | 6,056 |
| 3 | 16.7% | 5.5% | 6.0% | 6,056 |
| 4 | 19.7% | 5.5% | 7.7% | 4,302 |
| 5 | 21.7% | 6.7% | 12.4% | 2,526 |

**結論**：資料提供方已排除首次健檢就有三高的人，這是一個「baseline 健康」的 cohort。

---

## 滑動窗口後的 Y-2 患病比例

由於滑動窗口使 Y-2 不一定是 Times=1，仍有部分觀測值的 Y-2 為患病狀態：

| 疾病 | Y-2 患病數 | 佔比 | 排除後剩餘 |
|------|-----------|------|------------|
| 高血壓 | 1,320 | 9.8% | 12,194 (90.2%) |
| 高血糖 | 366 | 2.7% | 13,148 (97.3%) |
| 高血脂 | 548 | 4.1% | 12,966 (95.9%) |

### Y0 標籤組成分析

| 疾病 | Y0 患病總數 | 新發病例 | 持續患病（Y-2 就有） |
|------|------------|----------|---------------------|
| 高血壓 | 2,607 | 2,204 (**84.5%**) | 403 (15.5%) |
| 高血糖 | 801 | 606 (75.7%) | 195 (**24.3%**) |
| 高血脂 | 1,073 | 886 (82.6%) | 187 (17.4%) |

### 決定：不排除 Y-2 患病者

**理由**：
1. 資料量影響不大（最多損失 10%）
2. 需重跑所有實驗，工作量大
3. 論文定位可調整為「預測下次健檢異常風險」
4. 約 75-85% 的正標籤仍為真正的新發病例

---

## 潛在問題

### 1. 標籤污染

某人的情況：
- Y-2：SBP = 150（高血壓）
- Y-1：開始服藥，SBP = 130
- Y0：持續服藥，SBP = 125

我們的標籤判定：Y0 **正常**（SBP < 130）

實際情況：他**本來就是高血壓患者**，只是藥物控制中

### 2. 特徵干擾

- 服藥者的 `SBP_Y-1` 被藥物壓低
- 這個數值不代表真實的生理狀態
- 模型可能學到錯誤的特徵關係

### 3. 預測目標模糊

| 我們預測的 | 理想預測的 |
|------------|------------|
| 血壓數值是否超標 | **新發**高血壓 |
| 包含服藥控制者 | 排除已知患者 |

---

## 需要確認的事項

1. SUA 資料集是否有診斷碼（ICD）？
2. SUA 資料集是否有用藥紀錄？
3. SUA 資料集是否有病史問卷？
4. 資料提供方是否已做過排除處理？

---

## 論文 Limitations 建議文字

> **Limitation: Lack of medication and diagnosis history**
>
> Our dataset contains only clinical measurement values (e.g., blood pressure, blood glucose) without medication records or prior diagnosis history. Unlike Kanegae et al. (2020), who excluded individuals with existing hypertension diagnosis or antihypertensive medication use, we could not apply such exclusion criteria. This may lead to label contamination, where individuals with controlled hypertension (normal blood pressure due to medication) are incorrectly labeled as non-hypertensive. Future studies should incorporate medication and diagnosis records to more accurately predict new-onset disease.

---

## 對三高的影響

| 疾病 | 常見藥物 | 影響程度 |
|------|----------|----------|
| 高血壓 | 降壓藥（ACE inhibitors, ARBs, etc.） | **高** - 藥物可顯著降低血壓 |
| 高血糖 | 降糖藥、胰島素 | **高** - 藥物可顯著降低血糖 |
| 高血脂 | Statins | **中** - 藥物影響 TC, LDL |

**三種疾病都可能受到藥物影響，這是普遍性的限制。**

---

## 相關文件

- [Paper_Kanegae_Hypertension_2020.md](../02_literature/summaries/Paper_Kanegae_Hypertension_2020.md)
- [External_Validation_Analysis.md](../03_experiments/summaries/External_Validation_Analysis.md)
