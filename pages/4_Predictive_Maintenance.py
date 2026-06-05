import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score
)

import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Predictive Maintenance")
st.markdown("Machine Failure Prediction using Multiple ML Algorithms")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/maintenance_failure_dataset.csv"
    )

df = load_data()

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

with st.expander("📂 View Dataset"):
    st.dataframe(
        df,
        use_container_width=True
    )

# --------------------------------------------------
# FEATURES & TARGET
# --------------------------------------------------

X = df[
    [
        "Operating_Hours",
        "Temperature",
        "Vibration",
        "Pressure",
        "Humidity",
        "Downtime_Hours",
        "Maintenance_Cost"
    ]
]

y = df["Failure_Count"]

# --------------------------------------------------
# TRAIN TEST SPLIT
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------------
# MODELS
# --------------------------------------------------

models = {
    "Linear Regression":
        LinearRegression(),

    "KNN Regressor":
        KNeighborsRegressor(n_neighbors=5),

    "Random Forest":
        RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ),

    "XGBoost":
        XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=4,
            random_state=42
        )
}

# --------------------------------------------------
# MODEL TRAINING
# --------------------------------------------------

results = []

predictions = {}

for name, model in models.items():

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    predictions[name] = y_pred

    mse = mean_squared_error(
        y_test,
        y_pred
    )

    rmse = np.sqrt(mse)

    mae = mean_absolute_error(
        y_test,
        y_pred
    )

    r2 = r2_score(
        y_test,
        y_pred
    )

    results.append(
        {
            "Model": name,
            "MSE": round(mse, 4),
            "RMSE": round(rmse, 4),
            "MAE": round(mae, 4),
            "R2 Score": round(r2, 4)
        }
    )

# --------------------------------------------------
# RESULTS TABLE
# --------------------------------------------------

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="R2 Score",
    ascending=False
)

st.subheader("📊 Model Comparison")

st.dataframe(
    results_df,
    use_container_width=True
)

# --------------------------------------------------
# BEST MODEL
# --------------------------------------------------

best_model_name = results_df.iloc[0]["Model"]

best_r2 = results_df.iloc[0]["R2 Score"]

st.success(
    f"Best Model: {best_model_name} | R² Score: {best_r2}"
)

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

st.subheader("🏆 Best Model Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "MSE",
    results_df.iloc[0]["MSE"]
)

col2.metric(
    "RMSE",
    results_df.iloc[0]["RMSE"]
)

col3.metric(
    "MAE",
    results_df.iloc[0]["MAE"]
)

col4.metric(
    "R²",
    results_df.iloc[0]["R2 Score"]
)

# --------------------------------------------------
# MODEL COMPARISON CHART
# --------------------------------------------------

st.subheader("📈 R² Score Comparison")

fig1 = px.bar(
    results_df,
    x="Model",
    y="R2 Score",
    color="Model",
    title="Model Performance Comparison"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# --------------------------------------------------
# ACTUAL VS PREDICTED
# --------------------------------------------------

st.subheader("🎯 Actual vs Predicted")

best_predictions = predictions[
    best_model_name
]

actual_pred_df = pd.DataFrame(
    {
        "Actual": y_test.values,
        "Predicted": best_predictions
    }
)

fig2 = px.scatter(
    actual_pred_df,
    x="Actual",
    y="Predicted",
    title=f"{best_model_name} Predictions"
)

fig2.add_trace(
    go.Scatter(
        x=actual_pred_df["Actual"],
        y=actual_pred_df["Actual"],
        mode="lines",
        name="Perfect Fit"
    )
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

st.subheader("⚡ Feature Importance")

rf_model = models["Random Forest"]

importance_df = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": rf_model.feature_importances_
    }
)

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

fig3 = px.bar(
    importance_df,
    x="Feature",
    y="Importance",
    color="Importance",
    title="Random Forest Feature Importance"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------------------------
# FAILURE PREDICTION TOOL
# --------------------------------------------------

st.subheader("🔮 Predict Machine Failures")

col1, col2 = st.columns(2)

with col1:

    operating_hours = st.number_input(
        "Operating Hours",
        value=1500
    )

    temperature = st.number_input(
        "Temperature",
        value=75
    )

    vibration = st.number_input(
        "Vibration",
        value=3.5
    )

    pressure = st.number_input(
        "Pressure",
        value=38
    )

with col2:

    humidity = st.number_input(
        "Humidity",
        value=60
    )

    downtime = st.number_input(
        "Downtime Hours",
        value=12
    )

    maintenance_cost = st.number_input(
        "Maintenance Cost",
        value=2000
    )

# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------

best_model = models[best_model_name]

if st.button("Predict Failure Count"):

    input_data = pd.DataFrame(
        {
            "Operating_Hours": [operating_hours],
            "Temperature": [temperature],
            "Vibration": [vibration],
            "Pressure": [pressure],
            "Humidity": [humidity],
            "Downtime_Hours": [downtime],
            "Maintenance_Cost": [maintenance_cost]
        }
    )

    prediction = best_model.predict(
        input_data
    )[0]

    st.success(
        f"Predicted Failure Count: {prediction:.2f}"
    )

# --------------------------------------------------
# DOWNLOAD RESULTS
# --------------------------------------------------

st.subheader("📥 Download Model Results")

csv = results_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "Download Evaluation Report",
    csv,
    "model_comparison.csv",
    "text/csv"
)
