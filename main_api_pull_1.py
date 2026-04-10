
import pandas as pd

# ---------------------------------------------------------------------------
# HMDA Bank vs Nonbank Originations 1990-2023
# Source: Philadelphia Fed HMDA Lender File (institution classification)
# Output: hmda_bank_nonbank_1990_2023.csv
# ---------------------------------------------------------------------------

LENDER_FILE_1990_2017 = "/Users/simonrossgilbert/Downloads/hmda-1990-2017.xlsx"
LENDER_FILE_2018_2024 = "/Users/simonrossgilbert/Downloads/hmda-2018-present.xlsx"
OUTPUT_FILE = "hmda_bank_nonbank_1990_2023.csv"

def classify_type(t):
    if 10 <= t <= 14:
        return "Depository (bank)"
    elif 20 <= t <= 23:
        return "Depository (bank)"
    elif 30 <= t <= 33:
        return "Depository (bank)"
    elif 40 <= t <= 41:
        return "Independent Mortgage Co (nonbank)"
    else:
        return "Other/Unknown"

print("Reading 1990-2017 file...")
df1 = pd.read_excel(LENDER_FILE_1990_2017)
df1 = df1[df1["YEAR"] <= 2017]
df1 = df1[["YEAR", "TYPE", "ORIG", "ORIGD"]].copy()
df1 = df1[df1["ORIG"] > 0]
df1["institution_type"] = df1["TYPE"].apply(classify_type)
df1["origination_count"] = df1["ORIG"]
df1["origination_volume_000s"] = df1["ORIG"] * df1["ORIGD"]

print("Reading 2018-2023 file...")
df2 = pd.read_excel(LENDER_FILE_2018_2024)
df2 = df2[df2["YEAR"] <= 2023]
df2 = df2[["YEAR", "TYPE", "ORIG", "ORIGD"]].copy()
df2 = df2[df2["ORIG"] > 0]
df2["institution_type"] = df2["TYPE"].apply(classify_type)
df2["origination_count"] = df2["ORIG"]
df2["origination_volume_000s"] = df2["ORIG"] * df2["ORIGD"]

print("Combining and aggregating...")
df = pd.concat([df1, df2], ignore_index=True)
result = (
    df.groupby(["YEAR", "institution_type"])
    .agg(origination_count=("origination_count", "sum"),
         origination_volume_000s=("origination_volume_000s", "sum"))
    .reset_index()
    .rename(columns={"YEAR": "year"})
    .sort_values(["year", "institution_type"])
    .reset_index(drop=True)
)

result.to_csv(OUTPUT_FILE, index=False)
print(f"Done. Saved to {OUTPUT_FILE}")
print()
print(result.to_string(index=False))
print()
print("--- Other/Unknown as % of total by year ---")
for year in sorted(result["year"].unique()):
    yr = result[result["year"] == year]
    total = yr["origination_count"].sum()
    unknown = yr[yr["institution_type"] == "Other/Unknown"]["origination_count"].sum()
    pct = unknown / total * 100
    print(f"{year}: {pct:.1f}% Other/Unknown")
