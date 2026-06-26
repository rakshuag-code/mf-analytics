from sqlalchemy import create_engine
import pandas as pd

# -------------------
# CREATE DATABASE
# -------------------
engine = create_engine("sqlite:///mf_analytics.db")

# -------------------
# LOAD NAV DATA
# -------------------
nav = pd.read_csv("data/processed/nav_cleaned.csv")
nav.to_sql("fact_nav", engine, if_exists='replace', index=False)
print("NAV data loaded!")

# -------------------
# LOAD TRANSACTIONS
# -------------------
tx = pd.read_csv("data/processed/transactions_cleaned.csv")

# 🔧 STANDARDIZE COLUMN NAME (VERY IMPORTANT)
# Find amount column automatically
for col in tx.columns:
    if "amt" in col or "amount" in col or "value" in col:
        tx.rename(columns={col: "amount"}, inplace=True)

tx.to_sql("fact_transactions", engine, if_exists='replace', index=False)
print("Transactions data loaded!")

# Show columns to confirm
print("\nFACT_TRANSACTIONS COLUMNS:")
print(tx.columns)

# -------------------
# LOAD PERFORMANCE
# -------------------
perf = pd.read_csv("data/processed/performance_cleaned.csv")
perf.to_sql("fact_performance", engine, if_exists='replace', index=False)
print("Performance data loaded!")

# -------------------
# BASIC SQL QUERY
# -------------------
query = """
SELECT transaction_type, COUNT(*) as total_transactions
FROM fact_transactions
GROUP BY transaction_type
"""
print("\nTransaction Summary:")
print(pd.read_sql(query, engine))

# -------------------
# FINAL ANALYTICAL QUERIES
# -------------------

# 1 Top 5 funds by AUM
q1 = """
SELECT fund_house, SUM(aum_crore) as total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5
"""
print("\nTop 5 Funds by AUM:\n", pd.read_sql(q1, engine))

# 2 Average NAV per month
q2 = """
SELECT strftime('%Y-%m', date) as month, AVG(nav) as avg_nav
FROM fact_nav
GROUP BY month
"""
print("\nAverage NAV per Month:\n", pd.read_sql(q2, engine))

# 3 Transaction count by type
q3 = """
SELECT transaction_type, COUNT(*) as total
FROM fact_transactions
GROUP BY transaction_type
"""
print("\nTransaction Types:\n", pd.read_sql(q3, engine))

# 4 Expense ratio < 1%
q4 = """
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
"""
print("\nLow Expense Funds:\n", pd.read_sql(q4, engine))

# 5 Total transaction amount (NOW FIXED)
q5 = """
SELECT SUM(amount) as total_amount
FROM fact_transactions
"""
print("\nTotal Transaction Amount:\n", pd.read_sql(q5, engine))