fig, axs = plt.subplots(1, 2, figsize=(9, 3), sharey=True)
axs[0].plot(x, np.sin(x)); axs[0].set_title("Square panel")
axs[0].set_box_aspect(1)

axs[1].plot(x, np.sin(2*x)); axs[1].set_title("Elongated panel")
axs[1].set_box_aspect(0.5)

for ax in axs:
    ax.grid(True, alpha=0.3)

fig.suptitle("Controlling panel aspect ratios")
fig.tight_layout()
plt.show()
