# utils/carbon_calculator.py

"""
Carbon Calculator Module
========================

## Purpose:

1. Calculate Carbon Emissions
2. Estimate Carbon Footprint
3. Calculate Carbon Intensity
4. Carbon Reduction Analysis
5. Net-Zero Progress Tracking
6. ESG Environmental Metrics

## Used By:

* ESG Dashboard
* Carbon Forecasting
* Net-Zero Planner
* Sustainability Advisor
* ESG Scoring

Author: AI-ESG-Predictive-Maintenance
"""

import pandas as pd
import numpy as np

# ==========================================================

# CARBON EMISSION CALCULATOR

# ==========================================================

def calculate_carbon_emission(
electricity_kwh,
fuel_liters,
travel_km
):
"""
Calculate total carbon emissions.

```
Emission Factors:
Electricity = 0.82 kg CO₂/kWh
Fuel = 2.31 kg CO₂/liter
Travel = 0.12 kg CO₂/km
"""

electricity_emission = electricity_kwh * 0.82
fuel_emission = fuel_liters * 2.31
travel_emission = travel_km * 0.12

total_emission = (
    electricity_emission
    + fuel_emission
    + travel_emission
)

return round(total_emission, 2)
```

# ==========================================================

# ENERGY EMISSION

# ==========================================================

def calculate_energy_emission(
energy_consumption_kwh
):
"""
Calculate emissions from energy usage.
"""

```
emission_factor = 0.82

return round(
    energy_consumption_kwh * emission_factor,
    2
)
```

# ==========================================================

# FUEL EMISSION

# ==========================================================

def calculate_fuel_emission(
fuel_liters
):
"""
Calculate emissions from fuel.
"""

```
emission_factor = 2.31

return round(
    fuel_liters * emission_factor,
    2
)
```

# ==========================================================

# TRAVEL EMISSION

# ==========================================================

def calculate_travel_emission(
distance_km
):
"""
Calculate emissions from transportation.
"""

```
emission_factor = 0.12

return round(
    distance_km * emission_factor,
    2
)
```

# ==========================================================

# CARBON INTENSITY

# ==========================================================

def carbon_intensity(
carbon_emission,
production_output
):
"""
Carbon Emission per Unit Produced.
"""

```
if production_output == 0:
    return 0

return round(
    carbon_emission / production_output,
    4
)
```

# ==========================================================

# EMISSION PER EMPLOYEE

# ==========================================================

def emission_per_employee(
carbon_emission,
employee_count
):
"""
Carbon Emission per Employee.
"""

```
if employee_count == 0:
    return 0

return round(
    carbon_emission / employee_count,
    4
)
```

# ==========================================================

# CARBON REDUCTION PERCENTAGE

# ==========================================================

def carbon_reduction_percentage(
previous_emission,
current_emission
):
"""
Calculate reduction percentage.
"""

```
if previous_emission == 0:
    return 0

reduction = (
    (
        previous_emission
        - current_emission
    )
    / previous_emission
) * 100

return round(
    reduction,
    2
)
```

# ==========================================================

# NET ZERO PROGRESS

# ==========================================================

def net_zero_progress(
baseline_emission,
current_emission
):
"""
Calculate Net-Zero progress.
"""

```
if baseline_emission == 0:
    return 0

progress = (
    (
        baseline_emission
        - current_emission
    )
    / baseline_emission
) * 100

return round(
    progress,
    2
)
```

# ==========================================================

# CARBON FOOTPRINT CATEGORY

# ==========================================================

def classify_carbon_footprint(
carbon_emission
):
"""
Categorize carbon footprint.
"""

```
if carbon_emission < 100:
    return "Low"

elif carbon_emission < 300:
    return "Moderate"

elif carbon_emission < 600:
    return "High"

else:
    return "Critical"
```

# ==========================================================

# ESG ENVIRONMENTAL SCORE

# ==========================================================

def environmental_score(
renewable_energy,
waste_recycled,
carbon_emission
):
"""
Calculate Environmental Score (0–100).
"""

```
renewable_component = renewable_energy * 0.4
recycling_component = waste_recycled * 0.3

carbon_component = max(
    0,
    100 - carbon_emission
) * 0.3

score = (
    renewable_component
    + recycling_component
    + carbon_component
)

return round(
    min(score, 100),
    2
)
```

# ==========================================================

# CARBON SAVINGS ESTIMATION

# ==========================================================

def estimate_carbon_savings(
current_emission,
reduction_target_percent
):
"""
Estimate future carbon savings.
"""

```
savings = (
    current_emission
    * reduction_target_percent
) / 100

future_emission = (
    current_emission
    - savings
)

return {
    "Current Emission": round(current_emission, 2),
    "Reduction Target (%)": reduction_target_percent,
    "Carbon Savings": round(savings, 2),
    "Future Emission": round(future_emission, 2)
}
```

# ==========================================================

# DATAFRAME CARBON SUMMARY

# ==========================================================

def carbon_summary(df):
"""
Generate carbon summary statistics.
"""

```
if "Carbon_Emission" not in df.columns:
    return {}

summary = {
    "Total Emission":
        round(df["Carbon_Emission"].sum(), 2),

    "Average Emission":
        round(df["Carbon_Emission"].mean(), 2),

    "Maximum Emission":
        round(df["Carbon_Emission"].max(), 2),

    "Minimum Emission":
        round(df["Carbon_Emission"].min(), 2)
}

return summary
```

# ==========================================================

# RECOMMENDATIONS

# ==========================================================

def carbon_recommendations(
carbon_emission
):
"""
Generate sustainability recommendations.
"""

```
recommendations = []

if carbon_emission > 500:
    recommendations.append(
        "Switch to renewable energy sources."
    )

if carbon_emission > 300:
    recommendations.append(
        "Improve energy efficiency systems."
    )

if carbon_emission > 150:
    recommendations.append(
        "Optimize transportation logistics."
    )

if not recommendations:
    recommendations.append(
        "Excellent carbon management."
    )

return recommendations
```

# ==========================================================

# MAIN TEST

# ==========================================================

if **name** == "**main**":

```
print("=" * 60)
print("CARBON CALCULATOR MODULE")
print("=" * 60)

emission = calculate_carbon_emission(
    electricity_kwh=500,
    fuel_liters=100,
    travel_km=200
)

print(
    f"Total Carbon Emission: {emission} kg CO₂"
)

print(
    "Category:",
    classify_carbon_footprint(emission)
)

print(
    "Net-Zero Progress:",
    net_zero_progress(
        1000,
        emission
    ),
    "%"
)

print("=" * 60)
print("Module Loaded Successfully")
print("=" * 60)
```
