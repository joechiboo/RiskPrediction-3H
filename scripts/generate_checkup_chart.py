"""
生成檢查次數分佈長條圖
輸出到 experiments 資料夾
"""

import matplotlib.pyplot as plt
import matplotlib
import os

# 設定字體，避免中文顯示問題
matplotlib.rcParams['font.family'] = ['DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 資料
checkup_counts = ['3', '4', '5', '6+']
people_counts = [1754, 1776, 1935, 591]
percentages = [28.7, 29.0, 31.6, 9.7]

# 創建圖形
fig, ax = plt.subplots(figsize=(8, 6))

# 顏色設定 - 使用漸層藍色
colors = ['#3498db', '#2980b9', '#1f618d', '#154360']

# 繪製長條圖
bars = ax.bar(checkup_counts, people_counts, color=colors, edgecolor='white', linewidth=2)

# 在每個長條上方添加數值標籤
for bar, count, pct in zip(bars, people_counts, percentages):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 30,
            f'{count}\n({pct}%)',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# 設定標題和標籤
ax.set_title('Checkup Frequency Distribution', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Checkups', fontsize=12)
ax.set_ylabel('Number of Participants', fontsize=12)

# 設定y軸範圍
ax.set_ylim(0, max(people_counts) * 1.15)

# 添加格線
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)

# 添加統計資訊文字框
stats_text = 'Total: 6,056\nMean: 4.2\nCore Sample (3-5): 89.3%'
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
output_path = os.path.join(output_dir, 'checkup_distribution.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Chart saved to: {output_path}")

# 關閉圖形以釋放記憶體
plt.close()

print("Successfully generated checkup distribution chart!")