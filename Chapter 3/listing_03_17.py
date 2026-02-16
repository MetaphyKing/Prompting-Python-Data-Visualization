def clean_orders(df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    ...
    return df, report

cleaned_orders, cleaning_report = clean_orders(orders)
cleaned_orders.to_parquet("data/processed/orders_cleaned.parquet", index=False)
