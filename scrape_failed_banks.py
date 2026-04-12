import requests
import pandas as pd
from bs4 import BeautifulSoup

## fetch HTML page
url = "https://www.fdic.gov/bank/individual/failed/banklist.html"
response = requests.get(url)

## parse HTML page
soup = BeautifulSoup(response.content, 'html.parser')

## find table and get data
table = soup.find('table')
rows = table.find_all('tr')
headers = [th.get_text(strip=True) for th in rows[0].find_all("th")]
print(headers)
data = []
for row in rows[1:]:
    cols = row.find_all('td')
    data.append([col.get_text(strip=True) for col in cols])

## create DataFrame and print
df = pd.DataFrame(data, columns=headers)
print(df.shape)
print(df.head()) 
print(df.tail())

## save to csv
df.to_csv("failed_banks.csv", index=False)

