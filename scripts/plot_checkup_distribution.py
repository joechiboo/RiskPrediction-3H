"""
產生樣本健檢次數分佈圖
用於論文第三章
"""

import matplotlib.pyplot as plt
import numpy as np

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'DFKai-SB', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 資料
checkup_counts = [3, 4, 5, 6, 7, 8]
num_people = [1754, 1776, 1935, 556, 31, 4]
percentages = [28.96, 29.33, 31.95, 9.18, 0.51, 0.07]

# 建立圖表
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(checkup_counts, num_people, color='#4472C4', edgecolor='black', linewidth=0.5)

# 在每個柱子上方加上人數和百分比
for bar, count, pct in zip(bars, num_people, percentages):
    height = bar.get_height()
    ax.annotate(f'{count:,}\n({pct}%)',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9)

# 設定標籤
ax.set_xlabel('健檢次數', fontsize=12)
ax.set_ylabel('人數', fontsize=12)
ax.set_title('樣本健檢次數分佈（n = 6,056）', fontsize=14, fontweight='bold')

# 設定 x 軸刻度
ax.set_xticks(checkup_counts)
ax.set_xticklabels([str(x) for x in checkup_counts])

# 設定 y 軸範圍，留空間給標註
ax.set_ylim(0, max(num_people) * 1.2)

# 加入格線
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# 調整邊距
plt.tight_layout()

# 儲存圖片
output_path = 'd:/Personal/Project/RiskPrediction-3H/docs/thesis/figures/fig3-1_checkup_distribution.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f'圖片已儲存至: {output_path}')

plt.show()
