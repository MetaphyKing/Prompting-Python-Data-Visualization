import matplotlib as mpl
mpl.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "axes.unicode_minus": False,
})



import matplotlib as mpl
mpl.rcParams.update({
    "pgf.texsystem": "xelatex",
    "pgf.rcfonts": False,
    "font.family": "serif",
    "pgf.preamble": r"""
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}
\setmonofont{TeX Gyre Cursor}
""",
})

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 200)
y = np.exp(-5*x) * np.cos(8*np.pi*x)

fig, ax = plt.subplots(figsize=(3.25, 2.0))  # journal column width
ax.plot(x, y, label=r"$e^{-5x}\cos(8\pi x)$")
ax.set_xlabel(r"time $t$ (s)")
ax.set_ylabel(r"response $y$")
ax.legend()

plt.savefig("ch08_fig_03_response.pgf", bbox_inches="tight", pad_inches=0.02)
plt.close(fig)


def pt_to_in(pt: float) -> float:
    return pt / 72.27

def mm_to_in(mm: float) -> float:
    return mm / 25.4

col_pt = 246
fig_w = pt_to_in(col_pt)
fig_h = fig_w * 0.62
figsize = (fig_w, fig_h)




def export_figure(fig, basename: str, for_print=True, for_web=True, for_edit=True):
    common = dict(bbox_inches="tight", pad_inches=0.02)

    if for_print:
        fig.savefig(f"{basename}.pdf", metadata={"Title": basename}, **common)

    if for_web:
        fig.savefig(f"{basename}.png", dpi=300, **common)

    if for_edit:
        import matplotlib as mpl
        old = mpl.rcParams.get("svg.fonttype", None)
        mpl.rcParams["svg.fonttype"] = "none"
        try:
            fig.savefig(f"{basename}.svg", **common)
        finally:
            if old is not None:
                mpl.rcParams["svg.fonttype"] = old


