def sanity(df: pd.DataFrame, name: str):
    print(f" -  Check: {name}")
    print("Shape:", df.shape)
    print("Types:\n", df.dtypes)
    print("Missing:\n", df.isna().sum())
    print("Head:\n", df.head(3))

    if "quantity" in df:
        assert (df["quantity"].fillna(0) >= 0).all(), "quantity must be ≥ 0"
    if "discount" in df:
        assert df["discount"].between(0, 0.95, inclusive="both").all(), "discount out of range"
    if "order_id" in df:
        assert df["order_id"].is_unique, "order_id must be unique"

sanity(orders, "orders.csv")
sanity(products, "products.xlsx")
