# utils/feature_engineering.py

"""
Feature Engineering Module
==========================

## Purpose:

1. Handle Missing Values
2. Encode Categorical Features
3. Create Carbon Features
4. Create Maintenance Features
5. Create ESG Features
6. Remove Outliers
7. Scale Numerical Features
8. Build Complete Feature Engineering Pipeline

## Used By:

* Carbon Forecasting
* Predictive Maintenance
* ESG Scoring
* Climate Risk Assessment

Author: AI-ESG-Predictive-Maintenance
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import (
LabelEncoder,
StandardScaler
)

# ==========================================================

# HANDLE MISSING VALUES

# ==========================================================

def handle_missing_values(df):
"""
Fill missing values.

```
Numeric -> Median
Categorical -> Mode
"""

df = df.copy()

numerical_cols = df.select_dtypes(
    include=["int64", "float64"]
).columns

categorical_cols = df.select_dtypes(
    include=["object", "category"]
).columns

for col in numerical_cols:
    df[col] = df[col].fillna(
        df[col].median()
    )

for col in categorical_cols:
    df[col] = df[col].fillna(
        df[col].mode()[0]
    )

return df
```

# ==========================================================

# ENCODE CATEGORICAL FEATURES

# ==========================================================

def encode_categorical_features(df):
"""
Encode categorical columns using Label Encoding.
"""

```
df = df.copy()

categorical_cols = df.select_dtypes(
    include=["object", "category"]
).columns

encoders = {}

for col in categorical_cols:

    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(
        df[col].astype(str)
    )

    encoders[col] = encoder

return df, encoders
```

# ==========================================================

# CARBON FEATURE ENGINEERING

# ==========================================================

def create_carbon_features(df):
"""
Create carbon-related engineered features.
"""

```
df = df.copy()

if (
    "Energy_Consumption" in df.columns
    and "Production_Output" in df.columns
):
    df["Energy_Per_Output"] = (
        df["Energy_Consumption"]
        / (df["Production_Output"] + 1)
    )

if (
    "Carbon_Emission" in df.columns
    and "Employee_Count" in df.columns
):
    df["Emission_Per_Employee"] = (
        df["Carbon_Emission"]
        / (df["Employee_Count"] + 1)
    )

if (
    "Renewable_Energy_Usage" in df.columns
    and "Carbon_Emission" in df.columns
):
    df["Green_Energy_Index"] = (
        df["Renewable_Energy_Usage"]
        / (df["Carbon_Emission"] + 1)
    )

return df
```

# ==========================================================

# MAINTENANCE FEATURE ENGINEERING

# ==========================================================

def create_maintenance_features(df):
"""
Create machine health indicators.
"""

```
df = df.copy()

if (
    "Temperature" in df.columns
    and "Vibration" in df.columns
):
    df["Temp_Vibration_Index"] = (
        df["Temperature"]
        * df["Vibration"]
    )

if (
    "Pressure" in df.columns
    and "Operating_Hours" in df.columns
):
    df["Pressure_Load_Index"] = (
        df["Pressure"]
        * df["Operating_Hours"]
    )

if (
    "Temperature" in df.columns
    and "Operating_Hours" in df.columns
):
    df["Wear_Risk_Index"] = (
        df["Temperature"]
        * df["Operating_Hours"]
    )

return df
```

# ==========================================================

# ESG FEATURE ENGINEERING

# ==========================================================

def create_esg_features(df):
"""
Create ESG composite indicators.
"""

```
df = df.copy()

# Environmental Score
if (
    "Renewable_Energy_Usage" in df.columns
    and "Waste_Recycled" in df.columns
):
    df["Environmental_Index"] = (
        df["Renewable_Energy_Usage"]
        + df["Waste_Recycled"]
    ) / 2

# Social Score
if (
    "Employee_Satisfaction" in df.columns
    and "Gender_Diversity" in df.columns
):
    df["Social_Index"] = (
        df["Employee_Satisfaction"]
        + df["Gender_Diversity"]
    ) / 2

# Governance Score
if "Board_Independence" in df.columns:
    df["Governance_Index"] = (
        df["Board_Independence"]
    )

return df
```

# ==========================================================

# OUTLIER REMOVAL USING IQR

# ==========================================================

def remove_outliers(df):
"""
Remove outliers using IQR method.
"""

```
df = df.copy()

numerical_cols = df.select_dtypes(
    include=np.number
).columns

for col in numerical_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    df = df[
        (df[col] >= lower_bound)
        & (df[col] <= upper_bound)
    ]

return df
```

# ==========================================================

# SCALE NUMERICAL FEATURES

# ==========================================================

def scale_features(df):
"""
Standardize numerical features.
"""

```
df = df.copy()

scaler = StandardScaler()

numerical_cols = df.select_dtypes(
    include=np.number
).columns

scaled_data = scaler.fit_transform(
    df[numerical_cols]
)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=numerical_cols,
    index=df.index
)

return scaled_df, scaler
```

# ==========================================================

# FEATURE SELECTION

# ==========================================================

def select_features(df, target_column=None):
"""
Select features by removing target column.
"""

```
if target_column is not None:
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y

return df
```

# ==========================================================

# COMPLETE FEATURE ENGINEERING PIPELINE

# ==========================================================

def feature_engineering_pipeline(df):
"""
Full end-to-end pipeline.
"""

```
df = handle_missing_values(df)

df, _ = encode_categorical_features(df)

df = create_carbon_features(df)

df = create_maintenance_features(df)

df = create_esg_features(df)

df = remove_outliers(df)

return df
```

# ==========================================================

# MODEL PREPARATION PIPELINE

# ==========================================================

def prepare_ml_dataset(df, target_column):

```
df = feature_engineering_pipeline(df)

X, y = select_features(
    df,
    target_column
)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_scaled = pd.DataFrame(
    X_scaled,
    columns=X.columns
)

return X_scaled, y, scaler
```

# ==========================================================

# DATASET SUMMARY

# ==========================================================

def dataset_summary(df):

```
summary = {
    "Rows": df.shape[0],
    "Columns": df.shape[1],
    "Missing Values": int(df.isnull().sum().sum()),
    "Duplicate Rows": int(df.duplicated().sum())
}

return summary
```

# ==========================================================

# FEATURE IMPORTANCE PREVIEW

# ==========================================================

def get_numeric_features(df):

```
return df.select_dtypes(
    include=np.number
).columns.tolist()
```

# ==========================================================

# MAIN TESTING

# ==========================================================

if **name** == "**main**":

```
print("=" * 60)
print("FEATURE ENGINEERING MODULE")
print("=" * 60)

sample_data = pd.DataFrame({
    "Temperature": [80, 90, 100],
    "Vibration": [0.3, 0.5, 0.7],
    "Pressure": [100, 120, 140],
    "Operating_Hours": [1000, 2000, 3000]
})

processed_data = create_maintenance_features(
    sample_data
)

print("\nOriginal Data")
print(sample_data)

print("\nEngineered Data")
print(processed_data)

print("\nModule Loaded Successfully")
print("=" * 60)
```

