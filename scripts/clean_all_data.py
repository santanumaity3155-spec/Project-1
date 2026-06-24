import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

# -------------------
# 01 FUND MASTER
# -------------------
fund = pd.read_csv(f"{RAW}/01_fund_master.csv")

fund = fund.drop_duplicates()

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

fund.to_csv(
    f"{PROCESSED}/clean_fund_master.csv",
    index=False
)

print("✓ Fund Master cleaned")

# -------------------
# 02 NAV HISTORY
# -------------------
nav = pd.read_csv(f"{RAW}/02_nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    f"{PROCESSED}/clean_nav_history.csv",
    index=False
)

print("✓ NAV History cleaned")

# -------------------
# 03 AUM
# -------------------
aum = pd.read_csv(
    f"{RAW}/03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum = aum.drop_duplicates()

aum.to_csv(
    f"{PROCESSED}/clean_aum.csv",
    index=False
)

print("✓ AUM cleaned")

# -------------------
# 04 SIP INFLOWS
# -------------------
sip = pd.read_csv(
    f"{RAW}/04_monthly_sip_inflows.csv"
)

sip["month"] = pd.to_datetime(
    sip["month"],
    errors="coerce"
)

sip = sip.drop_duplicates()

sip.to_csv(
    f"{PROCESSED}/clean_sip.csv",
    index=False
)

print("✓ SIP cleaned")

# -------------------
# 05 CATEGORY INFLOWS
# -------------------
cat = pd.read_csv(
    f"{RAW}/05_category_inflows.csv"
)

cat["month"] = pd.to_datetime(
    cat["month"],
    errors="coerce"
)

cat = cat.drop_duplicates()

cat.to_csv(
    f"{PROCESSED}/clean_category_inflows.csv",
    index=False
)

print("✓ Category cleaned")

# -------------------
# 06 FOLIO COUNT
# -------------------
folio = pd.read_csv(
    f"{RAW}/06_industry_folio_count.csv"
)

folio["month"] = pd.to_datetime(
    folio["month"],
    errors="coerce"
)

folio = folio.drop_duplicates()

folio.to_csv(
    f"{PROCESSED}/clean_folio_count.csv",
    index=False
)

print("✓ Folio cleaned")

# -------------------
# 07 PERFORMANCE
# -------------------
perf = pd.read_csv(
    f"{RAW}/07_scheme_performance.csv"
)

perf = perf.drop_duplicates()

perf.to_csv(
    f"{PROCESSED}/clean_performance.csv",
    index=False
)

print("✓ Performance cleaned")

# -------------------
# 08 TRANSACTIONS
# -------------------
txn = pd.read_csv(
    f"{RAW}/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn = txn[txn["amount_inr"] > 0]

txn = txn.drop_duplicates()

txn.to_csv(
    f"{PROCESSED}/clean_transactions.csv",
    index=False
)

print("✓ Transactions cleaned")

# -------------------
# 09 HOLDINGS
# -------------------
hold = pd.read_csv(
    f"{RAW}/09_portfolio_holdings.csv"
)

hold["portfolio_date"] = pd.to_datetime(
    hold["portfolio_date"],
    errors="coerce"
)

hold = hold.drop_duplicates()

hold.to_csv(
    f"{PROCESSED}/clean_holdings.csv",
    index=False
)

print("✓ Holdings cleaned")

# -------------------
# 10 BENCHMARK
# -------------------
bench = pd.read_csv(
    f"{RAW}/10_benchmark_indices.csv"
)

bench["date"] = pd.to_datetime(
    bench["date"],
    errors="coerce"
)

bench = bench.drop_duplicates()

bench.to_csv(
    f"{PROCESSED}/clean_benchmark.csv",
    index=False
)

print("✓ Benchmark cleaned")

print("\nALL DATASETS CLEANED SUCCESSFULLY")