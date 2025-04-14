import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ========== Step 1: File Path ==========
file_path = '/Users/srushtikochare/Downloads/Warehouse_and_Retail_Sales.csv'

# Check if file exists
if not os.path.exists(file_path):
    print(f"❌ File not found: {file_path}")
    exit()

# ========== Step 2: Preview Raw File ==========
with open(file_path, 'r', encoding='latin1') as file:
    preview = file.read(300)
    print("\n📄 File Content Preview:")
    print(preview)

# ========== Step 3: Try Reading with Common Delimiters ==========
separators = [',', ';', '\t']
df = None

for sep in separators:
    try:
        temp_df = pd.read_csv(file_path, sep=sep, encoding='latin1')
        if temp_df.shape[1] > 1:  # More than one column
            df = temp_df
            print(f"\n✅ Successfully loaded with separator: '{sep}'")
            break
    except Exception as e:
        print(f"❌ Failed with separator '{sep}': {e}")

if df is None:
    print("❌ Could not load the CSV with any known separator.")
    exit()

# ========== Step 4: Show Basic Info ==========
print("\n🔍 First 5 Rows:")
print(df.head())

print("\n🧾 Info:")
print(df.info())

print("\n📈 Stats Summary:")
print(df.describe(include='all'))

print("\n❓ Missing Values:")
print(df.isnull().sum())

# ========== Step 5: Data Cleaning ==========
if 'Sales' in df.columns:
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df['Sales'].fillna(df['Sales'].mean(), inplace=True)

df.drop_duplicates(inplace=True)

if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)

# ========== Step 6: Univariate Analysis ==========
if 'Sales' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sales'], bins=30, kde=True)
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

if 'Product_Category' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Product_Category')
    plt.title('Product Category Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ========== Step 7: Bivariate Analysis ==========
numeric_cols = df.select_dtypes(include='number')

if not numeric_cols.empty:
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()
else:
    print("\n⚠️ No numeric columns found for correlation heatmap.")

# ========== Step 8: Time-Based Trend ==========
if 'Date' in df.columns and 'Sales' in df.columns:
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_sales, x='Month', y='Sales')
    plt.title('Monthly Sales Trend')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ========== Step 9: Save Cleaned Data ==========
output_file = 'cleaned_retail_sales.csv'
df.to_csv(output_file, index=False)
print(f"\n✅ Cleaned data saved to: {output_file}")
