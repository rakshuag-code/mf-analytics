import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav.columns = nav.columns.str.lower()

nav['date'] = pd.to_datetime(nav['date'], errors='coerce')

nav = nav.sort_values(by=['amfi_code', 'date'])

nav = nav.drop_duplicates()

nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()

nav = nav[nav['nav'] > 0]

nav.to_csv("data/processed/nav_cleaned.csv", index=False)

print("nav_cleaned.csv created successfully!")

# =============================
# CLEAN INVESTOR TRANSACTIONS
# =============================

tx = pd.read_csv("data/raw/08_investor_transactions.csv")

tx.columns = tx.columns.str.lower()

# Check columns first (important)
print("Transaction columns:", tx.columns)

# Convert date (adjust column name if needed)
if 'date' in tx.columns:
    tx['date'] = pd.to_datetime(tx['date'], errors='coerce')
elif 'transaction_date' in tx.columns:
    tx['transaction_date'] = pd.to_datetime(tx['transaction_date'], errors='coerce')

# Standardize transaction type
if 'transaction_type' in tx.columns:
    tx['transaction_type'] = tx['transaction_type'].str.upper()

# Keep valid amounts
if 'amount' in tx.columns:
    tx = tx[tx['amount'] > 0]

# Save cleaned file
tx.to_csv("data/processed/transactions_cleaned.csv", index=False)

print("transactions_cleaned.csv created successfully!")

# =============================
# CLEAN SCHEME PERFORMANCE
# =============================

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

perf.columns = perf.columns.str.lower()

# Convert return columns to numeric
return_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct',
    'benchmark_3yr_pct',
    'alpha',
    'beta',
    'sharpe_ratio',
    'sortino_ratio',
    'std_dev_ann_pct',
    'max_drawdown_pct'
]

for col in return_cols:
    perf[col] = pd.to_numeric(perf[col], errors='coerce')

# Validate expense ratio (0.1% to 2.5%)
perf = perf[
    (perf['expense_ratio_pct'] >= 0.1) &
    (perf['expense_ratio_pct'] <= 2.5)
]

# Remove duplicates
perf = perf.drop_duplicates()

# Save cleaned file
perf.to_csv("data/processed/performance_cleaned.csv", index=False)

print("performance_cleaned.csv created successfully!")

