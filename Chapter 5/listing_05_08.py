norm = (df["B"] - df["B"].min()) / (df["B"].max() - df["B"].min())

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, norm, color="#F58518", linewidth=2.2)
ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=0))
ax.set_ylim(0, 1)
ax.set_title("Percentage format for normalized values", loc="left")
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.show()




from matplotlib.ticker import ScalarFormatter, EngFormatter

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.4))

# Scientific notation with thresholds
ax1.plot(df.index, 1e-3 + 2e-3*df["A"], color="#4C78A8")
sf = ScalarFormatter(useMathText=True)
sf.set_powerlimits((-3, 3))
ax1.yaxis.set_major_formatter(sf)
ax1.set_title("Scientific notation (ScalarFormatter)", loc="left")
ax1.grid(True, axis="y", alpha=0.25)

# Engineering prefixes (kilo, mega, etc.)
ax2.plot(df.index, 1e6*(1 + 0.1*df["B"]), color="#F58518")
ax2.yaxis.set_major_formatter(EngFormatter(unit="Hz"))
ax2.set_title("Engineering prefixes (EngFormatter)", loc="left")
ax2.grid(True, axis="y", alpha=0.25)

plt.tight_layout()
plt.show()
