import seaborn as sns
import pandas as pd
import numpy as np

penguins = sns.load_dataset("penguins").dropna()

# Matrix: rows = observations, columns = numeric features
X = penguins[["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]]

# Standardize columns (important for distances)
g = sns.clustermap(
    X,
    z_score=1,                 # 1 = columns, 0 = rows
    cmap="vlag", center=0,
    figsize=(8, 8),
    cbar_kws={"label": "z-score"},
    method="average",          # linkage method
    metric="euclidean"         # distance metric
)
g.fig.suptitle("Clustermap: standardized penguin features", y=1.02)


species_palette = dict(zip(penguins["species"].unique(), sns.color_palette(n_colors=3)))
island_palette  = dict(zip(penguins["island"].unique(),  sns.color_palette(n_colors=3)))

row_colors = pd.DataFrame({
    "species": penguins["species"].map(species_palette),
    "island":  penguins["island"].map(island_palette)
})

g = sns.clustermap(
    X,
    z_score=1,
    row_colors=row_colors,
    method="average", metric="euclidean",
    cmap="vlag", center=0, figsize=(9, 9),
    cbar_kws={"label": "z-score"}
)


sns.clustermap(
    X,
    z_score=1,
    row_cluster=True,
    col_cluster=False,   # cluster rows only, keep column order fixed
    cmap="vlag", center=0
)

corr = X.corr(method="spearman")
sns.clustermap(
    corr,
    cmap="vlag", center=0, vmin=-1, vmax=1,
    method="average", metric="euclidean",
    annot=True, fmt=".2f"
).fig.suptitle("Clustermap of correlation matrix (Spearman)", y=1.02)



from scipy.cluster.hierarchy import fcluster

g = sns.clustermap(X, z_score=1, method="average", metric="euclidean")
Z = g.dendrogram_row.linkage
labels = fcluster(Z, t=4, criterion="maxclust")  # 4 clusters

