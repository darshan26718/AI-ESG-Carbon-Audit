"""
Climate Risk Assessment Module
==============================

Purpose:
--------
1. Climate Risk Scoring
2. Physical Risk Assessment
3. Transition Risk Assessment
4. Carbon Exposure Analysis
5. Climate Vulnerability Index
6. ESG Climate Risk Reporting

Used By:
--------
- 10_Climate_Risk_Assessment.py
- ESG Dashboard
- AI Sustainability Advisor
- Net Zero Planner

Author:
--------
AI-ESG-Predictive-Maintenance
"""

import pandas as pd
import numpy as np


# ==========================================================
# PHYSICAL CLIMATE RISK
# ==========================================================

def calculate_physical_risk(
    flood_risk,
    drought_risk,
    heatwave_risk
):
    """
    Calculate physical climate risk score.
    Inputs expected between 0 and 100.
    """

    score = (
        flood_risk * 0.35 +
        drought_risk * 0.30 +
        heatwave_risk * 0.35
    )

    return round(score, 2)


# ==========================================================
# TRANSITION RISK
# ==========================================================

def calculate_transition_risk(
    carbon_dependency,
    fossil_fuel_usage,
    regulatory_exposure
):
    """
    Calculate transition risk score.
    Inputs expected between 0 and 100.
    """

    score = (
        carbon_dependency * 0.40 +
        fossil_fuel_usage * 0.30 +
        regulatory_exposure * 0.30
    )

    return round(score, 2)


# ==========================================================
# CLIMATE VULNERABILITY INDEX
# ==========================================================

def calculate_vulnerability_index(
    physical_risk,
    transition_risk
):
    """
    Combined climate vulnerability index.
    """

    vulnerability = (
        physical_risk * 0.5 +
        transition_risk * 0.5
    )

    return round(vulnerability, 2)


# ==========================================================
# CARBON EXPOSURE SCORE
# ==========================================================

def calculate_carbon_exposure(
    carbon_emission,
    industry_benchmark
):
    """
    Compare emissions against benchmark.
    """

    if industry_benchmark <= 0:
        return 0

    exposure = (
        carbon_emission /
        industry_benchmark
    ) * 100

    return round(exposure, 2)


# ==========================================================
# OVERALL CLIMATE RISK SCORE
# ==========================================================

def calculate_climate_risk_score(
    physical_risk,
    transition_risk,
    carbon_exposure
):
    """
    Overall climate risk score.
    """

    score = (
        physical_risk * 0.4 +
        transition_risk * 0.4 +
        min(carbon_exposure, 100) * 0.2
    )

    return round(score, 2)


# ==========================================================
# CLIMATE RISK CATEGORY
# ==========================================================

def classify_climate_risk(
    climate_risk_score
):
    """
    Risk classification.
    """

    if climate_risk_score >= 80:
        return "Very High"

    elif climate_risk_score >= 60:
        return "High"

    elif climate_risk_score >= 40:
        return "Moderate"

    elif climate_risk_score >= 20:
        return "Low"

    else:
        return "Very Low"


# ==========================================================
# CLIMATE RISK RECOMMENDATIONS
# ==========================================================

def generate_climate_risk_recommendations(
    climate_risk_score
):
    """
    Generate climate adaptation recommendations.
    """

    recommendations = []

    if climate_risk_score >= 80:
        recommendations.extend([
            "Develop an immediate climate adaptation strategy.",
            "Invest in resilient infrastructure.",
            "Reduce carbon-intensive operations."
        ])

    elif climate_risk_score >= 60:
        recommendations.extend([
            "Strengthen climate resilience planning.",
            "Increase renewable energy adoption.",
            "Conduct quarterly climate risk reviews."
        ])

    elif climate_risk_score >= 40:
        recommendations.extend([
            "Monitor climate-related risks regularly.",
            "Implement energy efficiency initiatives."
        ])

    else:
        recommendations.append(
            "Current climate risk is manageable. Continue monitoring."
        )

    return recommendations


# ==========================================================
# CLIMATE READINESS SCORE
# ==========================================================

def calculate_climate_readiness(
    renewable_energy_usage,
    sustainability_investment,
    climate_policy_score
):
    """
    Organization readiness for climate challenges.
    Inputs expected between 0 and 100.
    """

    score = (
        renewable_energy_usage * 0.4 +
        sustainability_investment * 0.3 +
        climate_policy_score * 0.3
    )

    return round(score, 2)


# ==========================================================
# CLIMATE IMPACT FORECAST
# ==========================================================

def forecast_climate_impact(
    current_risk_score,
    annual_improvement_percent,
    years=5
):
    """
    Forecast future climate risk.
    """

    forecast = []

    risk = current_risk_score

    for year in range(1, years + 1):

        risk = risk * (
            1 - annual_improvement_percent / 100
        )

        forecast.append({
            "Year": year,
            "Projected_Risk": round(risk, 2)
        })

    return pd.DataFrame(forecast)


# ==========================================================
# ESG CLIMATE IMPACT
# ==========================================================

def estimate_esg_climate_impact(
    current_esg_score,
    climate_risk_score
):
    """
    Estimate ESG impact due to climate risk.
    """

    impact_factor = climate_risk_score * 0.10

    adjusted_esg_score = max(
        0,
        current_esg_score - impact_factor
    )

    return {
        "Current ESG Score":
            current_esg_score,

        "Climate Adjusted ESG Score":
            round(adjusted_esg_score, 2)
    }


# ==========================================================
# COMPLETE CLIMATE RISK REPORT
# ==========================================================

def generate_climate_risk_report(
    flood_risk,
    drought_risk,
    heatwave_risk,
    carbon_dependency,
    fossil_fuel_usage,
    regulatory_exposure,
    carbon_emission,
    industry_benchmark
):
    """
    Complete climate risk assessment.
    """

    physical_risk = calculate_physical_risk(
        flood_risk,
        drought_risk,
        heatwave_risk
    )

    transition_risk = calculate_transition_risk(
        carbon_dependency,
        fossil_fuel_usage,
        regulatory_exposure
    )

    carbon_exposure = calculate_carbon_exposure(
        carbon_emission,
        industry_benchmark
    )

    climate_risk_score = calculate_climate_risk_score(
        physical_risk,
        transition_risk,
        carbon_exposure
    )

    return {
        "Physical Risk":
            physical_risk,

        "Transition Risk":
            transition_risk,

        "Carbon Exposure":
            carbon_exposure,

        "Climate Risk Score":
            climate_risk_score,

        "Risk Category":
            classify_climate_risk(
                climate_risk_score
            ),

        "Recommendations":
            generate_climate_risk_recommendations(
                climate_risk_score
            )
    }


# ==========================================================
# DATASET CLIMATE SUMMARY
# ==========================================================

def climate_dataset_summary(
    df,
    risk_column="Climate_Risk_Score"
):
    """
    Dataset-level summary.
    """

    if risk_column not in df.columns:
        return {}

    return {
        "Average Risk":
            round(df[risk_column].mean(), 2),

        "Maximum Risk":
            round(df[risk_column].max(), 2),

        "Minimum Risk":
            round(df[risk_column].min(), 2),

        "Total Records":
            len(df)
    }


# ==========================================================
# TEST MODULE
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("CLIMATE RISK MODULE")
    print("=" * 60)

    report = generate_climate_risk_report(
        flood_risk=70,
        drought_risk=60,
        heatwave_risk=75,
        carbon_dependency=80,
        fossil_fuel_usage=65,
        regulatory_exposure=55,
        carbon_emission=450,
        industry_benchmark=300
    )

    print("\nClimate Risk Report")

    for key, value in report.items():
        print(f"{key}: {value}")

    print("\nModule Loaded Successfully")
    print("=" * 60)
