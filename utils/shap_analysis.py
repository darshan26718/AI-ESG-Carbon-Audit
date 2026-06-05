# utils/shap_analysis.py

"""
SHAP Analysis Module
====================

## Purpose:

1. Explain Machine Learning Predictions
2. Generate SHAP Values
3. Feature Importance Analysis
4. Global Explainability
5. Local Explainability
6. SHAP Summary Plots
7. SHAP Waterfall Plots

## Used By:

* 5_SHAP_Explainability.py
* Predictive Maintenance
* ESG Scoring
* Carbon Forecasting

## Author:

AI-ESG-Predictive-Maintenance
"""

import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
import joblib

# ==========================================================

# LOAD MODEL

# ==========================================================

def load_model(model_path):
"""
Load trained ML model.
"""

```
model = joblib.load(model_path)

return model
```

# ==========================================================

# CREATE SHAP EXPLAINER

# ==========================================================

def create_explainer(model):
"""
Create SHAP Tree Explainer.
"""

```
explainer = shap.TreeExplainer(model)

return explainer
```

# ==========================================================

# CALCULATE SHAP VALUES

# ==========================================================

def calculate_shap_values(
model,
X
):
"""
Generate SHAP values.
"""

```
explainer = create_explainer(model)

shap_values = explainer.shap_values(X)

return explainer, shap_values
```

# ==========================================================

# FEATURE IMPORTANCE

# ==========================================================

def get_feature_importance(
shap_values,
feature_names
):
"""
Calculate mean absolute SHAP values.
"""

```
importance = np.abs(
    shap_values
).mean(axis=0)

importance_df = pd.DataFrame({

    "Feature":
        feature_names,

    "Importance":
        importance

})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

return importance_df
```

# ==========================================================

# TOP FEATURES

# ==========================================================

def get_top_features(
shap_values,
feature_names,
top_n=10
):
"""
Return top N features.
"""

```
importance_df = get_feature_importance(
    shap_values,
    feature_names
)

return importance_df.head(top_n)
```

# ==========================================================

# SHAP SUMMARY BAR PLOT

# ==========================================================

def plot_summary_bar(
shap_values,
X
):
"""
SHAP Feature Importance Bar Plot.
"""

```
plt.figure(figsize=(10, 6))

shap.summary_plot(
    shap_values,
    X,
    plot_type="bar",
    show=False
)

fig = plt.gcf()

return fig
```

# ==========================================================

# SHAP SUMMARY PLOT

# ==========================================================

def plot_summary(
shap_values,
X
):
"""
SHAP Summary Plot.
"""

```
plt.figure(figsize=(10, 6))

shap.summary_plot(
    shap_values,
    X,
    show=False
)

fig = plt.gcf()

return fig
```

# ==========================================================

# WATERFALL PLOT

# ==========================================================

def plot_waterfall(
explainer,
shap_values,
X,
row_index=0
):
"""
SHAP Waterfall Plot.
"""

```
explanation = shap.Explanation(

    values=shap_values[row_index],

    base_values=
        explainer.expected_value,

    data=X.iloc[row_index],

    feature_names=X.columns

)

plt.figure(figsize=(12, 6))

shap.plots.waterfall(
    explanation,
    show=False
)

fig = plt.gcf()

return fig
```

# ==========================================================

# FORCE PLOT

# ==========================================================

def create_force_plot(
explainer,
shap_values,
X,
row_index=0
):
"""
Interactive SHAP Force Plot.
"""

```
force_plot = shap.force_plot(

    explainer.expected_value,

    shap_values[row_index],

    X.iloc[row_index],

    matplotlib=False

)

return force_plot
```

# ==========================================================

# FEATURE CONTRIBUTION

# ==========================================================

def explain_prediction(
shap_values,
X,
row_index=0
):
"""
Explain individual prediction.
"""

```
contributions = pd.DataFrame({

    "Feature":
        X.columns,

    "SHAP Value":
        shap_values[row_index]

})

contributions["Impact"] = np.where(

    contributions["SHAP Value"] > 0,

    "Increase Prediction",

    "Decrease Prediction"

)

contributions = contributions.sort_values(

    by="SHAP Value",
    ascending=False

)

return contributions
```

# ==========================================================

# GLOBAL EXPLANATION REPORT

# ==========================================================

def generate_global_report(
shap_values,
X
):
"""
Global Explainability Report.
"""

```
importance_df = get_feature_importance(

    shap_values,
    X.columns

)

report = {

    "Top Feature":
        importance_df.iloc[0]["Feature"],

    "Top Importance":
        float(
            importance_df.iloc[0]["Importance"]
        ),

    "Total Features":
        len(importance_df)

}

return report
```

# ==========================================================

# LOCAL EXPLANATION REPORT

# ==========================================================

def generate_local_report(
shap_values,
X,
row_index=0
):
"""
Individual Prediction Report.
"""

```
explanation = explain_prediction(

    shap_values,
    X,
    row_index

)

return explanation.head(10)
```

# ==========================================================

# SAVE FEATURE IMPORTANCE

# ==========================================================

def save_feature_importance(
shap_values,
feature_names,
output_file
):
"""
Export SHAP Importance CSV.
"""

```
importance_df = get_feature_importance(

    shap_values,
    feature_names

)

importance_df.to_csv(
    output_file,
    index=False
)

return output_file
```

# ==========================================================

# COMPLETE PIPELINE

# ==========================================================

def run_shap_analysis(
model,
X
):
"""
End-to-End SHAP Analysis.
"""

```
explainer = create_explainer(model)

shap_values = explainer.shap_values(X)

importance_df = get_feature_importance(

    shap_values,
    X.columns

)

report = generate_global_report(

    shap_values,
    X

)

return {

    "explainer":
        explainer,

    "shap_values":
        shap_values,

    "importance":
        importance_df,

    "report":
        report

}
```

# ==========================================================

# MAIN TEST

# ==========================================================

if **name** == "**main**":

```
print("=" * 60)
print("SHAP ANALYSIS MODULE")
print("=" * 60)

print(
    "Load your model and dataset to run SHAP analysis."
)

print("=" * 60)
print("Module Loaded Successfully")
print("=" * 60)
```
