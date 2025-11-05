# 系統性文獻回顧







台灣政府資料開放平台：https://data.gov.tw/
UCI機器學習資料庫 https://archive.ics.uci.edu/datasets
https://blog.csdn.net/qq_32892383/article/details/104424358
世界銀行公開數據 https://data.worldbank.org.cn/
世界衛生組織：http://apps.who.int/gho/data/node.home
---
衛生福利資料科學中心 https://www.apre.mohw.gov.tw/

## 表格內容


### 表格 1

| 研究標的 | 處理問題 | 輸入 | 資料集 | 前處理 | 機器學習方法 | 評估準則 | 輸出 | 提出解決方案 |
|---|---|---|---|---|---|---|---|---|
| 15(sci)
糖尿病風險預測 | 罹患疾病前預測糖尿病機率 | 人口特徵
生理測量
血液檢驗 | 臺中榮總EHR
不可下載 | 資料篩選
欄位轉換
資料分割 | LR、RF、XGBoost | Accuracy、Precision、Recall、F1-Score、AUC | 預測糖尿病風險 |  |
| 16 (sci)
**Taiwan MTL (2025)**
多慢性病預測 | 同時預測多種慢性病並探索疾病共病關係 | ICD診斷代碼序列（10年）
個人資訊（年齡、性別、居住地、職業） | 台灣HWDC
健保資料庫
555,124樣本
不可下載 | ICD Word2Vec Embedding
每2月選3個最常見疾病
缺失值用<PAD>
排除已患病者 | **Multi-Task Learning**:
MAND-LR
MAND-MLP
MAND-LSTM
MAND-MHSA
**CTR Models**:
FM、DCN | Log Loss
AUC
BAC
Precision、Recall
F1-Score
FPR、FNR | 同時預測：
糖尿病(22.4%)
心臟病(24.6%)
中風(8.7%)
高血壓(39.0%) | **MTL架構**:
Hard parameter sharing
**可解釋性**:
Attention scores分析
Permutation feature importance
**發現**:
MTL參數量僅STL的1/4
高血脂為關鍵風險因子 |

### 表格 2

| 研究標的 | 處理問題 | 輸入 | 資料集 | 前處理 | 機器學習方法 | 評估準則 | 輸出 | 提出解決方案 |
|---|---|---|---|---|---|---|---|---|
| 01
腎臟疾病預測 | 比較參數與準確度的影響 | 血液檢驗
尿液檢驗 | 美國NCHS(CDC) 
NHANES 可下載 | 資料不平衡Under-Sampling | DT(Cart) | Recall | 預測腎臟病風險 |  |
| 研究標的 | 處理問題 | 輸入 | 資料集 | 前處理 | 機器學習方法 | 評估準則 | 輸出 | 提出解決方案 |
| 01
腎臟疾病預測 | 比較參數與準確度的影響 | 血液檢驗
尿液檢驗 | 美國NCHS(CDC) 
NHANES 可下載 | 資料不平衡Under-Sampling | DT(Cart) | Recall | 預測腎臟病風險 |  |
| 02
心臟疾病預測 | 媒合保險與顧客 | 年齡性別
生活習慣
血液檢驗
生理量測 | UCI (Cleveland Clinic Foundation)/
Framingham Heart Study | 資料不平衡
上、下、SMOTE
缺失值
有處理 | DT、RF、LR、SVM、XGBoost
、Light GBM、ANN | Recall | 預測心臟疾病風險 |  |
| 03
腎病病理分類 | 檢驗數據分型預測 | 年齡性別
檢驗結果 | 北醫/萬芳/馬偕/雙和db無法下載 | 資料不平衡SMOTE
缺失值KNN | RF、LR、SVM
、XGBoost、KNN | Accuracy, AUC | 預測腎臟病風險 |  |
| 04(sci) 
中風風險評估 | 融合結構化與非結構化資訊提高並加速疾病風險準確率 | 生活習慣
檢驗結果
醫生記錄
病歷描述 | 中國中部某醫院的 電子健康記錄（EHR）無法下載 | 缺失值
LFM | DT 、CNN、Naïve Bayes、KNN | Accuracy,Recall | 預測慢性疾病風險 | CNN-MDRP |
| 05(sci) 
miRNA疾病預測 | 新增資料時的災難性遺忘問題 | 基因序列
基因疾病關聯
疾病語意資料
基因功能資料 | HMDD v3.0
miRBase
可下載 |  | DT、RF、SVM、BLS | Accuracy, AUC | 基因與癌症關聯 | MISSIM |
| 06(sci) 
慢性病風險預測 | 即時計算預測風險值 | 血液檢查
生理量測 | Catapult Health | 資料不平衡
oversampling
undersampling
SMOTE | DT、RF、LR、SVM、NB、KNN、GB | Accuracy, AUC | 即時預測慢性疾病風險 |  |
| 07(sci)
尿酸回歸預測 | 降低檢測成本與頻率 | 生理量測
檢驗結果
飲食習慣 | 公司員工健檢數據
無法下載 |  | BDT、RF、LR、NN、BLR | RMSE | 預測血中尿酸值 |  |
| 08
糖尿病分類預測 | 探討各種 ML 模型預測糖尿病風險 | 血液檢查
生理量測
社會經歷 | 美國 CDC 健康調查資料集
可下載 | 變數處理
欄位轉換
移除缺失值 | DT、RF、LR、SVM、KNN、GBM、MARS | Accuracy、Precision、Recall、F1、 AUC | 糖尿病風險預測值 + 對應 SHAP 解釋 |  |
| 10
醫療資料集分類 | 類別不平衡 | 血液檢查
腫瘤影像
飲酒頻率 | UCI機器學習庫
可下載 | 移除缺失值
欄位轉換 | SVM
GP + Fave fitness | Accuracy、Precision、Specificity Recall、F1、 AUC | 預測腎病、乳癌、肝病與不孕症等疾病 | Proposed GP |
| 12
血糖回歸預測 | 比較模型準確度 | 血糖值
胰島素劑量
皮膚電反應 | Ohio2020 dataset
要申請才可下載 | 特徵交集化、缺值處理 | GP、GP-OS、GE、MOGE、LR、RF、ARIMA | RMSE、MAE、Clarke Error Grid | 30 分鐘與 60 分鐘血糖值預測 |  |