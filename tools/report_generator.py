import pandas as pd

def generate_report(file):
    df = pd.read_csv(file)

    report = df.describe()

    report.to_csv("data/report.csv")

    print("Report generated -> data/report.csv")
    print(report.to_string())