"""
Explore key health modules for 3H disease prediction
"""

import pandas as pd
import pyreadstat
from pathlib import Path

def explore_health_modules():
    """Explore health modules relevant for 3H prediction"""

    base_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\raw\other')
    output_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\processed\HRS_Excel')

    # Key health files for 3H diseases
    health_files = {
        'health_2022': 'h22core/h22sps/h22c_r.sav',     # 2022 Health Status
        'medical_2022': 'h22core/h22sps/h22e_h.sav',    # 2022 Medical History
        'health_2020': 'h20core/h20sps/h20c_r.sav',     # 2020 Health Status
        'medical_2020': 'h20core/h20sps/h20e_h.sav',    # 2020 Medical History
    }

    all_variables = {}

    print("HRS Health Modules Explorer")
    print("=" * 60)

    for module_name, file_path in health_files.items():
        full_path = base_path / file_path

        if full_path.exists():
            try:
                print(f"\nExploring: {module_name}")
                print("-" * 40)

                # Get metadata (fast)
                meta = pyreadstat.read_sav(str(full_path), metadataonly=True)[1]
                n_vars = len(meta.column_names)
                print(f"Variables: {n_vars}")

                # Look for 3H-related variables
                h_vars = find_3h_variables(meta.column_names)
                print(f"3H-related variables found: {len(h_vars)}")

                if h_vars:
                    print("Key variables:")
                    for category, vars_list in h_vars.items():
                        if vars_list:
                            print(f"  {category}: {len(vars_list)} variables")
                            print(f"    {', '.join(vars_list[:5])}{'...' if len(vars_list) > 5 else ''}")

                # Store all variables for this module
                all_variables[module_name] = {
                    'total_vars': n_vars,
                    'variable_names': meta.column_names,
                    'h3_vars': h_vars
                }

                # Save variable list
                var_df = pd.DataFrame({
                    'Variable': meta.column_names,
                    'Is_3H_Related': [is_3h_variable(var) for var in meta.column_names]
                })
                var_file = output_path / f"{module_name}_variables.xlsx"
                var_df.to_excel(var_file, index=False)

            except Exception as e:
                print(f"Error reading {module_name}: {str(e)}")
        else:
            print(f"File not found: {file_path}")

    # Create summary report
    create_summary_report(all_variables, output_path)

def find_3h_variables(var_names):
    """Find variables related to 3H diseases"""

    h3_vars = {
        'hypertension': [],
        'hyperglycemia': [],
        'dyslipidemia': [],
        'general_health': [],
        'medications': [],
        'demographics': []
    }

    for var in var_names:
        var_upper = var.upper()

        # Hypertension related
        if any(term in var_upper for term in ['BP', 'BLOOD', 'PRESS', 'HYPER']):
            h3_vars['hypertension'].append(var)
        # Diabetes/Hyperglycemia related
        elif any(term in var_upper for term in ['DIAB', 'SUGAR', 'GLUCOSE', 'A1C', 'HBA1C']):
            h3_vars['hyperglycemia'].append(var)
        # Dyslipidemia related
        elif any(term in var_upper for term in ['CHOL', 'LIPID', 'STATIN', 'HDL', 'LDL']):
            h3_vars['dyslipidemia'].append(var)
        # Medications
        elif any(term in var_upper for term in ['MED', 'DRUG', 'PILL', 'RX']):
            h3_vars['medications'].append(var)
        # General health
        elif any(term in var_upper for term in ['HEALTH', 'CONDITION', 'DISEASE', 'DOCTOR']):
            h3_vars['general_health'].append(var)
        # Demographics
        elif any(term in var_upper for term in ['AGE', 'SEX', 'RACE', 'EDUC', 'INCOME']):
            h3_vars['demographics'].append(var)

    return h3_vars

def is_3h_variable(var_name):
    """Check if a variable is potentially relevant for 3H diseases"""
    var_upper = var_name.upper()

    keywords = ['BP', 'BLOOD', 'PRESS', 'HYPER', 'DIAB', 'SUGAR', 'GLUCOSE',
                'CHOL', 'LIPID', 'STATIN', 'HDL', 'LDL', 'MED', 'DRUG',
                'HEALTH', 'CONDITION', 'DOCTOR', 'AGE', 'SEX', 'RACE']

    return any(keyword in var_upper for keyword in keywords)

def create_summary_report(all_variables, output_path):
    """Create a summary report of all modules"""

    summary_data = []

    for module_name, module_data in all_variables.items():
        total_3h = sum(len(vars_list) for vars_list in module_data['h3_vars'].values())

        summary_data.append({
            'Module': module_name,
            'Total_Variables': module_data['total_vars'],
            'H3_Related_Variables': total_3h,
            'Hypertension_Vars': len(module_data['h3_vars']['hypertension']),
            'Hyperglycemia_Vars': len(module_data['h3_vars']['hyperglycemia']),
            'Dyslipidemia_Vars': len(module_data['h3_vars']['dyslipidemia']),
            'Medication_Vars': len(module_data['h3_vars']['medications']),
            'General_Health_Vars': len(module_data['h3_vars']['general_health']),
        })

    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        summary_file = output_path / "HRS_3H_Variables_Summary.xlsx"
        summary_df.to_excel(summary_file, index=False)
        print(f"\n{'='*60}")
        print(f"SUMMARY REPORT saved to: {summary_file}")
        print("\nModule Overview:")
        for row in summary_data:
            print(f"  {row['Module']}: {row['H3_Related_Variables']}/{row['Total_Variables']} variables")

if __name__ == '__main__':
    explore_health_modules()
    print(f"\n{'='*60}")
    print("NEXT STEPS:")
    print("1. Review the summary Excel file")
    print("2. Check individual module variable lists")
    print("3. Select specific variables for your 3H prediction model")
    print("4. Consider using R or Stata for full data conversion")