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

# Reconnect to run a query (we closed the connection earlier)
conn = sqlite3.connect("data/processed/health_data.db")

# Query 1: highest health spenders (2023)
q1 = "SELECT country, value FROM indicators WHERE indicator = 'health_expenditure_per_capita' AND year = 2023 ORDER BY value DESC LIMIT 5"
print("\nTop 5 health expenditure (2023):")
print(pd.read_sql(q1, conn))

# Query 2: lowest life expectancy (2023)
q2 = "SELECT country, value FROM indicators WHERE indicator = 'life_expectancy' AND year = 2023 ORDER BY value ASC LIMIT 5"
print("\nLowest 5 life expectancy (2023):")
print(pd.read_sql(q2, conn))

# --- Pure Python/pandas analysis below (no SQL) ---
# Pull full 2023 data for two indicators, then compare them side by side
spend = pd.read_sql("SELECT country, value AS spend FROM indicators WHERE indicator = 'health_expenditure_per_capita' AND year = 2023", conn)
life = pd.read_sql("SELECT country, value AS life_exp FROM indicators WHERE indicator = 'life_expectancy' AND year = 2023", conn)

# merge() joins two tables together, matching rows where 'country' is the same in both
combined = spend.merge(life, on="country")

# .corr() calculates how strongly two columns move together (-1 to 1; closer to 1 = strong positive relationship)
correlation = combined["spend"].corr(combined["life_exp"])
print(f"\nCorrelation between health spend and life expectancy: {correlation:.2f}")

conn.close()