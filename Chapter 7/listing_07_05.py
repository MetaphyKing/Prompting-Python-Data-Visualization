# Example: "aware" UTC timestamps
utc_index = pd.date_range("2023-06-01", "2023-06-07", freq="H", tz="UTC")
s_utc = pd.Series(np.sin(np.linspace(0, 6*np.pi, len(utc_index))), index=utc_index)

# Convert to Athens (Europe/Athens)
ath_tz = ZoneInfo("Europe/Athens")
s_ath = s_utc.tz_convert(ath_tz)

fig, ax = plt.subplots(figsize=(9, 3.8))
ax.plot(s_ath.index, s_ath.values)

# IMPORTANT: For timezone-aware timestamps, pass the timezone explicitly to DateFormatter.
# Otherwise, Matplotlib may mis-handle DST transitions and shift labels by 1–2 hours.
ax.xaxis.set_major_locator(mdates.HourLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b %H:%M", tz=ath_tz))


ax.set_title("Hourly Series (Europe/Athens)")
ax.grid(True, alpha=0.2)
fig.autofmt_xdate()
fig.savefig("timeseries.png", dpi=200, bbox_inches="tight")
# or vector format for publications:
fig.savefig("timeseries.pdf", bbox_inches="tight")

