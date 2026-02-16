first_purchase = (orders
                  .groupby("customer_id", as_index=False)
                  .agg(first_date=("date", "min")))
first_purchase["cohort_month"] = first_purchase["first_date"].dt.to_period("M")

orders = orders.merge(first_purchase[["customer_id", "first_date", "cohort_month"]],
                      on="customer_id", how="left", validate="many_to_one")

orders["customer_age_m"] = ((orders["date"].dt.to_period("M")
                             - orders["first_date"].dt.to_period("M")).apply(lambda p: p.n))

orders = (orders
          .sort_values(["customer_id", "date"])
          .assign(order_index=lambda df: df.groupby("customer_id").cumcount() + 1,
                  is_repeat=lambda df: df["order_index"] > 1))




bins = [-np.inf, 50, 200, 1000, np.inf]
labels = ["Very Small", "Small", "Medium", "Large"]
orders["order_size"] = pd.cut(orders["net"], bins=bins, labels=labels, ordered=True)

orders["net_quantile"] = pd.qcut(orders["net"].rank(method="first"), q=4,
                                 labels=["Q1","Q2","Q3","Q4"])





bins = [-np.inf, 50, 200, 1000, np.inf]
labels = ["Very Small", "Small", "Medium", "Large"]
orders["order_size"] = pd.cut(orders["net"], bins=bins, labels=labels, ordered=True)

orders["net_quantile"] = pd.qcut(orders["net"].rank(method="first"), q=4,
                                 labels=["Q1","Q2","Q3","Q4"])




top_products = (orders
                .groupby(["region", "product_id"], as_index=False)
                .agg(net_total=("net", "sum"))
                .assign(rank=lambda df: df.groupby("region")["net_total"]
                                        .rank(method="first", ascending=False))
                .query("rank <= 5"))




cat_counts = (products["category"].astype("string").str.strip().str.title()).value_counts()
top_k = 8
top_cats = set(cat_counts.iloc[:top_k].index)

products["category_slim"] = products["category"].astype("string").str.strip().str.title()
products.loc[~products["category_slim"].isin(top_cats), "category_slim"] = "Other"
products["category_slim"] = products["category_slim"].astype("category")

orders = orders.merge(products[["product_id", "category_slim"]],
                      on="product_id", how="left")

