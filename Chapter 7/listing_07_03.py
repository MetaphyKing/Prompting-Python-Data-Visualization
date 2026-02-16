
weekly = s.resample("W").mean()
roll = s.rolling(window=14, min_periods=7).mean()  # 14-day average

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(s.index, s.values, alpha=0.35, label="Daily")
ax.plot(weekly.index, weekly.values, linewidth=2, label="Weekly (mean)")
ax.plot(roll.index, roll.values, linewidth=2, linestyle="--", label="14d MA")
ax.legend()
ax.grid(True, alpha=0.2)
