import pandas as pd
import joblib
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

def train_models(input_file):
    """
    Train Random Forest and XGBoost models on the dataset.
    Save the trained models to the 'models/' directory.
    """
    df = pd.read_csv(input_file)

    if 'likesCount' not in df.columns or 'commentsCount' not in df.columns:
        print("Error: Required columns not found in dataset!")
        return

    X = df[['likesCount', 'commentsCount']]
    y = df['text_length']  # Using text_length as a proxy for engagement

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    joblib.dump(rf_model, 'models/random_forest.pkl')

    xgb_model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100)
    xgb_model.fit(X_train, y_train)
    xgb_model.save_model("models/xgboost.json")

    print("✅ Random Forest and XGBoost models saved successfully.")

if __name__ == "__main__":
    os.makedirs('models', exist_ok=True)
    train_models('data/engineered_climate_data.csv')
