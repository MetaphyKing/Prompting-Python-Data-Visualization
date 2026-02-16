import os, matplotlib as mpl
user_style_dir = os.path.join(mpl.get_configdir(), "stylelib")
os.makedirs(user_style_dir, exist_ok=True)
# Copy reporting.mplstyle and slides.mplstyle here
mpl.style.reload_library()  # refresh available styles


import matplotlib.pyplot as plt

plt.style.use(["default", "reporting"])  # "default" + our custom "reporting"


# brand_overrides.mplstyle  -  brand-specific tweaks
axes.titlesize: 14
axes.titleweight: bold
axes.labelsize: 11
axes.prop_cycle: cycler('color', ['#003f5c', '#bc5090', '#ffa600', '#58508d', '#2f4b7c'])
legend.framealpha: 0.92


