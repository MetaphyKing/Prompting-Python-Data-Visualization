import pandas as pd

def expect_monthly(df, date_col="month", min_rows=6):
    assert date_col in df.columns, "Missing date/month column"
    assert pd.api.types.is_datetime64_any_dtype(df[date_col]), "Date column must be datetime"
    assert len(df) >= min_rows, "Too few observations for trend analysis"

expect_monthly(monthly_df)
