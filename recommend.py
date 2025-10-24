import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('movies.db')
df = pd.read_sql_query("SELECT * FROM movies", conn)

# Ask user for favorite genre
user_genre = input("Enter your favorite genre (SciFi, Action, Romance, Adventure): ").capitalize()

# Filter movies by genre
recommended = df[df['genre'] == user_genre]

if recommended.empty:
    print("Sorry, no movies found for this genre.")
else:
    # Show all movies in that genre
    print("\nRecommended Movies:")
    print(recommended[['title', 'rating']])
    