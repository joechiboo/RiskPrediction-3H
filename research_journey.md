# Research Journey - RiskPrediction-3H Project
## An Empirical Comparison of Interpretable and Black-box Models for Predicting Hypertension, Hyperglycemia, and Dyslipidemia

---

## 📅 **Research Progress Timeline**

### **Project Initiation - January 2025**

#### **January 8, 2025: Project Foundation**
- **Meeting Status**: Domain Knowledge Preparation Meeting
- **Key Accomplishments**:
  - ✅ Complete project structure establishment
  - ✅ Git version control setup with SSH authentication
  - ✅ Dataset import: SUA_CVDs_risk_factors.csv (25,744 records)
  - ✅ Configuration files created (model_config.yaml, data_config.yaml)
  - ✅ README.md documentation completed

- **Two-Week Research Plan Initiated**:
  - Week 1: Basic definitions, epidemiology, clinical associations research
  - Week 2: Data sources, research methods, research gaps investigation

### **Meeting Series Overview (01-13)**
Based on the meeting presentation files found, the research progressed through 13 formal meetings from December 2024 to September 2025:

#### **Meeting 01 (December 31, 2024)**: `meeting01_21138X006_紀伯喬.pptx`
- Initial project proposal and research scope definition

#### **Meetings 02-04 (January-February 2025)**: 
- `meeting02_21138X006_紀伯喬_wVBA.pptm` (January 6)
- `meeting03_21138X006_紀伯喬_wVBA.pptm` (January 21) 
- `meeting04_21138X006_紀伯喬_wVBA.pptm` (February 11)
- Focus on literature review and domain knowledge development

#### **Meeting 05 (March 2025)**:
- `meeting05_21138X006_紀伯喬_wVBA.pptm` (March 20)
- `meeting05.docx` (March 11) - Additional documentation
- Methodology design and research framework establishment

#### **Meetings 06-09 (April-July 2025)**:
- `meeting06_21138X006_紀伯喬_wVBA.pptm` (April 14)
- `meeting07_21138X006_紀伯喬_wVBA.pptm` (May 20)
- `meeting08_21138X006_紀伯喬_wVBA.pptm` (July 16)
- `meeting09_21138X006_紀伯喬_wVBA.pptm` (July 25)
- Data analysis and model development phase

#### **Meeting 10 (July-August 2025)**:
- `meeting10_21138X006_紀伯喬_wVBA.pptm` (August 1)
- `meeting10_Dataset.txt` (July 29) - Dataset comparison analysis
- **Key Dataset Decisions Made**:
  1. **Chronic Kidney Disease (CKD)** - 400 records, CKD/not CKD (27:73 imbalance)
  2. **Fertility Diagnosis** - 100 records, Normal/Abnormal (88:12 imbalance)
  3. **Wisconsin Diagnostic Breast Cancer (WDBC)** - 569 records, Benign/Malignant
  4. **BUPA Liver Disorders** - 345 records, Liver disease classification

#### **Meetings 11-13 (August-September 2025)**:
- `meeting11_21138X006_紀伯喬_wVBA.pptm` (August 5)
- `meeting12_21138X006_紀伯喬_wVBA.pptm` (August 26)
- `meeting13_21138X006_紀伯喬_wVBA.pptm` (September 3)
- Results analysis and thesis finalization phase

---

## 📚 **Literature Review & Domain Knowledge Development**

### **Six-Pillar Research Framework**
Based on professor guidance, comprehensive domain knowledge research was structured around 6 key areas:

#### **1. Clinical Definitions & Diagnostic Standards**
- **Hypertension**: ≥140/90 mmHg (multiple measurements required)
- **Hyperglycemia/Diabetes**: 
  - Fasting blood glucose ≥126 mg/dL
  - HbA1c ≥6.5%
- **Dyslipidemia**: High LDL-C, elevated TG, low HDL
- **Key Insight**: Understanding diagnostic cutoff values is fundamental for any classification/labeling approach

#### **2. Epidemiological Background**
- Global and Taiwan/East Asia prevalence rates (WHO, NCD-RisC, NHANES data)
- Age and gender distribution patterns
- Temporal trends (1975-2020 blood pressure/glucose/lipid changes)
- **Research Value**: Establishes disease burden and public health significance

#### **3. Clinical & Physiological Associations**
- Common risk factors: obesity, metabolic syndrome, lifestyle factors
- Comorbidity patterns: three-high diseases often co-occur with synergistic cardiovascular risk
- Related conditions: diabetes, kidney disease, heart disease, stroke
- **Research Gap**: Can ML models capture these interaction effects?

#### **4. Data Sources & Common Indicators**
- Clinical lab data: blood pressure, glucose (FBG, HbA1c), lipids (TC, LDL, HDL, TG)
- Derived indicators: BMI, waist-hip ratio, GFR, uric acid
- Major datasets: Framingham Heart Study, NHANES, NCD-RisC, MIMIC
- **Project Dataset**: SUA_CVDs_risk_factors.csv with complete data for 25,744 participants

#### **5. Research Methods & Applications**
- Statistical models: Cox regression, Logistic regression
- ML/DL applications: risk prediction, early diagnosis, missing value imputation
- Clinical applications: disease risk prediction tools, health management platforms
- **Research Focus**: Interpretable vs Black-box model comparison

#### **6. Controversies & Research Gaps**
- Hypertension "normal-high" thresholds (120-139 systolic controversy)
- Hyperglycemia: HbA1c vs FBG as primary diagnostic criterion
- Dyslipidemia: Population-specific cutoff values
- **Critical Gap**: Three-high interaction effects often ignored in models

### **Literature Search Strategy**
- **Databases**: PubMed, Google Scholar, IEEE Xplore
- **Keywords**: interpretable machine learning, hypertension prediction, diabetes prediction, cardiovascular risk, explainable AI
- **Target Journals**: Nature Medicine, JMIR, Artificial Intelligence in Medicine

---

## ⚙️ **Methodology Evolution**

### **Research Approach Development**
The methodology followed a systematic 7-stage research process:

#### **Stage 1: Literature Review (Completed)**
- **Duration**: 2-4 weeks 
- **Status**: Completed domain knowledge research
- **Output**: 6-pillar framework knowledge base

#### **Stage 2: Research Question Definition**
- **Core Question**: How do interpretable models compare to black-box models in three-high disease prediction?
- **Hypothesis**: Interpretable models provide clinically relevant insights with comparable performance
- **Success Metrics**: Accuracy, Precision, Recall, F1-score, AUC + Interpretability measures

#### **Stage 3: Data Understanding** 
- **Primary Dataset**: SUA_CVDs_risk_factors.csv (25,744 participants, 2010-2018 community survey)
- **Features**: Age, Sex, BMI, SBP/DBP, FBG, TC, Cr, GFR, UA, Times
- **Targets**: Hypertension, Hyperglycemia, Dyslipidemia (binary classification)
- **Data Quality**: Complete dataset with no missing values

#### **Stage 4: Model Selection Strategy**
- **Interpretable Models**: 
  - Logistic Regression (linear relationships, feature coefficients)
  - Decision Trees (rule-based, hierarchical decisions)
- **Black-box Models**:
  - Random Forest (ensemble, feature interactions)
  - Support Vector Machines (non-linear boundaries)
  - Neural Networks (complex patterns, deep learning)

#### **Stage 5: Experimental Design**
- Cross-validation methodology
- Train/validation/test split strategy
- Hyperparameter tuning protocols
- Fair comparison frameworks

#### **Stage 6: Interpretability Analysis**
- **Methods**: SHAP (SHapley Additive exPlanations), Feature Importance
- **Goal**: Quantify and compare model interpretability
- **Clinical Relevance**: Map model insights to domain knowledge

---

## 🎯 **Key Decisions & Pivots**

### **Dataset Selection Evolution**
**Meeting 10 Decision**: Expanded beyond primary dataset to include comparative analysis with 4 additional datasets:
1. **Chronic Kidney Disease** - Medical classification with class imbalance
2. **Fertility Diagnosis** - Highly imbalanced binary classification
3. **Wisconsin Breast Cancer** - Well-known benchmark dataset
4. **BUPA Liver Disorders** - Liver disease classification

**Rationale**: This multi-dataset approach strengthens the research by:
- Testing model generalizability across different medical domains
- Handling various levels of class imbalance
- Providing benchmark comparisons with established datasets

### **Research Scope Refinement**
**Initial Focus**: Single-dataset three-high prediction
**Evolved Focus**: Multi-dataset comparative analysis with emphasis on:
- Cross-domain model performance
- Interpretability consistency across datasets
- Class imbalance handling capabilities

---

## 📊 **Current Research Status** (As of September 2025)

### **Completed Phases**
1. ✅ **Project Infrastructure** - Complete development environment
2. ✅ **Literature Review** - Comprehensive domain knowledge
3. ✅ **Research Design** - Methodology framework established
4. ✅ **Dataset Preparation** - Primary + 4 comparative datasets ready
5. ✅ **Meeting Series** - 13 advisor meetings completed

### **Implementation Progress**
Based on the project structure and timeline:
- **Data Processing**: Likely in progress/completed (Meetings 6-9 focus)
- **Model Development**: Advanced stage (Meetings 10-13 focus)
- **Results Analysis**: Current focus area
- **Thesis Writing**: Likely initiated

### **Technical Infrastructure**
- **Development Environment**: Complete project structure
- **Version Control**: Git with SSH authentication
- **Configuration Management**: YAML-based model and data configs
- **Documentation**: Comprehensive research methodology guide

---

## 🔮 **Future Directions & Next Steps**

### **Immediate Priorities** (Based on Research Methodology Guide)
1. **Results Analysis & Statistical Testing**
   - Performance comparison across all datasets
   - Statistical significance testing
   - Clinical significance assessment

2. **Interpretability Evaluation**
   - SHAP analysis for all models
   - Feature importance ranking consistency
   - Clinical insight validation

3. **Thesis Writing** (Recommended Order)
   - **Methods Section**: Document experimental design
   - **Results Section**: Present findings and comparisons
   - **Discussion**: Interpret results and limitations
   - **Introduction**: Contextualize research contribution
   - **Abstract**: Summarize key findings

### **Research Contributions**
1. **Methodological**: Systematic comparison framework for interpretable vs black-box models
2. **Clinical**: Insights into three-high disease prediction interpretability
3. **Technical**: Multi-dataset evaluation approach for medical ML models
4. **Practical**: Guidelines for model selection in clinical prediction tasks

### **Timeline Expectations**
- **Total Project Duration**: 22 weeks (5-6 months from start)
- **Current Stage**: Months 8-9 (Results analysis and thesis writing phase)
- **Expected Completion**: 2026 (per thesis info)

---

## 💡 **Key Insights & Lessons Learned**

### **Research Process Insights**
1. **Systematic Literature Review First**: The 6-pillar domain knowledge framework proved essential
2. **Multi-Dataset Validation**: Expanding beyond single dataset strengthened research validity
3. **Interpretability as Core Focus**: Not just performance, but explainability for clinical applications
4. **Regular Advisory Meetings**: 13 structured meetings ensured consistent progress and guidance

### **Technical Decisions**
1. **Complete Dataset Advantage**: No missing data simplifies preprocessing and focuses on modeling
2. **Class Imbalance Consideration**: Multiple datasets with varying imbalance levels provide robust testing
3. **Clinical Relevance Priority**: All decisions grounded in domain knowledge and clinical applicability

### **Methodological Strengths**
1. **Comprehensive Framework**: 7-stage research methodology provides clear progression
2. **Balanced Approach**: Both statistical rigor and clinical relevance considered
3. **Reproducible Design**: Well-documented process and structured codebase

---

## 📁 **Project Resources**

### **Documentation Structure**
- `D:\Personal\Project\RiskPrediction-3H\docs\work_journal.md` - Progress tracking
- `D:\Personal\Project\RiskPrediction-3H\docs\domain_knowledge_research_plan.md` - Literature framework
- `D:\Personal\Project\RiskPrediction-3H\docs\research_methodology_guide.md` - Process guidelines
- `D:\Personal\Project\RiskPrediction-3H\docs\meeting_notes\` - 13 presentation files + notes

### **Data Resources**
- **Primary Dataset**: `SUA_CVDs_risk_factors.csv` (25,744 participants)
- **Source**: https://datadryad.org/dataset/doi%3A10.5061/dryad.z08kprrk1
- **Comparative Datasets**: 4 UCI ML repository datasets for validation

### **Academic Context**
- **Institution**: National Taipei University of Education, Department of Computer Science
- **Program**: In-Service Master's Program  
- **Student**: 紀伯喬 (Student ID: 21138X006)
- **Advisor**: Prof. 許揚
- **Target Completion**: 2026

---

*This research journey document captures the comprehensive development process of a master's thesis comparing interpretable and black-box machine learning models for three-high disease prediction. The systematic approach from domain knowledge through implementation demonstrates rigorous academic research methodology combined with practical clinical applications.*