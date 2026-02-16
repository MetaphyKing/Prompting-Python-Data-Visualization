date_min = orders["date"].min().floor("D")
date_max = orders["date"].max().ceil("D")

calendar = (pd.DataFrame({"date": pd.date_range(date_min, date_max, freq="D", tz="UTC")})
            .assign(
                day  = lambda df: df["date"].dt.day,
                month= lambda df: df["date"].dt.month,
                year = lambda df: df["date"].dt.year,
                dow  = lambda df: df["date"].dt.dayofweek.astype(dow_order),
                is_weekend = lambda df: df["dow"].isin([5, 6]),
                week = lambda df: df["date"].dt.to_period("W"),
                month_period = lambda df: df["date"].dt.to_period("M"),
                quarter = lambda df: df["date"].dt.quarter
            ))


orders["date_day"] = orders["date"].dt.floor("D")
orders = orders.merge(calendar.rename(columns={"date": "date_day"}),
                      on="date_day", how="left", validate="many_to_one")
