
def mm_to_in(mm: float) -> float:
    return mm / 25.4

def size_for_width(mm: float, aspect: float) -> tuple[float, float]:
    w_in = mm_to_in(mm)
    h_in = w_in * aspect
    return (w_in, h_in)

# Example: figure width 90 mm, aspect ratio 0.62
figsize = size_for_width(90, aspect=0.62)  # -> (~3.54", ~2.20")



import matplotlib as mpl
mpl.rcParams.update({
    "figure.dpi": 100,    # lightweight preview
    "savefig.dpi": 300,   # production export
})




