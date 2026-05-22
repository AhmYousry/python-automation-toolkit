import pandas as pd

def clean_csv(file):
    df = pd.read_csv(file)
    before = len(df)

    df = df.dropna()

    df.to_csv("data/clean_data.csv", index=False)

    print(f"CSV cleaned: removed {before - len(df)} rows with missing values, {len(df)} rows remaining")