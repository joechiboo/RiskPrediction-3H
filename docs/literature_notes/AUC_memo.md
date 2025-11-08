# AUC (Area Under the ROC Curve) 備忘錄

## ROC 曲線座標軸

### Y 軸：TPR (True Positive Rate)
- **定義**：真陽性率 = TP / (TP + FN)
- **別名**：Sensitivity (敏感度)、Recall (召回率)
- **意義**：在所有**真實為陽性**的樣本中，模型預測正確的比例

### X 軸：FPR (False Positive Rate)
- **定義**：偽陽性率 = FP / (FP + TN)
- **計算**：1 - Specificity (特異度)
- **意義**：在所有**真實為陰性**的樣本中，模型預測錯誤的比例

## AUC 值解讀

| AUC 值範圍 | 模型表現 |
|-----------|---------|
| 0.9 - 1.0 | 優秀 (Excellent) |
| 0.8 - 0.9 | 良好 (Good) |
| 0.7 - 0.8 | 尚可 (Fair) |
| 0.6 - 0.7 | 差 (Poor) |
| 0.5 - 0.6 | 失敗 (Fail) |
| 0.5 | 隨機猜測 (Random) |

## 關鍵概念

### ROC 曲線繪製方式
1. 改變分類閾值 (threshold)，從 0 到 1
2. 在每個閾值下計算 TPR 和 FPR
3. 以 FPR 為 X 軸、TPR 為 Y 軸繪製曲線

### AUC 的優點
- **閾值無關**：不需要選擇特定閾值
- **類別不平衡適用**：相較於準確率更穩定
- **機率意義**：隨機選一個正樣本和一個負樣本，模型給正樣本較高分數的機率

### 理想 ROC 曲線
- 左上角：(0, 1) → FPR = 0, TPR = 1 (完美分類)
- 對角線：FPR = TPR (隨機猜測，AUC = 0.5)
- 曲線越靠近左上角，AUC 越大，模型越好

## 混淆矩陣對應關係

```
                預測結果
              Positive  Negative
實際 Positive    TP        FN
     Negative    FP        TN

TPR = TP / (TP + FN)  ← 真陽性率
FPR = FP / (FP + TN)  ← 偽陽性率
```

## 與其他指標的關係

- **Precision** = TP / (TP + FP) → 預測為陽性中真正為陽性的比例
- **Recall (TPR)** = TP / (TP + FN) → 真實陽性中被預測出來的比例
- **Specificity** = TN / (TN + FP) = 1 - FPR → 真實陰性中被預測對的比例
- **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall)

## 實務應用考量

### 何時使用 AUC
✓ 評估模型整體分類能力
✓ 比較不同模型效能
✓ 類別不平衡的資料集

### 何時不只看 AUC
✗ 需要明確分類決策（選定閾值後看 Precision/Recall）
✗ 偽陽性和偽陰性代價差異大（考慮業務成本）
✗ 極度不平衡資料（可搭配 PR-AUC）
