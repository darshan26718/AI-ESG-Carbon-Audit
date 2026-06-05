# utils/esg_scoring.py

"""
ESG Scoring Module
==================

## Purpose:

1. Calculate ESG Score
2. Calculate Environmental Score
3. Calculate Social Score
4. Calculate Governance Score
5. Generate ESG Ratings
6. Benchmark ESG Performance
7. ESG Recommendations

## Used By:

* ESG Dashboard
* ESG Scoring Page
* ESG Benchmarking
* AI Sustainability Advisor
* Net-Zero Planner

Author: AI-ESG-Predictive-Maintenance
"""

import pandas as pd
import numpy as np

# ==========================================================

# ENVIRONMENTAL SCORE

# ==========================================================

def calculate_environmental_score(
renewable_energy_usage,
waste_recycled,
carbon_emission
):
"""
Environmental Score (0-100)
"""

```
renewable_score = renewable_energy_usage * 0.4
recycling_score = waste_recycled * 0.3

carbon_score = max(
    0,
    100 - carbon_emission
) * 0.3

score = (
    renewable_score
    + recycling_score
    + carbon_score
)

return round(
    min(score, 100),
    2
)
```

# ==========================================================

# SOCIAL SCORE

# ==========================================================

def calculate_social_score(
employee_satisfaction,
gender_diversity
):
"""
Social Score (0-100)
"""

```
score = (
    employee_satisfaction * 0.6
    + gender_diversity * 0.4
)

return round(score, 2)
```

# ==========================================================

# GOVERNANCE SCORE

# ==========================================================

def calculate_governance_score(
board_independence
):
"""
Governance Score (0-100)
"""

```
return round(
    board_independence,
    2
)
```

# ==========================================================

# OVERALL ESG SCORE

# ==========================================================

def calculate_esg_score(
renewable_energy_usage,
waste_recycled,
carbon_emission,
employee_satisfaction,
gender_diversity,
board_independence
):
"""
Calculate Final ESG Score.
"""

```
environmental = calculate_environmental_score(
    renewable_energy_usage,
    waste_recycled,
    carbon_emission
)

social = calculate_social_score(
    employee_satisfaction,
    gender_diversity
)

governance = calculate_governance_score(
    board_independence
)

esg_score = (
    environmental * 0.4
    + social * 0.3
    + governance * 0.3
)

return {
    "Environmental Score": round(environmental, 2),
    "Social Score": round(social, 2),
    "Governance Score": round(governance, 2),
    "ESG Score": round(esg_score, 2)
}
```

# ==========================================================

# ESG RATING

# ==========================================================

def get_esg_rating(esg_score):
"""
ESG Grade Classification
"""

```
if esg_score >= 90:
    return "AAA"

elif esg_score >= 80:
    return "AA"

elif esg_score >= 70:
    return "A"

elif esg_score >= 60:
    return "BBB"

elif esg_score >= 50:
    return "BB"

elif esg_score >= 40:
    return "B"

else:
    return "CCC"
```

# ==========================================================

# ESG PERFORMANCE CATEGORY

# ==========================================================

def get_esg_category(esg_score):

```
if esg_score >= 80:
    return "Excellent"

elif esg_score >= 60:
    return "Good"

elif esg_score >= 40:
    return "Moderate"

else:
    return "Poor"
```

# ==========================================================

# ESG BENCHMARK COMPARISON

# ==========================================================

def benchmark_esg_score(
company_score,
industry_average
):
"""
Compare company ESG against industry.
"""

```
difference = (
    company_score
    - industry_average
)

if difference > 0:
    status = "Above Industry Average"

elif difference < 0:
    status = "Below Industry Average"

else:
    status = "Equal to Industry Average"

return {
    "Company Score": company_score,
    "Industry Average": industry_average,
    "Difference": round(difference, 2),
    "Status": status
}
```

# ==========================================================

# ESG RISK LEVEL

# ==========================================================

def calculate_esg_risk(
esg_score
):
"""
ESG Risk Assessment
"""

```
if esg_score >= 80:
    return "Low Risk"

elif esg_score >= 60:
    return "Medium Risk"

else:
    return "High Risk"
```

# ==========================================================

# ESG RECOMMENDATIONS

# ==========================================================

def generate_esg_recommendations(
renewable_energy_usage,
waste_recycled,
carbon_emission,
employee_satisfaction,
gender_diversity,
board_independence
):
"""
Generate ESG improvement recommendations.
"""

```
recommendations = []

if renewable_energy_usage < 50:
    recommendations.append(
        "Increase renewable energy adoption."
    )

if waste_recycled < 50:
    recommendations.append(
        "Improve recycling initiatives."
    )

if carbon_emission > 100:
    recommendations.append(
        "Reduce carbon emissions through green technologies."
    )

if employee_satisfaction < 70:
    recommendations.append(
        "Improve employee engagement and workplace culture."
    )

if gender_diversity < 40:
    recommendations.append(
        "Enhance workforce diversity programs."
    )

if board_independence < 60:
    recommendations.append(
        "Strengthen governance and board independence."
    )

if not recommendations:
    recommendations.append(
        "Excellent ESG performance. Maintain current strategy."
    )

return recommendations
```

# ==========================================================

# DATAFRAME ESG ANALYSIS

# ==========================================================

def dataframe_esg_summary(df):
"""
ESG Dataset Summary
"""

```
required_columns = [
    "ESG_Score"
]

for col in required_columns:
    if col not in df.columns:
        return {}

summary = {
    "Average ESG Score":
        round(df["ESG_Score"].mean(), 2),

    "Maximum ESG Score":
        round(df["ESG_Score"].max(), 2),

    "Minimum ESG Score":
        round(df["ESG_Score"].min(), 2),

    "Total Records":
        len(df)
}

return summary
```

# ==========================================================

# ESG TREND ANALYSIS

# ==========================================================

def esg_trend_analysis(
previous_score,
current_score
):
"""
ESG Growth Analysis
"""

```
change = current_score - previous_score

percentage_change = (
    (change / previous_score) * 100
    if previous_score != 0
    else 0
)

return {
    "Previous Score": previous_score,
    "Current Score": current_score,
    "Change": round(change, 2),
    "Percentage Change":
        round(percentage_change, 2)
}
```

# ==========================================================

# MAIN TESTING

# ==========================================================

if **name** == "**main**":

```
print("=" * 60)
print("ESG SCORING MODULE")
print("=" * 60)

result = calculate_esg_score(
    renewable_energy_usage=60,
    waste_recycled=70,
    carbon_emission=40,
    employee_satisfaction=85,
    gender_diversity=45,
    board_independence=80
)

print("\nESG Results")
print(result)

rating = get_esg_rating(
    result["ESG Score"]
)

print("\nESG Rating:", rating)

risk = calculate_esg_risk(
    result["ESG Score"]
)

print("Risk Level:", risk)

print("=" * 60)
print("Module Loaded Successfully")
print("=" * 60)
```
