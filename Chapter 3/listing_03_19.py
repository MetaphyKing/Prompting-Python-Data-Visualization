orders = (orders
    .assign(
        unit_price = orders["price"].astype("float64"),
        gross = orders["quantity"].astype("float64") * orders["unit_price"],
        net   = lambda df: df["gross"] * (1.0 - df["discount"]),
        date  = lambda df: pd.to_datetime(df["order_date"], utc=True),
        year  = lambda df: df["date"].dt.year,
        month = lambda df: df["date"].dt.to_period("M"),
        week  = lambda df: df["date"].dt.to_period("W"),
        dow   = lambda df: df["date"].dt.dayofweek,   # 0=Mon … 6=Sun
        is_weekend = lambda df: df["date"].dt.dayofweek.isin([5, 6]),
        month_end  = lambda df: df["date"].dt.is_month_end,
        quarter    = lambda df: df["date"].dt.quarter,
    )
)

dow_order = pd.CategoricalDtype(categories=[0,1,2,3,4,5,6], ordered=True)
orders["dow"] = orders["dow"].astype(dow_order)

