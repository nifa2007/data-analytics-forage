# Analysis script for Forage Data Analytics simulation
# Author: [Your Name]
# Date: [Today’s Date]

# Import libraries
import pandas as pd

# Load dataset (replace 'data/sample_dataset.csv' with your actual file)
data = pd.read_csv('../data/sample_dataset.csv')

# Quick data overview
print(data.head())
print(data.info())

# Example: Basic analysis
# Calculate summary statistics for numeric columns
print(data.describe())

# Example: Count of unique values in a column
# print(data['ColumnName'].value_counts())
