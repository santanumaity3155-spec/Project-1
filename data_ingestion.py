"""
Data Ingestion Module
Handles loading, validating, and processing data from various sources.
"""

import os
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Union
from datetime import datetime


class DataIngestion:
    """Main class for data ingestion operations."""

    def __init__(self, raw_dir: str = "data/raw", processed_dir: str = "data/processed"):
        self.raw_dir = Path(raw_dir)
        self.processed_dir = Path(processed_dir)
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)

    def load_csv(self, file_path: str, **kwargs) -> pd.DataFrame:
        """Load data from a CSV file."""
        try:
            df = pd.read_csv(file_path, **kwargs)
            print(f"Successfully loaded {file_path} with shape {df.shape}")
            return df
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            raise

    def load_excel(self, file_path: str, **kwargs) -> pd.DataFrame:
        """Load data from an Excel file."""
        try:
            df = pd.read_excel(file_path, **kwargs)
            print(f"Successfully loaded {file_path} with shape {df.shape}")
            return df
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            raise

    def load_json(self, file_path: str, **kwargs) -> pd.DataFrame:
        """Load data from a JSON file."""
        try:
            df = pd.read_json(file_path, **kwargs)
            print(f"Successfully loaded {file_path} with shape {df.shape}")
            return df
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            raise

    def save_raw(self, df: pd.DataFrame, filename: str) -> str:
        """Save raw data to the raw directory."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = self.raw_dir / f"{filename}_{timestamp}.csv"
        df.to_csv(filepath, index=False)
        print(f"Raw data saved to {filepath}")
        return str(filepath)

    def save_processed(self, df: pd.DataFrame, filename: str) -> str:
        """Save processed data to the processed directory."""
        filepath = self.processed_dir / f"{filename}.csv"
        df.to_csv(filepath, index=False)
        print(f"Processed data saved to {filepath}")
        return str(filepath)

    def validate_data(self, df: pd.DataFrame, required_columns: list) -> bool:
        """Validate that required columns exist in the dataframe."""
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            print(f"Missing required columns: {missing_cols}")
            return False
        print("Data validation passed")
        return True

    def get_data_info(self, df: pd.DataFrame) -> dict:
        """Get basic information about the dataframe."""
        info = {
            "shape": df.shape,
            "columns": list(df.columns),
            "dtypes": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "duplicate_rows": df.duplicated().sum()
        }
        return info


def main():
    """Main execution function."""
    ingestion = DataIngestion()

    # Example usage
    print("Data Ingestion Module Ready")
    print(f"Raw data directory: {ingestion.raw_dir}")
    print(f"Processed data directory: {ingestion.processed_dir}")


if __name__ == "__main__":
    main()