# file: harness.py
HARNESS = r"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def __validate_and_save(path, dpi=150):
    fig = plt.gcf()
    axes = fig.get_axes()
    if not axes:
        raise RuntimeError("No axes on figure")
    ax = axes[0]
    if not ax.get_title():
        raise RuntimeError("Missing title")
    if not ax.get_xlabel() or not ax.get_ylabel():
        raise RuntimeError("Missing axis labels")
    fig.tight_layout()
    fig.savefig(path, dpi=dpi)
"""

def inject_harness(code: str) -> str:
    patched = code.replace("plt.savefig(", "__validate_and_save(")
    return HARNESS + "\n" + patched
