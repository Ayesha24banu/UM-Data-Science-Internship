import pandas as pd
import os

def create_features():
    df = pd.read_csv('data/cleaned_world_population.csv')
    if '2022 Population' in df.columns:
        df['GrowthRate'] = df['2022 Population'].pct_change() * 100
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/feature_engineered_population.csv', index=False)

if __name__ == "__main__":
    create_features()
