pareto = (by_region_product
          .sort_values(["region", "net_sum"], ascending=[True, False])
          .assign(cum_net=lambda df: df.groupby("region", observed=True)["net_sum"].cumsum(),
                  total_net=lambda df: df.groupby("region", observed=True)["net_sum"].transform("sum"))
          .assign(cum_pct=lambda df: (df["cum_net"] / df["total_net"] * 100).round(2)))

# Flag top 80%
pareto["in_80_pct"] = pareto["cum_pct"] <= 80.0
