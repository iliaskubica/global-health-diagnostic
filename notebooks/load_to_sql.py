import sqlite3   # Python's built-in tool for creating/using SQLite databases
import pandas as pd  # already familiar - handles our table data

# Read the CSV we created on Day 3
df = pd.read_csv("data/raw/worldbank_health_indicators.csv")

print(df.head())  # show the first 5 rows, just to confirm it loaded correctly

# Connect to (or create, if it doesn't exist yet) a SQLite database file
conn = sqlite3.connect("data/processed/health_data.db")

# Load our DataFrame into that database as a table called 'indicators'
df.to_sql("indicators", conn, if_exists="replace", index=False)

print("\nData successfully loaded into SQLite database: data/processed/health_data.db")

conn.close()