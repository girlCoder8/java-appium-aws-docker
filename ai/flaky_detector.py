
import pandas as pd
import numpy as np

def detect_flaky_tests(log_csv):
    df = pd.read_csv(log_csv)
    grouped = df.groupby("test_name")["status"].apply(lambda x: x.value_counts(normalize=True))
    flaky = grouped.loc[grouped.index.get_level_values(1) == "fail"].reset_index()
    flaky.columns = ["test_name", "status", "fail_rate"]
    return flaky[flaky["fail_rate"] > 0.3]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python flaky_detector.py <log.csv>")
        sys.exit(1)
    result = detect_flaky_tests(sys.argv[1])
    print(result)
