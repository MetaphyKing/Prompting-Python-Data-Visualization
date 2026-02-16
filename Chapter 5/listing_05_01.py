import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 60
x = np.linspace(0, 2*np.pi, n)
df = pd.DataFrame({
    "A": np.sin(x) + 0.15*rng.standard_normal(n),
    "B": np.cos(x) + 0.15*rng.standard_normal(n),
    "C": 0.5*np.sin(2*x - 0.5) + 0.1*rng.standard_normal(n),
}, index=pd.Index(x, name="x"))
