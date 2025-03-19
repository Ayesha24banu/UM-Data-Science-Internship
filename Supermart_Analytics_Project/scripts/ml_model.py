import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ✅ 1. Load Cleaned Data
data = pd.read_csv('data/cleaned_supermart_data.csv')
print("✅ Available Columns in Cleaned Data:", data.columns.tolist())

# ✅ 2. Drop Non-Numeric Columns
features = data.drop(columns=['Order_ID', 'Customer_Name', 'Order_Date', 'Sales'])
target = data['Sales']

# ✅ 3. Encode Categorical Variables (Including 'Month')
categorical_cols = ['Category', 'Sub_Category', 'City', 'Region', 'State', 'Month']
le = LabelEncoder()
for col in categorical_cols:
    features[col] = le.fit_transform(features[col])

# ✅ 4. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# ✅ 5. Standardize Numerical Features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ✅ 6. Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ 7. Make Predictions
y_pred = model.predict(X_test)

# ✅ 8. Evaluate Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📉 Mean Squared Error: {mse}")
print(f"📊 R-squared Score: {r2}")
print("✅ Model Training Completed Successfully!")
