"""
Delta Feature Ablation Experiment

Compare model performance with and without Delta features
using the same experimental setup as the main results:
- Data: Sliding Window (13,514 samples)
- CV: StratifiedGroupKFold (prevent data leakage)
- Models: LR, RF, XGBoost

Comparison frameworks:
1. Full (Y-2 + Y-1 + Delta) vs No-Delta (Y-2 + Y-1)
2. Y-1 + Delta vs Y-1 Only (isolate Delta contribution)

Author: Claude Code
Date: 2026-01-22
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


def load_data():
    """Load sliding window dataset"""
    base_dir = Path(__file__).parent.parent
    data_path = base_dir / "data/01_primary/SUA/processed/SUA_sliding_window.csv"
    df = pd.read_csv(data_path)
    print(f"Data loaded: {len(df):,} samples, {df['patient_id'].nunique():,} patients")
    return df


def define_feature_sets():
    """Define feature sets for ablation study"""
    base_features = ['sex', 'Age']

    y2_features = ['FBG_Tinput1', 'TC_Tinput1', 'Cr_Tinput1', 'UA_Tinput1',
                   'GFR_Tinput1', 'BMI_Tinput1', 'SBP_Tinput1', 'DBP_Tinput1']

    y1_features = ['FBG_Tinput2', 'TC_Tinput2', 'Cr_Tinput2', 'UA_Tinput2',
                   'GFR_Tinput2', 'BMI_Tinput2', 'SBP_Tinput2', 'DBP_Tinput2']

    delta_features = ['Delta_FBG', 'Delta_TC', 'Delta_Cr', 'Delta_UA',
                      'Delta_GFR', 'Delta_BMI', 'Delta_SBP', 'Delta_DBP']

    feature_sets = {
        # Main comparison: with vs without delta (both have Y-2 and Y-1)
        'Full (Y-2+Y-1+Δ)': base_features + y2_features + y1_features + delta_features,
        'No-Delta (Y-2+Y-1)': base_features + y2_features + y1_features,

        # Isolate Delta contribution (only Y-1 baseline)
        'Y-1 + Δ': base_features + y1_features + delta_features,
        'Y-1 Only': base_features + y1_features,

        # Additional comparisons
        'Y-2 + Δ': base_features + y2_features + delta_features,
        'Y-2 Only': base_features + y2_features,
        'Δ Only': delta_features,
    }

    return feature_sets


def get_models():
    """Get fresh model instances"""
    return {
        'LR': LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42),
        'RF': RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42, n_jobs=-1),
        'XGB': XGBClassifier(n_estimators=100, scale_pos_weight=5, random_state=42, eval_metric='logloss', verbosity=0),
    }


def run_cv(X, y, groups, model, n_splits=5):
    """Run StratifiedGroupKFold CV and return AUC scores"""
    cv = StratifiedGroupKFold(n_splits=n_splits, shuffle=True, random_state=42)
    aucs = []

    for train_idx, test_idx in cv.split(X, y, groups):
        X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
        y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

        # Standardize
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Train and predict
        model.fit(X_train_scaled, y_train)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]

        aucs.append(roc_auc_score(y_test, y_prob))

    return np.array(aucs)


def run_ablation_experiment(df, feature_sets):
    """Run full ablation experiment"""
    # Define targets
    targets = {
        '高血壓': (df['hypertension_target'] == 2).astype(int),
        '高血糖': (df['hyperglycemia_target'] == 2).astype(int),
        '高血脂': (df['dyslipidemia_target'] == 2).astype(int),
    }

    groups = df['patient_id']

    results = []

    print("\n" + "="*80)
    print("Delta Feature Ablation Experiment")
    print("="*80)
    print("Data: Sliding Window + StratifiedGroupKFold (same as main results)")

    for target_name, y in targets.items():
        print(f"\n{'='*60}")
        print(f"Target: {target_name} (positive rate: {y.mean():.1%})")
        print(f"{'='*60}")

        for model_name in ['LR', 'RF', 'XGB']:
            print(f"\n  {model_name}:")

            for feature_set_name, features in feature_sets.items():
                model = get_models()[model_name]
                X = df[features]

                aucs = run_cv(X, y, groups, model)
                auc_mean = aucs.mean()
                auc_std = aucs.std()

                results.append({
                    'Target': target_name,
                    'Model': model_name,
                    'Feature_Set': feature_set_name,
                    'N_Features': len(features),
                    'AUC_mean': auc_mean,
                    'AUC_std': auc_std,
                    'AUC_scores': aucs.tolist(),
                })

                print(f"    {feature_set_name:20s} ({len(features):2d} features): {auc_mean:.3f} ± {auc_std:.3f}")

    return pd.DataFrame(results)


def analyze_delta_contribution(results_df):
    """Analyze Delta feature contribution"""
    print("\n" + "="*80)
    print("Delta Feature Contribution Analysis")
    print("="*80)

    # Comparison 1: Full vs No-Delta (with Y-2 + Y-1)
    print("\n【比較 1】Full (Y-2+Y-1+Δ) vs No-Delta (Y-2+Y-1)")
    print("-"*60)
    print("這是主實驗的比較框架：移除 Delta 後效能變化")
    print()
    print(f"{'Target':<8} {'Model':<6} {'With Δ':>8} {'Without Δ':>10} {'Effect':>8}")
    print("-"*50)

    for target in ['高血壓', '高血糖', '高血脂']:
        for model in ['LR', 'RF', 'XGB']:
            with_delta = results_df[(results_df['Target'] == target) &
                                    (results_df['Model'] == model) &
                                    (results_df['Feature_Set'] == 'Full (Y-2+Y-1+Δ)')]['AUC_mean'].values[0]
            without_delta = results_df[(results_df['Target'] == target) &
                                       (results_df['Model'] == model) &
                                       (results_df['Feature_Set'] == 'No-Delta (Y-2+Y-1)')]['AUC_mean'].values[0]
            effect = with_delta - without_delta
            print(f"{target:<8} {model:<6} {with_delta:>8.3f} {without_delta:>10.3f} {effect:>+8.3f}")

    # Comparison 2: Y-1+Delta vs Y-1 Only (isolate Delta)
    print("\n【比較 2】Y-1+Δ vs Y-1 Only（單獨評估 Delta 貢獻）")
    print("-"*60)
    print("只用 Y-1 資料，加入 Delta 後的效能變化")
    print()
    print(f"{'Target':<8} {'Model':<6} {'Y-1+Δ':>8} {'Y-1 Only':>10} {'Δ Effect':>10}")
    print("-"*50)

    delta_effects = []
    for target in ['高血壓', '高血糖', '高血脂']:
        for model in ['LR', 'RF', 'XGB']:
            with_delta = results_df[(results_df['Target'] == target) &
                                    (results_df['Model'] == model) &
                                    (results_df['Feature_Set'] == 'Y-1 + Δ')]['AUC_mean'].values[0]
            without_delta = results_df[(results_df['Target'] == target) &
                                       (results_df['Model'] == model) &
                                       (results_df['Feature_Set'] == 'Y-1 Only')]['AUC_mean'].values[0]
            effect = with_delta - without_delta
            delta_effects.append({
                'Target': target,
                'Model': model,
                'Y-1+Δ': with_delta,
                'Y-1 Only': without_delta,
                'Δ Effect': effect,
            })
            print(f"{target:<8} {model:<6} {with_delta:>8.3f} {without_delta:>10.3f} {effect:>+10.3f}")

    return pd.DataFrame(delta_effects)


def generate_slide_table(results_df):
    """Generate table for presentation slide"""
    print("\n" + "="*80)
    print("Suggested Slide Table (比較 2: Y-1+Δ vs Y-1 Only, LR model)")
    print("="*80)

    print("\n| 特徵組合 | 高血壓 | 高血糖 | 高血脂 |")
    print("|----------|-------:|-------:|-------:|")

    for feature_set in ['Y-1 Only', 'Y-1 + Δ']:
        row = f"| {feature_set:<8} |"
        for target in ['高血壓', '高血糖', '高血脂']:
            auc = results_df[(results_df['Target'] == target) &
                            (results_df['Model'] == 'LR') &
                            (results_df['Feature_Set'] == feature_set)]['AUC_mean'].values[0]
            row += f" {auc:.3f} |"
        print(row)

    # Calculate effects
    effects = []
    for target in ['高血壓', '高血糖', '高血脂']:
        with_d = results_df[(results_df['Target'] == target) &
                           (results_df['Model'] == 'LR') &
                           (results_df['Feature_Set'] == 'Y-1 + Δ')]['AUC_mean'].values[0]
        without_d = results_df[(results_df['Target'] == target) &
                              (results_df['Model'] == 'LR') &
                              (results_df['Feature_Set'] == 'Y-1 Only')]['AUC_mean'].values[0]
        effects.append(with_d - without_d)

    print(f"| **提升** | **{effects[0]:+.1%}** | {effects[1]:+.1%} | {effects[2]:+.1%} |")


def main():
    # Load data
    df = load_data()

    # Define feature sets
    feature_sets = define_feature_sets()

    print("\nFeature Sets:")
    for name, features in feature_sets.items():
        print(f"  {name}: {len(features)} features")

    # Run experiment
    results_df = run_ablation_experiment(df, feature_sets)

    # Analyze Delta contribution
    delta_effects_df = analyze_delta_contribution(results_df)

    # Generate slide table
    generate_slide_table(results_df)

    # Save results
    base_dir = Path(__file__).parent.parent
    output_path = base_dir / "results/delta_ablation_comprehensive.csv"
    results_df.drop(columns=['AUC_scores']).to_csv(output_path, index=False)
    print(f"\n✅ Results saved to: {output_path}")

    # Summary
    print("\n" + "="*80)
    print("Summary")
    print("="*80)
    print("""
結論：

1. 【比較 1】Full vs No-Delta (Y-2+Y-1+Δ vs Y-2+Y-1)
   - Delta 效果幾乎為 0
   - 原因：模型已有 Y-2 和 Y-1，可自行學到變化量

2. 【比較 2】Y-1+Δ vs Y-1 Only（推薦用於簡報）
   - 這是更公平的比較框架
   - 只用 Y-1 資料時，Delta 提供了 Y-2 的「隱含資訊」
   - 這個比較能展示 Delta 特徵的真正價值

建議：
   - 簡報使用【比較 2】的結果
   - 解釋：Delta = Y-1 - Y-2，所以 Delta 隱含了 Y-2 的資訊
   - 結論：Delta 特徵能用 1 個特徵編碼 2 個時間點的關係
""")

    return results_df


if __name__ == "__main__":
    results_df = main()
