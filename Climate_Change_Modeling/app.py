import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed_climate_data.csv")
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Load Models
rf_model = joblib.load("models/random_forest.pkl")

xgb_model = xgb.XGBRegressor()
xgb_model.load_model("models/xgboost.json")

# Sidebar Navigation
st.sidebar.title("Navigation")
options = ["Home", "EDA", "Model Evaluation", "Future Projections"]
choice = st.sidebar.radio("Go to", options)

# Home Page
if choice == "Home":
    st.title("Climate Change Analysis Dashboard")
    st.write("Welcome to the Climate Change Analysis Web App.")
    st.write("Explore climate change insights, model evaluations, and future projections.")

# EDA Page
elif choice == "EDA":
    st.title("Exploratory Data Analysis")

    st.subheader("Comments Trend Over Time")
    plt.figure(figsize=(12, 5))
    df.groupby(df['date'].dt.date)['commentsCount'].sum().plot(kind='line', color='red')
    plt.xlabel("Date")
    plt.ylabel("Total Comments Per Day")
    plt.xticks(rotation=45)
    st.pyplot(plt)

    st.subheader("Likes Distribution")
    plt.figure(figsize=(10, 5))
    sns.histplot(df['likesCount'], bins=30, kde=True, color='blue')
    plt.xlabel("Number of Likes")
    plt.ylabel("Frequency")
    st.pyplot(plt)

# Model Evaluation Page
elif choice == "Model Evaluation":
    st.title("Model Evaluation")

    # Load engineered data
    df_eval = pd.read_csv("data/engineered_climate_data.csv")

    # Prepare test data
    X_test = df_eval[['likesCount', 'commentsCount']]
    y_test = df_eval['text_length']

    # Predictions
    rf_preds = rf_model.predict(X_test)
    xgb_preds = xgb_model.predict(X_test)

    # Compute MSE
    from sklearn.metrics import mean_squared_error
    rf_mse = mean_squared_error(y_test, rf_preds)
    xgb_mse = mean_squared_error(y_test, xgb_preds)

    st.write(f"✅ Random Forest MSE: {rf_mse:.4f}")
    st.write(f"✅ XGBoost MSE: {xgb_mse:.4f}")

# Future Projections Page
elif choice == "Future Projections":
    st.title("Future Projections")

    # Load future climate data
    df_future = pd.read_csv("data/future_predictions.csv")

    # Display predictions
    st.write("✅ Future Predictions:")
    st.write(df_future[['date', 'RF_Predicted_Engagement', 'XGB_Predicted_Engagement']].head())

