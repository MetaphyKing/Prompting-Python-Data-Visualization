by_region = (orders
             .groupby("region", observed=True, sort=False, as_index=False)
             .agg(net_sum=("net", "sum"),
                  net_mean=("net", "mean"),
                  orders_cnt=("order_id", "nunique")))

# Sanity check
assert {"region", "net_sum", "net_mean", "orders_cnt"}.issubset(by_region.columns)

# Time-based grouping with Grouper
monthly_region = (orders
                  .groupby([pd.Grouper(key="date", freq="M"), "region"],
                           observed=True, sort=True, as_index=False)
                  .agg(net_sum=("net", "sum"),
                       orders_cnt=("order_id", "nunique")))


# Revenue by region and product
by_region_product = (orders
                     .groupby(["region", "product_id"], observed=True, sort=False, as_index=False)
                     .agg(net_sum=("net", "sum"),
                          qty_sum=("quantity", "sum")))

# Top products per region (for horizontal bars and facets)
top_k = 5
top_products = (by_region_product
                .sort_values(["region", "net_sum"], ascending=[True, False])
                .groupby("region", observed=True, sort=False, as_index=False)
                .head(top_k))





orders["month"] = orders["date"].dt.to_period("M")

month_region_total = (orders
                      .groupby(["month", "region"], observed=True)["net"]
                      .transform("sum"))

orders["share_in_month_region"] = orders["net"] / month_region_total

# Category shares by month and region
orders = orders.merge(products[["product_id", "category_slim"]],
                      on="product_id", how="left")

share_tbl = (orders
             .groupby(["month", "region", "category_slim"], observed=True, as_index=False)
             .agg(net_sum=("net","sum")))

share_tbl["month_region_total"] = (share_tbl
                                   .groupby(["month", "region"], observed=True)["net_sum"]
                                   .transform("sum"))
share_tbl["pct"] = (share_tbl["net_sum"] / share_tbl["month_region_total"] * 100).round(2)
