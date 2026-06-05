# pages/6_SHAP_Explainability.py

import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
import shap
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SHAP Explainability",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Explainable Maintenance (SHAP)")
st.markdown("""
Understand why the AI model predicts **machine failure risk** using SHAP.
""")

# =====================================================
# SAFE MODEL LOADER (FIXES YOUR ERROR)
# =====================================================

@st.cache_resource
def load_model():

    model_path = "models/maintenance_xgb_model.pkl"

    if not os.path.exists(model_path):
        st.error("❌ Missing model: models/maintenance_xgb_model.pkl")
        st.stop()

    try:
        model = joblib.load(model_path)
        return model

    except Exception as e:
        st.error("❌ Model loading failed (pickle/version mismatch)")
        st.exception(e)
        st.stop()

model = load_model()

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():
    df = pd.read_csv("data/maintenance_failure_dataset.csv")
    return df

df = load_data()

TARGET = "Failure"

X = df.drop(columns=[TARGET])

# Encode categorical columns safely
X = pd.get_dummies(X, drop_first=True)

# =====================================================
# SHAP EXPLAINER (SAFE VERSION)
# =====================================================

st.subheader("📊 SHAP Model Explanation")

try:
    explainer = shap.TreeExplainer(model)
except Exception:
    st.warning("TreeExplainer failed → switching to generic SHAP Explainer")
    explainer = shap.Explainer(model)

# Sample data (fast performance)
sample_size = min(300, len(X))
X_sample = X.sample(sample_size, random_state=42)

# SHAP values
shap_values = explainer(X_sample)

# =====================================================
# GLOBAL FEATURE IMPORTANCE
# =====================================================

st.subheader("📌 Feature Importance (Global)")

fig, ax = plt.subplots()

shap.summary_plot(
    shap_values,
    X_sample,
    plot_type="bar",
    show=False
)

st.pyplot(fig)

# =====================================================
# SHAP SUMMARY PLOT
# =====================================================

st.subheader("📈 SHAP Summary Plot")

fig2, ax2 = plt.subplots()

shap.summary_plot(
    shap_values,
    X_sample,
    show=False
)

st.pyplot(fig2)

# =====================================================
# INDIVIDUAL PREDICTION EXPLANATION
# =====================================================

st.subheader("🎯 Individual Prediction Explanation")

selected_index = st.selectbox(
    "Select Record",
    X_sample.index
)

row = X.loc[[selected_index]]

st.write("Selected Input Data")
st.dataframe(row)

# Prediction
prediction = model.predict(row)[0]

st.metric("Prediction", "Failure" if prediction == 1 else "Healthy")

# SHAP for single row
single_shap = explainer(row)

# =====================================================
# WATERFALL PLOT (SAFE)
# =====================================================

st.subheader("🌊 SHAP Waterfall Explanation")

try:
    fig3 = plt.figure()

    shap.plots.waterfall(
        single_shap[0],
        max_display=10,
        show=False
    )

    st.pyplot(fig3)

except Exception:
    st.warning("Waterfall plot not supported for this model.")

# =====================================================
# TOP FEATURES TABLE
# =====================================================

st.subheader("🏆 Top Influencing Features")

importance = pd.DataFrame({
    "Feature": X_sample.columns,
    "Impact": np.abs(shap_values.values).mean(axis=0)
})

importance = importance.sort_values(by="Impact", ascending=False)

st.dataframe(importance)

# =====================================================
# INSIGHTS
# =====================================================

st.subheader("💡 AI Insights")

top_feature = importance.iloc[0]["Feature"]

st.info(f"""
Most influential factor: **{top_feature}**

This feature has the highest impact on machine failure prediction.
""")

# =====================================================
# DOWNLOAD REPORT
# =====================================================

csv = importance.to_csv(index=False)

st.download_button(
    label="📥 Download SHAP Report",
    data=csv,
    file_name="shap_report.csv",
    mime="text/csv"
)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.caption("🔍 AI ESG Predictive Maintenance | SHAP Explainability Module")
