import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('streaming_data.csv')

# Strip leading/trailing whitespace from column names
df.columns = df.columns.str.strip()

# Print column names for debugging
print("Available columns:", df.columns.tolist())

# Basic stats
try:
    average_completion = df['completion_rate'].mean()
except KeyError:
    print("Column 'completion_rate' not found.")
    average_completion = None

try:
    total_listening_time = df['duration'].sum()
except KeyError:
    print("Column 'duration' not found.")
    total_listening_time = None

# Top 5 artists
top_artists = df['artist'].value_counts().head(5) if 'artist' in df.columns else None

# Top 10 songs
top_songs = df['song'].value_counts().head(10) if 'song' in df.columns else None

# Top 5 genres
top_genres = df['genre'].value_counts().head(5) if 'genre' in df.columns else None

# Songs listened by day
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    songs_by_day = df['timestamp'].dt.date.value_counts().sort_index()
    songs_by_month = df['timestamp'].dt.to_period('M').value_counts().sort_index()
else:
    songs_by_day = songs_by_month = None

# Print summary
print("\nYour Year in Music Summary:")
if average_completion is not None:
    print(f"Average Completion Rate: {average_completion:.2f}")
if total_listening_time is not None:
    print(f"Total Listening Time (seconds): {total_listening_time}")

if top_artists is not None:
    print("\nTop Artists:")
    print(top_artists)

if top_songs is not None:
    print("\nTop Songs:")
    print(top_songs)

if top_genres is not None:
    print("\nTop Genres:")
    print(top_genres)

if songs_by_day is not None:
    print("\nSongs Listened by Day:")
    print(songs_by_day)

if songs_by_month is not None:
    print("\nSongs Listened by Month:")
    print(songs_by_month)

# Visualization: Line graph of songs by day
if songs_by_day is not None:
    plt.figure(figsize=(10, 5))
    songs_by_day.plot(kind='line')
    plt.title('Songs Listened by Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Songs')
    plt.tight_layout()
    plt.show()

# Visualization: Bar chart of top artists
if top_artists is not None:
    plt.figure(figsize=(8, 5))
    top_artists.plot(kind='bar', color='skyblue')
    plt.title('Top 5 Most Listened Artists')
    plt.xlabel('Artist')
    plt.ylabel('Play Count')
    plt.tight_layout()
    plt.show()

# Visualization: Histogram of completion rates
if 'completion_rate' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.hist(df['completion_rate'].dropna(), bins=10, color='salmon', edgecolor='black')
    plt.title('Distribution of Completion Rates')
    plt.xlabel('Completion Rate')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()