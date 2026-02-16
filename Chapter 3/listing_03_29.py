# Order size structure by region (% shares)
size_region = pd.crosstab(
    orders["order_size"],
    orders["region"],
    values=orders["net"],
    aggfunc="sum",
    normalize="columns",
    dropna=True
).multiply(100).round(1)

# Monthly × Region pivot for revenue
heat = (pd.pivot_table(orders,
                       index=orders["date"].dt.to_period("M"),
                       columns="region",
                       values="net",
                       aggfunc="sum",
                       observed=True)
        .fillna(0.0))


# 3-month rolling net revenue within region
monthly_net = (orders
               .set_index("date")
               .groupby("region", observed=True)[["net"]]
               .resample("M")
               .sum()
               .reset_index())

monthly_net["net_ma3"] = (monthly_net
                          .groupby("region", observed=True)["net"]
                          .transform(lambda s: s.rolling(window=3, min_periods=1).mean()))



comp = (orders
        .groupby(["region", pd.Grouper(key="date", freq="M"), "category_slim"],
                 observed=True, as_index=False)
        .agg(net_sum=("net","sum")))

comp["group_total"] = comp.groupby(["region", "date"], observed=True)["net_sum"].transform("sum")
comp["pct"] = comp["net_sum"] / comp["group_total"] * 100
