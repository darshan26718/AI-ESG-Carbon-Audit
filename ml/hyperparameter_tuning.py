"""
Hyperparameter Tuning Module
============================

Purpose:
--------
1. Random Forest Hyperparameter Tuning
2. XGBoost Hyperparameter Tuning
3. ESG Model Optimization
4. Carbon Forecast Model Optimization
5. Predictive Maintenance Model Optimization
6. Save Best Tuned Models

Datasets:
---------
data/carbon_emission_dataset.csv
data/maintenance_failure_dataset.csv
data/esg_benchmark_dataset.csv

Outputs:
--------
models/best_carbon_model.pkl
models/best_maintenance_model.pkl
models/best_esg_model.pkl

Author:
-------
AI-ESG-Predictive-Maintenance
"""

import os
import joblib
import warnings
import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV
)

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import (
    RandomForestRegressor,
    RandomForestClassifier
)

from sklearn.metrics import (
    r2_score,
    accuracy_score
)

warnings.filterwarnings("ignore")

try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except:
    XGBOOST_AVAILABLE = False


# ==========================================================
# PATHS
# ==========================================================

CARBON_DATASET = "data/carbon_emission_dataset.csv"

MAINTENANCE_DATASET = (
    "data/maintenance_failure_dataset.csv"
)

ESG_DATASET = "data/esg_benchmark_dataset.csv"


# ==========================================================
# DATA PREPARATION
# ==========================================================

def prepare_dataset(
    file_path,
    target_column
):
    """
    Load and prepare dataset.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    df.dropna(inplace=True)

    X = df.drop(columns=[target_column])

    y = df[target_column]

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y


# ==========================================================
# RANDOM FOREST REGRESSOR TUNING
# ==========================================================

def tune_rf_regressor(
    X,
    y
):
    """
    Tune Random Forest Regressor.
    """

    print("\nTuning Carbon/ESG Model...")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(
        X_train
    )

    X_test = scaler.transform(
        X_test
    )

    param_grid = {
        "n_estimators": [100, 200, 300, 500],
        "max_depth": [5, 8, 10, 15, 20],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    rf = RandomForestRegressor(
        random_state=42
    )

    search = RandomizedSearchCV(
        estimator=rf,
        param_distributions=param_grid,
        n_iter=20,
        cv=5,
        scoring="r2",
        random_state=42,
        n_jobs=-1
    )

    search.fit(
        X_train,
        y_train
    )

    best_model = search.best_estimator_

    predictions = best_model.predict(
        X_test
    )

    score = r2_score(
        y_test,
        predictions
    )

    print(
        f"Best R² Score: {score:.4f}"
    )

    print(
        f"Best Parameters: {search.best_params_}"
    )

    return best_model, scaler


# ==========================================================
# RANDOM FOREST CLASSIFIER TUNING
# ==========================================================

def tune_rf_classifier(
    X,
    y
):
    """
    Tune Predictive Maintenance Model.
    """

    print("\nTuning Maintenance Model...")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        stratify=y,
        test_size=0.20,
        random_state=42
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(
        X_train
    )

    X_test = scaler.transform(
        X_test
    )

    param_grid = {
        "n_estimators": [100, 200, 300, 500],
        "max_depth": [5, 10, 15, 20],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    }

    rf = RandomForestClassifier(
        random_state=42
    )

    search = RandomizedSearchCV(
        estimator=rf,
        param_distributions=param_grid,
        n_iter=20,
        cv=5,
        scoring="accuracy",
        random_state=42,
        n_jobs=-1
    )

    search.fit(
        X_train,
        y_train
    )

    best_model = search.best_estimator_

    predictions = best_model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(
        f"Best Accuracy: {accuracy:.4f}"
    )

    print(
        f"Best Parameters: {search.best_params_}"
    )

    return best_model, scaler


# ==========================================================
# XGBOOST TUNING
# ==========================================================

def tune_xgboost(
    X,
    y
):
    """
    Tune XGBoost Classifier.
    """

    if not XGBOOST_AVAILABLE:
        print(
            "\nXGBoost not installed."
        )
        return None, None

    print("\nTuning XGBoost...")

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        stratify=y,
        test_size=0.20,
        random_state=42
    )

    scaler = StandardScaler()

    X_train = scaler.fit_transform(
        X_train
    )

    X_test = scaler.transform(
        X_test
    )

    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [3, 5, 7, 10],
        "learning_rate": [0.01, 0.05, 0.1],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0]
    }

    xgb = XGBClassifier(
        eval_metric="logloss",
        random_state=42
    )

    search = RandomizedSearchCV(
        estimator=xgb,
        param_distributions=param_grid,
        n_iter=20,
        cv=5,
        scoring="accuracy",
        random_state=42,
        n_jobs=-1
    )

    search.fit(
        X_train,
        y_train
    )

    best_model = search.best_estimator_

    predictions = best_model.predict(
        X_test
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(
        f"Best XGBoost Accuracy: {accuracy:.4f}"
    )

    print(
        f"Best Parameters: {search.best_params_}"
    )

    return best_model, scaler


# ==========================================================
# SAVE MODEL
# ==========================================================

def save_model(
    model,
    file_name
):
    """
    Save model.
    """

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        file_name
    )

    print(
        f"Saved: {file_name}"
    )


# ==========================================================
# MAIN
# ==========================================================

def main():

    print("=" * 60)
    print("HYPERPARAMETER TUNING")
    print("=" * 60)

    # Carbon Model
    try:

        X, y = prepare_dataset(
            CARBON_DATASET,
            "Carbon_Emission"
        )

        model, scaler = tune_rf_regressor(
            X,
            y
        )

        save_model(
            model,
            "models/best_carbon_model.pkl"
        )

    except Exception as e:

        print(
            f"\nCarbon Tuning Failed: {e}"
        )

    # ESG Model
    try:

        X, y = prepare_dataset(
            ESG_DATASET,
            "ESG_Score"
        )

        model, scaler = tune_rf_regressor(
            X,
            y
        )

        save_model(
            model,
            "models/best_esg_model.pkl"
        )

    except Exception as e:

        print(
            f"\nESG Tuning Failed: {e}"
        )

    # Maintenance Model
    try:

        X, y = prepare_dataset(
            MAINTENANCE_DATASET,
            "Failure"
        )

        model, scaler = tune_rf_classifier(
            X,
            y
        )

        save_model(
            model,
            "models/best_maintenance_rf.pkl"
        )

        if XGBOOST_AVAILABLE:

            xgb_model, _ = tune_xgboost(
                X,
                y
            )

            save_model(
                xgb_model,
                "models/best_maintenance_xgb.pkl"
            )

    except Exception as e:

        print(
            f"\nMaintenance Tuning Failed: {e}"
        )

    print("\nCompleted.")
    print("=" * 60)


# ==========================================================
# EXECUTION
# ==========================================================

if __name__ == "__main__":
    main()
