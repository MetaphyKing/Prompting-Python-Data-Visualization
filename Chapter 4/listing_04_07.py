import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
t = np.linspace(0, 24, 97)  # every 15 minutes
base = 50 + 10*np.sin(2*np.pi*t/24)
noise = rng.normal(0, 2, size=t.size)
series_a = base + noise
series_b = base*0.9 + rng.normal(0, 2.5, size=t.size)

fig, ax = plt.subplots(figsize=(8, 4.5), dpi=110)
ax.plot(t, series_a, marker="", label="Line A")
ax.plot(t, series_b, linestyle="--", label="Line B")

ax.set_title("Daily profile of the metric")
ax.set_xlabel("Hours")
ax.set_ylabel("Units")
ax.grid(True, alpha=0.3)
ax.legend(loc="best")

# mark the maximum of line A
idx_max = np.argmax(series_a)
ax.annotate("Peak",
            xy=(t[idx_max], series_a[idx_max]),
            xytext=(t[idx_max]+1, series_a[idx_max]+5),
            arrowprops=dict(arrowstyle="->"))

plt.tight_layout()
fig.savefig("daily_profile.svg", bbox_inches="tight")
plt.show()
