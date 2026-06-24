-- Top 5 funds by AUM
SELECT fund_house, MAX(aum_crore)
FROM fact_aum
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Transactions by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1
SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top performing funds
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;