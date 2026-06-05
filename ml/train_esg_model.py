"""
Train ESG Scoring Model
=======================

Purpose:
--------
1. Train ESG Score Prediction Model
2. Predict Overall ESG Score
3. Save ESG Model for Streamlit Deployment
4. Evaluate Model Performance

Input:
------
data/esg_benchmark_dataset.csv

Output:
-------
models/esg_scoring_model.pkl
models/esg_scaler.pkl

Expected Target Column:
-----------------------
ESG_Score

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
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

warnings.filterwarnings("ignore")


# ==========================================================
# PATHS
# ==========================================================

DATA_PATH = "data/esg_benchmark_dataset.csv"

MODEL_PATH = "models/esg_scoring_model.pkl"

SCALER_PATH = "models/esg_scaler.pkl"


# ==========================================================
# LOAD DATA
# ==========================================================

def load_dataset():
    """
    Load ESG benchmark dataset.
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
    Prepare ESG dataset.
    """

    df = df.copy()

    df.dropna(inplace=True)

    target_column = "ESG_Score"

    if target_column not in df.columns:
        raise ValueError(
            f"Target column '{target_column}' not found."
        )

    X = df.drop(columns=[target_column])

    y = df[target_column]

    # Convert categorical variables
    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y


# ==========================================================
# TRAIN MODEL
# ==========================================================

def train_model(
    X_train,
    y_train
):
    """
    Train Random Forest Regressor.
    """

    model = RandomForestRegressor(
        n_estimators=500,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# ==========================================================
# EVALUATE MODEL
# ==========================================================

def evaluate_model(
    model,
    X_test,
    y_test
):
    """
    Evaluate ESG model.
    """

    predictions = model.predict(
        X_test
    )

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    print("\n" + "=" * 50)
    print("MODEL PERFORMANCE")
    print("=" * 50)

    print(f"MAE  : {mae:.4f}")
    print(f"MSE  : {mse:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R²   : {r2:.4f}")

    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    }


# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

def display_feature_importance(
    model,
    feature_names,
    top_n=15
):
    """
    Display most important ESG features.
    """

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": model.feature_importances_
    })

    importance_df = (
        importance_df
        .sort_values(
            by="Importance",
            ascending=False
        )
        .head(top_n)
    )

    print("\nTOP ESG FEATURES")
    print("-" * 50)

    print(importance_df)

    return importance_df


# ==========================================================
# SAVE MODEL
# ==========================================================

def save_model(
    model,
    scaler
):
    """
    Save model and scaler.
    """

    os.makedirs(
        "models",
        exist_ok=True
    )

    joblib.dump(
        model,
        MODEL_PATH
    )

    joblib.dump(
        scaler,
        SCALER_PATH
    )

    print("\nSaved Files:")
    print(MODEL_PATH)
    print(SCALER_PATH)


# ==========================================================
# MAIN PIPELINE
# ==========================================================

def main():

    print("=" * 60)
    print("ESG SCORING MODEL TRAINING")
    print("=" * 60)

    # Load Dataset
    df = load_dataset()

    print(
        f"\nDataset Shape: {df.shape}"
    )

    # Prepare Data
    X, y = preprocess_data(df)

    print(
        f"Features: {X.shape[1]}"
    )

    # Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
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

    # Train Model
    model = train_model(
        X_train_scaled,
        y_train
    )

    # Evaluate
    evaluate_model(
        model,
        X_test_scaled,
        y_test
    )

    # Feature Importance
    display_feature_importance(
        model,
        X.columns
    )

    # Save
    save_model(
        model,
        scaler
    )

    print("\nTraining Completed Successfully")
    print("=" * 60)


# ==========================================================
# EXECUTION
# ==========================================================

if __name__ == "__main__":
    main()
