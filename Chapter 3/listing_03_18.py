import pandas as pd
import numpy as np
from pathlib import Path

processed = Path("data/processed")
orders = pd.read_parquet(processed / "orders_cleaned.parquet")   # from Part 2
products = pd.read_parquet(processed / "products.parquet")       # product reference 
