import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 24, 200)  # hours
temp_c = 10 + 8*np.sin((x-6)/24*2*np.pi)

def c_to_f(c): return c*9/5 + 32
def f_to_c(f): return (f-32)*5/9

fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, temp_c)
ax.set_xlabel("Time, h")
ax.set_ylabel("Temperature, °C")

sec = ax.secondary_yaxis('right', functions=(c_to_f, f_to_c))
sec.set_ylabel("Temperature, °F")

ax.set_title("Secondary axis instead of twinx")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()



import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 24, 200)  # hours
temp_c = 10 + 8*np.sin((x-6)/24*2*np.pi)

def c_to_f(c): return c*9/5 + 32
def f_to_c(f): return (f-32)*5/9

fig, ax = plt.subplots(figsize=(7, 3))
ax.plot(x, temp_c)
ax.set_xlabel("Time, h")
ax.set_ylabel("Temperature, °C")

sec = ax.secondary_yaxis('right', functions=(c_to_f, f_to_c))
sec.set_ylabel("Temperature, °F")

ax.set_title("Secondary axis instead of twinx")
ax.grid(True, alpha=0.3)
fig.tight_layout()
plt.show()
