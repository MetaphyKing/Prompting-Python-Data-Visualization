orders["price"] = pd.to_numeric(orders["price"], errors="coerce")
orders["discount"] = pd.to_numeric(orders["discount"], errors="coerce")
orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce", utc=True)

orders["region"] = (orders["region"]
                    .astype("string")
                    .str.strip()
                    .str.upper()
                    .replace({"EU": "EMEA", "EME A": "EMEA"}))
orders["region"] = orders["region"].astype("category")

orders["customer_id"] = orders["customer_id"].astype("string")
orders["product_id"] = orders["product_id"].astype("string")
