import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_likes_trend(df):
    plt.figure(figsize=(12, 5))
    df.groupby(df['date'].dt.date)['likesCount'].sum().plot(kind='line', color='blue')
    plt.title("Likes Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Likes Per Day")
    plt.xticks(rotation=45)
    plt.show()

def plot_comments_distribution(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df['commentsCount'], bins=30, kde=True, color='green')
    plt.title("Comments Count Distribution")
    plt.xlabel("Number of Comments")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('data/processed_climate_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    
    plot_likes_trend(df)
    plot_comments_distribution(df)
