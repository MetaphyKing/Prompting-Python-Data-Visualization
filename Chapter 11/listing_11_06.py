import pandas as pd
fmri = sns.load_dataset("fmri")

g = sns.lineplot(
    data=fmri, x="timepoint", y="signal",
    hue="region", estimator=None, alpha=0.2
)
fmri_mean = fmri.groupby(["region","timepoint"])["signal"].mean().reset_index()
sns.lineplot(
    data=fmri_mean, x="timepoint", y="signal",
    hue="region", linewidth=2, legend=False
)
plt.title("Signal dynamics over time: individual paths and smoothed trend")
plt.show()
import numpy as np

df = tips.copy()
z = (df["tip"] - df["tip"].mean()) / df["tip"].std()
df["is_outlier"] = (np.abs(z) > 3)

ax = sns.scatterplot(
    data=df, x="total_bill", y="tip",
    hue="is_outlier", style="is_outlier", s=40, alpha=0.7
)
ax.set_title("Outlier candidates highlighted by |z|>3")
plt.show()


ax = sns.residplot(
    data=tips, x="total_bill", y="tip",
    lowess=True,
    scatter_kws={"alpha": 0.5, "s": 35}
)
ax.axhline(0, ls="--", lw=1)
ax.set_title("Residual plot: checking for systematic deviations")
plt.show()


ax = sns.scatterplot(data=df, x="total_bill", y="tip", alpha=0.6)
oi = df[df["is_outlier"]]
for _, r in oi.iterrows():
    ax.annotate("outlier?",
                (r["total_bill"], r["tip"]),
                xytext=(5, 8), textcoords="offset points",
                arrowprops=dict(arrowstyle="->", lw=1))
ax.set_title("Targeted annotation of anomalous points")
plt.show()


ax = sns.boxenplot(data=tips, x="day", y="total_bill")
ax.set_title("Long tails and anomalies by day of week (boxenplot)")
plt.show()
