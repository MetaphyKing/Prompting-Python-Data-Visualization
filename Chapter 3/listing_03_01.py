import pandas as pd
import numpy as np
from pathlib import Path

NA_VALUES = ["", "NA", "N/A", "n/a", "null", "None", "NaN", "-"]
DATE_COLS = ["order_date"]

CSV_DTYPES = {
    "order_id": "Int64",       # nullable integer type
    "customer_id": "string",
    "region": "string",        # will convert to category later
    "product_id": "string",
    "quantity": "Int64",
    "price": "float64",
    "discount": "float64",
}

def memory_mb(df: pd.DataFrame) -> float:
    return df.memory_usage(deep=True).sum() / (1024**2)

def read_csv_strict(path: Path,
                    dtypes: dict,
                    date_cols: list,
                    sep: str = ",",
                    encoding: str = "utf-8",
                    decimal: str = ".",
                    thousands: str | None = None,
                    na_values: list | None = None,
                    low_memory: bool = False) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        sep=sep,
        encoding=encoding,
        dtype=dtypes,
        parse_dates=date_cols,
        na_values=na_values or NA_VALUES,
        decimal=decimal,
        thousands=thousands,
        keep_default_na=True,
        low_memory=low_memory,
    )
    # Basic checks
    assert set(dtypes.keys()).issubset(df.columns), "Unexpected/missing columns"
    if "order_id" in df.columns:
        assert df["order_id"].isna().sum() == 0, "order_id must not have nulls"
        assert df["order_id"].nunique() == len(df), "order_id must be unique"
    # Normalize categories
    if "region" in df.columns:
        df["region"] = df["region"].str.strip().str.upper()
        df["region"] = df["region"].astype("category")
    # Memory usage
    print(f"Loaded {len(df):,} rows; ~ {memory_mb(df):.2f} MB")
    return df

orders = read_csv_strict(
    Path("data/raw/orders.csv"),
    dtypes=CSV_DTYPES,
    date_cols=DATE_COLS
)
print(orders.head(3))
print(orders.dtypes)
