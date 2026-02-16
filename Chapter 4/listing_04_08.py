import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7, 4), dpi=110, constrained_layout=True)

# data and graphics
x = [0, 1, 2, 3]
y = [1, 2, 1, 3]
ax.plot(x, y, marker="o", label="Observation")

# titles and labels
fig.suptitle("Figure-level title")      # applies to the whole Figure
ax.set_title("Axes plotting area")      # applies to a specific Axes
ax.set_xlabel("X, units")
ax.set_ylabel("Y, units")

# styling
ax.grid(True, alpha=0.3)
ax.legend()
plt.show()
