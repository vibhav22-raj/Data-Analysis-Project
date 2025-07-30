import pandas as pd

df = pd.read_csv('ADSI_Table_1A.2.csv')

print("Initial shape:", df.shape)
print("Columns:", df.columns.tolist())

df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('-', '_').str.replace('.', '').str.replace('/', '_')

df.drop_duplicates(inplace=True)

df.replace(['', 'NA', 'NaN', 'Total (States)', 'Total (UTs)', 'Total (All India)', 'Total (Cities)'], pd.NA, inplace=True)
df.dropna(subset=['State'], inplace=True)  

numeric_cols = df.columns.drop(['Sl._No_', 'State'])
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df = df.dropna(thresh=len(df.columns) - 2)  

df.reset_index(drop=True, inplace=True)

print("Cleaned shape:", df.shape)
print(df.head())

df.to_csv('ADSI_Table_1A.2_cleaned.csv', index=False)

