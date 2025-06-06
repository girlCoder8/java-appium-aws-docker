
import pandas as pd
import joblib
import sys

def prioritize(test_metadata_csv):
    model = joblib.load("model.pkl")
    data = pd.read_csv(test_metadata_csv)
    features = data[["execution_time", "last_run_status", "num_assertions", "file_changes"]]
    data["priority_score"] = model.predict_proba(features)[:, 1]
    prioritized = data.sort_values(by="priority_score", ascending=False)
    print(prioritized[["test_name", "priority_score"]])
    return prioritized

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prioritizer.py <metadata.csv>")
        sys.exit(1)
    prioritize(sys.argv[1])
