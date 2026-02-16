import matplotlib.pyplot as plt
fig, ax1 = plt.subplots(figsize=(7, 4))
ax2 = ax1.twinx()  # second y-axis

t = [1, 2, 3, 4]
temp = [18, 20, 23, 21]
rain = [5, 12, 8, 15]

l1 = ax1.plot(t, temp, color="tab:red", label="Temperature")[0]
l2 = ax2.bar(t, rain, alpha=0.3, label="Rainfall", color="tab:blue")

ax1.set_xlabel("Day")
ax1.set_ylabel("Temperature, °C", color="tab:red")
ax2.set_ylabel("Rainfall, mm", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:red")
ax2.tick_params(axis="y", labelcolor="tab:blue")

# combined legend
lines = [l1]
labels = [l1.get_label(), "Rainfall"]
ax1.legend(lines, labels, loc="upper left", frameon=False)

plt.tight_layout()
plt.show()
