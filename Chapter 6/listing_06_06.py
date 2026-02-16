rng = np.random.default_rng(42)
t = np.arange(0, 100)
A = rng.normal(0, 1, size=(4, len(t))).cumsum(axis=1)  # four time series

fig, axs = plt.subplots(2, 2, figsize=(9, 6), sharex=True)
labels = ["Sensor A", "Sensor B", "Sensor C", "Sensor D"]

# Place one series per panel
for ax, i in zip(axs.ravel(), range(4)):
    ax.plot(t, A[i], label=labels[i])
    ax.set_title(labels[i])
    ax.grid(True, alpha=0.3)

# Shared legend below the figure
handles, _ = axs[0, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=4)
fig.suptitle("Mini-dashboard: four sensors with a shared legend", y=0.98)

fig.tight_layout(rect=[0, 0.05, 1, 0.97])  # reserve space for legend
plt.show()
