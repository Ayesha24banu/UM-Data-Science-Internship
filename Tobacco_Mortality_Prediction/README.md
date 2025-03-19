# Tobacco Mortality Prediction

## Overview
This project predicts tobacco-related mortality using various factors such as year, metric, tobacco use duration, affordability index, and population percentage. The model is built using machine learning and deployed with Flask.

## Project Structure
```
Tobacco_Mortality_Prediction/
│── data/
│   ├── fatalities.csv (Raw dataset)
│   ├── cleaned_fatalities.csv (Processed dataset)
│── src/
│   ├── data_preprocessing.py (Preprocesses raw data)
│   ├── train_model.py (Trains and saves the prediction model)
│   ├── app.py (Flask app for prediction interface)
│── models/
│   ├── mortality_model.pkl (Trained ML model)
│── templates/
│   ├── index.html (Web interface for input and prediction)
│── requirements.txt (List of dependencies)
│── README.md (Project documentation)
│── .venv/ (Virtual environment)
```

## Installation and Setup
### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/Tobacco_Mortality_Prediction.git
cd Tobacco_Mortality_Prediction
```

### 2. Create a Virtual Environment
```sh
python -m venv .venv
source .venv/bin/activate   # On Mac/Linux
.venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Data Preprocessing
Run the following command to clean the dataset:
```sh
python src/data_preprocessing.py
```
**Expected Output:**
```
Initial dataset shape: (1749, 7)
Final dataset shape: (1729, 10)
Data saved to data/cleaned_fatalities.csv
```

## Model Training
Train the machine learning model with:
```sh
python src/train_model.py
```
**Expected Output:**
```
Model trained and saved successfully!
```

## Running the Flask Application
Start the web interface using:
```sh
python src/app.py
```
Then, open `http://127.0.0.1:5000` in your browser to access the prediction interface.

## Usage
1. Enter the required details:
   - **Year** (e.g., 2024)
   - **Metric** (e.g., 15)
   - **Tobacco Use Duration** (e.g., 11)
   - **Affordability Index** (e.g., 4)
   - **Population Percentage** (e.g., 30)
2. Click **Predict** to get the mortality prediction.

## Screenshorts of Output

![Screenshot 2025-03-08 151440](https://github.com/user-attachments/assets/205966fa-1eb3-4433-844c-f11c60d3754a)

![Screenshot 2025-03-08 151937](https://github.com/user-attachments/assets/409deca9-7bf3-4228-b25a-68c318e271ee)

## Troubleshooting
- **Missing Features in Data:** Ensure `cleaned_fatalities.csv` contains all required columns.
- **Model Training Error:** Ensure preprocessing was completed before training.
- **Flask App Not Found:** Verify that `app.py` exists in the  directory.
  
## Author Details:
Name: Ayesha Banu

Education: MSc in Computer Science (2024), Gold Medalist

Linkedin: https://www.linkedin.com/in/ayesha-banu-cs

## License
This project is licensed under the MIT License.

