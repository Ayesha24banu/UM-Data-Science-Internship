import pandas as pd
import joblib
import xgboost as xgb
from sklearn.metrics import mean_squared_error

def evaluate_models(input_file):
    """
    Load trained models and evaluate them on the test dataset.
    """
    df = pd.read_csv(input_file)

    if 'likesCount' not in df.columns or 'commentsCount' not in df.columns:
        print("Error: Required columns not found in dataset!")
        return

    X_test = df[['likesCount', 'commentsCount']]
    y_test = df['text_length']

    rf_model = joblib.load('models/random_forest.pkl')
    rf_predictions = rf_model.predict(X_test)
    rf_mse = mean_squared_error(y_test, rf_predictions)
    print(f"✅ Random Forest MSE: {rf_mse:.4f}")

    xgb_model = xgb.XGBRegressor()
    xgb_model.load_model('models/xgboost.json')
    xgb_predictions = xgb_model.predict(X_test)
    xgb_mse = mean_squared_error(y_test, xgb_predictions)
    print(f"✅ XGBoost MSE: {xgb_mse:.4f}")

if __name__ == "__main__":
    evaluate_models('data/engineered_climate_data.csv')
