# pages/12_Green_Investment_Analyzer.py

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Green Investment Analyzer",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Green Investment Analyzer")
st.markdown("""
This AI system evaluates **green investments** such as:
- Solar energy systems
- Wind power projects
- EV fleet transition
- Energy efficiency upgrades

It estimates **ROI, carbon savings, and payback period**.
""")

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📥 Investment Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    investment_type = st.selectbox(
        "Investment Type",
        [
            "Solar Energy",
            "Wind Energy",
            "EV Fleet Transition",
            "Energy Efficiency Upgrade",
            "Waste Recycling System"
        ]
    )

with col2:
    investment_cost = st.number_input(
        "Investment Cost ($)",
        min_value=0.0,
        value=100000.0
    )

with col3:
    annual_savings = st.number_input(
        "Expected Annual Savings ($)",
        min_value=0.0,
        value=25000.0
    )

col4, col5 = st.columns(2)

with col4:
    carbon_reduction = st.number_input(
        "Annual Carbon Reduction (tons)",
        min_value=0.0,
        value=500.0
    )

with col5:
    project_lifetime = st.number_input(
        "Project Lifetime (years)",
        min_value=1,
        value=10
    )

# =====================================================
# AI INVESTMENT ENGINE
# =====================================================

def calculate_investment_metrics():

    # ROI
    roi = ((annual_savings * project_lifetime) - investment_cost) / investment_cost * 100

    # Payback period
    payback_period = investment_cost / annual_savings if annual_savings > 0 else 0

    # Total savings
    total_savings = annual_savings * project_lifetime

    # Carbon value score (simulated ESG impact value)
    carbon_value = carbon_reduction * 50  # $ per ton impact value

    # Sustainability score
    sustainability_score = (
        carbon_reduction * 0.4 +
        annual_savings * 0.0005 +
        (100 - payback_period * 5)
    )

    sustainability_score = np.clip(sustainability_score, 0, 100)

    return roi, payback_period, total_savings, carbon_value, sustainability_score

# =====================================================
# BUTTON
# =====================================================

if st.button("📊 Analyze Green Investment"):

    roi, payback, savings, carbon_value, score = calculate_investment_metrics()

    # =====================================================
    # RESULTS
    # =====================================================

    st.subheader("📊 Investment Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("ROI (%)", f"{roi:.2f}")

    with col2:
        st.metric("Payback Period (years)", f"{payback:.2f}")

    with col3:
        st.metric("Total Savings ($)", f"{savings:,.2f}")

    # =====================================================
    # SUSTAINABILITY SCORE
    # =====================================================

    st.subheader("🌱 Sustainability Score")

    st.metric("Green Impact Score", f"{score:.2f} / 100")

    if score >= 80:
        st.success("🌟 Excellent Green Investment")
    elif score >= 60:
        st.info("🟢 Good Sustainable Investment")
    elif score >= 40:
        st.warning("🟡 Moderate Impact Investment")
    else:
        st.error("🔴 Low Sustainability Impact")

    # =====================================================
    # CARBON IMPACT
    # =====================================================

    st.subheader("🌍 Carbon Impact Analysis")

    st.metric("Total Carbon Value Impact", f"${carbon_value:,.2f}")

    # =====================================================
    # AI INSIGHTS
    # =====================================================

    st.subheader("💡 AI Investment Insights")

    insights = []

    if roi < 20:
        insights.append("⚠️ Low ROI — consider optimizing investment structure.")

    if payback > 7:
        insights.append("⏳ Long payback period — evaluate faster-return alternatives.")

    if carbon_reduction > 500:
        insights.append("🌍 High environmental impact — strong ESG contribution.")

    if investment_type == "Solar Energy":
        insights.append("☀️ Solar projects provide long-term stable ROI.")

    elif investment_type == "Wind Energy":
        insights.append("🌬️ Wind energy is highly scalable for industrial use.")

    elif investment_type == "EV Fleet Transition":
        insights.append("🚗 EV transition reduces long-term fuel dependency.")

    elif investment_type == "Energy Efficiency Upgrade":
        insights.append("⚡ Efficiency upgrades provide fastest payback.")

    elif investment_type == "Waste Recycling System":
        insights.append("♻️ Recycling systems improve circular economy value.")

    for i in insights:
        st.warning(i)

    if not insights:
        st.success("🎯 Strong green investment profile!")

    # =====================================================
    # REPORT
    # =====================================================

    st.subheader("📄 Download Investment Report")

    report = f"""
GREEN INVESTMENT ANALYSIS REPORT
Generated: {datetime.now()}

Investment Type: {investment_type}
Cost: ${investment_cost}
Annual Savings: ${annual_savings}
Project Lifetime: {project_lifetime} years

ROI: {roi:.2f}%
Payback Period: {payback:.2f} years
Total Savings: ${savings:.2f}

Carbon Reduction: {carbon_reduction} tons/year
Carbon Value Impact: ${carbon_value:.2f}

Sustainability Score: {score:.2f}/100

Generated by AI Green Investment Analyzer
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="green_investment_report.txt",
        mime="text/plain"
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("💰 AI ESG Predictive Maintenance | Green Investment Analyzer Module")
