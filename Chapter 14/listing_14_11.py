import pandas as pd

def sanity_check_before_plot(df: pd.DataFrame) -> None:
    has_dates = "date" in df.columns and pd.api.types.is_datetime64_any_dtype(df["date"])
    no_all_na = df.drop(columns=["date"]).notna().any().any()

    assert has_dates, "Date column missing or wrong type"
    assert no_all_na, "All values are NaN — check preprocessing pipeline"

sanity_check_before_plot(df)
