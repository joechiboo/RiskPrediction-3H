"""
Decode HRS variable naming conventions
Based on HRS Tracker documentation analysis
"""

import pandas as pd
import pyreadstat
from pathlib import Path

def decode_hrs_variables():
    """Decode HRS variables using HRS naming conventions"""

    base_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\raw\other')
    output_path = Path(r'D:\Personal\Project\RiskPrediction-3H\data\processed\HRS_Excel')

    # Key HRS files and their sections
    files_to_decode = {
        '2022_health_c': {
            'path': 'h22core/h22sps/h22c_r.sav',
            'section': 'C - Health',
            'prefix': 'SC',
            'description': 'Health status, chronic conditions, functional limitations'
        },
        '2022_medical_e': {
            'path': 'h22core/h22sps/h22e_h.sav',
            'section': 'E - Medical',
            'prefix': 'SE',
            'description': 'Medical history, doctor visits, medications'
        },
        '2020_health_c': {
            'path': 'h20core/h20sps/h20c_r.sav',
            'section': 'C - Health',
            'prefix': 'RC',
            'description': 'Health status, chronic conditions (2020)'
        },
        '2020_medical_e': {
            'path': 'h20core/h20sps/h20e_h.sav',
            'section': 'E - Medical',
            'prefix': 'RE',
            'description': 'Medical history, medications (2020)'
        }
    }

    all_decoded = {}

    print("HRS Variable Decoder")
    print("=" * 60)

    for file_name, file_info in files_to_decode.items():
        full_path = base_path / file_info['path']

        if full_path.exists():
            print(f"\nDecoding: {file_name}")
            print(f"Section: {file_info['section']}")
            print("-" * 40)

            try:
                # Get variable names
                meta = pyreadstat.read_sav(str(full_path), metadataonly=True)[1]
                all_vars = meta.column_names

                print(f"Total variables: {len(all_vars)}")

                # Decode variables
                decoded_vars = decode_section_variables(all_vars, file_info)

                # Count by category
                categories = {}
                for var_info in decoded_vars:
                    cat = var_info['Likely_Topic']
                    categories[cat] = categories.get(cat, 0) + 1

                print("Variable categories found:")
                for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
                    print(f"  {cat}: {count}")

                # Save decoded variables
                decoded_df = pd.DataFrame(decoded_vars)
                output_file = output_path / f"{file_name}_decoded.xlsx"
                decoded_df.to_excel(output_file, index=False)
                print(f"Saved: {output_file.name}")

                all_decoded[file_name] = decoded_vars

            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print(f"File not found: {file_info['path']}")

    # Create combined summary
    create_3h_summary(all_decoded, output_path)

def decode_section_variables(var_names, file_info):
    """Decode variables based on HRS conventions"""

    decoded = []

    for var in var_names:
        var_info = {
            'Variable': var,
            'Section': file_info['section'],
            'Prefix': var[:2] if len(var) >= 2 else '',
            'Number': extract_number(var),
            'Likely_Topic': categorize_variable(var),
            'Potential_3H_Relevance': assess_3h_relevance(var),
            'Priority': get_priority(var)
        }
        decoded.append(var_info)

    return decoded

def extract_number(var_name):
    """Extract the number from HRS variable names"""
    import re
    match = re.search(r'(\d+)', var_name)
    return int(match.group(1)) if match else None

def categorize_variable(var_name):
    """Categorize variables based on common HRS patterns"""

    var_upper = var_name.upper()

    # Based on HRS documentation patterns
    if any(term in var_upper for term in ['001', '002', '005', '006']):
        return 'General Health Status'
    elif any(term in var_upper for term in ['010', '020', '021', '022', '023']):
        return 'Chronic Conditions'
    elif any(term in var_upper for term in ['050', '060', '070', '080']):
        return 'Functional Limitations'
    elif any(term in var_upper for term in ['100', '110', '120', '130']):
        return 'Doctor Visits'
    elif any(term in var_upper for term in ['150', '160', '170', '180']):
        return 'Medications'
    elif any(term in var_upper for term in ['200', '210', '220', '230']):
        return 'Specific Health Conditions'
    elif any(term in var_upper for term in ['250', '260', '270', '280']):
        return 'Health Behaviors'
    elif 'MODE' in var_upper or 'CSR' in var_upper:
        return 'Survey Administration'
    elif var_name in ['HHID', 'PN', 'SSUBHH', 'RSUBHH']:
        return 'Identifiers'
    else:
        return 'Other/Unknown'

def assess_3h_relevance(var_name):
    """Assess relevance for 3H diseases"""

    var_upper = var_name.upper()

    # High relevance indicators
    high_relevance_patterns = [
        # Blood pressure patterns (common HRS question numbers)
        '010', '011', '012',  # Often BP-related
        # Diabetes patterns
        '020', '021', '022',  # Often diabetes-related
        # Heart conditions
        '030', '031', '032',  # Often heart-related
        # Cholesterol
        '040', '041', '042',  # Often cholesterol-related
        # Medications
        '150', '151', '152', '153', '154', '155',
    ]

    if any(pattern in var_name for pattern in high_relevance_patterns):
        return 'High'
    elif any(term in var_upper for term in ['CONDITION', 'DISEASE', 'DOCTOR', 'MED']):
        return 'Medium'
    elif categorize_variable(var_name) in ['Chronic Conditions', 'Medications', 'Doctor Visits']:
        return 'Medium'
    else:
        return 'Low'

def get_priority(var_name):
    """Assign priority for 3H research"""

    relevance = assess_3h_relevance(var_name)
    category = categorize_variable(var_name)

    if relevance == 'High':
        return 1
    elif relevance == 'Medium' or category in ['Chronic Conditions', 'General Health Status']:
        return 2
    elif category == 'Identifiers':
        return 1  # Always need IDs
    else:
        return 3

def create_3h_summary(all_decoded, output_path):
    """Create summary focused on 3H diseases"""

    priority_vars = []

    for file_name, decoded_vars in all_decoded.items():
        for var_info in decoded_vars:
            if var_info['Priority'] <= 2:  # High and medium priority
                priority_vars.append({
                    'File': file_name,
                    **var_info
                })

    if priority_vars:
        summary_df = pd.DataFrame(priority_vars)
        summary_file = output_path / "HRS_3H_Priority_Variables.xlsx"

        with pd.ExcelWriter(summary_file, engine='openpyxl') as writer:
            # All priority variables
            summary_df.to_excel(writer, sheet_name='All_Priority', index=False)

            # By file
            for file_name in summary_df['File'].unique():
                file_vars = summary_df[summary_df['File'] == file_name]
                sheet_name = file_name[:30]  # Excel sheet name limit
                file_vars.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"\n{'='*60}")
        print(f"3H PRIORITY SUMMARY: {summary_file}")
        print(f"Priority variables found: {len(priority_vars)}")

        # Show summary by file
        file_counts = summary_df.groupby('File').size()
        for file_name, count in file_counts.items():
            print(f"  {file_name}: {count} priority variables")

if __name__ == '__main__':
    decode_hrs_variables()
    print(f"\n{'='*60}")
    print("DECODING COMPLETE!")
    print("\nKey findings:")
    print("- SC prefix = Section C (Health Status)")
    print("- SE prefix = Section E (Medical History)")
    print("- RC/RE = 2020 equivalents")
    print("\nNext steps:")
    print("1. Review HRS_3H_Priority_Variables.xlsx")
    print("2. Cross-reference with actual data samples")
    print("3. Select specific variables for analysis")