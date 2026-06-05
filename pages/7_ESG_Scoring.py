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

st.title("🌱 AI ESG Scoring Engine (Fixed & Safe)")
st.markdown("""
Predict ESG score (0–100) using AI model with **safe deployment handling**.
""")

# =====================================================
# SAFE MODEL LOADER (FIX FOR YOUR ERROR)
# =====================================================

@st.cache_resource
def load_model():

    model_path = "models/esg_scoring_model.pkl"
    scaler_path = "models/esg_scaler.pkl"

    # Check model file
    if not os.path.exists(model_path):
        st.error("❌ Missing file: models/esg_scoring_model.pkl")
        st.stop()

    # Check scaler file
    if not os.path.exists(scaler_path):
        st.error("❌ Missing file: models/esg_scaler.pkl")
        st.stop()

    try:
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        return model, scaler

    except Exception as e:
        st.error("❌ Model loading failed. Check compatibility of .pkl file.")
        st.exception(e)
        st.stop()

model, scaler = load_model()

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📥 Enter ESG Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    carbon_emission = st.number_input("Carbon Emission", value=100.0)

with col2:
    renewable_energy = st.number_input("Renewable Energy (%)", value=40.0)

with col3:
    waste_recycled = st.number_input("Waste Recycled (%)", value=50.0)

col4, col5, col6 = st.columns(3)

with col4:
    employee_satisfaction = st.number_input("Employee Satisfaction (%)", value=75.0)

with col5:
    gender_diversity = st.number_input("Gender Diversity (%)", value=45.0)

with col6:
    board_independence = st.number_input("Board Independence (%)", value=60.0)

# =====================================================
# PREDICTION
# =====================================================

if st.button("🔍 Predict ESG Score"):

    input_data = pd.DataFrame([{
        "Carbon_Emission": carbon_emission,
        "Renewable_Energy_Usage": renewable_energy,
        "Waste_Recycled": waste_recycled,
        "Employee_Satisfaction": employee_satisfaction,
        "Gender_Diversity": gender_diversity,
        "Board_Independence": board_independence
    }])

    try:
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]

        prediction = np.clip(prediction, 0, 100)

        st.subheader("📊 ESG Score Result")
        st.metric("Predicted ESG Score", f"{prediction:.2f} / 100")

        # Rating
        if prediction >= 80:
            st.success("🌟 Excellent ESG Performance")
        elif prediction >= 60:
            st.info("🟢 Good ESG Performance")
        elif prediction >= 40:
            st.warning("🟡 Moderate ESG Performance")
        else:
            st.error("🔴 Poor ESG Performance")

    except Exception as e:
        st.error("❌ Prediction failed due to model mismatch.")
        st.exception(e)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("🌱 AI ESG System | Fixed Production-Ready Version")
