"""
Convert Synthea synthetic data to SUA_CVDs_risk_factors format

This script transforms Synthea's multiple CSV files into the standardized
SUA format used for 3H (hypertension, hyperglycemia, hyperlipidemia) risk prediction.

Author: Generated with Claude Code
Date: 2025-09-30
"""

import sys
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# File paths
DATA_DIR = Path("d:/Personal/Project/RiskPrediction-3H/data/raw/1000_synthea_sample_data")
OUTPUT_DIR = Path("d:/Personal/Project/RiskPrediction-3H/data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("Converting Synthea Data to SUA_CVDs_risk_factors Format")
print("=" * 80)

# ============================================================================
# Step 1: Load Synthea data
# ============================================================================
print("\n[1/6] Loading Synthea data files...")

patients = pd.read_csv(DATA_DIR / "patients.csv")
observations = pd.read_csv(DATA_DIR / "observations.csv")
conditions = pd.read_csv(DATA_DIR / "conditions.csv")

print(f"  ✓ Patients: {len(patients):,} records")
print(f"  ✓ Observations: {len(observations):,} records")
print(f"  ✓ Conditions: {len(conditions):,} records")

# ============================================================================
# Step 2: Filter and pivot observations
# ============================================================================
print("\n[2/6] Processing observations...")

# Key observation codes mapping
OBS_CODES = {
    '8480-6': 'SBP',      # Systolic Blood Pressure
    '8462-4': 'DBP',      # Diastolic Blood Pressure
    '2339-0': 'FBG',      # Glucose (using as FBG)
    '2093-3': 'TC',       # Total Cholesterol
    '38483-4': 'Cr',      # Creatinine
    '39156-5': 'BMI',     # Body Mass Index
    '2571-8': 'TG',       # Triglycerides (for reference)
    '4548-4': 'HbA1c',    # HbA1c (for reference)
}

# Filter relevant observations
obs_filtered = observations[observations['CODE'].isin(OBS_CODES.keys())].copy()
obs_filtered['CODE_NAME'] = obs_filtered['CODE'].map(OBS_CODES)
obs_filtered['DATE'] = pd.to_datetime(obs_filtered['DATE']).dt.tz_localize(None)  # Remove timezone
obs_filtered['VALUE'] = pd.to_numeric(obs_filtered['VALUE'], errors='coerce')

print(f"  ✓ Filtered observations: {len(obs_filtered):,} records")
print(f"  ✓ Unique patients: {obs_filtered['PATIENT'].nunique()}")

# ============================================================================
# Step 3: Process conditions (diagnoses)
# ============================================================================
print("\n[3/6] Processing diagnoses...")

# Map conditions to 3H diagnoses (use int keys to match data type)
CONDITION_CODES = {
    59621000: 'hypertension',      # Hypertension
    38341003: 'hypertension',      # Hypertensive disorder
    44054006: 'hyperglycemia',     # Diabetes
    15777000: 'hyperglycemia',     # Prediabetes
    55822004: 'dyslipidemia',      # Hyperlipidemia
}

# Process conditions
cond_filtered = conditions[conditions['CODE'].isin(CONDITION_CODES.keys())].copy()
cond_filtered['DIAGNOSIS'] = cond_filtered['CODE'].map(CONDITION_CODES)
cond_filtered['START'] = pd.to_datetime(cond_filtered['START'], errors='coerce')
cond_filtered = cond_filtered[cond_filtered['START'].notna()]  # Remove rows with invalid dates

print(f"  ✓ Filtered conditions: {len(cond_filtered):,} records")
print(f"  ✓ Patients with 3H diagnoses: {cond_filtered['PATIENT'].nunique()}")

# ============================================================================
# Step 4: Create patient visits with all measurements
# ============================================================================
print("\n[4/6] Creating patient visit records...")

# Group by patient and date to create visits
visit_data = []

for patient_id, patient_obs in obs_filtered.groupby('PATIENT'):
    # Get patient info
    patient_info = patients[patients['Id'] == patient_id].iloc[0]
    birth_date = pd.to_datetime(patient_info['BIRTHDATE'])
    sex = 1 if patient_info['GENDER'] == 'M' else 2

    # Get patient conditions
    patient_conds = cond_filtered[cond_filtered['PATIENT'] == patient_id]

    # Group observations by date
    for date, date_obs in patient_obs.groupby('DATE'):
        # Calculate age at visit
        age = (date - birth_date).days // 365

        # Pivot observations to columns
        obs_dict = date_obs.set_index('CODE_NAME')['VALUE'].to_dict()

        # Skip if missing critical values
        if 'SBP' not in obs_dict or 'DBP' not in obs_dict:
            continue

        # Determine diagnoses at this time point
        hypertension = 1  # Default to 1 (normal)
        hyperglycemia = 1
        dyslipidemia = 1

        for _, cond in patient_conds.iterrows():
            if pd.notna(cond['START']) and cond['START'] <= date:
                if cond['DIAGNOSIS'] == 'hypertension':
                    hypertension = 2
                elif cond['DIAGNOSIS'] == 'hyperglycemia':
                    hyperglycemia = 2
                elif cond['DIAGNOSIS'] == 'dyslipidemia':
                    dyslipidemia = 2

        # Create visit record
        visit = {
            'PATIENT': patient_id,
            'DATE': date,
            'sex': sex,
            'Age': age,
            'BMI': obs_dict.get('BMI', np.nan),
            'SBP': obs_dict.get('SBP', np.nan),
            'DBP': obs_dict.get('DBP', np.nan),
            'FBG': obs_dict.get('FBG', np.nan),
            'TC': obs_dict.get('TC', np.nan),
            'Cr': obs_dict.get('Cr', np.nan),
            'hypertension': hypertension,
            'hyperglycemia': hyperglycemia,
            'dyslipidemia': dyslipidemia,
        }

        visit_data.append(visit)

visits_df = pd.DataFrame(visit_data)
print(f"  ✓ Created {len(visits_df):,} visit records")
print(f"  ✓ From {visits_df['PATIENT'].nunique()} patients")

# ============================================================================
# Step 5: Calculate derived variables and add visit times
# ============================================================================
print("\n[5/6] Calculating derived variables...")

# Sort by patient and date
visits_df = visits_df.sort_values(['PATIENT', 'DATE'])

# Add visit number (Times)
visits_df['Times'] = visits_df.groupby('PATIENT').cumcount() + 1

# Calculate GFR using CKD-EPI formula
# Note: Synthea Cr is in mg/dL, need to convert to μmol/L for comparison with SUA format
# 1 mg/dL = 88.4 μmol/L
def calculate_gfr(row):
    if pd.isna(row['Cr']) or row['Cr'] == 0:
        return np.nan

    # Convert Cr from mg/dL to μmol/L to match SUA format
    cr_mg_dl = row['Cr']
    cr_umol = cr_mg_dl * 88.4

    age = row['Age']
    is_female = (row['sex'] == 2)

    # CKD-EPI formula (μmol/L version)
    # κ: 62 (female) or 80 (male) μmol/L
    # α: -0.329 (female) or -0.411 (male)
    kappa = 62 if is_female else 80
    alpha = -0.329 if is_female else -0.411

    # Calculate GFR
    gfr = 141 * min(cr_umol/kappa, 1)**alpha * max(cr_umol/kappa, 1)**(-1.209) * (0.993**age)

    # Adjust for female
    if is_female:
        gfr *= 1.018

    return gfr

visits_df['GFR'] = visits_df.apply(calculate_gfr, axis=1)

# Note: UA (Uric Acid) is not available in Synthea data
# Setting to NaN
visits_df['UA'] = np.nan

print("  ✓ Added visit times (Times)")
print("  ✓ Calculated GFR")
print("  ⚠️  UA (Uric Acid) not available in Synthea - set to NaN")

# ============================================================================
# Step 6: Create final SUA format and assign IDs
# ============================================================================
print("\n[6/6] Finalizing SUA format...")

# Create sequential patient IDs
patient_id_map = {pid: idx + 1 for idx, pid in enumerate(visits_df['PATIENT'].unique())}
visits_df['ID'] = visits_df['PATIENT'].map(patient_id_map)

# Select and order columns to match SUA format
final_columns = [
    'ID', 'sex', 'Age', 'BMI', 'SBP', 'DBP', 'FBG', 'TC', 'Cr', 'GFR', 'UA', 'Times',
    'hypertension', 'hyperglycemia', 'dyslipidemia'
]

sua_format_df = visits_df[final_columns].copy()

# Round numeric columns
numeric_cols = ['BMI', 'SBP', 'DBP', 'FBG', 'TC', 'Cr', 'GFR', 'UA']
for col in numeric_cols:
    if col in sua_format_df.columns:
        sua_format_df[col] = sua_format_df[col].round(2)

# Sort by ID and Times
sua_format_df = sua_format_df.sort_values(['ID', 'Times'])

print(f"  ✓ Final dataset: {len(sua_format_df):,} records")
print(f"  ✓ Unique patients: {sua_format_df['ID'].nunique()}")

# ============================================================================
# Save output
# ============================================================================
output_file = OUTPUT_DIR / "Synthea_SUA_format.csv"
sua_format_df.to_csv(output_file, index=False)

print("\n" + "=" * 80)
print("✅ Conversion Complete!")
print("=" * 80)
print(f"\nOutput file: {output_file}")
print(f"Total records: {len(sua_format_df):,}")
print(f"Unique patients: {sua_format_df['ID'].nunique()}")

# ============================================================================
# Summary statistics
# ============================================================================
print("\n" + "=" * 80)
print("📊 Summary Statistics")
print("=" * 80)

print("\n1. Visit Distribution:")
visit_counts = sua_format_df.groupby('ID')['Times'].max()
print(f"   Patients with ≥3 visits: {(visit_counts >= 3).sum()} ({(visit_counts >= 3).sum() / len(visit_counts) * 100:.1f}%)")
print(f"   Mean visits per patient: {visit_counts.mean():.1f}")
print(f"   Median visits per patient: {visit_counts.median():.0f}")

print("\n2. Diagnosis Distribution:")
print(f"   Hypertension (status=2): {(sua_format_df['hypertension'] == 2).sum()} records")
print(f"   Hyperglycemia (status=2): {(sua_format_df['hyperglycemia'] == 2).sum()} records")
print(f"   Dyslipidemia (status=2): {(sua_format_df['dyslipidemia'] == 2).sum()} records")

print("\n3. Data Completeness:")
for col in ['BMI', 'SBP', 'DBP', 'FBG', 'TC', 'Cr', 'GFR', 'UA']:
    missing_pct = sua_format_df[col].isna().sum() / len(sua_format_df) * 100
    print(f"   {col}: {100 - missing_pct:.1f}% complete")

print("\n4. Sample Preview (first 10 rows):")
print(sua_format_df.head(10).to_string(index=False))

print("\n" + "=" * 80)
print("🎯 Ready for 3H Risk Prediction!")
print("=" * 80)
