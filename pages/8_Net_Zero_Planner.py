# pages/8_Net_Zero_Planner.py

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Net Zero Planner",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 AI Net-Zero Planner (2030–2050)")
st.markdown("""
This AI system generates a **decarbonization roadmap** to help organizations
achieve **Net-Zero emissions goals** using predictive analytics.
""")

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📥 Enter Sustainability Baseline")

col1, col2, col3 = st.columns(3)

with col1:
    current_emissions = st.number_input(
        "Current Annual Emissions (tons CO₂)",
        min_value=0.0,
        value=120.0
    )

with col2:
    renewable_usage = st.number_input(
        "Renewable Energy Usage (%)",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

with col3:
    energy_efficiency = st.number_input(
        "Energy Efficiency (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

industry = st.selectbox(
    "Industry Type",
    ["Manufacturing", "IT Services", "Energy", "Transportation", "Healthcare"]
)

# =====================================================
# NET ZERO ENGINE
# =====================================================

def generate_net_zero_plan(emissions, renewable, efficiency, industry):

    roadmap = []
    timeline = []

    # Emission reduction target simulation
    target_2030 = emissions * 0.7
    target_2040 = emissions * 0.4
    target_2050 = 0

    # ================= BASE ROADMAP =================

    if renewable < 50:
        roadmap.append("Increase renewable energy adoption to 60%+ by 2030")

    if efficiency < 70:
        roadmap.append("Deploy AI-driven energy optimization systems")

    if emissions > 100:
        roadmap.append("Implement carbon capture & storage technologies")

    # ================= INDUSTRY STRATEGY =================

    if industry == "Manufacturing":
        roadmap.append("Upgrade to low-emission smart factories")
        roadmap.append("Adopt circular economy manufacturing systems")

    elif industry == "IT Services":
        roadmap.append("Migrate to green cloud infrastructure")
        roadmap.append("Optimize data center cooling systems")

    elif industry == "Energy":
        roadmap.append("Shift fossil fuel plants to renewable hybrid systems")

    elif industry == "Transportation":
        roadmap.append("Transition fleet to electric/hydrogen vehicles")

    elif industry == "Healthcare":
        roadmap.append("Reduce hospital energy consumption via smart grids")

    # ================= TIMELINE =================

    timeline = [
        ("2030 Target", f"{target_2030:.1f} tons CO₂"),
        ("2040 Target", f"{target_2040:.1f} tons CO₂"),
        ("2050 Target", "Net Zero (0 emissions)")
    ]

    return roadmap, timeline

# =====================================================
# BUTTON
# =====================================================

if st.button("🌍 Generate Net-Zero Roadmap"):

    roadmap, timeline = generate_net_zero_plan(
        current_emissions,
        renewable_usage,
        energy_efficiency,
        industry
    )

    # ================= OUTPUT =================

    st.subheader("📊 Net-Zero Emission Timeline")

    for year, value in timeline:
        st.metric(year, value)

    # ================= ROADMAP =================

    st.subheader("🛣️ Decarbonization Strategy")

    if roadmap:
        for step in roadmap:
            st.success(f"✔ {step}")
    else:
        st.info("Company already aligned with Net-Zero pathway!")

    # ================= RISK SCORE =================

    risk_score = (
        current_emissions * 0.3 +
        (100 - renewable_usage) * 0.3 +
        (100 - energy_efficiency) * 0.4
    )

    st.subheader("⚠️ Net-Zero Risk Index")

    st.metric("Risk Score", f"{risk_score:.2f} / 100")

    if risk_score > 60:
        st.error("High carbon risk — immediate action required")
    elif risk_score > 30:
        st.warning("Moderate risk — optimization needed")
    else:
        st.success("Low risk — strong sustainability position")

    # ================= REPORT =================

    st.subheader("📄 Download Net-Zero Report")

    report = f"""
NET-ZERO PLAN REPORT
Generated: {datetime.now()}

Current Emissions: {current_emissions}
Renewable Usage: {renewable_usage}%
Energy Efficiency: {energy_efficiency}%
Industry: {industry}

2030 Target: {target_2030:.1f} tons CO2
2040 Target: {target_2040:.1f} tons CO2
2050 Target: Net Zero

Risk Score: {risk_score:.2f}

ROADMAP:
- {chr(10).join(roadmap)}
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="net_zero_plan.txt",
        mime="text/plain"
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("🌿 AI ESG Predictive Maintenance | Net-Zero Planner Module")
