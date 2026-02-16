# file: data_checks.py
import pandas as pd

def sanity(df: pd.DataFrame, x: str, y: str) -> list[str]:
    issues = []
    if df.empty:
        issues.append("Empty dataset")
    if x not in df or y not in df:
        issues.append("Required columns missing")
    if df[y].dropna().nunique() <= 1:
        issues.append("Insufficient variance in target column")
    if df[y].isna().mean() > 0.3:
        issues.append("Too many missing values")
    return issues
