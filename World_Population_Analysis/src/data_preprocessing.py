import pandas as pd
import os

def preprocess_data():
    df = pd.read_csv('data/world_population.csv')
    df.drop(columns=['CCA3', 'Capital'], inplace=True, errors='ignore')
    df.dropna(inplace=True)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/cleaned_world_population.csv', index=False)

if __name__ == "__main__":
    preprocess_data()
