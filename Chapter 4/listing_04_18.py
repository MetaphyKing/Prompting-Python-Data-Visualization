import pandas as pd

# CSV, encoding, and explicit types
df = pd.read_csv("orders.csv", encoding="utf-8")

# quick scan
print(df.shape)         # table size
print(df.dtypes)        # column dtypes
print(df.head(3))       # first rows
print(df.isna().mean()) # share of missing values by column


# dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# categories with an explicit type
df["segment"] = df["segment"].astype("category")

# numeric columns
for col in ["amount", "qty"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# duplicates and obvious artifacts
df = df.drop_duplicates()
df = df.dropna(subset=["date", "amount"])

