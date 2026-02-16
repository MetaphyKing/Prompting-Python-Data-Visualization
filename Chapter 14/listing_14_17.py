import pandas as pd
import numpy as np

def validate_inputs(df: pd.DataFrame, date_col: str, value_cols: list[str]) -> None:
    assert date_col in df.columns, "Missing date column"
    assert all(c in df.columns for c in value_cols), "Some metrics not found"
    assert pd.api.types.is_datetime64_any_dtype(df[date_col]), "Date column must be datetime"

    # Missing values are allowed, but volume matters
    na_share = df[value_cols].isna().mean().max()
    assert na_share < 0.3, "Too many missing values; review handling rules"

    # Duplicates can distort aggregation (duplicates by date_col)
    dup = df.duplicated(subset=[date_col]).sum()
    assert dup < len(df) * 0.05, "Suspiciously high number of duplicate timestamps"

    # Check for infinities (coerce to numeric to avoid object-type surprises)
    numeric = df[value_cols].apply(pd.to_numeric, errors="coerce")
    assert np.isfinite(numeric.to_numpy()).all(), "Found ±inf (or non-numeric values); requires cleaning"


def validate_aggregation(
    monthly: pd.DataFrame, value_cols: list[str], time_col: str = "month"
) -> pd.DataFrame:
    # AI-generated pipelines often produce unsorted time series after merges/filtering.
    # Always sort before monotonicity checks.
    if time_col not in monthly.columns:
        raise ValueError(f"Missing time column: {time_col}")

    monthly = monthly.sort_values(time_col, kind="mergesort").reset_index(drop=True)

    assert pd.api.types.is_datetime64_any_dtype(monthly[time_col]), "Time column must be datetime"
    assert monthly[time_col].is_monotonic_increasing, "Time axis is not monotonic after sorting"
    assert all(c in monthly.columns for c in value_cols), "Metrics lost after aggregation"

    return monthly
