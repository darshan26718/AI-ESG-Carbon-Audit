import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Maintenance Analytics",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Maintenance Failure Analytics")
st.markdown("Root Cause Analysis and Maintenance Insights")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(
        "data/maintenance_failure_dataset.csv"
    )

df = load_data()

# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

with st.expander("📂 View Dataset"):
    st.dataframe(
        df,
        use_container_width=True
    )

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

total_failures = df["Failure_Count"].sum()

total_downtime = df["Downtime_Hours"].sum()

total_cost = df["Maintenance_Cost"].sum()

avg_temperature = df["Temperature"].mean()

st.subheader("📊 Maintenance KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Failures",
    int(total_failures)
)

col2.metric(
    "Downtime Hours",
    int(total_downtime)
)

col3.metric(
    "Maintenance Cost",
    f"${total_cost:,.0f}"
)

col4.metric(
    "Avg Temperature",
    f"{avg_temperature:.1f} °C"
)

st.divider()

# --------------------------------------------------
# DEPARTMENT FILTER
# --------------------------------------------------

department = st.selectbox(
    "Select Department",
    sorted(df["Department"].unique())
)

filtered_df = df[
    df["Department"] == department
]

# --------------------------------------------------
# FAILURE DISTRIBUTION
# --------------------------------------------------

st.subheader("📈 Failure Count Distribution")

fig1 = px.histogram(
    df,
    x="Failure_Count",
    nbins=10,
    title="Failure Count Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# --------------------------------------------------
# DEPARTMENT FAILURE ANALYSIS
# --------------------------------------------------

st.subheader("🏭 Department-wise Failures")

dept_failures = (
    df.groupby("Department")
    ["Failure_Count"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    dept_failures,
    x="Department",
    y="Failure_Count",
    color="Department",
    title="Total Failures by Department"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------------------------
# DOWNTIME ANALYSIS
# --------------------------------------------------

st.subheader("⏳ Downtime Analysis")

fig3 = px.scatter(
    df,
    x="Operating_Hours",
    y="Downtime_Hours",
    color="Department",
    size="Failure_Count",
    hover_data=["Machine_ID"],
    title="Operating Hours vs Downtime"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------------------------
# MAINTENANCE COST ANALYSIS
# --------------------------------------------------

st.subheader("💰 Maintenance Cost Analysis")

fig4 = px.box(
    df,
    x="Department",
    y="Maintenance_Cost",
    color="Department",
    title="Maintenance Cost by Department"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# --------------------------------------------------
# MACHINE FAILURE ANALYSIS
# --------------------------------------------------

st.subheader("⚙️ Top Machines with Failures")

machine_failure = (
    df.sort_values(
        by="Failure_Count",
        ascending=False
    )
    .head(10)
)

fig5 = px.bar(
    machine_failure,
    x="Machine_ID",
    y="Failure_Count",
    color="Failure_Count",
    title="Top 10 Machines by Failure Count"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# --------------------------------------------------
# CORRELATION HEATMAP
# --------------------------------------------------

st.subheader("🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(
    include=np.number
)

corr_matrix = numeric_df.corr()

fig6 = px.imshow(
    corr_matrix,
    text_auto=True,
    aspect="auto",
    title="Correlation Matrix"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

# --------------------------------------------------
# ROOT CAUSE ANALYSIS
# --------------------------------------------------

st.subheader("🕵️ Root Cause Analysis")

failure_corr = corr_matrix[
    "Failure_Count"
].sort_values(
    ascending=False
)

root_cause_df = pd.DataFrame(
    {
        "Feature": failure_corr.index,
        "Correlation": failure_corr.values
    }
)

root_cause_df = root_cause_df[
    root_cause_df["Feature"] != "Failure_Count"
]

fig7 = px.bar(
    root_cause_df,
    x="Feature",
    y="Correlation",
    color="Correlation",
    title="Factors Influencing Failures"
)

st.plotly_chart(
    fig7,
    use_container_width=True
)

# --------------------------------------------------
# ROOT CAUSE INSIGHTS
# --------------------------------------------------

st.subheader("💡 Key Insights")

top_factor = root_cause_df.iloc[0]["Feature"]

st.success(
    f"Most influential factor affecting failures: {top_factor}"
)

if top_factor == "Temperature":
    st.warning(
        "High machine temperature is strongly associated with failures."
    )

elif top_factor == "Vibration":
    st.warning(
        "Machine vibration appears to be a major contributor to failures."
    )

elif top_factor == "Operating_Hours":
    st.warning(
        "Machines with high operating hours show increased failure rates."
    )

elif top_factor == "Downtime_Hours":
    st.warning(
        "Downtime is closely linked with recurring machine failures."
    )

else:
    st.info(
        "Multiple operational factors contribute to failures."
    )

# --------------------------------------------------
# DEPARTMENT DETAILS
# --------------------------------------------------

st.subheader(f"📋 {department} Department Summary")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# --------------------------------------------------
# DOWNLOAD ANALYTICS
# --------------------------------------------------

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "📥 Download Department Data",
    csv,
    f"{department}_maintenance_report.csv",
    "text/csv"
)
