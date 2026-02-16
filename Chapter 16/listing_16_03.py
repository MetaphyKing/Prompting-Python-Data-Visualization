# Minimal imports
import matplotlib.pyplot as plt

# Figure configured for PDF publication
fig, ax = plt.subplots(figsize=(6, 3.2), dpi=300)

ax.plot(df["date"], df["value"], linewidth=1.6, label="Metric")

if {"low", "high"}.issubset(df.columns):
    ax.fill_between(df["date"], df["low"], df["high"], alpha=0.25, label="Confidence Interval")

if "events" in df.columns:
    for d, e in zip(df["date"], df["events"]):
        if isinstance(e, str) and e:
            ax.axvline(d, linestyle="--", alpha=0.5)
            ax.annotate(e[:30], xy=(d, ax.get_ylim()[1]), xytext=(5, -10),
                        textcoords="offset points", rotation=30, va="top")

ax.set_title("Metric Trend Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.grid(True, alpha=0.3)

ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False)
plt.tight_layout()
