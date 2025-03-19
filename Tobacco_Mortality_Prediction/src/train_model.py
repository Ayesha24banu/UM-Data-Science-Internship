import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model():
    try:
        # Load preprocessed data
        df = pd.read_csv("data/cleaned_fatalities.csv")

        # Define features and target
        features = ["Year", "Metric", "Tobacco Use Duration", "Affordability Index", "Population Percentage"]
        target = "Value"

        if not all(col in df.columns for col in features):
            print("Error: Missing required features in dataset")
            return

        # Drop NaN values in selected features
        df.dropna(subset=features + [target], inplace=True)

        # Prepare X and y
        X = df[features]
        y = df[target]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Scale the data
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Train the model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)

        # Save the model
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/mortality_model.pkl")
        joblib.dump(scaler, "models/scaler.pkl")
        print("Model trained and saved successfully!")

    except Exception as e:
        print(f"Error during training: {e}")

if __name__ == "__main__":
    train_model()
