import sqlite3
import pandas as pd

# Load movies from CSV
df = pd.read_csv('movies.csv')  # Make sure movies.csv is in the same folder

# Connect to SQLite database (creates if not exists)
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    rating REAL
)
''')

# Clear table if already exists (optional, avoids duplicate entries)
cursor.execute('DELETE FROM movies')

# Insert CSV data into table
for index, row in df.iterrows():
    cursor.execute('INSERT INTO movies (id, title, genre, rating) VALUES (?, ?, ?, ?)',
                   (row['id'], row['title'], row['genre'], row['rating']))

conn.commit()
conn.close()

print("Database created and CSV data inserted successfully!")
