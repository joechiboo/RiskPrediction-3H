"""
5-Fold Cross-Validation Model Comparison
Run all models with 5-fold stratified CV and generate comparison results.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
warnings.filterwarnings('ignore')

from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.base import clone
from sklearn.metrics import (
    roc_auc_score, f1_score,
    balanced_accuracy_score, confusion_matrix, roc_curve
)
import xgboost as xgb
# import lightgbm as lgb  # Removed - not installed
from scipy import stats

# Set paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'SUA_CVDs_wide_format.csv')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')

# Set Chinese font
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 80)
print("5-Fold Cross-Validation Model Comparison")
print("=" * 80)

# Load data
df = pd.read_csv(DATA_PATH)
print(f"\nData loaded: {df.shape[0]:,} patients, {df.shape[1]} columns")

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

# Convert targets: 1=normal, 2=disease -> 0=normal, 1=disease
targets = {}
for name, col in target_cols.items():
    targets[name] = (df[col] == 2).astype(int)

print("\nClass Imbalance:")
for name, y in targets.items():
    pos_rate = y.mean() * 100
    neg_count = (y == 0).sum()
    pos_count = (y == 1).sum()
    ratio = neg_count / pos_count
    print(f"  {name}: {pos_rate:.2f}% prevalence (neg:pos = {ratio:.1f}:1)")


def get_models(random_state=42):
    """Return dictionary of all models to compare"""
    return {
        'LR': LogisticRegression(
            class_weight='balanced',
            max_iter=1000,
            random_state=random_state
        ),
        'DT': DecisionTreeClassifier(
            max_depth=10,
            min_samples_split=20,
            min_samples_leaf=10,
            class_weight='balanced',
            random_state=random_state
        ),
        'RF': RandomForestClassifier(
            n_estimators=100,
            max_depth=15,
            min_samples_split=10,
            class_weight='balanced',
            random_state=random_state,
            n_jobs=-1
        ),
        'XGB': xgb.XGBClassifier(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            scale_pos_weight=5,
            random_state=random_state,
            eval_metric='logloss',
            verbosity=0
        ),
        'SVM': SVC(
            kernel='rbf',
            class_weight='balanced',
            probability=True,
            random_state=random_state
        ),
        'MLP': MLPClassifier(
            hidden_layer_sizes=(64, 32, 16),
            activation='relu',
            solver='adam',
            learning_rate_init=0.001,
            max_iter=500,
            random_state=random_state,
            early_stopping=True,
            validation_fraction=0.1
        )
    }


def evaluate_model_cv(X, y, model, n_splits=5, random_state=42):
    """
    Evaluate a model using stratified k-fold cross-validation.
    """
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)

    fold_metrics = {
        'auc': [], 'sensitivity': [], 'specificity': [],
        'f1': [], 'balanced_acc': [], 'y_true': [], 'y_prob': []
    }

    for fold, (train_idx, test_idx) in enumerate(cv.split(X, y)):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        # Standardize
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Clone model
        model_clone = clone(model)

        # Adjust XGBoost scale_pos_weight
        if hasattr(model_clone, 'scale_pos_weight'):
            scale = (y_train == 0).sum() / (y_train == 1).sum()
            model_clone.set_params(scale_pos_weight=scale)

        # Train
        model_clone.fit(X_train_scaled, y_train)

        # Predict
        y_prob = model_clone.predict_proba(X_test_scaled)[:, 1]
        y_pred = model_clone.predict(X_test_scaled)

        # Metrics
        fold_metrics['auc'].append(roc_auc_score(y_test, y_prob))

        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
        fold_metrics['sensitivity'].append(tp / (tp + fn) if (tp + fn) > 0 else 0)
        fold_metrics['specificity'].append(tn / (tn + fp) if (tn + fp) > 0 else 0)
        fold_metrics['f1'].append(f1_score(y_test, y_pred, zero_division=0))
        fold_metrics['balanced_acc'].append(balanced_accuracy_score(y_test, y_pred))

        fold_metrics['y_true'].extend(y_test.tolist())
        fold_metrics['y_prob'].extend(y_prob.tolist())

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

    result['y_true_all'] = fold_metrics['y_true']
    result['y_prob_all'] = fold_metrics['y_prob']

    return result


# Run 5-fold CV
print("\n" + "=" * 80)
print("Running 5-Fold Cross-Validation")
print("=" * 80)

all_results = []
detailed_results = {}
model_names = list(get_models().keys())

for disease_name, y in targets.items():
    print(f"\n{'=' * 60}")
    print(f"{disease_name}")
    print(f"{'=' * 60}")

    detailed_results[disease_name] = {}

    models = get_models()
    for model_name, model in models.items():
        print(f"  Training {model_name}...", end=" ")

        result = evaluate_model_cv(X, y, model)
        detailed_results[disease_name][model_name] = result

        all_results.append({
            'Disease': disease_name,
            'Model': model_name,
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
            'Balanced_Acc_std': result['balanced_acc_std']
        })

        print(f"AUC = {result['auc_mean']:.3f} +/- {result['auc_std']:.3f}")

results_df = pd.DataFrame(all_results)

# Display results
print("\n" + "=" * 100)
print("5-Fold CV Results Summary")
print("=" * 100)

for disease in targets.keys():
    print(f"\n--- {disease} ---")
    disease_df = results_df[results_df['Disease'] == disease].copy()
    disease_df = disease_df.sort_values('AUC', ascending=False)

    display_df = disease_df[['Model', 'AUC', 'AUC_std', 'AUC_CI',
                             'Sensitivity', 'Specificity', 'F1', 'Balanced_Acc']].copy()
    display_df = display_df.round(3)
    print(display_df.to_string(index=False))

# Statistical tests
print("\n" + "=" * 80)
print("Statistical Significance Tests (Paired t-test on AUC)")
print("=" * 80)

for disease_name in targets.keys():
    print(f"\n--- {disease_name} ---")

    best_model = None
    best_auc = 0
    for model_name in model_names:
        auc = detailed_results[disease_name][model_name]['auc_mean']
        if auc > best_auc:
            best_auc = auc
            best_model = model_name

    print(f"Best model: {best_model} (AUC = {best_auc:.3f})")
    print(f"Comparison with other models:")

    best_folds = detailed_results[disease_name][best_model]['auc_folds']

    for model_name in model_names:
        if model_name == best_model:
            continue

        other_folds = detailed_results[disease_name][model_name]['auc_folds']
        other_auc = detailed_results[disease_name][model_name]['auc_mean']

        t_stat, p_value = stats.ttest_rel(best_folds, other_folds)

        sig = "*" if p_value < 0.05 else ""
        sig += "*" if p_value < 0.01 else ""
        sig += "*" if p_value < 0.001 else ""

        diff = best_auc - other_auc
        print(f"  vs {model_name}: diff={diff:+.3f}, p={p_value:.4f} {sig}")

# Generate visualizations
print("\n" + "=" * 80)
print("Generating Visualizations")
print("=" * 80)

# 1. AUC comparison bar chart
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
diseases = list(targets.keys())
colors = plt.cm.Set2(np.linspace(0, 1, len(model_names)))

for idx, disease in enumerate(diseases):
    ax = axes[idx]
    disease_data = results_df[results_df['Disease'] == disease].sort_values('AUC', ascending=True)

    y_pos = np.arange(len(disease_data))
    bars = ax.barh(y_pos, disease_data['AUC'], xerr=disease_data['AUC_std'],
                   color=[colors[model_names.index(m)] for m in disease_data['Model']],
                   capsize=3, alpha=0.8)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(disease_data['Model'])
    ax.set_xlabel('AUC', fontsize=12)
    ax.set_title(f'{disease}', fontsize=14)
    ax.set_xlim(0.5, 1.0)
    ax.axvline(x=0.7, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=0.8, color='green', linestyle='--', alpha=0.5)

    for i, (v, s) in enumerate(zip(disease_data['AUC'], disease_data['AUC_std'])):
        ax.text(v + s + 0.01, i, f'{v:.3f}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '5fold_cv_auc_comparison.png'), dpi=150, bbox_inches='tight')
print("  Saved: 5fold_cv_auc_comparison.png")

# 2. ROC curves
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for idx, disease in enumerate(diseases):
    ax = axes[idx]

    for i, model_name in enumerate(model_names):
        y_true = detailed_results[disease][model_name]['y_true_all']
        y_prob = detailed_results[disease][model_name]['y_prob_all']
        auc = detailed_results[disease][model_name]['auc_mean']

        fpr, tpr, _ = roc_curve(y_true, y_prob)
        ax.plot(fpr, tpr, color=colors[i], lw=2,
                label=f'{model_name} ({auc:.3f})')

    ax.plot([0, 1], [0, 1], 'k--', lw=1)
    ax.set_xlabel('False Positive Rate', fontsize=12)
    ax.set_ylabel('True Positive Rate', fontsize=12)
    ax.set_title(f'{disease}', fontsize=14)
    ax.legend(loc='lower right', fontsize=8)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '5fold_cv_roc_curves.png'), dpi=150, bbox_inches='tight')
print("  Saved: 5fold_cv_roc_curves.png")

# 3. Heatmap
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
metrics_to_show = ['AUC', 'Sensitivity', 'Specificity', 'F1', 'Balanced_Acc']

for idx, disease in enumerate(diseases):
    ax = axes[idx]

    disease_data = results_df[results_df['Disease'] == disease]
    heatmap_data = disease_data.set_index('Model')[metrics_to_show]

    sns.heatmap(heatmap_data, annot=True, fmt='.3f', cmap='RdYlGn',
                ax=ax, vmin=0, vmax=1, cbar=idx==2)
    ax.set_title(f'{disease}', fontsize=14)
    ax.set_xlabel('')

plt.tight_layout()
plt.savefig(os.path.join(RESULTS_DIR, '5fold_cv_metrics_heatmap.png'), dpi=150, bbox_inches='tight')
print("  Saved: 5fold_cv_metrics_heatmap.png")

plt.close('all')

# Save results
results_df.to_csv(os.path.join(RESULTS_DIR, '5fold_cv_model_comparison.csv'), index=False)
print(f"\nSaved: 5fold_cv_model_comparison.csv")

# Summary table
summary_table = []
for disease in diseases:
    row = {'Disease': disease}
    for model_name in model_names:
        auc = detailed_results[disease][model_name]['auc_mean']
        std = detailed_results[disease][model_name]['auc_std']
        row[model_name] = f"{auc:.3f} ({std:.3f})"
    summary_table.append(row)

summary_df = pd.DataFrame(summary_table)
summary_df.to_csv(os.path.join(RESULTS_DIR, '5fold_cv_summary_table.csv'), index=False)
print("Saved: 5fold_cv_summary_table.csv")

print("\n" + "=" * 100)
print("Summary Table (AUC with std)")
print("=" * 100)
print(summary_df.to_string(index=False))

# Model ranking
print("\n" + "=" * 80)
print("Model Rankings by AUC")
print("=" * 80)

ranking_data = []
for disease in diseases:
    disease_df = results_df[results_df['Disease'] == disease].sort_values('AUC', ascending=False)
    for rank, (_, row) in enumerate(disease_df.iterrows(), 1):
        ranking_data.append({
            'Disease': disease,
            'Rank': rank,
            'Model': row['Model'],
            'AUC': row['AUC']
        })

ranking_df = pd.DataFrame(ranking_data)

avg_ranking = ranking_df.groupby('Model')['Rank'].mean().sort_values()
print("\nAverage Ranking (lower is better):")
for model, avg_rank in avg_ranking.items():
    print(f"  {model}: {avg_rank:.2f}")

print("\nBest Model per Disease:")
for disease in diseases:
    best = ranking_df[(ranking_df['Disease'] == disease) & (ranking_df['Rank'] == 1)].iloc[0]
    print(f"  {disease}: {best['Model']} (AUC = {best['AUC']:.3f})")

print("\n" + "=" * 80)
print("5-Fold CV Complete!")
print("=" * 80)
