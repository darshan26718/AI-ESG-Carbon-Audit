import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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
    page_title="Carbon Forecasting",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Carbon Emission Forecasting")
st.markdown("Predict Future Carbon Emissions using Machine Learning")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/carbon_emission_dataset.csv"
    )

df = load_data()

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

with st.expander("📂 View Dataset"):
    st.dataframe(df)

# --------------------------------------------------
# FEATURE SELECTION
# --------------------------------------------------

X = df[
    [
        "Electricity_kWh",
        "Fuel_Liters",
        "Travel_km",
        "Waste_kg",
        "Renewable_Energy_kWh"
    ]
]

y = df["CO2_Emission_Tons"]

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
# MODEL TRAINING
# --------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# --------------------------------------------------
# EVALUATION
# --------------------------------------------------

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

st.subheader("📊 Model Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "MSE",
    f"{mse:.4f}"
)

col2.metric(
    "RMSE",
    f"{rmse:.4f}"
)

col3.metric(
    "MAE",
    f"{mae:.4f}"
)

col4.metric(
    "R² Score",
    f"{r2:.4f}"
)

st.divider()

# --------------------------------------------------
# ACTUAL VS PREDICTED
# --------------------------------------------------

st.subheader("🎯 Actual vs Predicted Emissions")

results_df = pd.DataFrame(
    {
        "Actual": y_test.values,
        "Predicted": y_pred
    }
)

fig1 = px.scatter(
    results_df,
    x="Actual",
    y="Predicted",
    title="Actual vs Predicted CO₂ Emissions"
)

fig1.add_trace(
    go.Scatter(
        x=results_df["Actual"],
        y=results_df["Actual"],
        mode="lines",
        name="Perfect Prediction"
    )
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

st.subheader("⚡ Feature Importance")

importance_df = pd.DataFrame(
    {
        "Feature": X.columns,
        "Coefficient": model.coef_
    }
)

importance_df = importance_df.sort_values(
    by="Coefficient",
    ascending=False
)

fig2 = px.bar(
    importance_df,
    x="Feature",
    y="Coefficient",
    color="Coefficient",
    title="Feature Impact on CO₂ Emissions"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------------------------
# MONTHLY TREND
# --------------------------------------------------

st.subheader("📉 Historical Emission Trend")

monthly_df = (
    df.groupby("Month")["CO2_Emission_Tons"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    monthly_df,
    x="Month",
    y="CO2_Emission_Tons",
    markers=True,
    title="Historical Carbon Emission Trend"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------------------------
# FUTURE FORECAST
# --------------------------------------------------

st.subheader("🔮 Future Carbon Forecast")

future_data = pd.DataFrame(
    {
        "Electricity_kWh":[5200,5400,5600],
        "Fuel_Liters":[310,320,330],
        "Travel_km":[1500,1600,1700],
        "Waste_kg":[220,230,240],
        "Renewable_Energy_kWh":[850,900,950]
    }
)

future_predictions = model.predict(
    future_data
)

forecast_df = pd.DataFrame(
    {
        "Future_Period":
        [
            "Next Month",
            "Month +2",
            "Month +3"
        ],
        "Forecasted_CO2":
        future_predictions
    }
)

fig4 = px.line(
    forecast_df,
    x="Future_Period",
    y="Forecasted_CO2",
    markers=True,
    title="Future Carbon Emission Forecast"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.dataframe(
    forecast_df,
    use_container_width=True
)

# --------------------------------------------------
# INSIGHTS
# --------------------------------------------------

st.subheader("💡 Forecast Insights")

avg_forecast = forecast_df[
    "Forecasted_CO2"
].mean()

if avg_forecast < 4:
    st.success(
        "Carbon emissions are under control."
    )

elif avg_forecast < 6:
    st.warning(
        "Moderate emission levels detected."
    )

else:
    st.error(
        "High future emissions predicted. Sustainability actions recommended."
    )

# --------------------------------------------------
# DOWNLOAD RESULTS
# --------------------------------------------------

st.subheader("📥 Download Forecast Results")

csv = forecast_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Forecast CSV",
    data=csv,
    file_name="carbon_forecast.csv",
    mime="text/csv"
)
