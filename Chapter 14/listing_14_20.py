import os
import random
import numpy as np
import pandas as pd

# For reproducible parallel steps, set thread limits early (before heavy numeric imports in real projects)
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# Ensure deterministic category order (important after merges/filters)
cats = sorted(df["category"].dropna().astype(str).unique())
df["category"] = (
    df["category"]
    .astype("string")
    .astype(pd.CategoricalDtype(categories=cats, ordered=True))
)

# Ensure time column is a proper datetime before sorting
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Stable sort before plotting
df = df.sort_values(["category", "date"], kind="mergesort").reset_index(drop=True)
