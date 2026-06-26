-- =========================
-- DIMENSION TABLE: FUND
-- =========================
CREATE TABLE dim_fund (
    amfi_code TEXT PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_grade TEXT
);

-- =========================
-- DIMENSION TABLE: DATE
-- =========================
CREATE TABLE dim_date (
    date TEXT PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

-- =========================
-- FACT TABLE: NAV
-- =========================
CREATE TABLE fact_nav (
    amfi_code TEXT,
    date TEXT,
    nav REAL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

-- =========================
-- FACT TABLE: TRANSACTIONS
-- =========================
CREATE TABLE fact_transactions (
    amfi_code TEXT,
    date TEXT,
    transaction_type TEXT,
    amount REAL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY (date) REFERENCES dim_date(date)
);

-- =========================
-- FACT TABLE: PERFORMANCE
-- =========================
CREATE TABLE fact_performance (
    amfi_code TEXT,
    scheme_name TEXT,
    fund_house TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    aum_crore REAL,
    PRIMARY KEY (amfi_code),
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- =========================
-- FACT TABLE: AUM
-- =========================
CREATE TABLE fact_aum (
    amfi_code TEXT,
    aum_crore REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- =============================
-- 1. Top 5 Funds by AUM
-- =============================
SELECT fund_house, SUM(aum_crore) AS total_aum
FROM fact_performance
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- =============================
-- 2. Average NAV per Month
-- =============================
SELECT strftime('%Y-%m', date) AS month, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- =============================
-- 3. Transaction Count by Type
-- =============================
SELECT transaction_type, COUNT(*) AS total
FROM fact_transactions
GROUP BY transaction_type;

-- =============================
-- 4. Total Transaction Amount
-- =============================
SELECT SUM(amount) AS total_amount
FROM fact_transactions;

-- =============================
-- 5. Funds with Expense Ratio < 1%
-- =============================
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- =============================
-- 6. SIP YoY Growth (Basic)
-- =============================
SELECT 
    strftime('%Y', date) AS year,
    COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- =============================
-- 7. Transactions by Fund
-- =============================
SELECT amfi_code, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY amfi_code
ORDER BY total_transactions DESC;

-- =============================
-- 8. Average NAV per Fund
-- =============================
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- =============================
-- 9. Top Performing Funds (3-Year Return)
-- =============================
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- =============================
-- 10. High Risk Funds
-- =============================
SELECT scheme_name, risk_grade
FROM fact_performance
WHERE risk_grade = 'High';