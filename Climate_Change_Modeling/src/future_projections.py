import pandas as pd
import joblib
import xgboost as xgb

def future_predictions(input_file):
    """
    Predict future engagement scores using trained models.
    """
    df = pd.read_csv(input_file)

    # Load trained models
    rf_model = joblib.load('models/random_forest.pkl')
    xgb_model = xgb.XGBRegressor()
    xgb_model.load_model('models/xgboost.json')

    X_future = df[['likesCount', 'commentsCount']]

    # Predictions
    rf_preds = rf_model.predict(X_future)
    xgb_preds = xgb_model.predict(X_future)

    # Save predictions
    df['RF_Predicted_Engagement'] = rf_preds
    df['XGB_Predicted_Engagement'] = xgb_preds

    df.to_csv("data/future_predictions.csv", index=False)

    print("✅ Future Predictions saved!")
    print(df[['date', 'RF_Predicted_Engagement', 'XGB_Predicted_Engagement']].head())

if __name__ == "__main__":
    future_predictions('data/engineered_climate_data.csv')
