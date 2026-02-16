import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(4.5, 3.0))
ax.plot(x, y, label=r"$\sin(x)$")
ax.set_xlabel("x, radians")
ax.set_ylabel("amplitude")
ax.legend()

common = dict(bbox_inches="tight", pad_inches=0.02)

# PDF (vector, print)
plt.savefig("ch08_fig_02_sine.pdf", **common, metadata={"Title": "Sine", "Author": "Aleksei"})

# SVG (vector, DOM-editable)
plt.savefig("ch08_fig_02_sine.svg", **common)

# PNG (raster, presentations/web)
plt.savefig("ch08_fig_02_sine.png", dpi=300, **common)

plt.close(fig)  # free memory in batch rendering

import matplotlib as mpl
mpl.rcParams.update({
    "pdf.fonttype": 42,  # TrueType
    "ps.fonttype": 42,
})


sc = ax.scatter(x, y, s=2, rasterized=True)




import matplotlib as mpl
mpl.rcParams["svg.fonttype"] = "none"


plt.savefig("figure.png", dpi=300, bbox_inches="tight", pad_inches=0.02)



plt.savefig("figure_transparent.png", dpi=300, transparent=True)