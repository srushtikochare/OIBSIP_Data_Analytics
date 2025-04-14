

## 📌 Steps Performed

### 1. **File Path Check**
- Verifies the existence of the file.
- If not found, exits with an error message.

### 2. **File Preview**
- Displays the first 300 characters of the raw file using `latin1` encoding for inspection.

### 3. **CSV Parsing**
- Attempts to read the file with common delimiters: `,`, `;`, and `\t`.
- Selects the one with a valid structure (more than one column).

### 4. **Basic EDA**
- Shows:
  - First 5 rows
  - DataFrame info
  - Descriptive statistics
  - Count of missing values

### 5. **Data Cleaning**
- Converts `'Sales'` to numeric and fills missing values with the mean.
- Drops duplicates.
- Parses `'Date'` to datetime format and removes invalid dates.

### 6. **Univariate Analysis**
- Histogram and KDE plot of `'Sales'`
- Count plot of `'Product_Category'` (if available)

### 7. **Bivariate Analysis**
- Heatmap of correlation between numeric features.

### 8. **Time-Series Trend**
- Groups sales by month and plots a trend line for `'Sales'`.

### 9. **Save Output**
- Saves the cleaned dataset as `cleaned_retail_sales.csv` in the working directory.

---

## 📦 Output

A cleaned and preprocessed version of the original dataset.

---

## 📊 Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `os`

---

## 💡 Notes

- Handles encoding issues with `latin1` to prevent load errors.
- Designed to be robust to common file format problems like delimiters and missing values.
- Easily customizable for different columns or formats.

