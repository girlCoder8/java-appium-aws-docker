
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Test Automation Dashboard", layout="wide")

st.title("📊 AI-Enhanced Test Automation Dashboard")

# Upload and display metadata
st.header("1. Test Prioritization")
metadata_file = st.file_uploader("Upload metadata.csv", type=["csv"])
if metadata_file:
    df = pd.read_csv(metadata_file)
    model = joblib.load("../ai/model.pkl")
    features = df[["execution_time", "last_run_status", "num_assertions", "file_changes"]]
    df["priority_score"] = model.predict_proba(features)[:, 1]
    st.dataframe(df.sort_values(by="priority_score", ascending=False))

# Flaky test analysis
st.header("2. Flaky Test Detection")
log_file = st.file_uploader("Upload logs.csv", type=["csv"])
if log_file:
    log_df = pd.read_csv(log_file)
    flaky_df = log_df.groupby("test_name")["status"].value_counts(normalize=True).unstack().fillna(0)
    flaky_df["flaky_score"] = flaky_df.get("fail", 0)
    flaky_df = flaky_df[flaky_df["flaky_score"] > 0.3]
    st.dataframe(flaky_df)

# Anomaly detection
st.header("3. Anomaly Detection")
metrics_file = st.file_uploader("Upload metrics.csv", type=["csv"])
if metrics_file:
    from sklearn.ensemble import IsolationForest
    met_df = pd.read_csv(metrics_file)
    model = IsolationForest(contamination=0.2, random_state=42)
    met_df["anomaly"] = model.fit_predict(met_df[["execution_time", "num_assertions"]])
    st.dataframe(met_df[met_df["anomaly"] == -1])
