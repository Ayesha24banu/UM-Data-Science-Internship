# Climate Change Modeling and Prediction

## Description
This project analyzes climate change-related data collected from NASA's Facebook page. It performs data preprocessing, exploratory data analysis (EDA), feature engineering, and trains machine learning models (Random Forest and XGBoost) to predict engagement metrics. The results are showcased in an interactive Streamlit dashboard.

## Features
- **Data Preprocessing:** Clean raw data and convert date columns.
- **Exploratory Data Analysis (EDA):** Visualize trends in likes and comments.
- **Feature Engineering:** Create new features such as text length and engagement (derived as the sum of likes and comments).
- **Model Training:** Train Random Forest and XGBoost models.
- **Model Evaluation:** Evaluate models using Mean Squared Error (MSE).
- **Future Projections:** Predict future engagement using trained models.
- **Interactive Web Dashboard:** Display all outputs and visualizations using Streamlit.

## File Structure
Climate_Change_Modeling/ ├── data/ │ ├── climate_nasa.csv # Raw dataset │ ├── processed_climate_data.csv # Data after preprocessing │ ├── engineered_climate_data.csv # Data after feature engineering │ ├── future_predictions.csv # Future projection results ├── models/ │ ├── random_forest.pkl # Trained Random Forest model │ ├── xgboost.json # Trained XGBoost model ├── src/ │ ├── data_preprocessing.py # Preprocess raw data │ ├── eda.py # Exploratory Data Analysis │ ├── feature_engineering.py # Feature Engineering │ ├── ml_models.py # Train ML models │ ├── model_evaluation.py # Evaluate trained models │ ├── future_projections.py # Predict future engagement ├── app.py # Streamlit Web App ├── index.html # Basic HTML landing page ├── README.md # Project documentation (this file) └── requirements.txt # List of dependencies

## Installation & Setup

### Prerequisites
- Python 3.x installed
- [Streamlit](https://streamlit.io/) installed
- Other Python dependencies listed in `requirements.txt`

### Setup Steps

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/Climate_Change_Modeling.git
   cd Climate_Change_Modeling
2. **Create and Activate Virtual Environment:**
   python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
3. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
4. **Run the Data Pipeline: Execute the scripts in the following order:**
    ```sh
    python src/data_preprocessing.py
    python src/feature_engineering.py
    python src/ml_models.py
    python src/model_evaluation.py
    python src/future_projections.py
5. **Run the Streamlit App:**
    ```sh
    streamlit run app.py
## Usage:

**Data Preprocessing:**
Script: src/data_preprocessing.py
Function: Converts the date, fills missing values, and cleans the dataset.
Output: data/processed_climate_data.csv

**Feature Engineering:**
Script: src/feature_engineering.py
Function: Creates new features like text_length and engagement (calculated as likesCount + commentsCount).
Output: data/engineered_climate_data.csv

**Model Training:**
Script: src/ml_models.py
Function: Trains Random Forest and XGBoost models using likesCount and commentsCount to predict text_length as a proxy for engagement.
Output: Saved models in the models/ directory.

**Model Evaluation:**
Script: src/model_evaluation.py
Function: Loads the engineered dataset and evaluates the trained models using MSE.
Output: MSE scores printed in the console.

**Future Projections:**
Script: src/future_projections.py
Function: Uses the trained models to predict future engagement values based on future data.
Output: data/future_predictions.csv

**Web Dashboard:**
Script: app.py
Function: Interactive Streamlit dashboard to display EDA, model evaluation metrics, and future projections.
How to Run: streamlit run app.py

**Landing Page:**
File: index.html
Function: A basic HTML landing page linking to the Streamlit dashboard.
Screenshots

**Below are some screenshots of the output from the project (please replace the image paths with your actual screenshots):**


**Note:** Ensure these images are placed in the data/ folder (or update the paths accordingly).

## License:
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact:
For any queries, please contact Ayesha at [ayesha24banu@gmail.com].

## Author Details:
Name: Ayesha
Education: MSc in Computer Science (2024), Gold Medalist
Freelancing: Beginner in AI writing services on Fiverr
Current Training: Data Science Course at TEKS Academy, Secunderabad