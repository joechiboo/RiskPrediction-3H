"""
Sliding Window Dataset Creation Script

Convert longitudinal health checkup data to sliding window format:
- Each patient can generate multiple training samples
- (T1, T2) -> T3
- (T2, T3) -> T4
- (T3, T4) -> T5
- ...

Reference: Taiwan MJ 2024 (PLoS ONE)

Author: Claude Code
Date: 2026-01-12
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import List, Tuple


def load_raw_data(data_path: str) -> pd.DataFrame:
    """Load raw longitudinal data"""
    df = pd.read_csv(data_path)
    print(f"Loaded raw data: {len(df):,} records, {df['ID'].nunique():,} patients")
    return df


def create_sliding_window_samples(
    df: pd.DataFrame,
    feature_cols: List[str],
    target_cols: List[str],
    demographic_cols: List[str],
    min_checks: int = 3
) -> pd.DataFrame:
    """
    Create sliding window samples

    Each window: (T_i, T_{i+1}) -> T_{i+2}

    Parameters:
    -----------
    df : DataFrame
        Raw longitudinal data (long format)
    feature_cols : list
        Time-varying feature columns
    target_cols : list
        Target variable columns
    demographic_cols : list
        Demographic columns (time-invariant)
    min_checks : int
        Minimum number of checkups required

    Returns:
    --------
    DataFrame : Sliding window format data
    """

    # Sort by ID and Times
    df_sorted = df.sort_values(['ID', 'Times']).reset_index(drop=True)

    # Count checkups per patient
    check_counts = df_sorted.groupby('ID').size()
    valid_ids = check_counts[check_counts >= min_checks].index
    df_filtered = df_sorted[df_sorted['ID'].isin(valid_ids)]

    print(f"Filtered: {df_filtered['ID'].nunique():,} patients (>={min_checks} checkups)")

    # Create sliding window samples
    samples = []

    for patient_id in df_filtered['ID'].unique():
        patient_data = df_filtered[df_filtered['ID'] == patient_id].reset_index(drop=True)
        n_visits = len(patient_data)

        # Each possible window: (i, i+1) -> i+2
        for i in range(n_visits - 2):
            sample = {
                'patient_id': patient_id,
                'window_start': i + 1,  # 1-indexed (T1, T2, T3...)
                'window_id': f"{patient_id}_{i+1}"  # Unique identifier
            }

            # Demographics (from first timepoint)
            for col in demographic_cols:
                sample[col] = patient_data.loc[i, col]

            # T_input1 features (first timepoint in window)
            for col in feature_cols:
                sample[f'{col}_Tinput1'] = patient_data.loc[i, col]

            # T_input2 features (second timepoint in window)
            for col in feature_cols:
                sample[f'{col}_Tinput2'] = patient_data.loc[i + 1, col]

            # Delta features (T_input2 - T_input1)
            for col in feature_cols:
                val1 = patient_data.loc[i, col]
                val2 = patient_data.loc[i + 1, col]
                sample[f'Delta_{col}'] = val2 - val1

            # Target variables (T_target = T_input2 + 1)
            for col in target_cols:
                sample[f'{col}_target'] = patient_data.loc[i + 2, col]

            samples.append(sample)

    df_sliding = pd.DataFrame(samples)

    print(f"Generated {len(df_sliding):,} sliding window samples")
    print(f"Average {len(df_sliding) / df_sliding['patient_id'].nunique():.2f} samples per patient")

    return df_sliding


def analyze_samples_distribution(df_sliding: pd.DataFrame):
    """Analyze sliding window sample distribution"""
    print("\n" + "="*60)
    print("Sliding Window Sample Distribution Analysis")
    print("="*60)

    # Samples per patient distribution
    samples_per_patient = df_sliding.groupby('patient_id').size()
    print("\nSamples per patient:")
    print(samples_per_patient.describe())

    # Window start position distribution
    print("\nWindow start position distribution:")
    window_dist = df_sliding['window_start'].value_counts().sort_index()
    for start, count in window_dist.items():
        print(f"  T{start}->T{start+1}->T{start+2}: {count:,} samples ({count/len(df_sliding)*100:.1f}%)")

    # Target variable distribution
    print("\nTarget variable distribution (positive rate):")
    for col in ['hypertension_target', 'hyperglycemia_target', 'dyslipidemia_target']:
        if col in df_sliding.columns:
            # Note: In original data, 1=No, 2=Yes
            positive_rate = (df_sliding[col] == 2).mean() * 100
            print(f"  {col}: {positive_rate:.2f}%")


def save_dataset(df_sliding: pd.DataFrame, output_path: str):
    """Save sliding window dataset"""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df_sliding.to_csv(output_path, index=False)
    print(f"\nSaved to: {output_path}")
    print(f"File size: {Path(output_path).stat().st_size / 1024:.2f} KB")


def main():
    # Set paths (absolute paths)
    base_dir = Path(__file__).parent.parent
    raw_data_path = base_dir / "data/01_primary/SUA/raw/SUA_CVDs_risk_factors.csv"
    output_path = base_dir / "data/01_primary/SUA/processed/SUA_sliding_window.csv"

    # Define columns
    feature_cols = ['FBG', 'TC', 'Cr', 'UA', 'GFR', 'BMI', 'SBP', 'DBP']
    target_cols = ['hypertension', 'hyperglycemia', 'dyslipidemia']
    demographic_cols = ['sex', 'Age']

    print("="*60)
    print("Sliding Window Dataset Creation")
    print("="*60)
    print(f"\nFeature columns: {feature_cols}")
    print(f"Target variables: {target_cols}")
    print(f"Demographics: {demographic_cols}")

    # Load data
    print("\n[1/4] Loading raw data...")
    df = load_raw_data(raw_data_path)

    # Create sliding window samples
    print("\n[2/4] Creating sliding window samples...")
    df_sliding = create_sliding_window_samples(
        df=df,
        feature_cols=feature_cols,
        target_cols=target_cols,
        demographic_cols=demographic_cols,
        min_checks=3
    )

    # Analyze distribution
    print("\n[3/4] Analyzing sample distribution...")
    analyze_samples_distribution(df_sliding)

    # Save
    print("\n[4/4] Saving dataset...")
    save_dataset(df_sliding, output_path)

    print("\n" + "="*60)
    print("Done!")
    print("="*60)

    # Show column list
    print("\nColumn list:")
    print(f"  - ID columns: patient_id, window_start, window_id")
    print(f"  - Demographics: {demographic_cols}")
    print(f"  - Tinput1 features: {len(feature_cols)}")
    print(f"  - Tinput2 features: {len(feature_cols)}")
    print(f"  - Delta features: {len(feature_cols)}")
    print(f"  - Target variables: {len(target_cols)}")
    print(f"  - Total columns: {len(df_sliding.columns)}")

    return df_sliding


if __name__ == "__main__":
    df_sliding = main()
