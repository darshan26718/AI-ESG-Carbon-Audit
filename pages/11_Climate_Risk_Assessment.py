# pages/11_Climate_Risk_Assessment.py

import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Climate Intelligence System",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Climate Intelligence System (Advanced)")
st.markdown("""
A next-gen AI system for **climate risk prediction, scenario simulation,
and ESG climate intelligence forecasting (2030–2050)**.
""")

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📥 Climate Risk Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    carbon_intensity = st.number_input("Carbon Intensity", value=0.8)

with col2:
    renewable_dependency = st.number_input("Renewable Energy (%)", value=40.0)

with col3:
    climate_exposure = st.number_input("Climate Exposure Index (0–100)", value=60.0)

col4, col5, col6 = st.columns(3)

with col4:
    regulatory_risk = st.number_input("Regulatory Risk", value=50.0)

with col5:
    supply_chain_risk = st.number_input("Supply Chain Risk", value=55.0)

with col6:
    geo_region_risk = st.number_input("Geographical Risk Index", value=60.0)

industry = st.selectbox(
    "Industry Type",
    ["Manufacturing", "IT Services", "Energy", "Transportation", "Healthcare"]
)

# =====================================================
# AI RISK ENGINE (SIMULATED ML MODEL)
# =====================================================

def ai_climate_model():

    # Simulated ML prediction formula (acts like trained model)
    base_risk = (
        carbon_intensity * 25 +
        (100 - renewable_dependency) * 0.3 +
        climate_exposure * 0.25 +
        regulatory_risk * 0.2 +
        supply_chain_risk * 0.2 +
        geo_region_risk * 0.25
    )

    # Industry adjustment
    industry_factor = {
        "Manufacturing": 1.2,
        "Energy": 1.3,
        "Transportation": 1.15,
        "IT Services": 0.8,
        "Healthcare": 0.9
    }

    risk_score = base_risk * industry_factor[industry]

    risk_score = np.clip(risk_score, 0, 100)

    return risk_score

# =====================================================
# SCENARIO SIMULATION
# =====================================================

def simulate_future_risk(current_risk):

    years = [2030, 2040, 2050]

    # degradation or improvement scenarios
    projected = [
        current_risk * 0.9,
        current_risk * 0.7,
        current_risk * 0.4
    ]

    return years, projected

# =====================================================
# BUTTON
# =====================================================

if st.button("🌍 Run AI Climate Analysis"):

    risk_score = ai_climate_model()
    years, future_risk = simulate_future_risk(risk_score)

    # =====================================================
    # RISK SCORE
    # =====================================================

    st.subheader("📊 Climate Risk Score")

    st.metric("AI Predicted Risk", f"{risk_score:.2f} / 100")

    if risk_score > 75:
        st.error("🔴 Critical Climate Risk Zone")
    elif risk_score > 50:
        st.warning("🟠 High Climate Risk Zone")
    elif risk_score > 30:
        st.info("🟡 Moderate Climate Risk Zone")
    else:
        st.success("🟢 Low Climate Risk Zone")

    # =====================================================
    # FUTURE FORECAST
    # =====================================================

    st.subheader("📈 Climate Risk Forecast (2030–2050)")

    forecast_df = pd.DataFrame({
        "Year": years,
        "Predicted Risk": future_risk
    })

    st.line_chart(forecast_df.set_index("Year"))

    # =====================================================
    # RISK FACTOR BREAKDOWN
    # =====================================================

    st.subheader("📊 Risk Factor Breakdown")

    factors = pd.DataFrame({
        "Factor": [
            "Carbon Intensity",
            "Renewable Dependency",
            "Climate Exposure",
            "Regulatory Risk",
            "Supply Chain Risk",
            "Geo Risk"
        ],
        "Impact": [
            carbon_intensity * 100,
            100 - renewable_dependency,
            climate_exposure,
            regulatory_risk,
            supply_chain_risk,
            geo_region_risk
        ]
    })

    st.bar_chart(factors.set_index("Factor"))

    # =====================================================
    # AI INSIGHTS
    # =====================================================

    st.subheader("💡 AI Climate Insights")

    insights = []

    if carbon_intensity > 0.7:
        insights.append("⚠️ High carbon intensity → urgent decarbonization needed.")

    if renewable_dependency < 50:
        insights.append("🌱 Increase renewable energy adoption.")

    if geo_region_risk > 70:
        insights.append("🌍 High geographical exposure to climate disasters.")

    if regulatory_risk > 60:
        insights.append("📜 Carbon regulation penalties likely in future.")

    if supply_chain_risk > 60:
        insights.append("🚚 Supply chain disruption risk is critical.")

    for i in insights:
        st.warning(i)

    if not insights:
        st.success("🎯 Climate profile is stable and well managed.")

    # =====================================================
    # INSURANCE / FINANCIAL IMPACT
    # =====================================================

    st.subheader("💰 Estimated Financial Risk Impact")

    financial_risk = risk_score * 1.5  # simulated model

    st.metric("Potential Loss Index", f"${financial_risk * 10:.2f}K")

    # =====================================================
    # REPORT GENERATION
    # =====================================================

    st.subheader("📄 Download AI Climate Report")

    report = f"""
AI CLIMATE INTELLIGENCE REPORT
Generated: {datetime.now()}

Industry: {industry}

Inputs:
- Carbon Intensity: {carbon_intensity}
- Renewable Dependency: {renewable_dependency}
- Climate Exposure: {climate_exposure}
- Regulatory Risk: {regulatory_risk}
- Supply Chain Risk: {supply_chain_risk}
- Geo Risk: {geo_region_risk}

AI Risk Score: {risk_score:.2f}/100

FUTURE FORECAST:
2030: {future_risk[0]:.2f}
2040: {future_risk[1]:.2f}
2050: {future_risk[2]:.2f}

Financial Impact Index: ${financial_risk * 10:.2f}K

Generated by AI Climate Intelligence System
"""

    st.download_button(
        label="📥 Download Climate AI Report",
        data=report,
        file_name="climate_ai_report.txt",
        mime="text/plain"
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("🌍 AI ESG Predictive Maintenance | Climate Intelligence System v3.0")
