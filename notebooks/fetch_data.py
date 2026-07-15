# fetch_data.py
# Pulls health system indicators from the World Bank API for a set of countries,
# and saves the combined result as a CSV file in data/raw.

import requests   # lets us call the API
import pandas as pd  # lets us organise the results into a table

# The 15 countries we're comparing, using their World Bank 3-letter codes
countries = "GBR;USA;JPN;BRA;ZAF;IND;NGA;DEU;KEN;VNM;MEX;BGD;FRA;GHA;IDN"

# The 4 indicators we're pulling, with a friendly name for each
indicators = {
    "SH.XPD.CHEX.PC.CD": "health_expenditure_per_capita",
    "SP.DYN.LE00.IN": "life_expectancy",
    "SH.STA.MMRT": "maternal_mortality_ratio",
    "SH.MED.PHYS.ZS": "physicians_per_1000",
}

all_rows = []  # we'll collect every data point here before saving

# Loop through each indicator one at a time
for code, name in indicators.items():
    url = f"https://api.worldbank.org/v2/country/{countries}/indicator/{code}"
    params = {"format": "json", "per_page": 1000, "date": "2015:2023"}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # The API returns [metadata, actual_data] — we want the second part
    records = data[1]
    
    for record in records:
        all_rows.append({
            "country": record["country"]["value"],
            "country_code": record["countryiso3code"],
            "indicator": name,
            "year": record["date"],
            "value": record["value"],
        })
    
    print(f"Fetched {name}: {len(records)} records")

# Turn our collected rows into a table (DataFrame) and save it
df = pd.DataFrame(all_rows)
df.to_csv("data/raw/worldbank_health_indicators.csv", index=False)

print(f"\nSaved {len(df)} total rows to data/raw/worldbank_health_indicators.csv")