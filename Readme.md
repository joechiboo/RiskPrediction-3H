# RiskPrediction-3H
An Empirical Comparison of Interpretable and Black-box Models for Predicting Hypertension, Hyperglycemia, and Dyslipidemia

## 📘 專案簡介 (Overview)
本專案屬於碩士論文研究，主要比較 **可解釋 (Interpretable)** 與 **黑盒 (Black-box)** 機器學習模型，在三高疾病（高血壓 Hypertension、高血糖 Hyperglycemia、高血脂 Dyslipidemia）風險預測上的表現與差異。

This repository contains the implementation and materials for the master thesis:  
**"An Empirical Comparison of Interpretable and Black-box Models for Predicting Hypertension, Hyperglycemia, and Dyslipidemia".**

---

## 📂 專案結構 (Project Structure)
```
RiskPrediction-3H/
├── data/                           # 資料集
│   ├── raw/                        # 原始資料
│   │   ├── HRS_data/               # HRS 調查資料 (2022, 2020)
│   │   ├── SUA_CVDs_risk_factors.csv
│   │   └── 1000_synthea_sample_data/  # Synthea 合成資料
│   └── processed/                  # 處理後的資料
│       └── Synthea_SUA_format.csv
│
├── src/                            # 程式碼 (規劃中)
│   ├── data_preprocessing/         # 資料前處理
│   ├── models/                     # 模型實作
│   │   ├── interpretable/          # 可解釋模型 (LR, DT)
│   │   └── blackbox/               # 黑盒模型 (RF, SVM, NN)
│   ├── evaluation/                 # 模型評估
│   └── explainability/             # 模型解釋 (SHAP, Attention)
│
├── docs/                           # 📚 文件（核心資料夾）
│   ├── guidelines/                 # 🎓 論文格式規範
│   │   ├── 國立臺北教育大學學位論文格式規範.pdf
│   │   ├── 論文封面套用檔.docx
│   │   ├── 學位論文上傳與提交2024.pdf
│   │   └── 文獻閱讀報告格式檢查清單.md
│   │
│   ├── references/                 # 📖 參考文獻與論文
│   │   ├── s41598-025-99554-z.pdf  (Taiwan MTL 2025)
│   │   ├── Taiwan_MTL_2025_中文翻譯.md
│   │   ├── attention_mechanism_guide.md
│   │   └── [其他重要論文 PDF]
│   │
│   ├── literature_notes/           # 📝 文獻筆記與研究備忘錄
│   │   ├── Systematic_Literature_Review.md  (系統性文獻回顧)
│   │   ├── AUC_memo.md             (AUC/ROC 評估指標)
│   │   ├── confusion_matrix_metrics.md  (混淆矩陣指標)
│   │   └── literature_review_memo.md  (文獻回顧方法論)
│   │
│   ├── concepts/                   # 💡 方法論概念說明
│   │   ├── AUC-ROC_詳細說明.md
│   │   ├── Cross_Validation.md
│   │   ├── Feature_Selection_Marginal_Utility.md
│   │   ├── Class_Imbalance_in_Medical_Prediction.md
│   │   └── [其他概念文件]
│   │
│   └── meeting_notes/              # 📅 歷次會議記錄與簡報
│       ├── meeting01-15_*.pptm     (會議簡報)
│       ├── meeting16_21138X006_紀伯喬_wVBA.pptm
│       ├── meeting16_taiwan_mtl_presentation_outline_10min.md
│       └── 2025-01-08_domain_knowledge_prep.md
│
├── notebooks/                      # Jupyter Notebooks (規劃中)
├── results/                        # 實驗結果 (規劃中)
├── config/                         # 設定檔 (規劃中)
├── requirements.txt                # Python 套件需求
└── README.md                       # 專案說明
```

---

## 📊 資料集 (Dataset)
本研究使用 **Health and Retirement Study (HRS)** 縱貫性調查資料：
- **2022 HRS Core** (Wave 15) - 最新橫斷面資料
- **2020 HRS Core** (Wave 14) - 用於縱貫分析

⚠️ **重要**：由於資料檔案過大（~2.x GB），不包含在此儲存庫中。
請參考 [Data_Access_Guide.md](docs/Data_Access_Guide.md) 取得資料。

### 資料集比較文件
- [HRS vs NHANES 比較](docs/HRS_vs_NHANES_Comparison.md)
- [縱貫性資料集選擇](docs/longitudinal_datasets_for_3H.md)
- [Synthea 合成資料摘要](docs/Synthea_Dataset_Summary.md)

---

## ⚙️ 技術細節 (Technical Details)

### 模型比較
- **Interpretable Models**: Logistic Regression, Decision Tree
- **Black-box Models**: Random Forest, SVM, Neural Networks
- **Multi-Task Learning**: 參考 Taiwan MTL (2025) 架構

### 可解釋性方法
- **SHAP**: Model-agnostic 特徵重要性分析
- **Attention Mechanism**: 神經網路內建可解釋性
- 詳見 [Attention 機制應用指南](docs/references/attention_mechanism_guide.md)

### 評估指標
- **分類效能**: Accuracy, Precision, Recall, F1-score, AUC, BAC
- **臨床重要性**: FPR (誤診率), FNR (漏診率)
- 詳見 [AUC 備忘錄](docs/literature_notes/AUC_memo.md) 與 [混淆矩陣指標](docs/literature_notes/confusion_matrix_metrics.md)

---

## 📚 重要文件快速導覽 (Key Documents)

### 📋 論文格式與規範
- [學位論文格式規範](docs/guidelines/國立臺北教育大學學位論文格式規範1110912.pdf)
- [論文封面套用檔](docs/guidelines/論文封面套用檔(WORD檔1121227).docx)
- [格式檢查清單](docs/guidelines/文獻閱讀報告格式檢查清單.md)

### 📖 文獻回顧
- [系統性文獻回顧](docs/literature_notes/Systematic_Literature_Review.md) - 包含 Taiwan MTL (2025) 等 16+ 篇論文
- [文獻回顧方法論](docs/literature_notes/literature_review_memo.md)

### 💡 方法論概念
- [AUC/ROC 詳細說明](docs/concepts/AUC-ROC_詳細說明.md)
- [類別不平衡處理](docs/concepts/Class_Imbalance_in_Medical_Prediction.md)
- [交叉驗證](docs/concepts/Cross_Validation.md)
- [特徵選擇與邊際效用](docs/concepts/Feature_Selection_Marginal_Utility.md)

### 🔬 研究備忘錄
- [AUC 備忘錄](docs/literature_notes/AUC_memo.md)
- [混淆矩陣指標](docs/literature_notes/confusion_matrix_metrics.md)
- [Attention 機制應用指南](docs/references/attention_mechanism_guide.md)

### 📅 會議記錄
- [Meeting 16 - Taiwan MTL 論文](docs/meeting_notes/meeting16_taiwan_mtl_presentation_outline_10min.md)
- [歷次會議簡報](docs/meeting_notes/)

---

## 🚀 快速開始 (Quick Start)

### 1. Clone 專案
```bash
git clone https://github.com/joechiboo/RiskPrediction-3H.git
cd RiskPrediction-3H
```

### 2. 瀏覽文件
- 📖 閱讀 [系統性文獻回顧](docs/literature_notes/Systematic_Literature_Review.md)
- 💡 了解 [研究方法論](docs/concepts/)
- 📋 查看 [論文格式規範](docs/guidelines/)

### 3. 資料準備（進行中）
- 下載 HRS 資料：參考 [Data_Access_Guide.md](docs/Data_Access_Guide.md)
- 測試用合成資料：`data/raw/1000_synthea_sample_data/`

### 4. 模型開發（規劃中）
```bash
# 安裝環境
pip install -r requirements.txt

# 資料前處理
python src/data_preprocessing/clean_data.py

# 模型訓練
python src/models/train_models.py
```

---

## 📊 研究目標與預期成果

### 研究目標
1. **比較可解釋性**：Interpretable Models (LR, DT) vs Black-box Models (RF, SVM, NN)
2. **多任務學習探索**：參考 Taiwan MTL (2025) 架構同時預測三高
3. **臨床應用價值**：識別可修改風險因子，提供預防建議

### 預期成果
- ✅ 建立三高疾病風險預測模型（高血壓、高血糖、高血脂）
- ✅ 完整的模型可解釋性分析（SHAP + Attention）
- ✅ 評估指標全面比較（AUC, Precision, Recall, F1, FPR, FNR）
- ✅ 臨床應用建議與風險因子分析

---

## 📈 專案進度 (Progress)

### ✅ 已完成
- [x] 文獻回顧（16+ 篇論文）
- [x] 研究方法論整理
- [x] 資料集調查與比較
- [x] 論文格式規範準備
- [x] Taiwan MTL (2025) 深度解析

### 🔄 進行中
- [ ] HRS 資料申請與取得
- [ ] 資料前處理流程設計
- [ ] 特徵工程規劃

### 📅 待完成
- [ ] 模型實作（LR, DT, RF, SVM, NN）
- [ ] Multi-Task Learning 架構實作
- [ ] SHAP 與 Attention 可解釋性分析
- [ ] 實驗結果比較與視覺化
- [ ] 論文撰寫

---

## 📖 論文資訊 (Thesis Info)
- **學校 / 系所**：國立臺北教育大學 資訊科學系 在職碩士班
- **研究生**：紀伯喬
- **指導教授**：Prof. 許揚
- **預計完成時間**：2026 年