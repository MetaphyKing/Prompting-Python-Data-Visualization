totals = 0.0
for chunk in pd.read_csv(
        "data/raw/orders.csv",
        chunksize=200_000,
        dtype=CSV_DTYPES,
        parse_dates=DATE_COLS):
    chunk["gross"] = chunk["quantity"].astype("float64") * chunk["price"].astype("float64")
    totals += chunk["gross"].sum()
print("Approximate total revenue:", totals)
