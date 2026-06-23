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

        # Only apply date logic if 'date' column exists
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
            df = df.sort_values(by='date')

        print("Shape:", df.shape)
        print("\nDtypes:\n", df.dtypes)
        print("\nHead:\n", df.head())

        print("\nMissing values:\n", df.isnull().sum())
        print("\nDuplicate rows:", df.duplicated().sum())

        print("-" * 50)


# ===== FUND MASTER ANALYSIS =====
print("\n===== FUND MASTER ANALYSIS =====")

fm = pd.read_csv("data/raw/fund_master.csv")

print("Fund Houses:", fm['fund_house'].unique())
print("Categories:", fm['category'].unique())
print("Sub Categories:", fm['sub_category'].unique())
print("Risk Grades:", fm['risk_grade'].unique())


# ===== AMFI VALIDATION =====
print("\n===== AMFI CODE VALIDATION =====")

fm_codes = set(fm['scheme_code'])

api_codes = {125497,119551,120503,118632,119092,120841}

missing = fm_codes - api_codes

print("Missing Codes:", missing)

print("\n===== REAL AMFI CODE VALIDATION =====")

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Clean column names (important)
fund_master.columns = fund_master.columns.str.lower()
nav_history.columns = nav_history.columns.str.lower()

# Extract scheme codes
fm_codes = set(fund_master['scheme_code'].astype(str))
nav_codes = set(nav_history['scheme_code'].astype(str))

# Validation
missing_in_nav = fm_codes - nav_codes
missing_in_master = nav_codes - fm_codes

print("Codes in fund_master but NOT in nav_history:", missing_in_nav)
print("Codes in nav_history but NOT in fund_master:", missing_in_master)