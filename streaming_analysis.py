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

# Print summary
print("Your Year in Music Summary:")
print(f"Average Completion Rate: {average_completion:.2f}")
print(f"Total Listening Time (seconds): {total_listening_time}")

print("\nTop Artists:")
print(top_artists)

print("\nTop Songs:")
print(top_songs)

print("\nTop Genres:")
print(top_genres)

print("\nSongs Listened by Day:")
print(songs_by_day)

print("\nSongs Listened by Month:")
print(songs_by_month)

