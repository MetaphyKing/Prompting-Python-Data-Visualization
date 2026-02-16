rules = [
    ("quantity_non_negative", (orders["quantity"].fillna(0) >= 0)),
    ("price_non_negative", (orders["price"].fillna(0) >= 0)),
    ("discount_range", orders["discount"].between(0, 0.95, inclusive="both")),
]

failed = [name for name, mask in rules if not mask.all()]
if failed:
    bad_rows = orders.loc[~rules[0][1] | ~rules[1][1] | ~rules[2][1]]
    bad_rows.to_parquet("data/interim/orders_rule_violations.parquet", index=False)
    orders = orders.loc[rules[0][1] & rules[1][1] & rules[2][1]]
