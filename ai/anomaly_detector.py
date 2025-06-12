
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(metrics_csv):
    df = pd.read_csv(metrics_csv)
    clf = IsolationForest(contamination=0.2, random_state=42)
    df["anomaly"] = clf.fit_predict(df[["execution_time", "num_assertions"]])
    return df[df["anomaly"] == -1]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python anomaly_detector.py <metrics.csv>")
        sys.exit(1)
    result = detect_anomalies(sys.argv[1])
    print(result)
