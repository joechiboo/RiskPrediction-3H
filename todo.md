#### 🔬 技術研究與實作

**已完成** (2025-11-19):
- [x] ✅ **03_ModelBuilding.ipynb** - LR, RF, MTL 模型建立
  - 發現並修復嚴重 bug（資料錯位導致 AUC=0.5）
  - 修復後：高血糖 AUC 0.507→0.929 (+83%), 高血脂 AUC 0.567→0.888 (+57%)
  - 實作 MTL (MultiOutputClassifier, ClassifierChain)
  - 處理資料不平衡 (class_weight='balanced', SMOTE)
  - 最佳模型：MTL LR (balanced) - AUC >0.88 for all diseases

- [x] ✅ **04_XGBoost.ipynb** - XGBoost 進階模型
  - 單任務 XGBoost with scale_pos_weight
  - MTL XGBoost
  - 與 MTL LR 比較：F1 提升 9-39%
  - 特徵重要性：SBP (收縮壓) 最重要 (34.6%)

**明天計畫** (2025-11-20, 可跑到 19:00):
- [ ] 🔥 **05_NeuralNetworks.ipynb** - ANN (淺層神經網路)
  - 1-2 隱藏層
  - class_weight 處理不平衡
  - 與 XGBoost 比較
  - 預計時間：30-40 分鐘

- [ ] 🔥 **06_SVM.ipynb** - Support Vector Machine
  - RBF kernel
  - class_weight='balanced'
  - 可能較慢（1-2 小時）
  - 預計時間：1-2 小時

- [ ] 📊 **07_GeneticProgramming.ipynb** (指導教授專長領域)
  - **需先安裝**: `pip install gplearn` 或 `pip install deap`
  - 演化式特徵選擇與符號回歸
  - 可能遇到相依性問題，需預留除錯時間
  - 訓練較慢（演化 100 代約 1-2 小時）
  - 預計時間：1-2 小時（包含安裝除錯）
  - ⚠️ 如安裝失敗，改用超參數調優取代

**優先順序**:
1. ANN（快速，30 分鐘）✅ 容易成功
2. SVM（慢，1-2 小時）✅ 穩定
3. GP（教授專長，1-2 小時）⚠️ 可能有安裝問題

**時間規劃** (彈性調整):
- 14:00-14:40: ANN (40 分鐘)
- 14:40-16:40: SVM (2 小時)
- 16:40-18:00: GP (1.5 小時，含除錯)
  - 如 GP 失敗 → 改做超參數調優
- 18:00-19:00: 總結與模型比較表

**GP 備註**:
- 教授熟悉 GP，建議展示即使有挑戰也嘗試
- 如順利完成，會是亮點（符號回歸 + 可解釋性）
- 如失敗，有備案（超參數調優同樣有價值）

**11/20 19:00 後**: 影像處理課

---

#### 📊 下次 Meeting 準備
- [ ] 準備 Dual 2025 paper 10 pages
- [ ] 整理 實驗結果總結
