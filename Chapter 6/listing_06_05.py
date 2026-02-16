fig, axs = plt.subplots(
    2, 3, figsize=(10, 5),
    gridspec_kw={"width_ratios": [2, 1, 1], "height_ratios": [1, 1]}
)
for i, ax in enumerate(axs.ravel(), start=1):
    ax.plot(x, np.sin(i*x/2))
    ax.set_title(f"Panel {i}")
fig.suptitle("Controlling column widths with gridspec_kw")
fig.tight_layout()
plt.show()
