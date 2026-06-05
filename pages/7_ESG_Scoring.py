# pages/7_ESG_Scoring.py

import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="ESG Scoring Engine",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 AI ESG Scoring Engine")
st.markdown("""
Predict ESG Score using AI model (0–100 scale)
""")

# =====================================================
# SAFE MODEL LOADER
# =====================================================

@st.cache_resource
def load_model():

    model_path = "models/esg_scoring_model.pkl"
    scaler_path = "models/esg_scaler.pkl"

    # Check files exist
    if not os.path.exists(model_path):
        st.error("❌ Missing ESG model file: esg_scoring_model.pkl")
        st.stop()

    if not os.path.exists(scaler_path):
        st.error("❌ Missing scaler file: esg_scaler.pkl")
        st.stop()

    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler

    except Exception as e:
        st.error("❌ Failed to load model (pickle/version mismatch issue)")
        st.exception(e)
        st.stop()

# LOAD MODEL
model, scaler = load_model()

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📥 Enter ESG Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    carbon_emission = st.number_input("Carbon Emission", value=100.0)

with col2:
    renewable_energy = st.number_input("Renewable Energy Usage (%)", value=40.0)

with col3:
    waste_recycled = st.number_input("Waste Recycled (%)", value=50.0)

col4, col5, col6 = st.columns(3)

with col4:
    employee_satisfaction = st.number_input("Employee Satisfaction (%)", value=70.0)

with col5:
    gender_diversity = st.number_input("Gender Diversity (%)", value=45.0)

with col6:
    board_independence = st.number_input("Board Independence (%)", value=60.0)

# =====================================================
# PREDICTION BUTTON
# =====================================================

if st.button("🔍 Predict ESG Score"):

    # Input dataframe (must match training features)
    input_data = pd.DataFrame([{
        "Carbon_Emission": carbon_emission,
        "Renewable_Energy_Usage": renewable_energy,
        "Waste_Recycled": waste_recycled,
        "Employee_Satisfaction": employee_satisfaction,
        "Gender_Diversity": gender_diversity,
        "Board_Independence": board_independence
    }])

    try:
        # Scale input
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)[0]

        # Clamp result
        prediction = np.clip(prediction, 0, 100)

        # Output
        st.subheader("📊 ESG Score Result")
        st.metric("Predicted ESG Score", f"{prediction:.2f} / 100")

        # Rating system
        if prediction >= 80:
            st.success("🌟 Excellent ESG Performance")
        elif prediction >= 60:
            st.info("🟢 Good ESG Performance")
        elif prediction >= 40:
            st.warning("🟡 Moderate ESG Performance")
        else:
            st.error("🔴 Poor ESG Performance")

    except Exception as e:
        st.error("❌ Prediction failed (model mismatch or scaler issue)")
        st.exception(e)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("🌱 AI ESG System | Production Ready Version")
