# production_style.py
import matplotlib as mpl
import matplotlib.pyplot as plt

def use_production_style(
    base_font="DejaVu Sans",
    font_size=10,
    line_width=1.5,
    grid_alpha=0.25,
    legend_frame=False,
):
    mpl.rcParams.update({
        # Geometry and quality
        "figure.dpi": 100,                  
        "savefig.dpi": 300,                 
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,

        # Typography
        "font.family": base_font,
        "font.size": font_size,
        "axes.titlesize": font_size + 2,
        "axes.labelsize": font_size,
        "xtick.labelsize": font_size - 1,
        "ytick.labelsize": font_size - 1,
        "legend.fontsize": font_size - 1,

        # Lines and markers
        "lines.linewidth": line_width,
        "lines.markersize": 5,

        # Grid and axes
        "axes.grid": True,
        "grid.linewidth": 0.8,
        "grid.alpha": grid_alpha,
        "axes.spines.top": False,
        "axes.spines.right": False,

        # Legend
        "legend.frameon": legend_frame,
        "legend.handlelength": 2.0,

        # Font export
        "pdf.fonttype": 42,   # text remains text (TrueType)
        "ps.fonttype": 42,
        "svg.fonttype": "none",  
    })

    # Color-blind–safe sequence
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=[
        "#0072B2", "#D55E00", "#009E73", "#CC79A7",
        "#F0E442", "#56B4E9", "#E69F00", "#000000"
    ])

if __name__ == "__main__":
    use_production_style()
    import numpy as np
    x = np.linspace(0, 2*np.pi, 200)
    fig, ax = plt.subplots(figsize=(4.5, 3.0))
    ax.plot(x, np.sin(x), label="sin(x)")
    ax.plot(x, np.cos(x), "--", label="cos(x)")
    ax.set_xlabel("x, radians")
    ax.set_ylabel("value")
    ax.set_title("Sine and Cosine")
    ax.legend(ncols=2)
    plt.show()
