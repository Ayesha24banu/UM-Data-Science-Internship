import argparse
from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.model import train_model
from src.evaluation import evaluate_model
import src.dashboard as dash_app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dashboard", action="store_true", help="Launch dashboard after pipeline execution")
    args = parser.parse_args()

    preprocess_data()
    create_features()
    train_model()
    evaluate_model()

    if args.dashboard:
        dash_app.app.run_server(debug=False)
