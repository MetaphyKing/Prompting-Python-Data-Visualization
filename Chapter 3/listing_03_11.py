before = len(orders)
orders = orders.drop_duplicates(keep="first")
print("Dropped full duplicates:", before - len(orders))

dups = orders["order_id"].duplicated(keep=False)
if dups.any():
    if "updated_at" in orders.columns:
        orders = orders.sort_values("updated_at").drop_duplicates(subset=["order_id"], keep="last")
    else:
        agg_cols = {
            "quantity": "sum",
            "price": "mean",
            "discount": "mean",
            "order_date": "min",
            "customer_id": "first",
            "region": "first",
            "product_id": "first"
        }
        orders = (orders.groupby("order_id", as_index=False).agg(agg_cols))
