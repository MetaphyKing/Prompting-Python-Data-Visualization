import matplotlib as mpl, matplotlib.pyplot as plt

plt.style.use("reporting")  # or path to file
unknown = [k for k in mpl.rcParams if mpl.rcParams[k] is None]
print("No suspicious keys" if not unknown else f"Check these: {unknown}")

fig, ax = plt.subplots()
ax.plot([0,1,2],[0,1,0]); ax.set_title("Style check", loc="left")
plt.show()


from pathlib import Path
def use_style_if_exists(path):
    p = Path(path)
    if p.exists():
        import matplotlib.pyplot as plt
        plt.style.use(str(p))
        return True
    return False

use_style_if_exists("reporting.mplstyle")
