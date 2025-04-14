
import pandas as pd

# Load the dataset (replace with your actual file path)
data = pd.read_csv('/Users/srushtikochare/Downloads/AB_NYC_2019.csv')

# Display the first few rows of the dataset to understand its structure
print("Original Data:")
print(data.head())

# Check for missing values in the dataset
print("\nMissing Values:")
print(data.isnull().sum())

# Fill missing values for numerical columns with the mean
numeric_cols = data.select_dtypes(include=['number']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# For non-numeric columns, fill missing values with the mode (most frequent value)
non_numeric_cols = data.select_dtypes(exclude=['number']).columns
for col in non_numeric_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Check for duplicate rows in the dataset
duplicates = data.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

# Remove duplicate rows from the dataset
data.drop_duplicates(inplace=True)

# Display the cleaned dataset
print("\nCleaned Data:")
print(data.head())

# Save the cleaned dataset to a new CSV file
data.to_csv('cleaned_data.csv', index=False)
 