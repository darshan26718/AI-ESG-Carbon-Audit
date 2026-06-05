@st.cache_resource
def load_model():
    import joblib
    import os

    model_path = "models/esg_scoring_model.pkl"
    scaler_path = "models/esg_scaler.pkl"

    if not os.path.exists(model_path):
        st.error("ESG model missing")
        st.stop()

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    return model, scaler
