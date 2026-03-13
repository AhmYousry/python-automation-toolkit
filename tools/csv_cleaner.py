import pandas as pd

def clean_csv(file):
    df = pd.read_csv(file)

    df = df.dropna()

    df.to_csv("data/clean_data.csv", index=False)

    print("CSV cleaned successfully")