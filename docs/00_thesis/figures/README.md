# 論文圖片索引

> **來源檔案**：`論文流程圖.pptx`
> **最後更新**：2026-01-22

## 圖片清單

| 圖號 | 檔名 | 說明 | PPT 頁數 |
|------|------|------|----------|
| 圖 3-1 | `fig3-1_research_framework.png` | 研究架構圖 | 第 1 頁 |
| 圖 3-2 | `fig3-1-1_timeline.png` | 研究時間軸設計 | 第 2 頁 |
| 圖 3-3 | `checkup_distribution.png` | 樣本健檢次數分佈 | Python 產生 |

## 匯出設定

從 PowerPoint 匯出 PNG：
1. 選擇投影片
2. 檔案 → 另存新檔 → PNG
3. 解析度：建議 150-300 DPI

## 更新記錄

### 2026-01-22 更新

#### 圖 3-1 研究架構圖
- [x] 「80/20 分層抽樣」→「5-Fold StratifiedGroupKFold」
- [x] 「資料前處理」加入「滑動窗口法」
- [x] 模型列表加入「DT」
- [x] 時間點命名改為 Y-2, Y-1, Y0

#### 圖 3-2 時間軸設計
- [x] T1/T2/T3 → Y-2/Y-1/Y0
- [x] 簡化輸入特徵說明

## Python 產生的圖片

`checkup_distribution.png` 可用以下腳本重新產生：
```bash
python scripts/generate_checkup_chart.py
```