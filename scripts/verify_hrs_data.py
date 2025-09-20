"""
Verify HRS data files are properly downloaded and accessible.
"""
import os
from pathlib import Path
import pandas as pd

def verify_hrs_data():
    """Check if HRS data files exist and display basic information."""

    data_dir = Path('../data/HRS_data')

    # Expected files (adjust based on actual filenames)
    expected_files = {
        '2022 Core': ['h22core.dta', 'H22A_R.dta', 'h22core.sas7bdat'],
        '2020 Core': ['h20core.dta', 'H20A_R.dta', 'h20core.sas7bdat']
    }

    print("=" * 60)
    print("HRS Data Verification")
    print("=" * 60)

    # Check if data directory exists
    if not data_dir.exists():
        print(f"\n❌ Data directory not found: {data_dir.resolve()}")
        print("   Please create the directory and download HRS data.")
        return False

    print(f"\n✓ Data directory found: {data_dir.resolve()}")

    # Check for data files
    found_files = []
    all_files = list(data_dir.rglob('*'))

    print(f"\nFound {len(all_files)} files in data directory:")

    for file in all_files:
        if file.is_file():
            size_mb = file.stat().st_size / (1024 * 1024)
            print(f"  - {file.name} ({size_mb:.1f} MB)")
            found_files.append(file.name)

    # Check for expected datasets
    print("\n" + "=" * 60)
    print("Expected Datasets Status:")
    print("=" * 60)

    for dataset, possible_files in expected_files.items():
        found = any(f in found_files for f in possible_files)
        status = "✓" if found else "❌"
        print(f"{status} {dataset}")
        if found:
            matching = [f for f in possible_files if f in found_files]
            print(f"   Found: {', '.join(matching)}")
        else:
            print(f"   Expected one of: {', '.join(possible_files)}")

    # Try to read a sample if Stata files exist
    dta_files = [f for f in all_files if f.suffix == '.dta']
    if dta_files:
        print("\n" + "=" * 60)
        print("Data File Preview (first .dta file):")
        print("=" * 60)
        try:
            sample_file = dta_files[0]
            df = pd.read_stata(sample_file, convert_categoricals=False)
            print(f"\nFile: {sample_file.name}")
            print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]:,} columns")
            print(f"Memory usage: {df.memory_usage().sum() / (1024**2):.1f} MB")
            print(f"\nFirst 5 columns: {list(df.columns[:5])}")
        except Exception as e:
            print(f"Could not read file: {e}")
            print("You may need to install pyreadstat: pip install pyreadstat")

    return len(found_files) > 0

if __name__ == '__main__':
    success = verify_hrs_data()

    if not success:
        print("\n" + "=" * 60)
        print("Next Steps:")
        print("=" * 60)
        print("1. Follow the guide in docs/HRS_data_download_guide.md")
        print("2. Download 2022 and 2020 HRS Core data")
        print("3. Place files in data/HRS_data/")
        print("4. Run this script again to verify")