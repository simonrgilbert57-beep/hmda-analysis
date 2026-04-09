cd ~/projects/hmda-analysis && python3 -c "
import requests, zipfile, io, pandas as pd

def peek_panel(year):
    url = f'https://files.consumerfinance.gov/hmda-historic-institution-data/hmda_{year}_panel.zip'
    resp = requests.get(url, timeout=60)
    zf = zipfile.ZipFile(io.BytesIO(resp.content))
    name = [n for n in zf.namelist() if n.endswith(('.csv','.txt'))][0]
    with zf.open(name) as f:
        panel = pd.read_csv(f, dtype=str, nrows=5)
    panel.columns = panel.columns.str.strip().str.lower().str.replace(' ','_')
    resp_col = next((c for c in panel.columns if 'respondent' in c and 'id' in c and 'parent' not in c and 'rssd' not in c and 'fips' not in c), None)
    print(f'{year} panel resp_col={resp_col}')
    if resp_col:
        print(panel[resp_col].tolist())

for year in [2010, 2015, 2016]:
    peek_panel(year)
