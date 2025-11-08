# 混淆矩陣評估指標備忘錄

## 基本指標

### Accuracy（準確率）
- **公式**: (TP + TN) / (TP + TN + FP + FN)
- **意義**: 所有預測中，正確預測的比例

### Sensitivity / Recall（靈敏度/召回率）
- **公式**: TP / (TP + FN)
- **別名**: TPR (True Positive Rate)、真陽性率
- **意義**: 實際為陽性中，被正確預測為陽性的比例

### Specificity（特異性）
- **公式**: TN / (TN + FP)
- **別名**: TNR (True Negative Rate)、真陰性率
- **意義**: 實際為陰性中，被正確預測為陰性的比例

### Precision（精確度/精準度）
- **公式**: TP / (TP + FP)
- **意義**: 預測為陽性中，真正是陽性的比例

### False Positive Rate（偽陽性率）
- **公式**: FP / (TN + FP) = 1 - Specificity
- **別名**: FPR
- **意義**: 實際為陰性中，被錯誤預測為陽性的比例

## ROC 曲線與 AUC

### ROC Curve（Receiver Operating Characteristic Curve）
- **縱軸（Y軸）**: TPR = Sensitivity = Recall
- **橫軸（X軸）**: FPR = False Positive Rate = 1 - Specificity
- **意義**: 呈現不同閾值下，真陽性率 vs 偽陽性率的權衡關係

### AUC（Area Under Curve）
- **定義**: ROC 曲線下的面積
- **範圍**: 0 到 1
- **意義**:
  - AUC = 1: 完美分類器
  - AUC = 0.5: 隨機猜測
  - AUC 越接近 1 越好

## 混淆矩陣結構

```
                預測結果
              Positive  Negative
實際  Positive    TP        FN
結果  Negative    FP        TN
```

- **TP (True Positive)**: 真陽性 - 實際為正，預測為正
- **TN (True Negative)**: 真陰性 - 實際為負，預測為負
- **FP (False Positive)**: 偽陽性 - 實際為負，預測為正（Type I Error）
- **FN (False Negative)**: 偽陰性 - 實際為正，預測為負（Type II Error）

## 常見混淆澄清

❌ **錯誤理解**:
- FPR = 特異性
- Precision = FPR

✓ **正確理解**:
- FPR = 1 - Specificity（兩者互補）
- TPR = Sensitivity = Recall（同一概念的不同名稱）
- Precision 和 Recall 是不同的指標
