import pandas as pd

# read df
df = pd.read_csv("data/fires.csv", sep="\t", encoding="utf-8")

print("=== size ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n=== columns ===")
print(df.columns.tolist())

print("\n=== first 5 wors ===")
print(df.head())

print("\n=== type ===")
print(df.dtypes)

print("\n=== missings ===")
print(df.isnull().sum())