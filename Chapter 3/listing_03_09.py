import pandas as pd
import numpy as np

def profile(df: pd.DataFrame, name: str) -> pd.DataFrame:
    stats = pd.DataFrame({
        "dtype": df.dtypes.astype(str),
        "non_null": df.notna().sum(),
        "nulls": df.isna().sum(),
        "null_pct": (df.isna().mean() * 100).round(2),
        "n_unique": df.nunique(dropna=True)
    })
    # Approximate ranges for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    stats.loc[numeric_cols, "min"] = df[numeric_cols].min(numeric_only=True)
    stats.loc[numeric_cols, "p50"] = df[numeric_cols].median(numeric_only=True)
    stats.loc[numeric_cols, "p99"] = df[numeric_cols].quantile(0.99, numeric_only=True)
    stats.loc[numeric_cols, "max"] = df[numeric_cols].max(numeric_only=True)
    print(f" -  Profile: {name}  -  shape {df.shape}")
    return stats

orders_profile = profile(orders, "orders")
orders_profile.head(12)
