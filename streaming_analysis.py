import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('streaming_data.csv')

# Ensure timestamp is datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Basic stats
average_completion = df['completion_rate'].mean()
total_listening_time = df['duration'].sum()

# Top 5 artists
top_artists = df['artist'].value_counts().head(5)

# Top 10 songs
top_songs = df['song'].value_counts().head(10)

# Top 5 genres
top_genres = df['genre'].value_counts().head(5)

# Songs listened by day
songs_by_day = df['timestamp'].dt.date.value_counts().sort_index()

# Songs listened by month
songs_by_month = df['timestamp'].dt.to_period('M').value_counts().sort_index()

