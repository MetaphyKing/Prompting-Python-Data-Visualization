from matplotlib.gridspec import GridSpecFromSubplotSpec
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(7)
A = rng.normal(size=(3, 200)).cumsum(axis=1)
t = np.arange(A.shape[1])

fig = plt.figure(figsize=(10, 6), constrained_layout=False)

# Outer grid: 2 rows (top taller), 1 column
outer = gridspec.GridSpec(
    2, 1, figure=fig,
    height_ratios=[2.2, 1.0],
    hspace=0.35
)

ax_top = fig.add_subplot(outer[0])  # hero

# Inner grid in the bottom row: 1×3
inner = GridSpecFromSubplotSpec(1, 3, subplot_spec=outer[1], wspace=0.35)

ax_b1 = fig.add_subplot(inner[0, 0])
ax_b2 = fig.add_subplot(inner[0, 1])
ax_b3 = fig.add_subplot(inner[0, 2])

for i, lbl in enumerate(["X", "Y", "Z"]):
    ax_top.plot(t, A[i], label=lbl)
ax_top.set_title("Comparison of three series (hero)")
ax_top.grid(True, alpha=0.3); ax_top.legend()

ax_b1.plot(t, A[0]-A[1]); ax_b1.set_title("X−Y"); ax_b1.grid(True, alpha=0.25)
ax_b2.plot(t, A[1]-A[2]); ax_b2.set_title("Y−Z"); ax_b2.grid(True, alpha=0.25)
ax_b3.plot(t, A[0]-A[2]); ax_b3.set_title("X−Z"); ax_b3.grid(True, alpha=0.25)

fig.suptitle("Nested GridSpec for multi-level composition", y=0.98)
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
