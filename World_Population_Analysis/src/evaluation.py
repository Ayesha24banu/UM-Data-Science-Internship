import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def evaluate_model():
    df = pd.read_csv('data/feature_engineered_population.csv')
    features = ['1970 Population', '1980 Population', '1990 Population', '2000 Population', '2010 Population', '2020 Population']
    features = [f for f in features if f in df.columns]
    if not features:
        raise ValueError("No valid features found in dataset.")
    X = df[features].values
    y = df['2022 Population'].values if '2022 Population' in df.columns else None
    if y is None:
        raise ValueError("Target variable '2022 Population' not found in dataset.")
    model = joblib.load('models/population_model.pkl')
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    y_pred = model.predict(X_scaled)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")

if __name__ == "__main__":
    evaluate_model()
