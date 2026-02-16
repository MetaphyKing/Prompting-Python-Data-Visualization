orders["unit_price"] = orders["price"].astype("float64")
orders["gross"] = orders["quantity"].astype("float64") * orders["unit_price"]
orders["net"] = orders["gross"] * (1.0 - orders["discount"].astype("float64"))
orders["month"] = orders["order_date"].dt.to_period("M")

assert (orders["gross"] >= 0).all()
assert (orders["net"] >= 0).all()
