import pandas as pd

def feature_engineering(input_file, output_file):
    """
    Perform feature engineering on the dataset:
    - Create 'engagement' feature as sum of 'likesCount' and 'commentsCount'
    - Create 'text_length' feature to represent the length of the text column
    - Save the transformed dataset
    """
    df = pd.read_csv(input_file)

    # Ensure 'likesCount' and 'commentsCount' exist
    if 'likesCount' in df.columns and 'commentsCount' in df.columns:
        df['engagement'] = df['likesCount'] + df['commentsCount']
    
    # Create 'text_length' feature
    df['text_length'] = df['text'].astype(str).apply(len)

    # Save processed data
    df.to_csv(output_file, index=False)

    print("✅ Feature Engineering complete. Sample data:")
    print(df.head())

if __name__ == "__main__":
    feature_engineering('data/processed_climate_data.csv', 'data/engineered_climate_data.csv')
