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
├── data/                    # 資料集
│   ├── raw/                 # 原始資料
│   ├── processed/           # 處理後的資料
│   └── external/            # 外部資料來源
├── src/                     # 程式碼
│   ├── data_preprocessing/  # 資料前處理
│   │   ├── data_cleaning.py
│   │   ├── feature_engineering.py
│   │   └── data_split.py
│   ├── models/              # 模型實作
│   │   ├── interpretable/   # 可解釋模型
│   │   │   ├── logistic_regression.py
│   │   │   └── decision_tree.py
│   │   └── blackbox/        # 黑盒模型
│   │       ├── random_forest.py
│   │       ├── svm.py
│   │       └── neural_network.py
│   ├── evaluation/          # 模型評估
│   │   ├── metrics.py
│   │   ├── cross_validation.py
│   │   └── statistical_tests.py
│   ├── explainability/      # 模型解釋
│   │   ├── shap_analysis.py
│   │   ├── feature_importance.py
│   │   └── visualization.py
│   └── utils/               # 工具函式
│       ├── config.py
│       ├── logger.py
│       └── helpers.py
├── notebooks/               # Jupyter Notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_analysis.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_results_analysis.ipynb
├── results/                 # 實驗結果
│   ├── models/              # 訓練好的模型
│   ├── predictions/         # 預測結果
│   ├── metrics/             # 評估指標
│   └── comparisons/         # 模型比較結果
├── figures/                 # 圖表與視覺化
│   ├── eda/                 # 探索性資料分析圖表
│   ├── model_performance/   # 模型表現圖表
│   └── interpretability/    # 可解釋性分析圖表
├── docs/                    # 文件
│   ├── thesis/              # 論文相關
│   │   ├── chapters/        # 各章節
│   │   ├── references/      # 參考文獻
│   │   └── appendix/        # 附錄
│   ├── meeting_notes/       # 會議記錄
│   └── presentation/        # 簡報資料
├── tests/                   # 單元測試
│   ├── test_preprocessing.py
│   ├── test_models.py
│   └── test_evaluation.py
├── config/                  # 設定檔
│   ├── model_config.yaml
│   ├── data_config.yaml
│   └── experiment_config.yaml
├── requirements.txt         # Python 套件需求
├── environment.yml          # Conda 環境檔案
├── .gitignore              # Git 忽略檔案
└── README.md               # 專案說明
```

---

## ⚙️ 技術細節 (Technical Details)
- **資料前處理**：缺失值處理、特徵選擇、標準化
- **模型比較**：
  - Interpretable Models: Logistic Regression, Decision Tree
  - Black-box Models: Random Forest, SVM, Neural Networks
- **解釋方法**：SHAP, Feature Importance
- **評估指標**：Accuracy, Precision, Recall, F1-score, AUC

---

## 🚀 使用方式 (How to Use)
1. **Clone 專案**：
   ```bash
   git clone https://github.com/your-username/RiskPrediction-3H.git
   cd RiskPrediction-3H
   ```

2. **安裝環境**：
   ```bash
   pip install -r requirements.txt
   ```

3. **執行程式**：
   ```bash
   python code/train_models.py
   ```

---

## 📊 預期成果 (Expected Outcomes)
- 建立一套三高疾病風險預測模型
- 比較可解釋模型與黑盒模型之間的準確率與可解釋性
- 提供臨床應用上的洞見 (Clinical Insights)

---

## 📖 論文資訊 (Thesis Info)
- **學校 / 系所**：國立臺北教育大學 資訊科學系 在職碩士班
- **研究生**：紀伯喬
- **指導教授**：Prof. 許揚
- **預計完成時間**：2026 年