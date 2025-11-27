# 預防醫學框架 (Prevention Medicine Framework)

## 核心理念

- **預防勝於治療** (Prevention is better than cure)
- **早期發現早期治療** (Early detection, early treatment)

這是公共衛生與預防醫學的經典口號，源自 **Leavell & Clark (1965)** 提出的三段五級預防架構。

## 三段五級預防 (Levels of Prevention)

| 階段 | 級別 | 目標 | 策略範例 |
|------|------|------|----------|
| **初段預防** (Primary) | 1. 促進健康 | 維持健康狀態 | 健康教育、均衡飲食、規律運動 |
| | 2. 特殊保護 | 預防特定疾病 | 疫苗接種、職業防護 |
| **次段預防** (Secondary) | 3. 早期診斷 | 及早發現疾病 | 健康檢查、篩檢計畫 |
| | 4. 適當治療 | 及時介入治療 | 早期治療、控制病情 |
| **末段預防** (Tertiary) | 5. 限制殘障與復健 | 減少後遺症 | 復健治療、長期照護 |

## 與本專案的關聯

本研究「3H 健康風險預測模型」屬於**次段預防**的範疇：

- **目標**：透過機器學習預測 3 年內的健康風險（Hospitalization、Health decline、ADL difficulty）
- **價值**：識別高風險族群，達到「早期發現」的目的，以利及早介入
- **理念**：在疾病發生前或惡化前進行預測，實踐「預防勝於治療」

## 臨床應用情境

以糖尿病為例：

| 階段 | 血糖狀態 | 可逆性 | 介入價值 |
|------|----------|--------|----------|
| 正常 | FBG < 100 mg/dL | - | 初段預防：維持健康 |
| **前驅糖尿病** | FBG 100-125 mg/dL | **可逆轉** | 次段預防：早期介入效益最大 |
| 糖尿病 | FBG >= 126 mg/dL | 難以逆轉 | 末段預防：控制與延緩併發症 |

> 台灣約三分之一成人有空腹血糖異常 (FBG >= 100)，凸顯早期篩檢與預測的重要性。

## 參考文獻

- Leavell, H. R., & Clark, E. G. (1965). *Preventive Medicine for the Doctor in His Community: An Epidemiologic Approach* (3rd ed.). McGraw-Hill.
