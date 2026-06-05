"""
Investment Analysis Module
==========================

Purpose:
--------
1. Green Investment Analysis
2. ESG-Based Investment Scoring
3. Sustainability ROI Estimation
4. Investment Risk Assessment
5. Portfolio Sustainability Evaluation
6. Green Investment Recommendations

Used By:
--------
- 11_Green_Investment_Analyzer.py
- ESG Dashboard
- AI Sustainability Advisor

Author:
--------
AI-ESG-Predictive-Maintenance
"""

import pandas as pd
import numpy as np


# ==========================================================
# ESG INVESTMENT SCORE
# ==========================================================

def calculate_investment_score(
    esg_score,
    climate_risk_score,
    carbon_emission
):
    """
    Calculate investment attractiveness score.
    Score Range: 0 - 100
    """

    score = (
        (esg_score * 0.60)
        + ((100 - climate_risk_score) * 0.25)
        + ((100 - min(carbon_emission, 100)) * 0.15)
    )

    return round(score, 2)


# ==========================================================
# INVESTMENT RATING
# ==========================================================

def get_investment_rating(
    investment_score
):
    """
    Investment Rating Classification.
    """

    if investment_score >= 90:
        return "AAA"

    elif investment_score >= 80:
        return "AA"

    elif investment_score >= 70:
        return "A"

    elif investment_score >= 60:
        return "BBB"

    elif investment_score >= 50:
        return "BB"

    else:
        return "B"


# ==========================================================
# INVESTMENT RISK LEVEL
# ==========================================================

def calculate_investment_risk(
    climate_risk_score,
    esg_score
):
    """
    Risk Assessment.
    """

    risk = (
        climate_risk_score * 0.6
        + (100 - esg_score) * 0.4
    )

    return round(risk, 2)


# ==========================================================
# RISK CATEGORY
# ==========================================================

def classify_risk(
    risk_score
):
    """
    Risk Category.
    """

    if risk_score >= 75:
        return "High"

    elif risk_score >= 50:
        return "Medium"

    else:
        return "Low"


# ==========================================================
# GREEN ROI ESTIMATION
# ==========================================================

def estimate_green_roi(
    investment_amount,
    annual_savings,
    years=5
):
    """
    Return on Investment.
    """

    total_savings = annual_savings * years

    roi = (
        (
            total_savings
            - investment_amount
        )
        / investment_amount
    ) * 100

    return {
        "Investment Amount":
            round(investment_amount, 2),

        "Total Savings":
            round(total_savings, 2),

        "ROI (%)":
            round(roi, 2)
    }


# ==========================================================
# PAYBACK PERIOD
# ==========================================================

def calculate_payback_period(
    investment_amount,
    annual_savings
):
    """
    Years required to recover investment.
    """

    if annual_savings <= 0:
        return None

    return round(
        investment_amount / annual_savings,
        2
    )


# ==========================================================
# CARBON SAVINGS VALUE
# ==========================================================

def estimate_carbon_savings_value(
    carbon_reduction_tons,
    carbon_price=50
):
    """
    Monetary value of carbon savings.
    """

    value = (
        carbon_reduction_tons
        * carbon_price
    )

    return round(value, 2)


# ==========================================================
# PORTFOLIO SUSTAINABILITY SCORE
# ==========================================================

def portfolio_sustainability_score(
    esg_scores
):
    """
    Average ESG score of portfolio.
    """

    if len(esg_scores) == 0:
        return 0

    return round(
        np.mean(esg_scores),
        2
    )


# ==========================================================
# GREEN INVESTMENT ELIGIBILITY
# ==========================================================

def check_green_investment_eligibility(
    esg_score,
    climate_risk_score
):
    """
    Determine eligibility.
    """

    if (
        esg_score >= 70
        and climate_risk_score <= 50
    ):
        return "Eligible"

    return "Needs Improvement"


# ==========================================================
# INVESTMENT RECOMMENDATIONS
# ==========================================================

def generate_investment_recommendations(
    esg_score,
    climate_risk_score,
    carbon_emission
):
    """
    Generate investment recommendations.
    """

    recommendations = []

    if esg_score < 70:
        recommendations.append(
            "Improve ESG performance before seeking major green investments."
        )

    if climate_risk_score > 60:
        recommendations.append(
            "Reduce climate exposure through resilience initiatives."
        )

    if carbon_emission > 100:
        recommendations.append(
            "Invest in carbon reduction technologies."
        )

    if esg_score >= 80:
        recommendations.append(
            "Strong candidate for sustainable investment funds."
        )

    if not recommendations:
        recommendations.append(
            "Investment profile appears balanced."
        )

    return recommendations


# ==========================================================
# BENCHMARK COMPARISON
# ==========================================================

def compare_with_benchmark(
    company_score,
    benchmark_score
):
    """
    Compare investment score with benchmark.
    """

    difference = (
        company_score
        - benchmark_score
    )

    status = (
        "Above Benchmark"
        if difference > 0
        else "Below Benchmark"
    )

    return {
        "Company Score":
            company_score,

        "Benchmark Score":
            benchmark_score,

        "Difference":
            round(difference, 2),

        "Status":
            status
    }


# ==========================================================
# COMPLETE INVESTMENT REPORT
# ==========================================================

def generate_investment_report(
    esg_score,
    climate_risk_score,
    carbon_emission,
    investment_amount,
    annual_savings
):
    """
    Generate complete investment analysis.
    """

    investment_score = calculate_investment_score(
        esg_score,
        climate_risk_score,
        carbon_emission
    )

    risk_score = calculate_investment_risk(
        climate_risk_score,
        esg_score
    )

    return {
        "Investment Score":
            investment_score,

        "Investment Rating":
            get_investment_rating(
                investment_score
            ),

        "Risk Score":
            risk_score,

        "Risk Category":
            classify_risk(
                risk_score
            ),

        "ROI Analysis":
            estimate_green_roi(
                investment_amount,
                annual_savings
            ),

        "Payback Period (Years)":
            calculate_payback_period(
                investment_amount,
                annual_savings
            ),

        "Eligibility":
            check_green_investment_eligibility(
                esg_score,
                climate_risk_score
            ),

        "Recommendations":
            generate_investment_recommendations(
                esg_score,
                climate_risk_score,
                carbon_emission
            )
    }


# ==========================================================
# DATASET SUMMARY
# ==========================================================

def investment_dataset_summary(
    df,
    score_column="Investment_Score"
):
    """
    Dataset-level statistics.
    """

    if score_column not in df.columns:
        return {}

    return {
        "Average Score":
            round(df[score_column].mean(), 2),

        "Maximum Score":
            round(df[score_column].max(), 2),

        "Minimum Score":
            round(df[score_column].min(), 2),

        "Total Records":
            len(df)
    }


# ==========================================================
# TEST MODULE
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("GREEN INVESTMENT ANALYSIS MODULE")
    print("=" * 60)

    report = generate_investment_report(
        esg_score=82,
        climate_risk_score=35,
        carbon_emission=55,
        investment_amount=100000,
        annual_savings=25000
    )

    for key, value in report.items():
        print(f"{key}: {value}")

    print("\nModule Loaded Successfully")
    print("=" * 60)
