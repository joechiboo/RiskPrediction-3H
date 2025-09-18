"""
Check available HRS files and recommend key files for conversion
"""

import os
from pathlib import Path

def check_hrs_files():
    """Check what HRS files are available and prioritize for conversion"""

    base_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\raw\other')

    if not base_path.exists():
        print(f"Directory not found: {base_path}")
        return

    print("HRS Data Files Analysis")
    print("="*60)

    # Priority files for 3H disease prediction
    priority_health_files = {
        '2022 Health Core': [
            'h22core/h22sps/h22c_r.sav',     # Section C: Health Status
            'h22core/h22sps/h22e_h.sav',     # Section E: Medical History
            'h22core/h22sps/h22n_r.sav',     # Section N: Health Services
            'h22core/h22sps/h22b_r.sav',     # Section B: Demographics
        ],
        '2020 Health Core': [
            'h20core/h20sps/h20c_r.sav',     # Section C: Health Status
            'h20core/h20sps/h20e_h.sav',     # Section E: Medical History
            'h20core/h20sps/h20n_r.sav',     # Section N: Health Services
            'h20core/h20sps/h20b_r.sav',     # Section B: Demographics
        ],
        'Tracker (Essential)': [
            'trk2022v2/trk2022tr_r.sav'     # Linking file
        ]
    }

    found_files = []
    missing_files = []

    for category, files in priority_health_files.items():
        print(f"\n{category}:")
        print("-" * 40)

        for file_path in files:
            full_path = base_path / file_path
            if full_path.exists():
                file_size = full_path.stat().st_size / (1024*1024)  # MB
                print(f"  [OK] {file_path} ({file_size:.1f} MB)")
                found_files.append((category, file_path, file_size))
            else:
                print(f"  [MISSING] {file_path}")
                missing_files.append((category, file_path))

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Found files: {len(found_files)}")
    print(f"Missing files: {len(missing_files)}")

    if found_files:
        total_size = sum([size for _, _, size in found_files])
        print(f"Total size: {total_size:.1f} MB")

        print("\nRecommended conversion priority:")
        print("1. Tracker file - Essential for linking data")
        print("2. Section C (Health) - Disease diagnoses")
        print("3. Section E (Medical) - Treatment history")
        print("4. Section B (Demographics) - Basic covariates")
        print("5. Section N (Health Services) - Healthcare utilization")

    print("\nFor 3H prediction, focus on variables related to:")
    print("- Hypertension: Blood pressure, BP medications")
    print("- Hyperglycemia: Diabetes diagnosis, blood sugar")
    print("- Dyslipidemia: Cholesterol levels, lipid drugs")

    return found_files, missing_files

if __name__ == '__main__':
    found, missing = check_hrs_files()

    print("\nNext steps:")
    print("1. Install: pip install pandas pyreadstat openpyxl")
    print("2. Run conversion script on priority files")
    print("3. Check HRS codebook for variable definitions")