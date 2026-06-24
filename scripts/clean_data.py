import pandas as pd

# Load NAV History
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort data
nav = nav.sort_values(["amfi_code", "date"])

# Fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
nav = nav.drop_duplicates()

# Keep only valid NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("NAV History cleaned successfully!")