# utils/data_preprocessing.py

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

def load_dataset(file_path):
    """
    Load CSV dataset
    """

    df = pd.read_csv(file_path)

    return df


# --------------------------------------------------
# CLEAN DATA
# --------------------------------------------------

def clean_data(df):
    """
    Remove duplicates and handle missing values
    """

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill numeric columns
    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(
            df[col].median()
        )

    # Fill categorical columns
    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_cols:
        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

    return df


# --------------------------------------------------
# ENCODE CATEGORICAL FEATURES
# --------------------------------------------------

def encode_features(df):
    """
    Encode object columns
    """

    label_encoders = {}

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_cols:

        encoder = LabelEncoder()

        df[col] = encoder.fit_transform(
            df[col]
        )

        label_encoders[col] = encoder

    return df, label_encoders


# --------------------------------------------------
# FEATURE SCALING
# --------------------------------------------------

def scale_features(X):
    """
    Standardize numerical features
    """

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler


# --------------------------------------------------
# PREPARE MAINTENANCE DATA
# --------------------------------------------------

def prepare_maintenance_data(df):
    """
    Prepare maintenance dataset
    """

    df = clean_data(df)

    features = [
        "Operating_Hours",
        "Temperature",
        "Vibration",
        "Pressure",
        "Humidity",
        "Downtime_Hours",
        "Maintenance_Cost"
    ]

    target = "Failure_Count"

    X = df[features]

    y = df[target]

    X_scaled, scaler = scale_features(X)

    return X_scaled, y, scaler


# --------------------------------------------------
# PREPARE CARBON DATA
# --------------------------------------------------

def prepare_carbon_data(df):
    """
    Prepare carbon emission dataset
    """

    df = clean_data(df)

    features = [
        "Electricity_kWh",
        "Fuel_Liters",
        "Travel_km",
        "Waste_kg",
        "Renewable_Energy_kWh"
    ]

    target = "CO2_Emission_Tons"

    X = df[features]

    y = df[target]

    X_scaled, scaler = scale_features(X)

    return X_scaled, y, scaler


# --------------------------------------------------
# TRAIN TEST SPLIT
# --------------------------------------------------

def split_data(
    X,
    y,
    test_size=0.2,
    random_state=42
):
    """
    Split dataset into train and test
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )


# --------------------------------------------------
# COMPLETE PREPROCESSING PIPELINE
# --------------------------------------------------

def preprocess_dataset(
    file_path,
    target_column
):
    """
    Generic preprocessing pipeline
    """

    df = load_dataset(file_path)

    df = clean_data(df)

    df, encoders = encode_features(df)

    X = df.drop(
        columns=[target_column]
    )

    y = df[target_column]

    X_scaled, scaler = scale_features(X)

    X_train, X_test, y_train, y_test = split_data(
        X_scaled,
        y
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        scaler,
        encoders
    )


# --------------------------------------------------
# TEST MODULE
# --------------------------------------------------

if __name__ == "__main__":

    print("Data Preprocessing Module Loaded Successfully")
