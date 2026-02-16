import pandas as pd
import seaborn as sns

penguins = sns.load_dataset("penguins").copy()

# Basic cleaning: remove rows with missing values in key fields
penguins = penguins.dropna(subset=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "species"])

# Explicitly set categorical type with fixed order
cat_order = pd.CategoricalDtype(categories=["Adelie", "Chinstrap", "Gentoo"], ordered=True)
penguins["species"] = penguins["species"].astype(cat_order)

# Rename columns for cleaner labels
penguins = penguins.rename(columns={"bill_length_mm": "Bill length (mm)", "bill_depth_mm": "Bill depth (mm)"})

wide_back = long.pivot(index="group", columns="metric", values="value").reset_index()