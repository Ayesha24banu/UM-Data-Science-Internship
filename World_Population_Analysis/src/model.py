import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_model():
    df = pd.read_csv('data/feature_engineered_population.csv')
    features = ['1970 Population', '1980 Population', '1990 Population', '2000 Population', '2010 Population', '2020 Population']
    features = [f for f in features if f in df.columns]
    if not features:
        raise ValueError("No valid features found in dataset.")
    X = df[features].values
    y = df['2022 Population'].values if '2022 Population' in df.columns else None
    if y is None:
        raise ValueError("Target variable '2022 Population' not found in dataset.")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/population_model.pkl')

if __name__ == "__main__":
    train_model()
