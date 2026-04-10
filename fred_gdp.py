import requests
import pandas as pd
from config import KEY, FRED_API_URL, FDIC_API_URL
##define function to fetch GDP data from FRED API
def fetch_fred_gdp(observation_start, observation_end):
    params = {
        "series_id": "GDPC1"",
        "observation_start": observation_start,
        "observation_end": observation_end,
        "api_key": KEY,
        "file_type": "json"
    }
    response = requests.get(FRED_API_URL, params=params)
    data = response.json()
    observations = data["observations"]
    gdp_data = [(obs["date"], obs["value"]) for obs in observations]
    return pd.DataFrame(gdp_data, columns=["date", "gdp"])

##fetches GDP data from 2010 to 2025 and saves to CSV
df = fetch_fred_gdp("2010-01-01", "2025-12-31")
df.to_csv("fred_gdp_data.csv", index=False)


##print shape, first 5 rows, last 5 rows
print(df.shape)
print(df.head())
print(df.tail())