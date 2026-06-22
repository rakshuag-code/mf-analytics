import pandas as pd
import os

DATA_PATH = "data/raw"

files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

if not files:
    print("No CSV files found in data/raw/")
else:
    for file in files:
        print(f"\n===== {file} =====")

        df = pd.read_csv(os.path.join(DATA_PATH, file))

        # Convert date column
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

        # Sort by date
        df = df.sort_values(by='date')

        print("Shape:", df.shape)
        print("\nDtypes:\n", df.dtypes)
        print("\nHead:\n", df.head())

        print("\nMissing values:\n", df.isnull().sum())
        print("\nDuplicate rows:", df.duplicated().sum())

        print("-" * 50)