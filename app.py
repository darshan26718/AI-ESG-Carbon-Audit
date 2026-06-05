import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI ESG & Predictive Maintenance",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>
.main-title {
    font-size:40px;
    font-weight:bold;
    color:#1f77b4;
}

.sub-title {
    font-size:22px;
    color:#4CAF50;
}

.metric-box {
    background-color:#f5f5f5;
    padding:15px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    "<div class='main-title'>🌍 AI ESG & Predictive Maintenance Platform</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Carbon Analytics • ESG Intelligence • Predictive Maintenance</div>",
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4341/4341139.png",
        width=120
    )

    st.title("Navigation")

    st.success("Project Modules")

    st.markdown("""
    ✅ ESG Dashboard

    ✅ Carbon Forecasting

    ✅ Maintenance Analytics

    ✅ Predictive Maintenance

    ✅ PDF Reports
    """)

    st.divider()

    st.info(
        """
        Developed using:

        • Streamlit

        • Scikit-Learn

        • XGBoost

        • Plotly

        • SHAP
        """
    )

# ---------------------------------------------------
# PROJECT OVERVIEW
# ---------------------------------------------------

st.header("📌 Project Overview")

st.write(
    """
    This platform combines Environmental, Social and Governance (ESG)
    analytics with Predictive Maintenance Intelligence.

    The application helps organizations:

    - Track carbon emissions
    - Analyze sustainability performance
    - Forecast future emissions
    - Detect maintenance failures
    - Predict machine breakdowns
    - Generate downloadable reports
    """
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.header("📊 Platform Capabilities")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Datasets",
        value="3"
    )

with col2:
    st.metric(
        label="ML Models",
        value="4"
    )

with col3:
    st.metric(
        label="Analytics Modules",
        value="5"
    )

with col4:
    st.metric(
        label="Reports",
        value="PDF"
    )

# ---------------------------------------------------
# MODULE DETAILS
# ---------------------------------------------------

st.header("🚀 Available Modules")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "ESG Dashboard",
        "Carbon Forecasting",
        "Maintenance Analytics",
        "Predictive Maintenance"
    ]
)

with tab1:

    st.subheader("🌱 ESG Dashboard")

    st.write("""
    Features:
    - Carbon Footprint Tracking
    - Sustainability Score
    - Department Analysis
    - Global CO₂ Benchmarking
    """)

with tab2:

    st.subheader("📈 Carbon Forecasting")

    st.write("""
    Features:
    - Future Emission Forecasting
    - Trend Analysis
    - Sustainability Projections
    """)

with tab3:

    st.subheader("🔧 Maintenance Analytics")

    st.write("""
    Features:
    - Failure Root Cause Analysis
    - Downtime Monitoring
    - Cost Analysis
    - Correlation Heatmaps
    """)

with tab4:

    st.subheader("🤖 Predictive Maintenance")

    st.write("""
    Machine Learning Models:
    - Linear Regression
    - KNN Regressor
    - Random Forest Regressor
    - XGBoost Regressor

    Evaluation Metrics:
    - MSE
    - RMSE
    - MAE
    - R² Score
    """)

# ---------------------------------------------------
# DATASETS
# ---------------------------------------------------

st.header("🗂️ Project Datasets")

st.table({
    "Dataset": [
        "Carbon Emission Dataset",
        "Global CO₂ Emissions Dataset",
        "Maintenance Failure Dataset"
    ],
    "Purpose": [
        "Carbon Analytics",
        "Global Benchmarking",
        "Predictive Maintenance"
    ]
})

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "AI ESG & Predictive Maintenance Platform | Streamlit Deployment Project"
)
