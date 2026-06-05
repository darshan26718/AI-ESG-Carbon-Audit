# pages/10_ESG_Benchmarking.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="ESG Benchmarking",
    page_icon="📊",
    layout="wide"
)

st.title("📊 ESG Benchmarking Dashboard")
st.markdown("""
Compare your company’s ESG performance against **industry benchmarks**
and identify improvement gaps.
""")

# =====================================================
# SAMPLE BENCHMARK DATA (can replace with real dataset)
# =====================================================

benchmark_data = {
    "Manufacturing": 65,
    "IT Services": 78,
    "Energy": 60,
    "Transportation": 62,
    "Healthcare": 75
}

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("🏢 Company ESG Input")

col1, col2 = st.columns(2)

with col1:
    industry = st.selectbox(
        "Select Industry",
        list(benchmark_data.keys())
    )

with col2:
    company_esg_score = st.number_input(
        "Your Company ESG Score (0–100)",
        min_value=0.0,
        max_value=100.0,
        value=70.0
    )

# =====================================================
# BENCHMARK ENGINE
# =====================================================

def calculate_benchmark(industry, company_score):

    industry_avg = benchmark_data[industry]

    gap = company_score - industry_avg

    percentile_rank = np.clip(
        (company_score / 100) * 100,
        0,
        100
    )

    return industry_avg, gap, percentile_rank

# =====================================================
# BUTTON
# =====================================================

if st.button("📊 Compare with Industry Benchmark"):

    industry_avg, gap, percentile = calculate_benchmark(
        industry,
        company_esg_score
    )

    # =====================================================
    # METRICS
    # =====================================================

    st.subheader("📌 Benchmark Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Industry Average ESG", f"{industry_avg}")

    with col2:
        st.metric("Your ESG Score", f"{company_esg_score}")

    with col3:
        st.metric("Gap vs Industry", f"{gap:.2f}")

    # =====================================================
    # PERFORMANCE STATUS
    # =====================================================

    st.subheader("📈 Performance Status")

    if gap > 10:
        st.success("🌟 Above Industry Benchmark")
    elif gap >= 0:
        st.info("🟢 Slightly Above / Equal to Industry")
    elif gap >= -10:
        st.warning("🟡 Below Industry Average")
    else:
        st.error("🔴 Significantly Below Industry Standard")

    # =====================================================
    # VISUALIZATION
    # =====================================================

    st.subheader("📊 ESG Comparison Chart")

    fig, ax = plt.subplots(figsize=(8, 5))

    categories = ["Industry Average", "Your Company"]
    values = [industry_avg, company_esg_score]

    ax.bar(categories, values, color=["gray", "green"])

    ax.set_ylabel("ESG Score")
    ax.set_ylim(0, 100)

    for i, v in enumerate(values):
        ax.text(i, v + 2, str(round(v, 1)), ha="center")

    st.pyplot(fig)

    # =====================================================
    # INSIGHTS
    # =====================================================

    st.subheader("💡 AI Insights")

    insights = []

    if company_esg_score < industry_avg:
        insights.append(
            "⚠️ Improve ESG practices to meet industry standards."
        )

    if industry == "Manufacturing":
        insights.append("🏭 Focus on emissions reduction and energy efficiency.")

    elif industry == "IT Services":
        insights.append("☁️ Shift to green cloud infrastructure.")

    elif industry == "Energy":
        insights.append("⚡ Increase renewable energy share.")

    elif industry == "Transportation":
        insights.append("🚗 Transition to electric mobility.")

    elif industry == "Healthcare":
        insights.append("🏥 Improve waste and energy optimization.")

    for i in insights:
        st.warning(i)

    # =====================================================
    # PERCENTILE SCORE
    # =====================================================

    st.subheader("📊 ESG Percentile Score")

    st.progress(int(percentile))

    st.info(f"You are in the top ~{percentile:.1f}% ESG performance range.")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("🌍 AI ESG Predictive Maintenance | ESG Benchmarking Module")
