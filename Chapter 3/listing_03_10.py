# 1) Critical fields
critical = ["order_id", "order_date", "customer_id", "product_id"]
missing_critical = orders[critical].isna().any(axis=1).sum()
if missing_critical:
    broken = orders[orders[critical].isna().any(axis=1)]
    broken.to_parquet("data/interim/orders_missing_critical.parquet", index=False)
    orders = orders[~orders.index.isin(broken.index)]

# 2) Numeric fields: quantity, price, discount
orders["quantity"] = orders["quantity"].astype("Int64")
orders = orders[orders["quantity"].notna()]

global_price_median = orders["price"].median()
orders["price"] = orders.groupby("product_id")["price"].transform(
    lambda s: s.fillna(s.median())
).fillna(
    orders.groupby("region")["price"].transform("median")
).fillna(global_price_median)

orders["discount"] = orders["discount"].fillna(0.0)


#Dates (with care):

orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce", utc=True)
orders["date_imputed"] = orders["order_date"].isna()
orders = orders[~orders["order_date"].isna()]

