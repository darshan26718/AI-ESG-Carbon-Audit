"""
Net Zero Planner Module
=======================

Purpose:
--------
1. Net-Zero Roadmap Generation
2. Carbon Reduction Planning
3. Emission Reduction Forecasting
4. Sustainability Goal Tracking
5. Carbon Budget Estimation
6. Renewable Energy Transition Planning

Used By:
--------
- 8_Net_Zero_Planner.py
- ESG Dashboard
- AI Sustainability Advisor
- Climate Risk Assessment

Author:
--------
AI-ESG-Predictive-Maintenance
"""

from datetime import datetime
import pandas as pd
import numpy as np


# ==========================================================
# YEARS REMAINING TO TARGET
# ==========================================================

def calculate_years_remaining(target_year=2050):
    """
    Calculate years remaining until target year.
    """

    current_year = datetime.now().year

    return max(0, target_year - current_year)


# ==========================================================
# ANNUAL REDUCTION REQUIRED
# ==========================================================

def annual_reduction_required(
    current_emission,
    target_emission=0,
    target_year=2050
):
    """
    Calculate annual reduction required.
    """

    years = calculate_years_remaining(target_year)

    if years == 0:
        return 0

    reduction = (
        current_emission - target_emission
    ) / years

    return round(reduction, 2)


# ==========================================================
# NET ZERO ROADMAP
# ==========================================================

def generate_net_zero_roadmap(
    current_emission,
    target_year=2050
):
    """
    Generate year-wise roadmap.
    """

    current_year = datetime.now().year

    years_remaining = target_year - current_year

    if years_remaining <= 0:
        return pd.DataFrame()

    annual_reduction = (
        current_emission / years_remaining
    )

    roadmap = []

    remaining_emission = current_emission

    for year in range(
        current_year,
        target_year + 1
    ):

        roadmap.append({
            "Year": year,
            "Projected_Emission":
                round(
                    max(0, remaining_emission),
                    2
                )
        })

        remaining_emission -= annual_reduction

    return pd.DataFrame(roadmap)


# ==========================================================
# NET ZERO PROGRESS
# ==========================================================

def calculate_net_zero_progress(
    baseline_emission,
    current_emission
):
    """
    Calculate progress percentage.
    """

    if baseline_emission == 0:
        return 0

    progress = (
        (
            baseline_emission
            - current_emission
        )
        / baseline_emission
    ) * 100

    return round(progress, 2)


# ==========================================================
# CARBON BUDGET
# ==========================================================

def estimate_carbon_budget(
    current_emission,
    target_year=2050
):
    """
    Estimate allowable carbon budget.
    """

    years = calculate_years_remaining(
        target_year
    )

    budget = current_emission * years

    return round(budget, 2)


# ==========================================================
# RENEWABLE TRANSITION PLAN
# ==========================================================

def renewable_transition_plan(
    current_renewable_percentage,
    target_percentage=100,
    target_year=2050
):
    """
    Renewable energy adoption plan.
    """

    years = calculate_years_remaining(
        target_year
    )

    if years == 0:
        return 0

    annual_growth = (
        target_percentage
        - current_renewable_percentage
    ) / years

    return round(annual_growth, 2)


# ==========================================================
# NET ZERO STATUS
# ==========================================================

def classify_net_zero_status(
    progress_percentage
):
    """
    Categorize progress.
    """

    if progress_percentage >= 80:
        return "Excellent"

    elif progress_percentage >= 60:
        return "Good"

    elif progress_percentage >= 40:
        return "Moderate"

    else:
        return "Needs Improvement"


# ==========================================================
# EMISSION REDUCTION SCENARIO
# ==========================================================

def emission_reduction_scenario(
    current_emission,
    reduction_percent
):
    """
    Simulate reduction scenario.
    """

    reduced_emission = (
        current_emission
        * (1 - reduction_percent / 100)
    )

    savings = (
        current_emission
        - reduced_emission
    )

    return {
        "Current Emission":
            round(current_emission, 2),

        "Reduction (%)":
            reduction_percent,

        "Future Emission":
            round(reduced_emission, 2),

        "Carbon Savings":
            round(savings, 2)
    }


# ==========================================================
# NET ZERO RECOMMENDATIONS
# ==========================================================

def generate_net_zero_recommendations(
    current_emission,
    renewable_energy_percentage
):
    """
    Generate actionable recommendations.
    """

    recommendations = []

    if current_emission > 500:
        recommendations.append(
            "Urgently reduce emissions through operational efficiency."
        )

    if renewable_energy_percentage < 50:
        recommendations.append(
            "Increase renewable energy adoption."
        )

    if renewable_energy_percentage < 80:
        recommendations.append(
            "Expand solar and wind energy integration."
        )

    if current_emission < 200:
        recommendations.append(
            "Maintain current sustainability initiatives."
        )

    if not recommendations:
        recommendations.append(
            "Strong Net-Zero trajectory detected."
        )

    return recommendations


# ==========================================================
# ESG IMPACT ESTIMATION
# ==========================================================

def estimate_esg_impact(
    current_esg_score,
    emission_reduction_percent
):
    """
    Estimate ESG improvement.
    """

    esg_improvement = (
        emission_reduction_percent * 0.3
    )

    future_esg_score = min(
        100,
        current_esg_score + esg_improvement
    )

    return {
        "Current ESG Score":
            current_esg_score,

        "Estimated Future ESG Score":
            round(future_esg_score, 2)
    }


# ==========================================================
# COMPLETE NET ZERO REPORT
# ==========================================================

def generate_net_zero_report(
    baseline_emission,
    current_emission,
    renewable_energy_percentage,
    current_esg_score,
    target_year=2050
):
    """
    Generate complete report.
    """

    progress = calculate_net_zero_progress(
        baseline_emission,
        current_emission
    )

    roadmap = generate_net_zero_roadmap(
        current_emission,
        target_year
    )

    recommendations = (
        generate_net_zero_recommendations(
            current_emission,
            renewable_energy_percentage
        )
    )

    return {
        "Progress (%)":
            progress,

        "Status":
            classify_net_zero_status(
                progress
            ),

        "Annual Reduction Required":
            annual_reduction_required(
                current_emission,
                0,
                target_year
            ),

        "Carbon Budget":
            estimate_carbon_budget(
                current_emission,
                target_year
            ),

        "Renewable Growth Required":
            renewable_transition_plan(
                renewable_energy_percentage,
                100,
                target_year
            ),

        "Recommendations":
            recommendations,

        "Roadmap":
            roadmap,

        "ESG Impact":
            estimate_esg_impact(
                current_esg_score,
                progress
            )
    }


# ==========================================================
# TEST MODULE
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("NET ZERO PLANNER MODULE")
    print("=" * 60)

    report = generate_net_zero_report(
        baseline_emission=1000,
        current_emission=650,
        renewable_energy_percentage=45,
        current_esg_score=72,
        target_year=2050
    )

    print("\nProgress:")
    print(report["Progress (%)"], "%")

    print("\nStatus:")
    print(report["Status"])

    print("\nAnnual Reduction Required:")
    print(report["Annual Reduction Required"])

    print("\nRecommendations:")

    for rec in report["Recommendations"]:
        print("-", rec)

    print("\nModule Loaded Successfully")
    print("=" * 60)
