import requests
import pandas as pd
from config import KEY, FRED_API_URL
series_list = ["GDPC1", "UNRATE", "CPIAUCSL"]  # Example series IDs for GDP, Unemployment Rate, and CPI
df = pd.DataFrame()
##define function to fetch GDP data from FRED API
def fetch_fred_series(series_id, observation_start, observation_end):
    params = {
        "series_id": series_id,
        "observation_start": observation_start,
        "observation_end": observation_end,
        "api_key": KEY,
        "file_type": "json"
    }
    response = requests.get(FRED_API_URL, params=params)
    data = response.json()
    observations = data["observations"]
    series_data = [(obs["date"], obs["value"]) for obs in observations]
    return pd.DataFrame(series_data, columns=["date", "value"])
## fetches data for each series and merges into a single DataFrame
for series in series_list:
    series_df = fetch_fred_series(series, "2010-01-01", "2025-12-31")
    series_df.rename(columns={"value": series}, inplace=True)
    if df.empty:
        df = series_df
    else:
        df = pd.merge(df, series_df, on="date", how="outer")
df.to_csv("fred_macro_data.csv", index=False)
print(df.shape)
print(df.head())
