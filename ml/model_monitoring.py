"""
Model Monitoring Module
=======================

Purpose:
--------
1. Monitor Carbon Forecast Model Performance
2. Monitor ESG Scoring Model Performance
3. Monitor Predictive Maintenance Models
4. Detect Data Drift
5. Detect Prediction Drift
6. Generate Model Health Reports
7. Streamlit Dashboard Integration

Models:
-------
- carbon_forecast_model.pkl
- maintenance_rf_model.pkl
- maintenance_xgb_model.pkl
- esg_scoring_model.pkl

Author:
-------
AI-ESG-Predictive-Maintenance
"""

import os
import joblib
import numpy as np
import pandas as pd

from datetime import datetime

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from scipy.stats import ks_2samp


# ==========================================================
# MODEL LOADER
# ==========================================================

def load_model(model_path):
    """
    Load trained model.
    """

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    return joblib.load(model_path)


# ==========================================================
# REGRESSION METRICS
# ==========================================================

def regression_monitor(
    y_true,
    y_pred
):
    """
    Monitor regression models.
    """

    mae = mean_absolute_error(
        y_true,
        y_pred
    )

    mse = mean_squared_error(
        y_true,
        y_pred
    )

    rmse = np.sqrt(mse)

    r2 = r2_score(
        y_true,
        y_pred
    )

    return {
        "MAE": round(mae, 4),
        "MSE": round(mse, 4),
        "RMSE": round(rmse, 4),
        "R2": round(r2, 4)
    }


# ==========================================================
# CLASSIFICATION METRICS
# ==========================================================

def classification_monitor(
    y_true,
    y_pred
):
    """
    Monitor classification models.
    """

    accuracy = accuracy_score(
        y_true,
        y_pred
    )

    precision = precision_score(
        y_true,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        y_pred,
        zero_division=0
    )

    return {
        "Accuracy": round(accuracy, 4),
        "Precision": round(precision, 4),
        "Recall": round(recall, 4),
        "F1 Score": round(f1, 4)
    }


# ==========================================================
# DATA DRIFT DETECTION
# ==========================================================

def detect_data_drift(
    reference_data,
    current_data,
    threshold=0.05
):
    """
    Detect drift using
    Kolmogorov-Smirnov Test.
    """

    drift_results = {}

    common_columns = list(
        set(reference_data.columns)
        &
        set(current_data.columns)
    )

    for column in common_columns:

        try:

            stat, p_value = ks_2samp(
                reference_data[column],
                current_data[column]
            )

            drift_results[column] = {
                "p_value":
                    round(p_value, 5),

                "Drift Detected":
                    p_value < threshold
            }

        except Exception:

            continue

    return drift_results


# ==========================================================
# PREDICTION DRIFT
# ==========================================================

def detect_prediction_drift(
    historical_predictions,
    current_predictions,
    threshold=0.05
):
    """
    Detect prediction distribution drift.
    """

    stat, p_value = ks_2samp(
        historical_predictions,
        current_predictions
    )

    return {
        "p_value":
            round(p_value, 5),

        "Prediction Drift":
            p_value < threshold
    }


# ==========================================================
# MODEL HEALTH STATUS
# ==========================================================

def model_health_status(
    score,
    model_type="regression"
):
    """
    Determine health status.
    """

    if model_type == "regression":

        if score >= 0.90:
            return "Excellent"

        elif score >= 0.75:
            return "Good"

        elif score >= 0.60:
            return "Moderate"

        else:
            return "Poor"

    else:

        if score >= 0.95:
            return "Excellent"

        elif score >= 0.85:
            return "Good"

        elif score >= 0.70:
            return "Moderate"

        else:
            return "Poor"


# ==========================================================
# MONITOR REGRESSION MODEL
# ==========================================================

def monitor_regression_model(
    model,
    X_test,
    y_test
):
    """
    Evaluate regression model.
    """

    predictions = model.predict(
        X_test
    )

    metrics = regression_monitor(
        y_test,
        predictions
    )

    metrics["Health Status"] = (
        model_health_status(
            metrics["R2"],
            "regression"
        )
    )

    return metrics


# ==========================================================
# MONITOR CLASSIFICATION MODEL
# ==========================================================

def monitor_classification_model(
    model,
    X_test,
    y_test
):
    """
    Evaluate classifier.
    """

    predictions = model.predict(
        X_test
    )

    metrics = classification_monitor(
        y_test,
        predictions
    )

    metrics["Health Status"] = (
        model_health_status(
            metrics["Accuracy"],
            "classification"
        )
    )

    return metrics


# ==========================================================
# PERFORMANCE HISTORY
# ==========================================================

def create_performance_log(
    metrics,
    model_name
):
    """
    Create performance history log.
    """

    log = {
        "Timestamp":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "Model":
            model_name
    }

    log.update(metrics)

    return log


# ==========================================================
# SAVE MONITORING REPORT
# ==========================================================

def save_monitoring_report(
    report,
    file_name="monitoring_report.csv"
):
    """
    Save monitoring report.
    """

    report_df = pd.DataFrame(
        [report]
    )

    report_df.to_csv(
        file_name,
        index=False
    )

    return file_name


# ==========================================================
# MONITORING DASHBOARD SUMMARY
# ==========================================================

def monitoring_dashboard_summary(
    logs_df
):
    """
    Dashboard summary.
    """

    return {
        "Total Records":
            len(logs_df),

        "Latest Monitoring":
            logs_df.iloc[-1]["Timestamp"]
            if len(logs_df) > 0
            else "N/A"
    }


# ==========================================================
# COMPLETE MODEL REPORT
# ==========================================================

def generate_model_report(
    model_name,
    metrics,
    drift_results=None
):
    """
    Comprehensive monitoring report.
    """

    report = {
        "Model Name":
            model_name,

        "Generated At":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
    }

    report.update(metrics)

    if drift_results:

        report["Drift Status"] = (
            "Detected"
            if any(
                v.get(
                    "Drift Detected",
                    False
                )
                for v in drift_results.values()
            )
            else "No Drift"
        )

    return report


# ==========================================================
# TEST MODULE
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("MODEL MONITORING MODULE")
    print("=" * 60)

    # Example Regression
    y_true = np.array(
        [100, 120, 140, 160, 180]
    )

    y_pred = np.array(
        [105, 118, 145, 158, 176]
    )

    regression_metrics = (
        regression_monitor(
            y_true,
            y_pred
        )
    )

    print("\nRegression Metrics:")
    print(regression_metrics)

    # Example Classification
    y_true_cls = np.array(
        [0, 1, 0, 1, 1]
    )

    y_pred_cls = np.array(
        [0, 1, 0, 1, 0]
    )

    classification_metrics = (
        classification_monitor(
            y_true_cls,
            y_pred_cls
        )
    )

    print("\nClassification Metrics:")
    print(classification_metrics)

    print("\nModule Loaded Successfully")
    print("=" * 60)
