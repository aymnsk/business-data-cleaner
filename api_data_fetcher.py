"""
API Data Fetcher - Demonstrates bulk API calls with rate limiting.
Similar to Zillow Zestimate automation.
"""
import pandas as pd
import time
import logging
from typing import List

class APIFetcher:
    def __init__(self, api_key: str, rate_limit_delay: float = 0.5):
        self.api_key = api_key
        self.rate_limit_delay = rate_limit_delay
        self.logger = logging.getLogger(__name__)
    
    def fetch_single_record(self, identifier: str):
        """Simulate API call for single record."""
        time.sleep(self.rate_limit_delay)  # Rate limiting
        # In real implementation: requests.get() to actual API
        return {
            "id": identifier,
            "value": f"API_Result_{identifier}",
            "timestamp": pd.Timestamp.now()
        }
    
    def process_csv_bulk(self, input_csv: str, output_csv: str):
        """Process CSV file with multiple API calls."""
        df = pd.read_csv(input_csv)
        results = []
        
        self.logger.info(f"Processing {len(df)} records with rate limiting...")
        
        for idx, row in df.iterrows():
            result = self.fetch_single_record(row['address'])  # Assuming 'address' column
            results.append(result)
            
            if idx % 10 == 0:
                self.logger.info(f"Processed {idx+1}/{len(df)} records")
        
        # Create results DataFrame
        results_df = pd.DataFrame(results)
        
        # Merge with original data
        final_df = pd.concat([df, results_df], axis=1)
        final_df.to_csv(output_csv, index=False)
        
        self.logger.info(f"Saved results to {output_csv}")
        return final_df

# Demo usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    # Create sample CSV
    sample_data = pd.DataFrame({
        'address': [f'Address_{i}' for i in range(1, 11)],
        'city': ['City_A', 'City_B'] * 5
    })
    sample_data.to_csv('sample_addresses.csv', index=False)
    
    # Demo the fetcher
    fetcher = APIFetcher(api_key="demo_key", rate_limit_delay=0.1)
    results = fetcher.process_csv_bulk('sample_addresses.csv', 'enriched_data.csv')
    print(f"Demo complete. Processed {len(results)} records.")
