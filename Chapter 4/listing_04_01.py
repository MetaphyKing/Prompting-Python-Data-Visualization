import matplotlib.pyplot as plt

# create the canvas and the plotting area
fig, ax = plt.subplots(figsize=(7, 4), dpi=100)

# draw the data
ax.plot([0, 1, 2, 3], [1, 2, 1, 3], marker="o")

# basic styling
ax.set_title("First meaningful plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True, alpha=0.3)

# finalize
plt.tight_layout()
plt.show()

