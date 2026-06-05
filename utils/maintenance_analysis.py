# utils/maintenance_analysis.py

import pandas as pd
import numpy as np

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

def load_maintenance_data(file_path):
    """
    Load maintenance dataset
    """

    return pd.read_csv(file_path)


# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

def calculate_kpis(df):
    """
    Calculate maintenance KPIs
    """

    kpis = {

        "Total Failures":
        int(df["Failure_Count"].sum()),

        "Total Downtime":
        float(df["Downtime_Hours"].sum()),

        "Average Downtime":
        round(
            df["Downtime_Hours"].mean(),
            2
        ),

        "Total Maintenance Cost":
        round(
            df["Maintenance_Cost"].sum(),
            2
        ),

        "Average Temperature":
        round(
            df["Temperature"].mean(),
            2
        ),

        "Average Vibration":
        round(
            df["Vibration"].mean(),
            2
        )
    }

    return kpis


# --------------------------------------------------
# FAILURE SUMMARY
# --------------------------------------------------

def failure_summary(df):
    """
    Summary of machine failures
    """

    return (
        df.groupby("Department")
        ["Failure_Count"]
        .sum()
        .reset_index()
        .sort_values(
            by="Failure_Count",
            ascending=False
        )
    )


# --------------------------------------------------
# DOWNTIME ANALYSIS
# --------------------------------------------------

def downtime_analysis(df):
    """
    Department-wise downtime
    """

    return (
        df.groupby("Department")
        ["Downtime_Hours"]
        .sum()
        .reset_index()
        .sort_values(
            by="Downtime_Hours",
            ascending=False
        )
    )


# --------------------------------------------------
# MAINTENANCE COST ANALYSIS
# --------------------------------------------------

def maintenance_cost_analysis(df):
    """
    Department-wise maintenance cost
    """

    return (
        df.groupby("Department")
        ["Maintenance_Cost"]
        .sum()
        .reset_index()
        .sort_values(
            by="Maintenance_Cost",
            ascending=False
        )
    )


# --------------------------------------------------
# TOP FAILED MACHINES
# --------------------------------------------------

def top_failed_machines(
    df,
    top_n=10
):
    """
    Top machines by failure count
    """

    return (
        df.sort_values(
            by="Failure_Count",
            ascending=False
        )
        .head(top_n)
    )


# --------------------------------------------------
# ROOT CAUSE ANALYSIS
# --------------------------------------------------

def root_cause_analysis(df):
    """
    Find factors most correlated
    with failure count
    """

    numeric_df = df.select_dtypes(
        include=np.number
    )

    corr_matrix = numeric_df.corr()

    failure_corr = (
        corr_matrix["Failure_Count"]
        .sort_values(
            ascending=False
        )
    )

    result = pd.DataFrame(
        {
            "Feature":
            failure_corr.index,

            "Correlation":
            failure_corr.values
        }
    )

    result = result[
        result["Feature"]
        != "Failure_Count"
    ]

    return result


# --------------------------------------------------
# CORRELATION MATRIX
# --------------------------------------------------

def correlation_matrix(df):
    """
    Correlation matrix
    """

    numeric_df = df.select_dtypes(
        include=np.number
    )

    return numeric_df.corr()


# --------------------------------------------------
# DEPARTMENT PERFORMANCE
# --------------------------------------------------

def department_performance(df):
    """
    Department level performance
    """

    summary = (
        df.groupby("Department")
        .agg(
            {
                "Failure_Count": "sum",
                "Downtime_Hours": "sum",
                "Maintenance_Cost": "sum",
                "Operating_Hours": "mean"
            }
        )
        .reset_index()
    )

    return summary


# --------------------------------------------------
# HIGH RISK MACHINES
# --------------------------------------------------

def high_risk_machines(
    df,
    failure_threshold=5
):
    """
    Machines with high failure count
    """

    return df[
        df["Failure_Count"]
        >= failure_threshold
    ].sort_values(
        by="Failure_Count",
        ascending=False
    )


# --------------------------------------------------
# MACHINE HEALTH SCORE
# --------------------------------------------------

def machine_health_score(df):
    """
    Simple health score calculation
    """

    temp_score = (
        100 - df["Temperature"]
    ) * 0.25

    vibration_score = (
        100 - df["Vibration"] * 10
    ) * 0.25

    downtime_score = (
        100 - df["Downtime_Hours"]
    ) * 0.25

    failure_score = (
        100 - df["Failure_Count"] * 10
    ) * 0.25

    df["Health_Score"] = (
        temp_score +
        vibration_score +
        downtime_score +
        failure_score
    )

    return df


# --------------------------------------------------
# HEALTH STATUS
# --------------------------------------------------

def health_status(score):

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Good"

    elif score >= 40:
        return "Moderate"

    return "Critical"


# --------------------------------------------------
# HEALTH REPORT
# --------------------------------------------------

def generate_health_report(df):
    """
    Machine health report
    """

    df = machine_health_score(df)

    df["Status"] = df[
        "Health_Score"
    ].apply(
        health_status
    )

    return df[
        [
            "Machine_ID",
            "Department",
            "Health_Score",
            "Status"
        ]
    ]


# --------------------------------------------------
# TEST MODULE
# --------------------------------------------------

if __name__ == "__main__":

    print(
        "Maintenance Analysis Module Loaded Successfully"
    )
