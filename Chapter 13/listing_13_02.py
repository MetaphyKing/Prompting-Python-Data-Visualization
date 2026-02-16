import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

rng = np.random.default_rng(42)
cities = np.array(["A", "B", "C"])
n = 300
df = pd.DataFrame({
    "area": rng.uniform(30, 180, size=n),
    "city": rng.choice(cities, size=n, p=[0.4, 0.35, 0.25])
})
base_price = 800.0
city_adj = {"A": 0.0, "B": 120.0, "C": 200.0}
noise = rng.normal(0, 60, size=n)
df["price"] = base_price + 5.2 * df["area"] + df["city"].map(city_adj) + noise

plt.figure(figsize=(9, 6))
ax = sns.scatterplot(data=df, x="area", y="price", hue="city", alpha=0.6)
sns.regplot(data=df, x="area", y="price", scatter=False, ci=None, ax=ax)

ax.set_title("Связь цены и площади жилья")
ax.set_xlabel("Площадь, м²")
ax.set_ylabel("Цена, тыс. у. е.")
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{int(v):,}".replace(",", " ")))
ax.legend(title="Город", bbox_to_anchor=(1.02, 1), loc="upper left")
ax.grid(True, axis="both", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("figures/price_area_reg.png", dpi=120)
plt.show()
