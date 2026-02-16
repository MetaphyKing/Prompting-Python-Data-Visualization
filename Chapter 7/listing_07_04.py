fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(s.index, s.values, linewidth=1.5)

# Shade weekends
for d in pd.date_range(s.index.min(), s.index.max(), freq="D"):
    if d.weekday() >= 5:  # 5=Saturday, 6=Sunday
        ax.axvspan(d, d + pd.Timedelta(days=1), alpha=0.06)

# Annotate event
event_day = pd.Timestamp("2023-05-15")
ax.axvline(event_day, color="tab:red", linewidth=1)
ax.annotate("Event", xy=(event_day, s.loc[event_day]),
            xytext=(10, 20), textcoords="offset points",
            arrowprops=dict(arrowstyle="->", alpha=0.6))

ax.grid(True, alpha=0.2)
