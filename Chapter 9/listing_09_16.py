import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# 1) Let Seaborn aggregate (mean by default)
g = sns.catplot(
    data=tips, x="day", y="total_bill", hue="sex",
    kind="bar",
    # errorbar="sd",  # for Seaborn ≥0.12
    height=3.2, aspect=1.3
)
g.set_axis_labels("Day of week", "Total bill (USD)")
plt.show()

# 2) Precompute with pandas (e.g., median and count)
agg = (
    tips
    .groupby(["day", "sex"], observed=True)["total_bill"]
    .agg(median="median", n="size")
    .reset_index()
)

g2 = sns.catplot(
    data=agg, x="day", y="median", hue="sex",
    kind="bar", height=3.2, aspect=1.3
)
g2.set_axis_labels("Day of week", "Median total bill (USD)")
plt.show()
