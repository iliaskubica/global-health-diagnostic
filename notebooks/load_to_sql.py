import sqlite3   # Python's built-in tool for creating/using SQLite databases
import pandas as pd  # already familiar - handles our table data

# Read the CSV we created on Day 3
df = pd.read_csv("data/raw/worldbank_health_indicators.csv")

print(df.head())  # show the first 5 rows, just to confirm it loaded correctly
