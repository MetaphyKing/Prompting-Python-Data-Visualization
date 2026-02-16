def parse_eu_number(s):
    if pd.isna(s): return np.nan
    if isinstance(s, (int, float)): return float(s)
    s = str(s).replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return np.nan


def normalize_text(s: pd.Series) -> pd.Series:
    s = s.astype("string").str.strip()
    s = s.str.replace("\u2013", "-", regex=False)
    s = s.str.replace("\u2014", "-", regex=False)
    return s

if "name" in products.columns:
    products["name"] = normalize_text(products["name"])
if "category" in products.columns:
    products["category"] = normalize_text(products["category"]).str.title().astype("category")
