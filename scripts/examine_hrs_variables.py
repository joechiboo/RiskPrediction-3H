"""
Examine HRS variable names in detail to identify 3H-related variables
"""

import pandas as pd
import pyreadstat
from pathlib import Path
import re

def examine_variables():
    """Examine variable names in detail"""

    base_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\raw\other')
    output_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\processed\HRS_Excel')

    # Focus on one health file first
    file_path = 'h22core/h22sps/h22c_r.sav'  # 2022 Health Status
    full_path = base_path / file_path

    print("HRS Variable Name Analysis")
    print("=" * 60)
    print(f"Analyzing: {file_path}")

    try:
        # Get all variable names
        meta = pyreadstat.read_sav(str(full_path), metadataonly=True)[1]
        all_vars = meta.column_names

        print(f"Total variables: {len(all_vars)}")

        # Show first 20 variable names
        print("\nFirst 20 variables:")
        for i, var in enumerate(all_vars[:20]):
            print(f"{i+1:2d}. {var}")

        # Look for patterns
        print("\nVariable patterns analysis:")

        # Group by prefix (first 2 characters)
        prefixes = {}
        for var in all_vars:
            prefix = var[:2].upper()
            if prefix not in prefixes:
                prefixes[prefix] = []
            prefixes[prefix].append(var)

        # Show top prefixes
        sorted_prefixes = sorted(prefixes.items(), key=lambda x: len(x[1]), reverse=True)
        print("\nTop 10 variable prefixes:")
        for prefix, vars_list in sorted_prefixes[:10]:
            print(f"  {prefix}: {len(vars_list)} variables")
            if len(vars_list) <= 5:
                print(f"      {', '.join(vars_list)}")
            else:
                print(f"      {', '.join(vars_list[:3])} ... {vars_list[-1]}")

        # Search for health-related terms (more flexible)
        health_terms = {
            'Blood Pressure': ['BP', 'PRESS'],
            'Diabetes': ['DIAB', 'SUGAR', 'GLUC'],
            'Cholesterol': ['CHOL', 'LIPID'],
            'Heart': ['HEART', 'CARD'],
            'Doctor': ['DOC', 'DR', 'PHYS'],
            'Medicine': ['MED', 'DRUG', 'PILL'],
            'Condition': ['COND', 'DISE', 'PROB'],
            'Health': ['HEAL', 'HLTH'],
        }

        print(f"\nSearching for health-related terms:")
        found_terms = {}

        for term_name, keywords in health_terms.items():
            matches = []
            for var in all_vars:
                var_upper = var.upper()
                if any(keyword in var_upper for keyword in keywords):
                    matches.append(var)
            if matches:
                found_terms[term_name] = matches
                print(f"  {term_name}: {len(matches)} matches")
                if len(matches) <= 3:
                    print(f"      {', '.join(matches)}")
                else:
                    print(f"      {', '.join(matches[:3])} ...")

        # Save detailed variable list
        var_analysis = []
        for i, var in enumerate(all_vars):
            var_upper = var.upper()
            potentially_health = any(
                any(keyword in var_upper for keyword in keywords)
                for keywords in health_terms.values()
            )

            var_analysis.append({
                'Position': i + 1,
                'Variable': var,
                'Prefix': var[:2].upper() if len(var) >= 2 else var,
                'Length': len(var),
                'Has_Numbers': bool(re.search(r'\d', var)),
                'Potentially_Health_Related': potentially_health
            })

        # Save to Excel
        analysis_df = pd.DataFrame(var_analysis)
        analysis_file = output_path / "2022_health_variables_detailed.xlsx"
        analysis_df.to_excel(analysis_file, index=False)

        print(f"\nDetailed analysis saved to: {analysis_file}")

        # Summary statistics
        health_count = sum(1 for item in var_analysis if item['Potentially_Health_Related'])
        print(f"\nSUMMARY:")
        print(f"  Total variables: {len(all_vars)}")
        print(f"  Potentially health-related: {health_count}")
        print(f"  Health percentage: {health_count/len(all_vars)*100:.1f}%")

        return True

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == '__main__':
    success = examine_variables()

    if success:
        print(f"\n{'='*60}")
        print("SUCCESS! Check the Excel file for detailed variable analysis.")
        print("\nNext steps:")
        print("1. Open the Excel file to review all variables")
        print("2. Filter by 'Potentially_Health_Related' = TRUE")
        print("3. Look for patterns in variable prefixes")
        print("4. Cross-reference with HRS codebook for definitions")