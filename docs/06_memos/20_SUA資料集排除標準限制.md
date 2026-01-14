# Memo 20：SUA 資料集排除標準限制

> **建立日期**：2026-01-14
> **來源**：Kanegae 2020 論文比較
> **狀態**：待確認 / 寫入 Limitations

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
| 高血壓診斷紀錄 | ❓ 不確定 | 可能只有血壓數值，無 ICD 診斷碼 |
| 藥物使用紀錄 | ❓ 不確定 | 健檢資料通常沒有用藥紀錄 |
| 病史問卷 | ❓ 不確定 | 是否有「過去是否診斷高血壓」的問卷 |

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
