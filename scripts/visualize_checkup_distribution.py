"""
檢查次數分佈視覺化腳本
生成長條圖展示受檢者的檢查次數分佈
"""

import matplotlib.pyplot as plt
import numpy as np

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 資料
checkup_counts = [3, 4, 5, 6]  # 簡化版，只顯示主要的
people_counts = [1754, 1776, 1935, 591]
percentages = [28.7, 29.0, 31.6, 9.7]

# 創建圖形
fig, ax = plt.subplots(figsize=(10, 6))

# 顏色設定 - 使用漸層藍色
colors = ['#2E86AB', '#4ECDC4', '#44AF69', '#95E77E']

# 繪製長條圖
bars = ax.bar(checkup_counts, people_counts, color=colors, edgecolor='black', linewidth=1.5)

# 在每個長條上方添加數值標籤
for bar, count, pct in zip(bars, people_counts, percentages):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{count}\n({pct}%)',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# 設定標題和標籤
ax.set_title('健檢次數分佈圖', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('檢查次數', fontsize=14)
ax.set_ylabel('人數', fontsize=14)

# 設定x軸刻度
ax.set_xticks(checkup_counts)
ax.set_xticklabels([f'{x}次' if x < 6 else '6次+' for x in checkup_counts])

# 設定y軸範圍
ax.set_ylim(0, max(people_counts) * 1.15)

# 添加格線
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# 添加統計資訊文字框
stats_text = f'總樣本數: 6,056人\n平均檢查次數: 4.2次\n核心樣本(3-5次): 89.3%'
ax.text(0.98, 0.97, stats_text,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 調整布局
plt.tight_layout()

# 儲存圖片
output_path = 'd:/Personal/Project/RiskPrediction-3H/figures/checkup_distribution.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"圖片已儲存至: {output_path}")

# 顯示圖片
plt.show()

# 創建詳細版本（包含所有檢查次數）
fig2, ax2 = plt.subplots(figsize=(12, 6))

# 完整資料
all_checkup_counts = [1, 2, 3, 4, 5, 6, 7, 8]
all_people_counts = [8, 55, 1754, 1776, 1935, 556, 31, 4]
all_percentages = [0.13, 0.90, 28.66, 29.02, 31.62, 9.09, 0.51, 0.07]

# 顏色設定 - 1-2次用灰色（已排除），3-5次用藍綠色系（主要），6-8次用淺色
colors_all = ['#CCCCCC', '#CCCCCC',  # 1-2次（已排除）
              '#2E86AB', '#4ECDC4', '#44AF69',  # 3-5次（主要）
              '#95E77E', '#F3DE8A', '#F7A072']  # 6-8次

# 繪製長條圖
bars2 = ax2.bar(all_checkup_counts, all_people_counts, color=colors_all,
                edgecolor='black', linewidth=1)

# 在每個長條上方添加數值標籤（只顯示大於100的）
for bar, count, pct in zip(bars2, all_people_counts, all_percentages):
    height = bar.get_height()
    if count > 100:
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=9)
    else:
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{count}',
                ha='center', va='bottom', fontsize=8)

# 標註已排除的資料
ax2.axvspan(0.5, 2.5, alpha=0.2, color='red', label='已排除(資料不足)')

# 設定標題和標籤
ax2.set_title('健檢次數分佈圖（完整版）', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('檢查次數', fontsize=14)
ax2.set_ylabel('人數', fontsize=14)

# 設定x軸刻度
ax2.set_xticks(all_checkup_counts)
ax2.set_xticklabels([f'{x}次' for x in all_checkup_counts])

# 設定y軸範圍
ax2.set_ylim(0, max(all_people_counts) * 1.15)

# 添加格線
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.set_axisbelow(True)

# 添加圖例
ax2.legend(loc='upper right')

# 添加統計資訊文字框
stats_text2 = (f'原始樣本: 6,119人\n'
               f'篩選後: 6,056人\n'
               f'平均次數: 4.2次\n'
               f'標準差: 1.0次\n'
               f'主力樣本(3-5次): 89.3%')
ax2.text(0.98, 0.85, stats_text2,
         transform=ax2.transAxes,
         fontsize=10,
         verticalalignment='top',
         horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# 調整布局
plt.tight_layout()

# 儲存詳細版圖片
output_path2 = 'd:/Personal/Project/RiskPrediction-3H/figures/checkup_distribution_detailed.png'
plt.savefig(output_path2, dpi=300, bbox_inches='tight')
print(f"詳細版圖片已儲存至: {output_path2}")

# 顯示圖片
plt.show()