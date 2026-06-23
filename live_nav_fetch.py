"""
Live NAV Fetch Module
Fetches Net Asset Value (NAV) data from various mutual fund APIs and sources.
"""

import requests
import pandas as pd
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import time
from pathlib import Path


class LiveNAVFetch:
    """Main class for fetching live NAV data."""

    def __init__(self, cache_dir: str = "data/raw"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def fetch_from_api(self, url: str, params: Optional[Dict] = None) -> Dict:
        """Fetch data from a given API endpoint."""
        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching from {url}: {e}")
            raise

    def fetch_mf_nav(self, scheme_code: str, api_url: str) -> Optional[Dict]:
        """Fetch NAV for a specific mutual fund scheme."""
        try:
            params = {"scheme_code": scheme_code}
            data = self.fetch_from_api(api_url, params)
            return data
        except Exception as e:
            print(f"Error fetching NAV for scheme {scheme_code}: {e}")
            return None

    def fetch_multiple_schemes(self, scheme_codes: List[str], api_url: str, delay: float = 0.5) -> pd.DataFrame:
        """Fetch NAV data for multiple schemes with rate limiting."""
        results = []
        for code in scheme_codes:
            data = self.fetch_mf_nav(code, api_url)
            if data:
                results.append(data)
            time.sleep(delay)  # Rate limiting

        return pd.DataFrame(results)

    def save_to_cache(self, data: pd.DataFrame, filename: str) -> str:
        """Save fetched data to cache directory."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = self.cache_dir / f"{filename}_{timestamp}.csv"
        data.to_csv(filepath, index=False)
        print(f"Data cached to {filepath}")
        return str(filepath)

    def load_from_cache(self, filepath: str) -> pd.DataFrame:
        """Load data from cache."""
        try:
            df = pd.read_csv(filepath)
            print(f"Loaded cached data from {filepath}")
            return df
        except Exception as e:
            print(f"Error loading cache {filepath}: {e}")
            raise

    def get_latest_nav(self, scheme_code: str, api_url: str) -> Optional[Dict]:
        """Get the latest NAV for a scheme."""
        data = self.fetch_mf_nav(scheme_code, api_url)
        if data and 'nav' in data:
            return {
                'scheme_code': scheme_code,
                'nav': data['nav'],
                'date': data.get('date', datetime.now().strftime("%Y-%m-%d")),
                'fetched_at': datetime.now().isoformat()
            }
        return None

    def batch_fetch_with_retry(self, scheme_codes: List[str], api_url: str, max_retries: int = 3) -> pd.DataFrame:
        """Fetch multiple schemes with retry logic."""
        results = []
        for code in scheme_codes:
            for attempt in range(max_retries):
                try:
                    data = self.fetch_mf_nav(code, api_url)
                    if data:
                        results.append(data)
                        break
                except Exception as e:
                    if attempt == max_retries - 1:
                        print(f"Failed to fetch {code} after {max_retries} attempts")
                    time.sleep(1 * (attempt + 1))

        return pd.DataFrame(results) if results else pd.DataFrame()

    def close(self):
        """Close the session."""
        self.session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


def main():
    """Main execution function."""
    fetcher = LiveNAVFetch()

    # Example usage
    print("Live NAV Fetch Module Ready")
    print(f"Cache directory: {fetcher.cache_dir}")

    # Example API configuration (replace with actual API)
    example_api_url = "https://api.mfapi.in/mf/{scheme_code}"
    print(f"Example API URL format: {example_api_url}")


if __name__ == "__main__":
    main()