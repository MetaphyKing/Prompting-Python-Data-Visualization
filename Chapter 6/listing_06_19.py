import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rng = np.random.default_rng(7)
t = np.arange(1, 25)
sales = 100 + 8*np.sin(t/4) + rng.normal(0, 2, size=t.size)       # sample sales
ad_spend = 20 + 5*np.cos(t/6) + rng.normal(0, 1.5, size=t.size)   # sample ad spend
x = rng.normal(0, 1, 200)
y = 0.6*x + rng.normal(0, 0.8, 200)                               # noisy linear relation
M = np.corrcoef(rng.normal(size=(80, 8)), rowvar=False)           # correlations matrix

fig, axs = plt.subplots(2, 2, figsize=(10, 6), sharex=False, sharey=False)

# Panel A: line plot (sales trend)
axA = axs[0, 0]
axA.plot(t, sales, linewidth=2, label="Sales")
axA.set_title("A. Sales dynamics")
axA.set_xlabel("Week"); axA.set_ylabel("Units")
axA.grid(True, alpha=0.3)
axA.legend(loc="upper left")

# Panel B: bar plot (ad spend)
axB = axs[0, 1]
axB.bar(t, ad_spend, width=0.8, label="Ad spend")
axB.set_title("B. Advertising budget")
axB.set_xlabel("Week"); axB.set_ylabel("k$")
axB.grid(True, axis="y", alpha=0.3)
axB.legend(loc="upper right")

# Panel C: scatter with regression (Seaborn regplot on Matplotlib Axes)
axC = axs[1, 0]
sns.regplot(x=x, y=y, ax=axC, scatter_kws={"alpha":0.5, "s":25}, line_kws={"linewidth":2})
axC.set_title("C. Feature relationship (regression)")
axC.set_xlabel("Factor X"); axC.set_ylabel("Factor Y")
axC.grid(True, alpha=0.25)

# Panel D: heatmap (Seaborn)
axD = axs[1, 1]
sns.heatmap(M, ax=axD, cmap="viridis", vmin=-1, vmax=1, cbar=True, square=True)
axD.set_title("D. Correlations (heatmap)")
axD.set_xlabel("Variables"); axD.set_ylabel("Variables")

fig.suptitle("Combining multiple plot types in a single figure", y=0.98)
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
