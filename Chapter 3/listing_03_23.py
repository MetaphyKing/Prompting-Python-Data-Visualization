daily = (orders
         .set_index("date")
         .resample("D")
         .agg(net_total=("net", "sum"),
              orders_cnt=("order_id", "nunique")))

monthly = (orders
           .set_index("date")
           .resample("M")
           .agg(net_total=("net", "sum"),
                orders_cnt=("order_id", "nunique")))
daily["net_ma7"] = daily["net_total"].rolling(window=7, min_periods=1).mean()

monthly = monthly.sort_index()
monthly["net_prev_month"] = monthly["net_total"].shift(1)
monthly["net_prev_year"]  = monthly["net_total"].shift(12)

monthly["mom_growth_pct"] = (monthly["net_total"] / monthly["net_prev_month"] - 1.0) * 100
monthly["yoy_growth_pct"] = (monthly["net_total"] / monthly["net_prev_year"]  - 1.0) * 100

