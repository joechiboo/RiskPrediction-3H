"""
生成完整檢查次數分佈長條圖 (1-8次)
輸出到 experiments 資料夾
"""

import matplotlib.pyplot as plt
import matplotlib
import os

# 設定字體，避免中文顯示問題
matplotlib.rcParams['font.family'] = ['DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 完整資料 (1-8次)
checkup_counts = ['1', '2', '3', '4', '5', '6', '7', '8']
people_counts = [8, 55, 1754, 1776, 1935, 556, 31, 4]
percentages = [0.13, 0.90, 28.66, 29.02, 31.62, 9.09, 0.51, 0.07]

# 創建圖形
fig, ax = plt.subplots(figsize=(10, 6))

# 顏色設定 - 1-2次用灰色（已排除），3-5次用藍色系（主要），6-8次用淺藍色
colors = ['#d3d3d3', '#d3d3d3',  # 1-2次（已排除，灰色）
          '#1e5f8e', '#2471a3', '#2e86c1',  # 3-5次（主要，深藍色系）
          '#5dade2', '#85c1e9', '#aed6f1']  # 6-8次（淺藍色系）

# 繪製長條圖
bars = ax.bar(checkup_counts, people_counts, color=colors, edgecolor='white', linewidth=2)

# 在每個長條上方添加數值標籤
for i, (bar, count, pct) in enumerate(zip(bars, people_counts, percentages)):
    height = bar.get_height()
    # 對於較小的值，調整標籤位置
    if count < 100:
        label_text = f'{count}\n({pct:.1f}%)'
        y_offset = 20
    else:
        label_text = f'{count}\n({pct:.1f}%)'
        y_offset = 30

    ax.text(bar.get_x() + bar.get_width()/2., height + y_offset,
            label_text,
            ha='center', va='bottom',
            fontsize=10 if count < 100 else 11,
            fontweight='bold')

# 添加分組標註
# 只標註已排除的資料 (1-2次)
ax.axvspan(-0.5, 1.5, alpha=0.1, color='red', zorder=0)
ax.text(0.5, max(people_counts) * 0.85, 'Excluded\n(Insufficient)',
        ha='center', fontsize=9, color='darkred', fontweight='bold')

# 設定標題和標籤
ax.set_title('Checkup Frequency Distribution (Complete)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Checkups', fontsize=12)
ax.set_ylabel('Number of Participants', fontsize=12)

# 設定y軸範圍
ax.set_ylim(0, max(people_counts) * 1.1)

# 添加格線
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

# 添加統計資訊文字框
stats_text = ('Original: 6,119\n'
              'Filtered: 6,056\n'
              'Mean: 4.2\n'
              'Core (3-5): 89.3%')
ax.text(0.98, 0.97, stats_text,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))

# 移除上方和右方的邊框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 調整布局
plt.tight_layout()

# 確保目錄存在
output_dir = 'd:/Personal/Project/RiskPrediction-3H/docs/experiments/figures'
os.makedirs(output_dir, exist_ok=True)

# 儲存圖片
output_path = os.path.join(output_dir, 'checkup_distribution_full.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Full chart saved to: {output_path}")

# 關閉圖形以釋放記憶體
plt.close()

print("Successfully generated complete checkup distribution chart (1-8 times)!")