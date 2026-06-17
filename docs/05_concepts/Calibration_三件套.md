# Calibration 校準度分析三件套

> **目的**：補強本研究 evaluation 框架，為 SCI 投稿準備
> **建立日期**：2026-06-08
> **對應簡報**：[口試演練_簡報.md](../04_meetings/口試演練_簡報.md) Slide 21

---

## 一、為什麼 Calibration 重要

### AUC 不夠用的情境

AUC 只看「排序能力」（高風險者是否被排在前面），**不看「絕對機率對不對」**。

兩個模型 AUC 都 0.9，但：

| 模型 | 預測「70%」的人實際發病率 | 判讀 |
| --- | :---: | --- |
| A | 68% | ✅ Well-calibrated |
| B | 35% | ⚠️ Overconfident |

→ B 模型對篩檢 ranking 一樣有用，但**不能告訴病人「你 70% 會發病」**

### 何時 Calibration 比 AUC 重要？

| 場景 | 關鍵指標 |
| --- | --- |
| 排序 + 排隊複檢 | AUC |
| 告訴病人「你 X% 會發病」 | **Calibration** |
| 保險定價 | **Calibration** |
| 臨床決策閾值（治療 yes/no） | AUC + Calibration |
| 個人化健康介入建議 | **Calibration** |

---

## 二、三件套詳解

### 1. Reliability Diagram（校準曲線）

**概念**：把預測機率分箱，看每箱內**實際發病率**。

```text
     1.0 ┤                                    ╱
         │                            ╱─ 模型 A（理想）
   實 0.7┤                       ╱
   際    │                  ╱         ╮
   發 0.5┤             ╱       模型 B（過度自信）
   病    │        ╱                 ╮
   率 0.3┤   ╱                    ╮
         │╱
       0 └────────────────────────────────
         0   0.3   0.5   0.7    1.0
               預測機率
```

**判讀**：

| 曲線位置 | 含義 |
| --- | --- |
| 線在對角線上 | ✅ 完美校準 |
| 線在對角線**下** | ⚠️ Overconfident（預測 70% 但實際只 50% 發病）|
| 線在對角線**上** | ⚠️ Underconfident（預測 30% 但實際 50% 發病）|
| 曲線扭曲 | 不同機率區間校準不一致 |

**怎麼做**：

```python
from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt

prob_true, prob_pred = calibration_curve(y_test, y_proba, n_bins=10)
plt.plot(prob_pred, prob_true, 'o-', label='Model')
plt.plot([0, 1], [0, 1], 'k--', label='Perfect calibration')
plt.xlabel('Predicted probability')
plt.ylabel('Observed frequency')
plt.legend()
```

---

### 2. Brier Score（布萊爾分數）

**公式**：

$$\text{Brier} = \frac{1}{N}\sum_{i=1}^{N}(p_i - y_i)^2$$

- $p_i$ = 模型預測機率
- $y_i$ = 實際標籤（0 或 1）
- 範圍 **0-1**，**越低越好**

**判讀基準**（醫學 ML 常見）：

| Brier | 判讀 |
| :---: | --- |
| < 0.10 | ✅ Excellent |
| 0.10 - 0.20 | ✅ Good |
| 0.20 - 0.25 | 🟡 Moderate |
| > 0.25 | ⚠️ Poor |

**可拆解性**（高階用法）：

$$\text{Brier} = \underbrace{\text{Reliability}}_{\text{校準偏差}} - \underbrace{\text{Resolution}}_{\text{鑑別力}} + \underbrace{\text{Uncertainty}}_{\text{baseline}}$$

→ 同時量化「校準度」+「鑑別力」+「baseline 機率」

**怎麼做**：

```python
from sklearn.metrics import brier_score_loss

brier = brier_score_loss(y_test, y_proba)
print(f"Brier score: {brier:.4f}")
```

---

### 3. Hosmer-Lemeshow Test（H-L 檢定）

**概念**：分箱後做 Chi-square 統計檢定，**檢定 H₀：預測與實際無差異**

**做法**：

1. 把樣本按預測機率排序，分成 G 箱（通常 G=10）
2. 每箱計算：
   - 預期病例數 $E_g = \sum p_i$
   - 實際病例數 $O_g$
3. 計算 H-L 統計量：

$$\hat{H} = \sum_{g=1}^{G} \frac{(O_g - E_g)^2}{E_g(1 - E_g/n_g)}$$

4. 比較 Chi-square 分布 (自由度 G-2)

**判讀**：

| p-value | 判讀 |
| :---: | --- |
| **p > 0.05** | ✅ 校準良好（接受 null = 無顯著差異）|
| p ≤ 0.05 | ⚠️ 校準差（拒絕 null = 預測與實際有差）|

**⚠️ 重要警告**：

- **樣本大時 p-value 容易顯著**（連微小差異都會被檢出）
- 不應單獨看 p-value，**配合 H-L statistic 值跟 reliability diagram 一起判讀**
- TRIPOD 2024 不再推薦 H-L 作為唯一指標，建議搭配視覺化 + Brier

**怎麼做**（Python 沒內建，需手動實作）：

```python
import numpy as np
from scipy.stats import chi2

def hosmer_lemeshow_test(y_true, y_proba, n_bins=10):
    # 按預測機率分箱
    bins = np.percentile(y_proba, np.linspace(0, 100, n_bins+1))
    bins[-1] += 1e-8  # 避免邊界
    bin_idx = np.digitize(y_proba, bins) - 1
    bin_idx = np.clip(bin_idx, 0, n_bins-1)
    
    obs = np.zeros(n_bins)
    exp = np.zeros(n_bins)
    n_per_bin = np.zeros(n_bins)
    for g in range(n_bins):
        mask = bin_idx == g
        if mask.sum() == 0: continue
        obs[g] = y_true[mask].sum()
        exp[g] = y_proba[mask].sum()
        n_per_bin[g] = mask.sum()
    
    # H-L statistic
    h_stat = np.sum((obs - exp)**2 / (exp * (1 - exp/n_per_bin) + 1e-8))
    p_val = 1 - chi2.cdf(h_stat, df=n_bins - 2)
    return h_stat, p_val
```

---

## 三、三件套互補性

| 工具 | 視覺化 | 單一指標 | 統計檢定 | 主要用途 |
| --- | :---: | :---: | :---: | --- |
| Reliability | ✅ | — | — | 看「哪個機率區間校準差」|
| Brier | — | ✅ | — | 量化整體校準 + 鑑別力 |
| H-L test | — | ✅ | ✅ | 統計顯著性檢定 |

→ **三個都報告才完整**，reviewer 不會有遺珠之憾

---

## 四、對本研究的應用

### LR 預期表現

- **理論上** LR 在 well-specified 時通常 well-calibrated
- **但** 本研究 §3.5 用 `class_weight='balanced'` → 改變 base rate → **calibration 會偏**
- 必須做 calibration check 才能告知

### 樹模型 vs LR 在 Calibration 上的差異

| 模型 | 典型行為 | 對應修正 |
| --- | --- | --- |
| LR | 通常 well-calibrated（class_weight 後例外）| 可能不需校正 |
| RF / XGBoost | 常 overconfident（極端機率太多）| Platt scaling 或 Isotonic regression |
| MLP | 常 underconfident（機率擠中段）| Platt scaling |

→ 預期 LR 表現會比樹模型好，呼應 Slide 11「真懂 vs 死背」narrative

---

## 五、SCI 補做計畫

### 工作量（1 週可完成）

| # | 步驟 | 工作量 |
| :---: | --- | :---: |
| 1 | 從 CV 結果重新跑 calibration curves（3 疾病 × 4 主要模型）| 0.5 天 |
| 2 | 計算 Brier score（各模型 × 3 疾病）| 0.5 天 |
| 3 | Hosmer-Lemeshow test | 0.5 天 |
| 4 | 寫 §3.5 新章節「Calibration analysis」| 1 天 |
| 5 | 加 Figure 7（reliability diagram, 3 panels）| 0.5 天 |
| 6 | Discussion 補一段對 calibration 的解釋 | 0.5 天 |
| 7 | 補 Reference（Steyerberg 2010 / Van Calster 2019）| 0.5 天 |

**總計 4-5 天**

### 在 manuscript 的位置

```text
manuscript_v1.md 現況：
§3.1 Model comparison
§3.2 Feature importance (SHAP)
§3.3 Delta-feature ablation
§3.4 Feature-count ablation
§3.5 Robustness: class imbalance and data filtering
§3.6 Longitudinal accumulation
§3.7 Multi-task vs single-task
§3.8 Symbolic regression

SCI 補完後新增：
§3.5 → §3.5b Calibration analysis （插在 robustness 後）
```

---

## 六、口試 Q&A 預備

| 問 | 答 |
| --- | --- |
| 為什麼 AUC 高的模型 calibration 可能差？ | AUC 只看順序、不看絕對值。LR 對閾值附近樣本可能系統性高估或低估，AUC 不變但機率歪掉 |
| Reliability diagram 怎麼看？ | X 軸是預測機率分箱（0-10%, 10-20%, ...），Y 軸是該箱內**實際**發病率。完美校準 = X=Y 對角線 |
| Brier score 怎麼判讀？ | 範圍 0-1、越低越好。≤ 0.1 算 excellent，≤ 0.2 算 good |
| Hosmer-Lemeshow 的 p-value 怎麼解讀？ | p > 0.05 表示校準良好。但**樣本大時 p 容易顯著**，要配合 H-L statistic 值跟視覺化一起看 |
| class_weight='balanced' 對 calibration 的影響？ | 改變了 base rate → 預測機率會系統性偏離真實發病率，**這就是為什麼必須做 calibration check** |
| 為什麼這個沒做？ | 學位論文時程內優先做核心 ML 比較（AUC + 11 模型 + 6 大實驗）。Calibration 屬於模型「對外部署」前的 evaluation，列為 SCI 必補項目 |

---

## 七、參考文獻（投稿時引用）

| 文獻 | 用途 |
| --- | --- |
| Hosmer & Lemeshow (1980) 原始論文 | H-L test 出處 |
| Steyerberg (2010) *Clinical Prediction Models* | 醫學 ML calibration 教科書 |
| Van Calster et al. (2019) "Calibration: the Achilles heel of predictive analytics" *BMC Medicine* | TRIPOD calibration framework |
| Brier (1950) "Verification of forecasts expressed in terms of probability" | Brier score 原始定義 |

---

**維護者**：紀伯喬
**建立日期**：2026-06-08
