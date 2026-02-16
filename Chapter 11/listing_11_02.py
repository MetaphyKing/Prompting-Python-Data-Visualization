import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = sns.load_dataset("penguins").dropna()
num_cols = df.select_dtypes(include="number")

corr = num_cols.corr(method="pearson")

ax = sns.heatmap(
    corr,
    annot=True,            # annotate cells
    fmt=".2f",             # numeric format
    cmap="vlag",           # diverging palette
    center=0,              # centered at zero
    vmin=-1, vmax=1,       # fixed bounds for comparability
    linewidths=.5,         # thin grid lines
    cbar_kws={"shrink": .8}
)
ax.set_title("Correlations among numeric features (Pearson)")
plt.tight_layout()
plt.show()


corr = num_cols.corr(method="spearman")
mask = np.triu(np.ones_like(corr, dtype=bool))

ax = sns.heatmap(
    corr, mask=mask,
    annot=True, fmt=".2f",
    cmap="vlag", center=0, vmin=-1, vmax=1,
    cbar_kws={"label": "ρ (Spearman)"}
)
ax.set_title("Correlations (Spearman), lower triangle only")
plt.tight_layout()
plt.show()



pivot = df.pivot_table(
    index="species", columns="island", values="bill_length_mm", aggfunc="mean"
)

# z-scores by row: subtract mean and divide by std for each row
pivot_z = (pivot - pivot.mean(axis=1).values[:, None]) / pivot.std(axis=1).values[:, None]

sns.heatmap(
    pivot_z, cmap="vlag", center=0, linewidths=.5,
    cbar_kws={"label": "z-score (by row)"}
).set_title("Mean bill length by island (standardized by species)")
plt.tight_layout()
plt.show()
