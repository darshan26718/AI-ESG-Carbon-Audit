# pages/8_AI_Sustainability_Advisor.py

import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Sustainability Advisor",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 AI Sustainability Advisor")
st.markdown("""
This AI advisor analyzes your ESG, carbon, and operational patterns
and provides **actionable sustainability recommendations**.
""")

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📥 Enter Operational Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    carbon_emission = st.number_input("Carbon Emission (tons)", value=100.0)

with col2:
    energy_efficiency = st.number_input("Energy Efficiency (%)", value=60.0)

with col3:
    renewable_usage = st.number_input("Renewable Energy Usage (%)", value=40.0)

col4, col5, col6 = st.columns(3)

with col4:
    waste_generation = st.number_input("Waste Generation (tons)", value=50.0)

with col5:
    recycling_rate = st.number_input("Recycling Rate (%)", value=45.0)

with col6:
    downtime_hours = st.number_input("Machine Downtime (hrs/month)", value=20.0)

# =====================================================
# ADVISOR LOGIC
# =====================================================

def generate_recommendations():
    recommendations = []

    # Carbon logic
    if carbon_emission > 120:
        recommendations.append(
            "⚠️ High carbon emissions detected. Transition to renewable energy sources immediately."
        )

    # Energy efficiency
    if energy_efficiency < 70:
        recommendations.append(
            "⚡ Improve energy efficiency using smart monitoring systems and IoT sensors."
        )

    # Renewable usage
    if renewable_usage < 50:
        recommendations.append(
            "🌱 Increase renewable energy adoption (solar, wind, hybrid systems)."
        )

    # Waste management
    if waste_generation > 60:
        recommendations.append(
            "♻️ Reduce waste generation through lean manufacturing practices."
        )

    # Recycling
    if recycling_rate < 50:
        recommendations.append(
            "🔄 Improve recycling systems and circular economy practices."
        )

    # Downtime (maintenance link)
    if downtime_hours > 15:
        recommendations.append(
            "🔧 High machine downtime detected. Apply predictive maintenance models."
        )

    return recommendations

# =====================================================
# BUTTON
# =====================================================

if st.button("🤖 Generate Sustainability Insights"):

    st.subheader("📊 AI Recommendations")

    recommendations = generate_recommendations()

    if recommendations:
        for r in recommendations:
            st.warning(r)
    else:
        st.success("🎯 Excellent sustainability performance across all metrics!")

# =====================================================
# EXTRA INSIGHT PANEL
# =====================================================

st.markdown("---")
st.subheader("💡 Smart AI Insight Engine")

st.info("""
This advisor combines:
- ESG Scoring trends
- Carbon emission analytics
- Predictive maintenance signals
- Resource efficiency metrics

to guide organizations toward **Net Zero transformation**.
""")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("AI ESG Predictive Maintenance Platform | Sustainability Advisor Module")
