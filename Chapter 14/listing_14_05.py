import pandas as pd
import numpy as np

def inspect(df):
    print(df.shape)
    print(df.dtypes)
    print(df.isna().sum())
    print(df.head(3))

# Example of type casting and cleaning
df["date"] = pd.to_datetime(df["date"], errors="coerce")
numeric_cols = ["sales_a", "sales_b"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df = df.dropna(subset=["date"])


import matplotlib
import seaborn as sns
import pandas as pd
import sys

print(sys.version)
print("matplotlib:", matplotlib.__version__)
print("seaborn:", sns.__version__)
print("pandas:", pd.__version__)


