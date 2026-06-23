# Project Name

A comprehensive data pipeline project for fetching, processing, and analyzing mutual fund NAV (Net Asset Value) data.

## Project Structure

```
project/
│
├── data/
│   ├── raw/              # Raw data files (CSV, JSON, Excel)
│   └── processed/        # Cleaned and processed data
│
├── notebooks/            # Jupyter notebooks for analysis and exploration
├── sql/                  # SQL scripts for database operations
├── dashboard/            # Dashboard application files
├── reports/              # Generated reports and visualizations
├── scripts/              # Utility scripts and automation
│
├── requirements.txt      # Python dependencies
├── data_ingestion.py     # Data loading and validation module
├── live_nav_fetch.py     # Live NAV data fetching module
└── README.md            # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "Project - 1"
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Data Ingestion

The `data_ingestion.py` module provides utilities for loading, validating, and processing data:

```python
from data_ingestion import DataIngestion

# Initialize the ingestion module
ingestion = DataIngestion()

# Load data from various sources
df_csv = ingestion.load_csv("path/to/file.csv")
df_excel = ingestion.load_excel("path/to/file.xlsx")
df_json = ingestion.load_json("path/to/file.json")

# Save processed data
ingestion.save_processed(df_csv, "processed_data")

# Validate data
is_valid = ingestion.validate_data(df_csv, required_columns=["col1", "col2"])
```

### Live NAV Fetch

The `live_nav_fetch.py` module handles fetching live NAV data from mutual fund APIs:

```python
from live_nav_fetch import LiveNAVFetch

# Initialize the fetcher
fetcher = LiveNAVFetch()

# Fetch NAV for a single scheme
nav_data = fetcher.get_latest_nav(
    scheme_code="119550",
    api_url="https://api.mfapi.in/mf/{scheme_code}"
)

# Fetch multiple schemes with retry logic
scheme_codes = ["119550", "119551", "119552"]
nav_df = fetcher.batch_fetch_with_retry(scheme_codes, api_url)

# Save to cache
fetcher.save_to_cache(nav_df, "nav_data")
```

## Module Details

### data_ingestion.py

**Key Features:**
- Load data from CSV, Excel, and JSON formats
- Automatic directory creation for raw and processed data
- Data validation for required columns
- Data quality reporting (missing values, duplicates, dtypes)
- Timestamp-based file naming for raw data

**Main Classes:**
- `DataIngestion`: Core class for all data ingestion operations

### live_nav_fetch.py

**Key Features:**
- Fetch NAV data from mutual fund APIs
- Rate limiting and retry logic
- Caching mechanism for fetched data
- Context manager support for resource management
- Batch fetching with error handling

**Main Classes:**
- `LiveNAVFetch`: Core class for NAV data fetching

## Directory Usage

- **data/raw/**: Store original, unmodified data files
- **data/processed/**: Store cleaned and transformed data ready for analysis
- **notebooks/**: Jupyter notebooks for exploratory data analysis
- **sql/**: SQL queries for database operations and data transformations
- **dashboard/**: Streamlit or other dashboard application code
- **reports/**: Generated reports, visualizations, and analysis outputs
- **scripts/**: Utility scripts for automation and maintenance

## Dependencies

See `requirements.txt` for the full list of dependencies. Key packages include:

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **requests**: HTTP library for API calls
- **sqlalchemy**: SQL toolkit and ORM
- **streamlit**: Dashboard framework
- **plotly**: Interactive visualizations
- **matplotlib/seaborn**: Static visualizations
- **scikit-learn**: Machine learning utilities

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please open an issue in the repository.

## Acknowledgments

- Mutual Fund API providers for NAV data
- Open source community for excellent Python libraries