"""
5-Fold Cross-Validation for PySR (Symbolic Regression)
Adds PySR to the model comparison with proper CV evaluation.

Note: PySR is slow (~5-10 min per fold), so this script runs separately.
"""
import pandas as pd
import numpy as np
import time
import warnings
import os
warnings.filterwarnings('ignore')

from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score, f1_score, balanced_accuracy_score, confusion_matrix
from scipy import stats

# PySR
try:
    from pysr import PySRRegressor
    PYSR_AVAILABLE = True
except ImportError:
    print("PySR not installed. Run: pip install pysr")
    PYSR_AVAILABLE = False

# Set paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'SUA_CVDs_wide_format.csv')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

print("=" * 80)
print("5-Fold Cross-Validation for PySR")
print("=" * 80)

if not PYSR_AVAILABLE:
    exit(1)

# Load data
df = pd.read_csv(DATA_PATH)
print(f"\nData loaded: {df.shape[0]:,} patients")

# Define features and targets
feature_cols = [
    'sex', 'Age',
    'FBG_T1', 'TC_T1', 'Cr_T1', 'UA_T1', 'GFR_T1', 'BMI_T1', 'SBP_T1', 'DBP_T1',
    'FBG_T2', 'TC_T2', 'Cr_T2', 'UA_T2', 'GFR_T2', 'BMI_T2', 'SBP_T2', 'DBP_T2',
    'Delta1_FBG', 'Delta1_TC', 'Delta1_Cr', 'Delta1_UA', 'Delta1_GFR', 'Delta1_BMI', 'Delta1_SBP', 'Delta1_DBP'
]

target_cols = {
    'Hypertension': 'hypertension_T3',
    'Hyperglycemia': 'hyperglycemia_T3',
    'Dyslipidemia': 'dyslipidemia_T3'
}

X = df[feature_cols].copy()

targets = {}
for name, col in target_cols.items():
    targets[name] = (df[col] == 2).astype(int)


def evaluate_pysr_cv(X, y, n_splits=5, niterations=100, timeout=600, random_state=42):
    """
    Evaluate PySR using stratified k-fold cross-validation.
    """
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    fold_metrics = {
        'auc': [], 'sensitivity': [], 'specificity': [],
        'f1': [], 'balanced_acc': [], 'formulas': [], 'times': []
    }

    for fold, (train_idx, test_idx) in enumerate(cv.split(X, y)):
        print(f"    Fold {fold+1}/{n_splits}...", end=" ", flush=True)
        start_time = time.time()

        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        # Standardize
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Convert to DataFrame for PySR
        X_train_df = pd.DataFrame(X_train_scaled, columns=feature_cols)
        X_test_df = pd.DataFrame(X_test_scaled, columns=feature_cols)
        y_train_reset = y_train.reset_index(drop=True)
        y_test_reset = y_test.reset_index(drop=True)

        # PySR model
        model = PySRRegressor(
            niterations=niterations,
            populations=15,
            binary_operators=["+", "-", "*", "/"],
            unary_operators=["exp", "log", "sqrt", "abs"],
            maxsize=20,
            timeout_in_seconds=timeout,
            temp_equation_file=True,
            verbosity=0,
            random_state=random_state + fold,
        )

        # Train
        model.fit(X_train_df, y_train_reset)

        # Predict
        y_pred_raw = model.predict(X_test_df)
        y_pred_proba = np.clip(y_pred_raw, 0, 1)

        # Threshold based on training prevalence
        threshold = y_train_reset.mean()
        y_pred = (y_pred_proba >= threshold).astype(int)

        # Metrics
        try:
            auc = roc_auc_score(y_test_reset, y_pred_proba)
        except:
            auc = 0.5

        tn, fp, fn, tp = confusion_matrix(y_test_reset, y_pred).ravel()
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        f1 = f1_score(y_test_reset, y_pred, zero_division=0)
        bal_acc = balanced_accuracy_score(y_test_reset, y_pred)

        fold_time = time.time() - start_time
        formula = str(model.sympy())

        fold_metrics['auc'].append(auc)
        fold_metrics['sensitivity'].append(sensitivity)
        fold_metrics['specificity'].append(specificity)
        fold_metrics['f1'].append(f1)
        fold_metrics['balanced_acc'].append(bal_acc)
        fold_metrics['formulas'].append(formula)
        fold_metrics['times'].append(fold_time)

        print(f"AUC={auc:.3f}, time={fold_time/60:.1f}min")

    # Summary statistics
    result = {}
    for metric in ['auc', 'sensitivity', 'specificity', 'f1', 'balanced_acc']:
        values = fold_metrics[metric]
        result[f'{metric}_mean'] = np.mean(values)
        result[f'{metric}_std'] = np.std(values)
        result[f'{metric}_folds'] = values

        # 95% CI
        ci = stats.t.interval(0.95, len(values)-1, loc=np.mean(values), scale=stats.sem(values))
        result[f'{metric}_ci_lower'] = ci[0]
        result[f'{metric}_ci_upper'] = ci[1]

    result['formulas'] = fold_metrics['formulas']
    result['total_time'] = sum(fold_metrics['times'])

    return result


# Run 5-fold CV for PySR
print("\n" + "=" * 80)
print("Running 5-Fold CV for PySR")
print("Warning: This may take 30-60 minutes total")
print("=" * 80)

pysr_results = []
detailed_results = {}

for disease_name, y in targets.items():
    print(f"\n{'=' * 60}")
    print(f"{disease_name}")
    print(f"{'=' * 60}")

    result = evaluate_pysr_cv(
        X, y,
        n_splits=5,
        niterations=100,  # Reduced for speed
        timeout=300,      # 5 min per fold max
        random_state=42
    )

    detailed_results[disease_name] = result

    pysr_results.append({
        'Disease': disease_name,
        'Model': 'PySR',
        'AUC': result['auc_mean'],
        'AUC_std': result['auc_std'],
        'AUC_CI': f"({result['auc_ci_lower']:.3f}, {result['auc_ci_upper']:.3f})",
        'Sensitivity': result['sensitivity_mean'],
        'Sensitivity_std': result['sensitivity_std'],
        'Specificity': result['specificity_mean'],
        'Specificity_std': result['specificity_std'],
        'F1': result['f1_mean'],
        'F1_std': result['f1_std'],
        'Balanced_Acc': result['balanced_acc_mean'],
        'Balanced_Acc_std': result['balanced_acc_std'],
        'Total_Time_min': result['total_time'] / 60
    })

    print(f"\n  Summary: AUC = {result['auc_mean']:.3f} +/- {result['auc_std']:.3f}")
    print(f"  Total time: {result['total_time']/60:.1f} minutes")
    print(f"  Formulas found:")
    for i, f in enumerate(result['formulas']):
        print(f"    Fold {i+1}: {f}")

# Save results
results_df = pd.DataFrame(pysr_results)
results_df.to_csv(os.path.join(RESULTS_DIR, '5fold_cv_pysr_results.csv'), index=False)
print(f"\n\nSaved: 5fold_cv_pysr_results.csv")

# Display summary
print("\n" + "=" * 100)
print("PySR 5-Fold CV Results Summary")
print("=" * 100)

for disease in targets.keys():
    r = detailed_results[disease]
    print(f"\n{disease}:")
    print(f"  AUC: {r['auc_mean']:.3f} +/- {r['auc_std']:.3f} (95% CI: {r['auc_ci_lower']:.3f}-{r['auc_ci_upper']:.3f})")
    print(f"  Sensitivity: {r['sensitivity_mean']:.3f} +/- {r['sensitivity_std']:.3f}")
    print(f"  Specificity: {r['specificity_mean']:.3f} +/- {r['specificity_std']:.3f}")

# Merge with existing results
print("\n" + "=" * 80)
print("Comparison with other models")
print("=" * 80)

try:
    existing_df = pd.read_csv(os.path.join(RESULTS_DIR, '5fold_cv_model_comparison.csv'))
    combined_df = pd.concat([existing_df, results_df], ignore_index=True)
    combined_df.to_csv(os.path.join(RESULTS_DIR, '5fold_cv_all_models.csv'), index=False)
    print("Saved: 5fold_cv_all_models.csv (combined with other models)")

    # Summary table
    print("\nAUC Comparison (mean ± std):")
    for disease in targets.keys():
        print(f"\n{disease}:")
        disease_data = combined_df[combined_df['Disease'] == disease].sort_values('AUC', ascending=False)
        for _, row in disease_data.iterrows():
            print(f"  {row['Model']}: {row['AUC']:.3f} ({row['AUC_std']:.3f})")
except FileNotFoundError:
    print("Note: Run run_5fold_cv.py first to get comparison with other models")

print("\n" + "=" * 80)
print("PySR 5-Fold CV Complete!")
print("=" * 80)
