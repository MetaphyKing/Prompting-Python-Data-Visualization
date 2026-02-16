med_price = orders.groupby("product_id")["unit_price"].transform("median")
orders["price_vs_median"] = orders["unit_price"] / med_price

conditions = [
    orders["price_vs_median"] <= 0.9,
    orders["price_vs_median"].between(0.9, 1.1),
    orders["price_vs_median"] > 1.1
]
choices = ["Under Median", "Around Median", "Above Median"]
orders["price_band"] = np.select(conditions, choices, default="Unknown")
orders["price_band"] = pd.Categorical(orders["price_band"],
                                      categories=choices + ["Unknown"], ordered=True)



out = processed / "orders_features.parquet"
orders.to_parquet(out, index=False)

check = pd.read_parquet(out)
assert len(check) == len(orders)
must_have = {"gross","net","month","week","is_weekend",
             "customer_age_m","order_size","price_band"}
