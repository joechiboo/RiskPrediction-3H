"""
Quick exploration of HRS data structure
"""

import pandas as pd
import pyreadstat
from pathlib import Path

def quick_explore():
    """Quickly explore HRS data structure"""

    base_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\raw\other')
    output_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\processed\HRS_Excel')
    output_path.mkdir(parents=True, exist_ok=True)

    # Start with the smallest file
    small_file = 'h22core/h22sps/h22b_r.sav'  # Demographics, 2.0 MB
    full_path = base_path / small_file

    print("HRS Data Quick Explorer")
    print("=" * 50)
    print(f"Exploring: {small_file}")

    try:
        # Read just metadata first (fast)
        meta = pyreadstat.read_sav(str(full_path), metadataonly=True)[1]
        print(f"Variables: {len(meta.column_names)}")
        print(f"Variable names preview: {meta.column_names[:10]}")

        # Read small sample (first 100 rows)
        df_sample = pyreadstat.read_sav(str(full_path), row_limit=100)[0]
        print(f"Sample shape: {df_sample.shape}")

        # Show basic info
        print("\nFirst few columns:")
        for col in df_sample.columns[:10]:
            print(f"  {col}: {df_sample[col].dtype}")

        # Save sample
        sample_file = output_path / "2022_demographics_sample100.xlsx"
        df_sample.to_excel(sample_file, index=False)
        print(f"\nSample saved to: {sample_file}")

        # Save all variable names
        var_info = pd.DataFrame({
            'Variable': meta.column_names,
            'Position': range(len(meta.column_names))
        })
        var_file = output_path / "2022_demographics_variables.xlsx"
        var_info.to_excel(var_file, index=False)
        print(f"Variable list saved to: {var_file}")

        return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == '__main__':
    success = quick_explore()

    if success:
        print("\n" + "=" * 50)
        print("SUCCESS! Check the Excel files to see:")
        print("1. Sample data structure")
        print("2. Complete variable list")
        print("\nRecommended approach:")
        print("1. Open the variable list to identify 3H-related variables")
        print("2. Use R or specialized tools for full conversion")
        print("3. Focus on specific columns for your analysis")