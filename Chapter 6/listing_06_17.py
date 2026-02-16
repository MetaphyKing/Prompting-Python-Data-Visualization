import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)

with mpl.rc_context({
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
}):
    fig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True)
    axs[0].plot(x, np.sin(x)); axs[0].set_title("Sine")
    axs[1].plot(x, np.cos(x)); axs[1].set_title("Cosine")

    fig.suptitle("Unified typography for the figure", y=0.98)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()
