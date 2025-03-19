import pandas as pd
import os

def preprocess_data(input_file, output_file):
    """
    Load and preprocess the dataset:
    - Convert 'date' column to datetime format
    - Fill missing values in 'commentsCount' with 0
    - Drop rows with missing 'text' values
    - Save the cleaned data to a new CSV file
    """
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found!")
        return

    df = pd.read_csv(input_file)
    
    # Convert 'date' column to datetime format
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Fill missing values
    df['commentsCount'] = df['commentsCount'].fillna(0)

    df.to_csv(output_file, index=False)
    print("✅ Data Preprocessing Complete! Sample Data:")
    print(df.head())

if __name__ == "__main__":
    preprocess_data('data/climate_nasa.csv', 'data/processed_climate_data.csv')
