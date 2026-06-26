# Data Dictionary

## dim_fund
- scheme_code: Unique fund identifier (AMFI)
- fund_name: Name of fund
- fund_house: AMC name

## fact_nav
- date: NAV date
- nav: Net Asset Value

## fact_transactions
- transaction_type: SIP / Lumpsum / Redemption
- amount: Transaction value

## fact_performance
- expense_ratio: Annual expense %

# 📊 Data Dictionary – Mutual Fund Analytics Project

---

## 🟢 1. fact_nav (NAV History)

| Column Name | Data Type | Description |
|------------|----------|------------|
| amfi_code | TEXT | Unique identifier for each mutual fund |
| date | DATE | NAV recorded date |
| nav | FLOAT | Net Asset Value of the fund on that date |

---

## 🔵 2. fact_transactions (Investor Transactions)

| Column Name | Data Type | Description |
|------------|----------|------------|
| amfi_code | TEXT | Mutual fund identifier |
| date | DATE | Transaction date |
| transaction_type | TEXT | Type of transaction (SIP / Lumpsum / Redemption) |
| amount | FLOAT | Transaction amount (must be > 0) |

---

## 🟡 3. fact_performance (Fund Performance Metrics)

| Column Name | Data Type | Description |
|------------|----------|------------|
| amfi_code | TEXT | Mutual fund identifier |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Asset Management Company (AMC) |
| return_1yr_pct | FLOAT | 1-year return (%) |
| return_3yr_pct | FLOAT | 3-year return (%) |
| return_5yr_pct | FLOAT | 5-year return (%) |
| expense_ratio_pct | FLOAT | Annual expense ratio (%) |
| aum_crore | FLOAT | Assets Under Management (in crores) |
| risk_grade | TEXT | Risk classification (Low / Moderate / High) |

---

## 🟣 4. dim_fund (Fund Dimension Table)

| Column Name | Data Type | Description |
|------------|----------|------------|
| amfi_code | TEXT | Primary key, unique fund ID |
| scheme_name | TEXT | Fund name |
| fund_house | TEXT | AMC name |
| category | TEXT | Fund category (Equity, Debt, Hybrid) |
| sub_category | TEXT | Sub classification (Large Cap, Mid Cap, etc.) |
| risk_grade | TEXT | Risk level |

---

## 🟠 5. dim_date (Date Dimension Table)

| Column Name | Data Type | Description |
|------------|----------|------------|
| date | DATE | Primary key |
| year | INTEGER | Year |
| month | INTEGER | Month |
| day | INTEGER | Day |

---

## 🔴 Data Sources

- NAV Data → Historical NAV CSV files
- Transactions Data → Investor transaction dataset
- Performance Data → Scheme performance dataset
- API Source → mfapi.in (for live NAV fetching)

---

## ⚠️ Data Validation Rules

- NAV must be > 0
- Transaction amount must be > 0
- Expense ratio must be between 0.1% and 2.5%
- Dates must be in valid datetime format
- No duplicate records allowed

---

## ✅ Notes

- All datasets were cleaned and standardized before loading into SQLite
- Column names were normalized for consistency (e.g., amount field)
- Database follows a star schema design for analytics