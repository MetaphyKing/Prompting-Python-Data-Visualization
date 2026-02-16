def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9

x = np.linspace(0, 24, 241)
temp_c = 10 + 8*np.sin(2*np.pi*(x-6)/24)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, temp_c, lw=2, label="Temperature (°C)")
ax.set_xlabel("Hour")
ax.set_ylabel("°C")
ax.grid(True, alpha=0.25)

sec = ax.secondary_yaxis("right", functions=(c_to_f, f_to_c))
sec.set_ylabel("°F")
plt.tight_layout(); plt.show()


days = np.arange(30)
price = 100 + np.cumsum(np.random.normal(0, 1.2, size=len(days)))
volume = np.random.randint(100, 600, size=len(days))

fig, ax1 = plt.subplots(figsize=(8, 4))
ax2 = ax1.twinx()

ax1.plot(days, price, lw=2, label="Price")
ax2.bar(days, volume, alpha=0.25, label="Volume", width=0.8)

ax1.set_xlabel("Day")
ax1.set_ylabel("Price ($)")
ax2.set_ylabel("Volume (k units)")
ax1.grid(True, alpha=0.25)

lines = ax1.get_lines() + ax2.containers
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left")

plt.tight_layout(); plt.show()

x = np.linspace(-3, 3, 401)
y = x**3 - 3*x

fig, ax = plt.subplots(figsize=(6.6, 4))
ax.plot(x, y, lw=2)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))
ax.tick_params(direction="inout", length=6, width=1)
ax.grid(True, alpha=0.2)
plt.tight_layout(); plt.show()

