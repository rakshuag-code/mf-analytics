-- DIMENSION TABLES
CREATE TABLE dim_fund (
    scheme_code TEXT PRIMARY KEY,
    fund_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE dim_date (
    date DATE PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

-- FACT TABLES
CREATE TABLE fact_nav (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code TEXT,
    date DATE,
    nav REAL,
    FOREIGN KEY (scheme_code) REFERENCES dim_fund(scheme_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

CREATE TABLE fact_transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code TEXT,
    date DATE,
    transaction_type TEXT,
    amount REAL
);

CREATE TABLE fact_performance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code TEXT,
    expense_ratio REAL
);

CREATE TABLE fact_aum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    aum REAL
);

from sqlalchemy import create_engine

engine = create_engine("sqlite:///mf_analytics.db")

# Load cleaned data
nav.to_sql("fact_nav", engine, if_exists='replace', index=False)
tx.to_sql("fact_transactions", engine, if_exists='replace', index=False)
perf.to_sql("fact_performance", engine, if_exists='replace', index=False)

print("Data loaded into SQLite")