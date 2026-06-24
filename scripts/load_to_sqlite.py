import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

files = {
    "dim_fund": "data/processed/clean_fund_master.csv",
    "fact_nav": "data/processed/clean_nav_history.csv",
    "fact_aum": "data/processed/clean_aum.csv",
    "fact_sip": "data/processed/clean_sip.csv",
    "fact_category_inflows": "data/processed/clean_category_inflows.csv",
    "fact_folio": "data/processed/clean_folio_count.csv",
    "fact_performance": "data/processed/clean_performance.csv",
    "fact_transactions": "data/processed/clean_transactions.csv",
    "fact_holdings": "data/processed/clean_holdings.csv",
    "fact_benchmark": "data/processed/clean_benchmark.csv"
}

for table_name, file_path in files.items():
    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✓ Loaded {table_name}")

print("\nDatabase created successfully!")