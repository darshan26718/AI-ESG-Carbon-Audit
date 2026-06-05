import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ESG Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 ESG Sustainability Dashboard")
st.markdown("Monitor Carbon Footprint and Sustainability Performance")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    carbon_df = pd.read_csv(
        "data/carbon_emission_dataset.csv"
    )

    global_df = pd.read_csv(
        "data/global_co2_emissions.csv"
    )

    return carbon_df, global_df


carbon_df, global_df = load_data()

# --------------------------------------------------
# ESG SCORE CALCULATION
# --------------------------------------------------

total_emission = carbon_df["CO2_Emission_Tons"].sum()

avg_emission = carbon_df["CO2_Emission_Tons"].mean()

renewable_usage = carbon_df["Renewable_Energy_kWh"].sum()

total_energy = carbon_df["Electricity_kWh"].sum()

renewable_percent = (
    renewable_usage / total_energy
) * 100

esg_score = max(
    0,
    round(
        100 - avg_emission * 10,
        2
    )
)

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

st.subheader("📊 Key ESG Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total CO₂ Emission",
    f"{total_emission:.2f} Tons"
)

col2.metric(
    "Average Emission",
    f"{avg_emission:.2f} Tons"
)

col3.metric(
    "Renewable Usage",
    f"{renewable_percent:.2f}%"
)

col4.metric(
    "ESG Score",
    f"{esg_score}/100"
)

st.divider()

# --------------------------------------------------
# DEPARTMENT FILTER
# --------------------------------------------------

departments = sorted(
    carbon_df["Department"].unique()
)

selected_department = st.selectbox(
    "Select Department",
    departments
)

filtered_df = carbon_df[
    carbon_df["Department"] == selected_department
]

# --------------------------------------------------
# DEPARTMENT EMISSION ANALYSIS
# --------------------------------------------------

st.subheader("🏢 Department Emission Analysis")

fig1 = px.bar(
    filtered_df,
    x="Month",
    y="CO2_Emission_Tons",
    color="Month",
    title=f"{selected_department} Monthly CO₂ Emissions"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# --------------------------------------------------
# MONTHLY TREND
# --------------------------------------------------

st.subheader("📈 Carbon Emission Trend")

monthly_trend = (
    carbon_df.groupby("Month")
    ["CO2_Emission_Tons"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    monthly_trend,
    x="Month",
    y="CO2_Emission_Tons",
    markers=True,
    title="Monthly Carbon Emission Trend"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------------------------
# DEPARTMENT CONTRIBUTION
# --------------------------------------------------

st.subheader("🥧 Department Contribution")

dept_emission = (
    carbon_df.groupby("Department")
    ["CO2_Emission_Tons"]
    .sum()
    .reset_index()
)

fig3 = px.pie(
    dept_emission,
    names="Department",
    values="CO2_Emission_Tons",
    title="Emission Contribution by Department"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------------------------
# RENEWABLE ENERGY ANALYSIS
# --------------------------------------------------

st.subheader("⚡ Renewable Energy Analysis")

fig4 = px.bar(
    carbon_df,
    x="Department",
    y="Renewable_Energy_kWh",
    color="Department",
    title="Renewable Energy Usage by Department"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# --------------------------------------------------
# GLOBAL CO2 BENCHMARKING
# --------------------------------------------------

st.subheader("🌎 Global CO₂ Benchmarking")

latest_year = global_df["Year"].max()

latest_data = global_df[
    global_df["Year"] == latest_year
]

fig5 = px.bar(
    latest_data,
    x="Country",
    y="CO2_Emissions",
    color="Country",
    title=f"Country-wise CO₂ Emissions ({latest_year})"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# --------------------------------------------------
# TOP POLLUTING COUNTRIES
# --------------------------------------------------

st.subheader("🏭 Top Polluting Countries")

top_countries = latest_data.sort_values(
    by="CO2_Emissions",
    ascending=False
)

st.dataframe(
    top_countries[
        [
            "Country",
            "CO2_Emissions",
            "Renewable_Energy_Percentage"
        ]
    ],
    use_container_width=True
)

# --------------------------------------------------
# ESG INSIGHTS
# --------------------------------------------------

st.subheader("💡 ESG Insights")

if esg_score >= 80:
    st.success(
        "Excellent Sustainability Performance."
    )

elif esg_score >= 60:
    st.warning(
        "Moderate Sustainability Performance. Improvement Recommended."
    )

else:
    st.error(
        "High Carbon Footprint Detected. Immediate Action Required."
    )

st.info(
    f"""
    Current ESG Score: {esg_score}/100

    Renewable Energy Usage: {renewable_percent:.2f}%

    Total Carbon Emission: {total_emission:.2f} Tons
    """
)

# --------------------------------------------------
# RAW DATA
# --------------------------------------------------

with st.expander("📂 View Dataset"):

    st.dataframe(
        carbon_df,
        use_container_width=True
    )
