# HRS Data Download Guide

## Overview
This project uses the Health and Retirement Study (HRS) public survey data for risk prediction analysis. Due to the large size of the dataset (~2.x GB), the data files are not included in this repository. This guide will help you download the necessary data files.

## Data Source
- **Website**: https://hrsdata.isr.umich.edu/data-products/public-survey-data
- **Dataset Type**: Public Survey Data (Longitudinal)
- **File Size**: Approximately 2.x GB

## Step-by-Step Download Instructions

### 1. Register for HRS Data Access
1. Go to https://hrsdata.isr.umich.edu/
2. Click on "Register" in the top menu
3. Fill out the registration form with:
   - Your institutional affiliation
   - Research purpose
   - Contact information
4. Wait for account approval (usually within 1-2 business days)

### 2. Access the Data Portal
1. Log in with your approved credentials
2. Navigate to "Data Products" → "Public Survey Data"
3. Select the appropriate survey waves/years for your analysis

### 3. Download Required Files
This project uses the following HRS datasets:

#### Primary Datasets (Required):
- **2022 HRS Core** (Wave 15)
  - File: `h22core` or similar naming
  - Contains: Most recent cross-sectional survey data
  - Topics: Health, cognition, demographics, insurance, income

- **2020 HRS Core** (Wave 14)
  - File: `h20core` or similar naming
  - Contains: Previous wave for longitudinal comparison
  - Topics: Same as 2022, allows for change analysis

#### Optional Additional Datasets:
- **RAND HRS Longitudinal File 2020 (V2)**: Pre-processed, user-friendly version
- **Exit Interview Data**: For mortality risk analysis
- **COVID-19 Module**: Special questions related to pandemic impact

### 4. File Placement
After downloading, organize the files as follows:
```
RiskPrediction-3H/
├── data/
│   ├── HRS_data/
│   │   ├── core/
│   │   │   └── [Core interview files]
│   │   ├── exit/
│   │   │   └── [Exit interview files]
│   │   ├── rand/
│   │   │   └── [RAND HRS files]
│   │   └── README.txt (this will be auto-generated)
```

### 5. Data Format Options
HRS data is available in multiple formats:
- **SAS** (.sas7bdat)
- **Stata** (.dta)
- **SPSS** (.sav)
- **ASCII** (.dat with .sps/.sas/.dct files)

For this project, we recommend using **Stata (.dta)** format for better Python compatibility.

## Alternative: Using Specific Waves
If you only need specific years/waves:
1. Go to "Browse HRS Data Products"
2. Filter by:
   - Year/Wave
   - Topic (e.g., Health, Demographics)
   - Data Type
3. Download only the necessary files

## Data Usage Notes
- **Citation**: Please cite HRS data as specified on their website
- **Privacy**: The public data is de-identified but still requires careful handling
- **Updates**: HRS releases new waves approximately every 2 years

## Troubleshooting
- **Access Issues**: Contact hrsquest@umich.edu
- **Download Problems**: Try using a download manager for large files
- **File Corruption**: Verify checksums if provided

## Required Python Packages
To work with the HRS data, install:
```bash
pip install pandas pyreadstat stata-setup
```

## Contact
For HRS data questions: hrsquest@umich.edu
For project-specific questions: [Your contact info]

## License and Terms
By downloading HRS data, you agree to:
- Use data only for research purposes
- Not attempt to identify individuals
- Cite HRS appropriately in publications
- Follow all HRS data use agreements