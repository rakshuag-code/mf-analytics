import requests
import pandas as pd
import os

# Ensure folder exists
os.makedirs("data/raw", exist_ok=True)

scheme_codes = {
    "HDFC_Top_100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for name, code in scheme_codes.items():
    print(f"\nFetching {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)
        data = response.json()

        df = pd.DataFrame(data['data'])

        file_path = f"data/raw/{name.lower()}_nav.csv"
        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path}")

    except Exception as e:
        print(f"Error fetching {name}: {e}")