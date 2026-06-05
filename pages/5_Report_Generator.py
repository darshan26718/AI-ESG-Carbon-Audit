import streamlit as st
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Report Generator",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ESG & Predictive Maintenance Report Generator")
st.markdown("Generate and Download PDF Reports")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    carbon_df = pd.read_csv(
        "data/carbon_emission_dataset.csv"
    )

    maintenance_df = pd.read_csv(
        "data/maintenance_failure_dataset.csv"
    )

    global_df = pd.read_csv(
        "data/global_co2_emissions.csv"
    )

    return carbon_df, maintenance_df, global_df


carbon_df, maintenance_df, global_df = load_data()

# --------------------------------------------------
# REPORT METRICS
# --------------------------------------------------

total_emission = carbon_df[
    "CO2_Emission_Tons"
].sum()

avg_emission = carbon_df[
    "CO2_Emission_Tons"
].mean()

renewable_energy = carbon_df[
    "Renewable_Energy_kWh"
].sum()

total_failures = maintenance_df[
    "Failure_Count"
].sum()

total_downtime = maintenance_df[
    "Downtime_Hours"
].sum()

total_maintenance_cost = maintenance_df[
    "Maintenance_Cost"
].sum()

esg_score = max(
    0,
    round(
        100 - avg_emission * 10,
        2
    )
)

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

st.subheader("📊 Report Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total CO₂",
    f"{total_emission:.2f} Tons"
)

col2.metric(
    "ESG Score",
    f"{esg_score}/100"
)

col3.metric(
    "Failures",
    int(total_failures)
)

col4.metric(
    "Downtime",
    int(total_downtime)
)

st.divider()

# --------------------------------------------------
# REPORT PREVIEW
# --------------------------------------------------

st.subheader("📋 Report Preview")

preview_data = pd.DataFrame({
    "Metric": [
        "Total CO₂ Emissions",
        "Average CO₂ Emissions",
        "Renewable Energy Usage",
        "ESG Score",
        "Total Failures",
        "Downtime Hours",
        "Maintenance Cost"
    ],
    "Value": [
        round(total_emission, 2),
        round(avg_emission, 2),
        round(renewable_energy, 2),
        esg_score,
        int(total_failures),
        int(total_downtime),
        round(total_maintenance_cost, 2)
    ]
})

st.dataframe(
    preview_data,
    use_container_width=True
)

# --------------------------------------------------
# PDF GENERATION FUNCTION
# --------------------------------------------------

def generate_pdf():

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    # Title

    content.append(
        Paragraph(
            "AI ESG & Predictive Maintenance Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    # ESG Section

    content.append(
        Paragraph(
            "ESG Sustainability Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Total CO₂ Emissions: {total_emission:.2f} Tons",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Average Emissions: {avg_emission:.2f} Tons",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Renewable Energy Usage: {renewable_energy:.2f} kWh",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"ESG Score: {esg_score}/100",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    # Maintenance Section

    content.append(
        Paragraph(
            "Maintenance Analytics Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Total Failures: {int(total_failures)}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Downtime Hours: {int(total_downtime)}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Maintenance Cost: ${total_maintenance_cost:,.2f}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    # Recommendations

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "• Increase renewable energy usage.",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "• Monitor high-failure machines regularly.",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "• Implement preventive maintenance schedules.",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "• Reduce carbon-intensive operations.",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # Global CO₂ Benchmark

    content.append(
        Paragraph(
            "Global CO₂ Benchmark",
            styles["Heading2"]
        )
    )

    latest_year = global_df["Year"].max()

    latest = global_df[
        global_df["Year"] == latest_year
    ]

    top_country = latest.sort_values(
        by="CO2_Emissions",
        ascending=False
    ).iloc[0]

    content.append(
        Paragraph(
            f"Highest Emitting Country ({latest_year}): "
            f"{top_country['Country']} "
            f"({top_country['CO2_Emissions']} Million Tons)",
            styles["BodyText"]
        )
    )

    doc.build(content)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf

# --------------------------------------------------
# GENERATE REPORT BUTTON
# --------------------------------------------------

st.subheader("📥 Download Report")

if st.button("Generate PDF Report"):

    pdf_data = generate_pdf()

    st.success(
        "PDF Report Generated Successfully!"
    )

    st.download_button(
        label="Download PDF Report",
        data=pdf_data,
        file_name="ESG_Predictive_Maintenance_Report.pdf",
        mime="application/pdf"
    )

# --------------------------------------------------
# INSIGHTS
# --------------------------------------------------

st.subheader("💡 Report Insights")

if esg_score >= 80:
    st.success(
        "Excellent ESG Performance."
    )

elif esg_score >= 60:
    st.warning(
        "Moderate ESG Performance."
    )

else:
    st.error(
        "High Carbon Footprint Detected."
    )

if total_failures > 150:
    st.warning(
        "High machine failure count detected. Preventive maintenance recommended."
    )
else:
    st.success(
        "Maintenance performance is within acceptable limits."
    )
