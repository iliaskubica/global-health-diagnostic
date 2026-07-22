import sqlite3   # Python's built-in tool for creating/using SQLite databases
import pandas as pd  # already familiar - handles our table data
import matplotlib.pyplot as plt  # for creating visualizations
import numpy as np  # for numerical operations, if needed

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



plt.figure(figsize=(8, 6))
plt.scatter(combined["spend"], combined["life_exp"], color="steelblue")

# Add a trend line: numpy calculates the best-fit line through the points
z = np.polyfit(combined["spend"], combined["life_exp"], 1)
trend = np.poly1d(z)

# Calculate what the trend line predicts for each country, then find the gap (residual)
combined["predicted_life_exp"] = trend(combined["spend"])
combined["residual"] = combined["life_exp"] - combined["predicted_life_exp"]

# Positive residual = doing better than spend would predict (efficient)
# Negative residual = doing worse than spend would predict (underperforming)
overperformers = combined.sort_values("residual", ascending=False).head(3)
underperformers = combined.sort_values("residual", ascending=True).head(3)

print("\nTop 3 overperformers (better life expectancy than spend predicts):")
print(overperformers[["country", "spend", "life_exp", "residual"]])

print("\nTop 3 underperformers (worse life expectancy than spend predicts):")
print(underperformers[["country", "spend", "life_exp", "residual"]])

x_range = np.linspace(combined["spend"].min(), combined["spend"].max(), 100)
plt.plot(x_range, trend(x_range), color="red", linestyle="--", label="Trend line")

plt.xscale("log")  # log scale spreads out the clustered lower-spend countries
plt.xlabel("Health Expenditure per Capita, log scale (current US$)")
plt.ylabel("Life Expectancy (years)")
plt.title("Health Spend vs Life Expectancy (2023)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("data/processed/spend_vs_life_expectancy.png", dpi=150, bbox_inches="tight")
print("\nChart saved to data/processed/spend_vs_life_expectancy.png")

conn.close()