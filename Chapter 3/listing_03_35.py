# Top-N products (horizontal bars)
top = (orders.groupby("product_id", as_index=False, observed=True)
              .agg(net_sum=("net","sum"))
              .sort_values("net_sum", ascending=False)
              .head(10))
ax = top.plot(kind="barh", x="product_id", y="net_sum", legend=False, title="Top-10 products by NET")
ax.invert_yaxis(); ax.set_xlabel("NET")

# Order size structure by region  -  100%
size_region = pd.crosstab(
    orders["order_size"], orders["region"],
    values=orders["net"], aggfunc="sum", normalize="columns"
).multiply(100.0).round(1)
print(size_region)

