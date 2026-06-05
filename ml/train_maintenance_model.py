"""
Train Predictive Maintenance Models
===================================

Purpose:
--------
1. Train Random Forest Classifier
2. Train XGBoost Classifier
3. Predict Equipment Failure
4. Save Models for Streamlit Deployment

Input:
------
data/maintenance_failure_dataset.csv

Output:
-------
models/maintenance_rf_model.pkl
models/maintenance_xgb_model.pkl
models/scaler.pkl

Author:
-------
AI-ESG-Predictive-Maintenance
"""

import os
import warnings
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

from sklearn.ensemble import RandomForestClassifier

try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False

warnings.filterwarnings("ignore")


# ==========================================================
# PATHS
# ==========================================================

DATA_PATH = "data/maintenance_failure_dataset.csv"

RF_MODEL_PATH = "models/maintenance_rf_model.pkl"

XGB_MODEL_PATH = "models/maintenance_xgb_model.pkl"

SCALER_PATH = "models/scaler.pkl"


# ==========================================================
# LOAD DATA
# ==========================================================

def load_dataset():
    """
    Load maintenance dataset.
    """

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    return df


# ==========================================================
# PREPROCESS DATA
# ==========================================================

def preprocess_data(df):
    """
    Prepare maintenance dataset.
    """

    df = df.copy()

    df.dropna(inplace=True)

    target_column = "Failure"

    if target_column not in df.columns:
        raise ValueError(
            f"Target column '{target_column}' not found."
        )

    X = df.drop(columns=[target_column])

    y = df[target_column]

    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y


# ==========================================================
# RANDOM FOREST MODEL
# ==========================================================

def train_random_forest(
    X_train,
    y_train
):
    """
    Train Random Forest Classifier.
    """

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# ==========================================================
# XGBOOST MODEL
# ==========================================================

def train_xgboost(
    X_train,
    y_train
):
    """
    Train XGBoost Classifier.
    """

    if not XGBOOST_AVAILABLE:
        return None

    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# ==========================================================
# MODEL EVALUATION
# ==========================================================

def evaluate_model(
    model,
    X_test,
    y_test,
    model_name="Model"
):
    """
    Evaluate classifier.
    """

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        zero_division=0
    )

    print("\n" + "=" * 50)
    print(model_name)
    print("=" * 50)

    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    print("\nConfusion Matrix")
    print(
        confusion_matrix(
            y_test,
            predictions
        )
    )

    print("\nClassification Report")
    print(
        classification_report(
            y_test,
            predictions
        )
    )

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1": f1
    }


# ==========================================================
# SAVE MODELS
# ==========================================================

def save_models(
    rf_model,
    xgb_model,
    scaler
):
    """
    Save trained models.
    """

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        rf_model,
        RF_MODEL_PATH
    )

    print(
        f"\nSaved: {RF_MODEL_PATH}"
    )

    if xgb_model is not None:

        joblib.dump(
            xgb_model,
            XGB_MODEL_PATH
        )

        print(
            f"Saved: {XGB_MODEL_PATH}"
        )

    joblib.dump(
        scaler,
        SCALER_PATH
    )

    print(
        f"Saved: {SCALER_PATH}"
    )


# ==========================================================
# MAIN PIPELINE
# ==========================================================

def main():

    print("=" * 60)
    print("PREDICTIVE MAINTENANCE MODEL TRAINING")
    print("=" * 60)

    # Load Data
    df = load_dataset()

    print(
        f"\nDataset Shape: {df.shape}"
    )

    # Prepare Data
    X, y = preprocess_data(df)

    print(
        f"Features: {X.shape[1]}"
    )

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        stratify=y,
        random_state=42
    )

    # Scaling
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(
        X_train
    )

    X_test_scaled = scaler.transform(
        X_test
    )

    # Random Forest
    rf_model = train_random_forest(
        X_train_scaled,
        y_train
    )

    evaluate_model(
        rf_model,
        X_test_scaled,
        y_test,
        "Random Forest"
    )

    # XGBoost
    xgb_model = None

    if XGBOOST_AVAILABLE:

        xgb_model = train_xgboost(
            X_train_scaled,
            y_train
        )

        evaluate_model(
            xgb_model,
            X_test_scaled,
            y_test,
            "XGBoost"
        )

    else:

        print(
            "\nXGBoost not installed. Skipping XGBoost training."
        )

    # Save Models
    save_models(
        rf_model,
        xgb_model,
        scaler
    )

    print("\nTraining Completed Successfully")
    print("=" * 60)


# ==========================================================
# EXECUTE
# ==========================================================

if __name__ == "__main__":
    main()
