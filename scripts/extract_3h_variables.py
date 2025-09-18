"""
Extract specific 3H-related variables from HRS data
Focus on the 94 priority variables identified
"""

import pandas as pd
import pyreadstat
from pathlib import Path

def extract_3h_variables():
    """Extract priority 3H variables from HRS files"""

    base_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\raw\other')
    output_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\processed\HRS_Excel')

    # Load the priority variables list
    priority_file = output_path / "HRS_3H_Priority_Variables.xlsx"

    if not priority_file.exists():
        print("Priority variables file not found. Run decode_hrs_variables.py first.")
        return

    print("HRS 3H Variables Extractor")
    print("=" * 60)

    # Read priority variables
    priority_vars = pd.read_excel(priority_file, sheet_name='All_Priority')
    print(f"Loading {len(priority_vars)} priority variables...")

    # Group by file
    files_to_process = {
        '2022_health_c': {
            'path': 'h22core/h22sps/h22c_r.sav',
            'output_name': '2022_Health_3H_Variables'
        },
        '2022_medical_e': {
            'path': 'h22core/h22sps/h22e_h.sav',
            'output_name': '2022_Medical_3H_Variables'
        },
        '2020_health_c': {
            'path': 'h20core/h20sps/h20c_r.sav',
            'output_name': '2020_Health_3H_Variables'
        },
        '2020_medical_e': {
            'path': 'h20core/h20sps/h20e_h.sav',
            'output_name': '2020_Medical_3H_Variables'
        }
    }

    extracted_data = {}

    for file_key, file_info in files_to_process.items():
        print(f"\n{'-'*40}")
        print(f"Processing: {file_key}")

        full_path = base_path / file_info['path']

        if not full_path.exists():
            print(f"File not found: {file_info['path']}")
            continue

        # Get variables for this file
        file_vars = priority_vars[priority_vars['File'] == file_key]['Variable'].tolist()

        if not file_vars:
            print("No priority variables for this file")
            continue

        print(f"Target variables: {len(file_vars)}")

        try:
            # Read the data
            print("Reading data...")
            df, meta = pyreadstat.read_sav(str(full_path))
            print(f"Full dataset: {df.shape[0]:,} rows x {df.shape[1]} columns")

            # Extract only the priority variables (that exist in the data)
            available_vars = [var for var in file_vars if var in df.columns]
            missing_vars = [var for var in file_vars if var not in df.columns]

            if missing_vars:
                print(f"Missing variables: {len(missing_vars)} - {missing_vars[:5]}...")

            if available_vars:
                df_subset = df[available_vars].copy()
                print(f"Extracted: {df_subset.shape[0]:,} rows x {len(available_vars)} columns")

                # Save the extracted data
                output_file = output_path / f"{file_info['output_name']}.xlsx"

                with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                    # Main data
                    df_subset.to_excel(writer, sheet_name='Data', index=False)

                    # Variable info
                    var_info = priority_vars[
                        (priority_vars['File'] == file_key) &
                        (priority_vars['Variable'].isin(available_vars))
                    ][['Variable', 'Likely_Topic', 'Potential_3H_Relevance', 'Priority']]

                    var_info.to_excel(writer, sheet_name='Variable_Info', index=False)

                    # Basic statistics
                    stats = df_subset.describe(include='all').T
                    stats['Missing_Count'] = df_subset.isnull().sum()
                    stats['Missing_Percent'] = (stats['Missing_Count'] / len(df_subset) * 100).round(2)
                    stats.to_excel(writer, sheet_name='Statistics')

                print(f"Saved: {output_file.name}")
                extracted_data[file_key] = {
                    'data': df_subset,
                    'variables': available_vars,
                    'file_name': output_file
                }

            else:
                print("No available variables to extract")

        except Exception as e:
            print(f"Error processing {file_key}: {str(e)}")

    # Create combined summary
    create_combined_summary(extracted_data, output_path)

def create_combined_summary(extracted_data, output_path):
    """Create a combined summary of all extracted data"""

    if not extracted_data:
        print("No data extracted")
        return

    print(f"\n{'='*60}")
    print("Creating combined summary...")

    summary_file = output_path / "HRS_3H_Extraction_Summary.xlsx"

    with pd.ExcelWriter(summary_file, engine='openpyxl') as writer:
        # Overall summary
        summary_rows = []
        total_vars = 0
        total_rows = 0

        for file_key, data_info in extracted_data.items():
            n_vars = len(data_info['variables'])
            n_rows = len(data_info['data'])
            total_vars += n_vars
            total_rows += n_rows

            summary_rows.append({
                'File': file_key,
                'Variables_Extracted': n_vars,
                'Rows': n_rows,
                'Output_File': data_info['file_name'].name
            })

        summary_df = pd.DataFrame(summary_rows)
        summary_df.to_excel(writer, sheet_name='Extraction_Summary', index=False)

        # Combined variable list
        all_vars = []
        for file_key, data_info in extracted_data.items():
            for var in data_info['variables']:
                all_vars.append({
                    'File': file_key,
                    'Variable': var,
                    'Year': '2022' if '2022' in file_key else '2020',
                    'Section': 'Health' if 'health' in file_key else 'Medical'
                })

        if all_vars:
            all_vars_df = pd.DataFrame(all_vars)
            all_vars_df.to_excel(writer, sheet_name='All_Variables', index=False)

    print(f"Combined summary saved: {summary_file.name}")
    print(f"\nFINAL RESULTS:")
    print(f"  Files processed: {len(extracted_data)}")
    print(f"  Total variables extracted: {total_vars}")
    print(f"  Average rows per file: {total_rows//len(extracted_data) if extracted_data else 0:,}")

    print(f"\n{'='*60}")
    print("EXTRACTION COMPLETE!")
    print("\nReady for 3H disease analysis:")
    print("✓ Priority health variables identified and extracted")
    print("✓ 2020 and 2022 data available for longitudinal analysis")
    print("✓ Variable documentation included")
    print("✓ Basic statistics computed")
    print("\nNext steps:")
    print("1. Review individual Excel files for each section")
    print("2. Identify specific 3H disease indicators")
    print("3. Begin exploratory data analysis")
    print("4. Develop prediction models")

if __name__ == '__main__':
    extract_3h_variables()