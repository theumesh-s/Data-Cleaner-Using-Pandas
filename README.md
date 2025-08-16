
# Data Cleaner

A Python project that automatically cleans messy CSV datasets using Pandas. It handles missing values, removes duplicates, converts data types, and adds derived columns like `Passed` based on scores.

## Features

- Fill missing IDs with `0`  
- Drop rows with missing Names and remove duplicate Names  
- Fill missing Age with mean and convert to integer  
- Fill missing Score with mean and round to 2 decimals  
- Fill missing City with `"Delhi"` and strip extra spaces  
- Add a `Passed` column (`Yes` if Score >= 33, else `No`)  
- Save cleaned data to a new CSV  

## Requirements

- Python 3.x  
- pandas (`pip install pandas`)

## Usage

1. Place your CSV file in the same folder as the script (e.g., `messy.csv`).  
2. Run the script:
```bash
python data_cleaner.py
