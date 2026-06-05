"""
Train Carbon Forecasting Model
==============================

Purpose:
--------
Train a Machine Learning model to predict future carbon emissions
and save the trained model for Streamlit deployment.

Input:
------
data/carbon_emission_dataset.csv

Output:
-------
models/carbon_forecast_model.pkl
models/scaler.pkl

Author:
-------
AI-ESG-Predictive-Maintenance
"""

import os
import joblib
import warnings

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

DATA_PATH = "data/carbon_emission_dataset.csv"

MODEL_PATH = "models/carbon_forecast_model.pkl"

SCALER_PATH = "models/scaler.pkl"


# ==========================================================
# LOAD DATA
# ==========================================================

def load_dataset():
    """
    Load carbon emission dataset.
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
    Prepare dataset for training.
    """

    df = df.copy()

    df = df.dropna()

    # Target Column
    target_column = "Carbon_Emission"

    if target_column not in df.columns:
        raise ValueError(
            f"'{target_column}' column not found."
        )

    X = df.drop(columns=[target_column])

    y = df[target_column]

    # Convert categorical columns
    X = pd.get_dummies(
        X,
        drop_first=True
    )

    return X, y


# ==========================================================
# TRAIN MODEL
# ==========================================================

def train_model(X_train, y_train):
    """
    Train Random Forest Regressor.
    """

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=12,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

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
    Evaluate regression model.
    """

    predictions = model.predict(X_test)

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

    print("\nModel Evaluation")
    print("-" * 50)

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
# SAVE MODEL
# ==========================================================

def save_model(
    model,
    scaler
):
    """
    Save trained model and scaler.
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

    print("\nSaved:")
    print(MODEL_PATH)
    print(SCALER_PATH)


# ==========================================================
# MAIN PIPELINE
# ==========================================================

def main():

    print("=" * 60)
    print("CARBON FORECAST MODEL TRAINING")
    print("=" * 60)

    # Load
    df = load_dataset()

    print(
        f"\nDataset Shape: {df.shape}"
    )

    # Prepare
    X, y = preprocess_data(df)

    print(
        f"Features: {X.shape[1]}"
    )

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    # Scale
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(
        X_train
    )

    X_test_scaled = scaler.transform(
        X_test
    )

    # Train
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

    # Save
    save_model(
        model,
        scaler
    )

    print("\nTraining Completed Successfully")
    print("=" * 60)


# ==========================================================
# EXECUTE
# ==========================================================

if __name__ == "__main__":
    main()
