fig, axs = plt.subplots(2, 3, figsize=(10, 5), sharex=True, sharey=True)
for ax in axs.ravel():
    ax.plot(x, np.sin(x) + 0.2*np.random.randn(len(x)))
    ax.grid(True, alpha=0.25)

# Hide inner tick labels
for ax in axs[0, :]:
    ax.tick_params(labelbottom=False)
for ax in axs[:, 1:-1].ravel():
    ax.tick_params(labelleft=False)

fig.suptitle("Maintaining readability with fewer labels")
fig.tight_layout()
plt.show()
