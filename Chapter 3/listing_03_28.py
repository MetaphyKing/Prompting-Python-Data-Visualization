ranked = (by_region_product
          .assign(rank=lambda df: df.groupby("region", observed=True)["net_sum"]
                                  .rank(method="first", ascending=False))
          .query("rank <= 5"))
