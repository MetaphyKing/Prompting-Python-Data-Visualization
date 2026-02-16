s_with_gaps = s.copy()
s_with_gaps.iloc[30:40] = np.nan   # artificial 10-day gap
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(s_with_gaps.index, s_with_gaps.values, label="With gaps")

# WARNING: Keep the raw series unchanged.
# Interpolation must be used ONLY for visualization (display), not for analysis.

interp = s_with_gaps.interpolate(limit_area="inside")
ax.plot(interp.index, interp.values, alpha=0.7, linestyle="--", label="Interpolated")

ax.legend()
ax.grid(True, alpha=0.2)


ax.plot(s.index[::7], s.values[::7], marker="o", linestyle="None")  # sparse points
# or
ax.step(s.index, s.values, where="post")
