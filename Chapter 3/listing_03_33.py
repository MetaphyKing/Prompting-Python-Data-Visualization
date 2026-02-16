

import pandas as pd
import numpy as np

def quick_info(df: pd.DataFrame, name: str = "df") -> None:
    print(f"\n -  {name}: shape={df.shape[0]}×{df.shape[1]}")
    print(df.dtypes.sort_index())
    print("\n.info():")
    df.info(memory_usage="deep")

def quick_numbers(df: pd.DataFrame, quantiles=(0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99)) -> pd.DataFrame:
    num = df.select_dtypes(include=[np.number])
    desc = num.describe(percentiles=quantiles).T
    desc["missing"] = num.isna().mean().round(4)
    desc["skew"] = num.skew(numeric_only=True)
    desc["kurt"] = num.kurt(numeric_only=True)
    return desc.sort_index()

def quick_categories(df: pd.DataFrame, top=10) -> dict[str, pd.Series]:
    out = {}
    for col in df.select_dtypes(include=["object", "string", "category"]).columns:
        vc = df[col].astype("string").str.strip().value_counts(dropna=True).head(top)
        out[col] = vc
    return out


from pathlib import Path
orders = pd.read_parquet(Path("data/processed/orders_features.parquet"))
products = pd.read_parquet(Path("data/processed/products.parquet"))

quick_info(orders, "orders")
quick_info(products, "products")

numbers_profile = quick_numbers(orders)
print(numbers_profile.head(10))

cat_profile = quick_categories(orders, top=8)
for c, vc in cat_profile.items():
    print(f"\nTop categories  -  {c}:\n{vc}")



import matplotlib.pyplot as plt

ax = orders["net"].plot(kind="hist", bins=40, alpha=0.7, title="NET distribution (linear scale)")
ax.set_xlabel("NET")

plt.figure()
ax = orders["net"].plot(kind="hist", bins=40, alpha=0.7, title="NET (logarithmic X axis)")
ax.set_xscale("log")
ax.set_xlabel("NET (log)")

plt.figure()
orders["net"].plot(kind="kde", title="NET  -  KDE (density)")
plt.xlabel("NET")


daily = (orders.set_index("date")
               .sort_index()
               .resample("D")
               .agg(net_total=("net","sum")))

daily["net_ma7"] = daily["net_total"].rolling(window=7, min_periods=1).mean()

ax = daily["net_total"].plot(title="Daily revenue")
daily["net_ma7"].plot(ax=ax)
ax.set_ylabel("NET"); ax.legend(["Daily", "MA7"])


by_region = (orders.groupby("region", observed=True, as_index=False)
                    .agg(net_sum=("net","sum"))
                    .sort_values("net_sum"))

ax = by_region.plot(kind="barh", x="region", y="net_sum", legend=False, title="Revenue by region")
ax.set_xlabel("NET")

plt.figure()
orders.boxplot(column="net", by="region")
plt.title("NET by region  -  boxplots"); plt.suptitle("")
plt.xlabel("region"); plt.ylabel("NET"); plt.tight_layout()









