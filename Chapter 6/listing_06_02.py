fig, axs = plt.subplots(1, 3, figsize=(9, 3), squeeze=False)  # always 2D
axs = axs.ravel()  # flatten to 1D
for i, ax in enumerate(axs, start=1):
    ax.plot(x, np.sin(i*x))
    ax.set_title(f"sin({i}x)")
fig.suptitle("Unified access to Axes via ravel()")
fig.tight_layout()
plt.show()
