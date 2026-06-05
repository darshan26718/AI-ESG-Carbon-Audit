# utils/report_generator.py

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet


# --------------------------------------------------
# ESG SCORE CALCULATION
# --------------------------------------------------

def calculate_esg_score(carbon_df):
    """
    Calculate ESG score based on average emissions.
    """

    avg_emission = carbon_df["CO2_Emission_Tons"].mean()

    score = max(
        0,
        round(100 - (avg_emission * 10), 2)
    )

    return score


# --------------------------------------------------
# PDF REPORT GENERATOR
# --------------------------------------------------

def generate_pdf_report(
    carbon_df,
    maintenance_df,
    global_df
):
    """
    Generate ESG & Predictive Maintenance PDF Report
    """

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # --------------------------------------------------
    # ESG METRICS
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

    esg_score = calculate_esg_score(
        carbon_df
    )

    # --------------------------------------------------
    # MAINTENANCE METRICS
    # --------------------------------------------------

    total_failures = maintenance_df[
        "Failure_Count"
    ].sum()

    total_downtime = maintenance_df[
        "Downtime_Hours"
    ].sum()

    total_maintenance_cost = maintenance_df[
        "Maintenance_Cost"
    ].sum()

    # --------------------------------------------------
    # TITLE
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "AI ESG & Predictive Maintenance Report",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    # --------------------------------------------------
    # ESG SECTION
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "ESG Sustainability Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"Total CO₂ Emissions: {total_emission:.2f} Tons",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Average CO₂ Emissions: {avg_emission:.2f} Tons",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Renewable Energy Usage: {renewable_energy:.2f} kWh",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"ESG Score: {esg_score}/100",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    # --------------------------------------------------
    # MAINTENANCE SECTION
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "Maintenance Analytics Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Failures: {int(total_failures)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Downtime Hours: {total_downtime:.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Maintenance Cost: ₹{total_maintenance_cost:,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    # --------------------------------------------------
    # GLOBAL CO₂ BENCHMARK
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "Global CO₂ Benchmark",
            styles["Heading1"]
        )
    )

    latest_year = global_df["Year"].max()

    latest_data = global_df[
        global_df["Year"] == latest_year
    ]

    top_country = latest_data.sort_values(
        by="CO2_Emissions",
        ascending=False
    ).iloc[0]

    elements.append(
        Paragraph(
            f"Highest Emitting Country ({latest_year}): "
            f"{top_country['Country']}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"CO₂ Emissions: "
            f"{top_country['CO2_Emissions']} Million Tons",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1, 15))

    # --------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------

    elements.append(
        Paragraph(
            "Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = [
        "Increase renewable energy adoption.",
        "Reduce fuel-intensive operations.",
        "Install energy-efficient equipment.",
        "Implement preventive maintenance schedules.",
        "Monitor machines with high downtime.",
        "Reduce carbon-intensive activities.",
        "Improve ESG compliance tracking.",
        "Encourage sustainable transportation."
    ]

    for recommendation in recommendations:
        elements.append(
            Paragraph(
                f"• {recommendation}",
                styles["BodyText"]
            )
        )

    elements.append(Spacer(1, 15))

    # --------------------------------------------------
    # ESG STATUS
    # --------------------------------------------------

    if esg_score >= 80:
        status = "Excellent Sustainability Performance"

    elif esg_score >= 60:
        status = "Moderate Sustainability Performance"

    else:
        status = "High Carbon Risk"

    elements.append(
        Paragraph(
            f"Overall ESG Status: {status}",
            styles["Heading2"]
        )
    )

    elements.append(PageBreak())

    # --------------------------------------------------
    # BUILD PDF
    # --------------------------------------------------

    doc.build(elements)

    pdf_data = buffer.getvalue()

    buffer.close()

    return pdf_data


# --------------------------------------------------
# SAVE PDF
# --------------------------------------------------

def save_pdf_report(
    pdf_data,
    filename="ESG_Predictive_Maintenance_Report.pdf"
):
    """
    Save PDF locally.
    """

    with open(filename, "wb") as file:
        file.write(pdf_data)

    return filename


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":
    print(
        "Report Generator Module Loaded Successfully"
    )
