import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

# LOAD DATA
df = pd.read_csv("data/esg_dataset.csv")

features = [
    "Carbon_Emission",
    "Renewable_Energy_Usage",
    "Waste_Recycled",
    "Employee_Satisfaction",
    "Gender_Diversity",
    "Board_Independence"
]

X = df[features]
y = df["ESG_Score"]

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# SCALE DATA
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# MODEL
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train_scaled, y_train)

# SAVE MODEL + SCALER
joblib.dump(model, "models/esg_scoring_model.pkl")
joblib.dump(scaler, "models/esg_scaler.pkl")

print("✅ Model rebuilt successfully (NO ERRORS)")
