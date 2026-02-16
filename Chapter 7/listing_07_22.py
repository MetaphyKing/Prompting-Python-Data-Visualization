from matplotlib.ticker import (ScalarFormatter, EngFormatter,
                               PercentFormatter, FuncFormatter)

fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))

# Engineering units
ax = axs[0]
ax.plot([0, 1e6], [0, 2e6])
ax.yaxis.set_major_formatter(EngFormatter(unit="B"))
ax.set_title("EngFormatter")

# Percentages
ax = axs[1]
ax.plot([0, 10], [0.0, 1.0])
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=0))
ax.set_title("PercentFormatter")

# Custom formatting
def thinspace(x, pos):
    return f"{x:,.0f}".replace(",", " ")

ax = axs[2]
ax.plot([0, 10], [0, 1200000])
ax.yaxis.set_major_formatter(FuncFormatter(thinspace))
ax.set_title("FuncFormatter (custom thousands)")



for ax in axs: ax.grid(True, alpha=0.25)
plt.tight_layout(); plt.show()
