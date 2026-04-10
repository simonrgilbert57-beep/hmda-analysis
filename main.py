from config import KEY, FRED_API_URL, FDIC_API_URL
def run_pipeline():
    print("Starting pipeline...")
    print(f'FRED API Key: {KEY}')
    print(f'FRED API URL: {FRED_API_URL}')
    print(f'FDIC API URL: {FDIC_API_URL}')
    print("Pipeline complete")
if __name__ == "__main__":
    run_pipeline()    