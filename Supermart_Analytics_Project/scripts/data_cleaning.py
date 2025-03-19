import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ✅ 1. Load the dataset
data = pd.read_csv('data/Supermart_Grocery_Sales.csv')

# ✅ 2. Standardize Column Names (Remove Spaces & Special Characters)
data.columns = data.columns.str.strip().str.replace(' ', '_').str.replace(',', '')

# ✅ 3. Convert 'Order_Date' to a Standard Format (Handles Different Date Formats)
data['Order_Date'] = pd.to_datetime(data['Order_Date'], errors='coerce', dayfirst=True)

# ✅ 4. Drop rows where 'Order_Date' is NaN (to avoid conversion errors)
data.dropna(subset=['Order_Date'], inplace=True)

# ✅ 5. Extract Full Month Name & Year
data['Month'] = data['Order_Date'].dt.strftime('%B')  # Converts numbers to full month names
data['Order_Year'] = data['Order_Date'].dt.year.astype('Int64')  # Ensures proper integer conversion

# 🔍 Debugging: Check if Month is extracted correctly
print("✅ Checking Month Column Before Saving:")
print(data[['Order_Date', 'Month']].head())

# ✅ 6. Handle Missing Values in Critical Columns
data.dropna(subset=['Order_ID', 'Customer_Name', 'Sales'], inplace=True)

# ✅ 7. Encode Categorical Columns
categorical_cols = ['Category', 'Sub_Category', 'City', 'Region', 'State']
le = LabelEncoder()
for col in categorical_cols:
    data[col] = le.fit_transform(data[col])

# ✅ 8. Ensure 'Month' stays as a string before saving
data['Month'] = data['Month'].astype(str)

# ✅ 9. Save Cleaned Data
data.to_csv('data/cleaned_supermart_data.csv', index=False)

# ✅ 10. Print Debug Info to Verify Fixes
print("✅ Data Cleaning Completed Successfully!")
print("🔍 Checking Month Column After Fix:")
print(data[['Order_Date', 'Month', 'Order_Year']].head())
