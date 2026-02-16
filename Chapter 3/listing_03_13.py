def parse_discount(x):
    if pd.isna(x): return np.nan
    if isinstance(x, str) and x.strip().endswith("%"):
        try:
            return float(x.strip().replace("%", "").replace(",", ".")) / 100.0
        except ValueError:
            return np.nan
    return float(x)

orders["discount"] = orders["discount"].apply(parse_discount)
orders.loc[~orders["discount"].between(0, 0.95, inclusive="both"), "discount"] = np.nan
orders["discount"] = orders["discount"].fillna(0.0)
