import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")
subset_ids = fmri["subject"].unique()[:4]
fmri_small = fmri[fmri["subject"].isin(subset_ids)]

g = sns.relplot(
    data=fmri_small,
    x="timepoint", y="signal",
    hue="event", style="region",
    col="subject", col_wrap=2,
    kind="line",
    height=2.8, aspect=1.3
)
g.set_axis_labels("Time (scan)", "Signal (a.u.)")
g.add_legend()
plt.show()
