# utils/predictive_models.py

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor

from xgboost import XGBRegressor

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

# --------------------------------------------------
# TRAIN LINEAR REGRESSION
# --------------------------------------------------

def train_linear_regression(
    X_train,
    y_train
):

    model = LinearRegression()

    model.fit(
        X_train,
        y_train
    )

    return model


# --------------------------------------------------
# TRAIN KNN
# --------------------------------------------------

def train_knn(
    X_train,
    y_train,
    n_neighbors=5
):

    model = KNeighborsRegressor(
        n_neighbors=n_neighbors
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# --------------------------------------------------
# TRAIN RANDOM FOREST
# --------------------------------------------------

def train_random_forest(
    X_train,
    y_train
):

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# --------------------------------------------------
# TRAIN XGBOOST
# --------------------------------------------------

def train_xgboost(
    X_train,
    y_train
):

    model = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        objective="reg:squarederror",
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    return model


# --------------------------------------------------
# EVALUATE MODEL
# --------------------------------------------------

def evaluate_model(
    model,
    X_test,
    y_test
):

    predictions = model.predict(
        X_test
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(mse)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    return {
        "MSE": round(mse, 4),
        "RMSE": round(rmse, 4),
        "MAE": round(mae, 4),
        "R2 Score": round(r2, 4)
    }


# --------------------------------------------------
# TRAIN ALL MODELS
# --------------------------------------------------

def train_all_models(
    X_train,
    y_train
):

    models = {

        "Linear Regression":
        train_linear_regression(
            X_train,
            y_train
        ),

        "KNN Regressor":
        train_knn(
            X_train,
            y_train
        ),

        "Random Forest":
        train_random_forest(
            X_train,
            y_train
        ),

        "XGBoost":
        train_xgboost(
            X_train,
            y_train
        )
    }

    return models


# --------------------------------------------------
# COMPARE MODELS
# --------------------------------------------------

def compare_models(
    models,
    X_test,
    y_test
):

    results = []

    for model_name, model in models.items():

        metrics = evaluate_model(
            model,
            X_test,
            y_test
        )

        results.append(
            {
                "Model": model_name,
                **metrics
            }
        )

    results_df = pd.DataFrame(
        results
    )

    results_df = results_df.sort_values(
        by="R2 Score",
        ascending=False
    )

    return results_df


# --------------------------------------------------
# GET BEST MODEL
# --------------------------------------------------

def get_best_model(
    models,
    results_df
):

    best_model_name = (
        results_df.iloc[0]["Model"]
    )

    best_model = models[
        best_model_name
    ]

    return (
        best_model_name,
        best_model
    )


# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

def get_feature_importance(
    model,
    feature_names
):

    if hasattr(
        model,
        "feature_importances_"
    ):

        importance_df = pd.DataFrame(
            {
                "Feature":
                feature_names,

                "Importance":
                model.feature_importances_
            }
        )

        importance_df = (
            importance_df
            .sort_values(
                by="Importance",
                ascending=False
            )
        )

        return importance_df

    return pd.DataFrame()


# --------------------------------------------------
# PREDICT NEW DATA
# --------------------------------------------------

def predict_failure(
    model,
    input_df
):

    prediction = model.predict(
        input_df
    )

    return prediction


# --------------------------------------------------
# TEST MODULE
# --------------------------------------------------

if __name__ == "__main__":

    print(
        "Predictive Models Module Loaded Successfully"
    )
