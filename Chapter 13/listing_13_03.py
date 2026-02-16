import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
n_days = 90
dates = pd.date_range("2025-01-01", periods=n_days, freq="D")
regions = np.array(["EMEA", "AMER", "APAC"])

df = pd.DataFrame({
    "date": np.repeat(dates, 60),
    "region": rng.choice(regions, size=n_days*60, p=[0.4, 0.35, 0.25])
})
df["latency_ms"] = rng.gamma(shape=5.0, scale=12.0, size=len(df)) + df["region"].map({"EMEA": 5, "AMER": 10, "APAC": 7})
df["throughput"] = rng.normal(loc=500, scale=80, size=len(df)) - 0.6*df["latency_ms"]

daily = df.groupby("date", as_index=False).agg(latency_ms=("latency_ms", "median"), throughput=("throughput", "mean"))

fig, axs = plt.subplots(2, 2, figsize=(12, 9))
(ax_t, ax_h), (ax_s, ax_b) = axs

ax_t.plot(daily["date"], daily["latency_ms"], lw=1.8)
ax_t.set_title("Медианная задержка по дням")
ax_t.set_xlabel("Дата")
ax_t.set_ylabel("Задержка, мс")
ax_t.grid(True, axis="y", linestyle="--", alpha=0.4)

ax_h.hist(df["latency_ms"], bins=30)
ax_h.set_title("Распределение задержек")
ax_h.set_xlabel("Задержка, мс")
ax_h.set_ylabel("Частота")
ax_h.grid(True, axis="y", linestyle="--", alpha=0.4)

for reg, g in df.groupby("region"):
    ax_s.scatter(g["latency_ms"], g["throughput"], s=12, alpha=0.6, label=reg)
ax_s.set_title("Пропускная способность vs задержка")
ax_s.set_xlabel("Задержка, мс")
ax_s.set_ylabel("Пропускная способность, ед.")
ax_s.legend(title="Регион")
ax_s.grid(True, linestyle="--", alpha=0.4)

data_box = [df.loc[df["region"] == r, "latency_ms"] for r in regions]
ax_b.boxplot(data_box, labels=regions, showmeans=True)
ax_b.set_title("Задержка по регионам")
ax_b.set_xlabel("Регион")
ax_b.set_ylabel("Задержка, мс")
ax_b.grid(True, axis="y", linestyle="--", alpha=0.4)

fig.suptitle("Панель мониторинга производительности", y=0.98, fontsize=14)
plt.tight_layout()
plt.savefig("figures/perf_dashboard.png", dpi=140)
plt.show()
