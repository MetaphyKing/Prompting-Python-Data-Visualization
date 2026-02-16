
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
n = 800
df = pd.DataFrame({
    "month": rng.integers(1, 13, size=n),
    "value": rng.normal(100, 15, size=n) + np.sin(rng.integers(1, 13, size=n))*5
})

means = df.groupby("month")["value"].mean().sort_index()

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(13, 4), dpi=120)

# line
axes[0].plot(means.index, means.values, marker="o")
axes[0].set_title("Monthly means (line)")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Value, units")
axes[0].grid(True, alpha=0.3)

# bars
axes[1].bar(means.index, means.values)
axes[1].set_title("Same means (bar)")
axes[1].set_xlabel("Month")
axes[1].grid(True, axis="y", alpha=0.3)

# histogram of raw observations
axes[2].hist(df["value"], bins=30)
axes[2].set_title("Distribution of values")
axes[2].set_xlabel("Value")
axes[2].set_ylabel("Frequency")
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
