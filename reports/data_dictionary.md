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