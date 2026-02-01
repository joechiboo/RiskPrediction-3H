HRS Data Directory
==================

This directory should contain the HRS (Health and Retirement Study) data files.

Required Files:
- 2022 HRS Core data (Wave 15)
- 2020 HRS Core data (Wave 14)

File formats supported:
- .dta (Stata) - Recommended
- .sas7bdat (SAS)
- .sav (SPSS)

To download these files:
1. See the guide at: docs/HRS_data_download_guide.md
2. Register at https://hrsdata.isr.umich.edu/
3. Download the Core interview data for 2020 and 2022
4. Place the files in this directory

Note: These data files are not included in the repository due to their large size (~2.x GB).

To verify your data is properly set up, run:
python scripts/verify_hrs_data.py