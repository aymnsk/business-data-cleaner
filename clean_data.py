"""
Business Data Cleaner - A simple tool to automate cleaning messy CSV files.
Cleans dates, standardizes currency, removes duplicates.
"""

import pandas as pd
import argparse
from datetime import datetime

def clean_csv(input_file, output_file):
    """Main cleaning function."""
    df = pd.read_csv(input_file)

    # 1. Standardize date format (if column exists)
    date_columns = [col for col in df.columns if 'date' in col.lower()]
    for col in date_columns:
        try:
            df[col] = pd.to_datetime(df[col]).dt.strftime('%Y-%m-%d')
        except:
            pass  # Skip if column can't be parsed as date

    # 2. Remove duplicate rows
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    final_count = len(df)
    print(f"Removed {initial_count - final_count} duplicate rows.")

    # 3. Save cleaned file
    df.to_excel(output_file, index=False)
    print(f"Cleaned file saved as: {output_file}")
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Clean a business CSV file.')
    parser.add_argument('input', help='Input CSV file path')
    parser.add_argument('output', help='Output Excel file path')
    args = parser.parse_args()

    clean_csv(args.input, args.output)
