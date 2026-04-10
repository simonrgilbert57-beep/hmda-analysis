import pandas as pd

##read csv 1
df_1 = pd.read_csv(r'/Users/simonrossgilbert/projects/CSVs/hmda_bank_nonbank_1990_2023.csv')
print(df_1.shape)
print(df_1.head())

## read csv 2
df_2 = pd.read_csv('fred_macro_data.csv')
print(df_2.shape)  
print(df_2.head())

## filter csv 1 into csv 3 for 2015+
df_3 = df_1[df_1['year'] >= 2015]
print(df_3.shape)
print(df_3.head())
