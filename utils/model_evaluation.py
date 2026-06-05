# utils/model_evaluation.py

import numpy as np
import pandas as pd

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# --------------------------------------------------
# CALCULATE MSE
# --------------------------------------------------

def calculate_mse(
    y_true,
    y_pred
):
    return mean_squared_error(
        y_true,
        y_pred
    )


# --------------------------------------------------
# CALCULATE RMSE
# --------------------------------------------------

def calculate_rmse(
    y_true,
    y_pred
):

    mse = mean_squared_error(
        y_true,
        y_pred
    )

    return np.sqrt(mse)


# --------------------------------------------------
# CALCULATE MAE
# --------------------------------------------------

def calculate_mae(
    y_true,
    y_pred
):
    return mean_absolute_error(
        y_true,
        y_pred
    )


# --------------------------------------------------
# CALCULATE R2 SCORE
# --------------------------------------------------

def calculate_r2(
    y_true,
    y_pred
):
    return r2_score(
        y_true,
        y_pred
    )


# --------------------------------------------------
# COMPLETE MODEL EVALUATION
# --------------------------------------------------

def evaluate_model(
    y_true,
    y_pred
):
    """
    Returns all evaluation metrics
    """

    mse = calculate_mse(
        y_true,
        y_pred
    )

    rmse = calculate_rmse(
        y_true,
        y_pred
    )

    mae = calculate_mae(
        y_true,
        y_pred
    )

    r2 = calculate_r2(
        y_true,
        y_pred
    )

    return {
        "MSE": round(mse, 4),
        "RMSE": round(rmse, 4),
        "MAE": round(mae, 4),
        "R2 Score": round(r2, 4)
    }


# --------------------------------------------------
# CREATE MODEL COMPARISON TABLE
# --------------------------------------------------

def create_comparison_table(
    results
):
    """
    Convert model results to DataFrame

    Example:

    results = [
        {
            "Model": "Linear Regression",
            "MSE": 0.45,
            "RMSE": 0.67,
            "MAE": 0.52,
            "R2 Score": 0.88
        }
    ]
    """

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="R2 Score",
        ascending=False
    )

    return df


# --------------------------------------------------
# RESIDUAL ANALYSIS
# --------------------------------------------------

def residual_analysis(
    y_true,
    y_pred
):
    """
    Returns residual values
    """

    residuals = (
        y_true - y_pred
    )

    return pd.DataFrame(
        {
            "Actual": y_true,
            "Predicted": y_pred,
            "Residual": residuals
        }
    )


# --------------------------------------------------
# ACTUAL VS PREDICTED DATAFRAME
# --------------------------------------------------

def actual_vs_predicted(
    y_true,
    y_pred
):

    return pd.DataFrame(
        {
            "Actual": y_true,
            "Predicted": y_pred
        }
    )


# --------------------------------------------------
# MODEL SUMMARY
# --------------------------------------------------

def model_summary(
    model_name,
    y_true,
    y_pred
):
    """
    Returns formatted model summary
    """

    metrics = evaluate_model(
        y_true,
        y_pred
    )

    summary = {
        "Model": model_name,
        "MSE": metrics["MSE"],
        "RMSE": metrics["RMSE"],
        "MAE": metrics["MAE"],
        "R2 Score": metrics["R2 Score"]
    }

    return summary


# --------------------------------------------------
# BEST MODEL SELECTION
# --------------------------------------------------

def get_best_model(
    results_df
):
    """
    Select best model based on R² Score
    """

    best_row = results_df.iloc[0]

    return {
        "Model": best_row["Model"],
        "R2 Score": best_row["R2 Score"],
        "RMSE": best_row["RMSE"],
        "MAE": best_row["MAE"]
    }


# --------------------------------------------------
# PRINT EVALUATION
# --------------------------------------------------

def print_metrics(
    metrics
):

    print(
        f"MSE : {metrics['MSE']}"
    )

    print(
        f"RMSE : {metrics['RMSE']}"
    )

    print(
        f"MAE : {metrics['MAE']}"
    )

    print(
        f"R² Score : {metrics['R2 Score']}"
    )


# --------------------------------------------------
# TEST MODULE
# --------------------------------------------------

if __name__ == "__main__":

    y_true = np.array(
        [2, 4, 6, 8, 10]
    )

    y_pred = np.array(
        [2.2, 3.9, 5.8, 8.1, 9.7]
    )

    metrics = evaluate_model(
        y_true,
        y_pred
    )

    print_metrics(
        metrics
    )

    print(
        "\nModel Evaluation Module Loaded Successfully"
    )
