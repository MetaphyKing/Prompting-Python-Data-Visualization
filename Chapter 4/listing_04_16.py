from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, ax = plt.subplots(figsize=(7, 4))
x = np.linspace(0, 10, 300)
y = np.sin(x) + 0.2*np.sin(10*x)
ax.plot(x, y)
ax.set_title("Signal with local zoom")
ax.grid(True, alpha=0.3)

# inset axes in the upper-right corner of the current Axes
ax_ins = inset_axes(ax, width="40%", height="40%", loc="upper right")
mask = (x > 3) & (x < 5)
ax_ins.plot(x[mask], y[mask])
ax_ins.set_xticks([])
ax_ins.set_yticks([])
ax_ins.grid(True, alpha=0.3)
plt.show()
