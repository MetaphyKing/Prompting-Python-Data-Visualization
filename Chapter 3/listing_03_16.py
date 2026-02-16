def iqr_outliers_mask(s: pd.Series, k: float = 1.5) -> pd.Series:
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr = q3 - q1
    lo, hi = q1 - k*iqr, q3 + k*iqr
    return (s < lo) | (s > hi)

orders["gross"] = orders["quantity"].astype("float64") * orders["price"].astype("float64")
out_mask = iqr_outliers_mask(orders["gross"])
orders["is_outlier_gross"] = out_mask
