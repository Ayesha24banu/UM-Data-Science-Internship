import pandas as pd
import os

def preprocess_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        print(f"Initial dataset shape: {df.shape}")
        print(f"Available columns: {df.columns.tolist()}")

        # Drop unnecessary columns (like 'Sex' if it's empty)
        if 'Sex' in df.columns and df['Sex'].isna().all():
            df = df.drop(columns=['Sex'])
            print("'Sex' column dropped due to lack of data.")

        # Convert categorical 'Metric' to numeric
        if 'Metric' in df.columns:
            df['Metric'] = df['Metric'].astype('category').cat.codes
            print("'Metric' column converted to categorical codes.")

        # Ensure 'Value' is numeric
        if 'Value' in df.columns:
            df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

        # **NEW FEATURES ADDED**
        df["Tobacco Use Duration"] = df["Year"] - 2000  # Example: Years since 2000
        df["Affordability Index"] = df["Value"] / (df["Year"] - 1990)  # Example calculation
        df["Population Percentage"] = df["Value"] / df["Value"].max()  # Normalization
        
        # Drop NaN values
        before_dropna = df.shape[0]
        df = df.dropna(subset=["Metric", "Value", "Tobacco Use Duration", "Affordability Index", "Population Percentage"])
        print(f"Rows dropped due to NaN: {before_dropna - df.shape[0]}")

        # Remove invalid values
        df = df[df["Value"] >= 0]

        # Save cleaned dataset
        df.to_csv(output_file, index=False)
        print(f"✅ Data saved to {output_file}")
    
    except Exception as e:
        print(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    input_path = "data/fatalities.csv"
    output_path = "data/cleaned_fatalities.csv"

    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
    else:
        preprocess_data(input_path, output_path)
