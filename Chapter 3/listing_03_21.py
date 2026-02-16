#A) Month × Region cube → net totals
mn = (orders
      .groupby(["month", "region"], as_index=False)
      .agg(net_total=("net", "sum")))

heat = (mn
        .pivot_table(index="month", columns="region", values="net_total", aggfunc="sum")
        .sort_index()
        .fillna(0.0))


#B) Back to long form for faceting:

long_again = heat.reset_index().melt(id_vars="month",
                                     var_name="region",
                                     value_name="net_total")

pivot()