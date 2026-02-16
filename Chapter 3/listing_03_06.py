from pathlib import Path

Path("data/processed").mkdir(parents=True, exist_ok=True)
orders.to_parquet("data/processed/orders.parquet", index=False)
products.to_parquet("data/processed/products.parquet", index=False)

orders_round = pd.read_parquet("data/processed/orders.parquet")
assert orders_round.equals(orders), "Data changed during write/read  -  check types/categories"

#If strict equality is too harsh (e.g., category order differences):
assert set(orders_round.columns) == set(orders.columns)
assert len(orders_round) == len(orders)
