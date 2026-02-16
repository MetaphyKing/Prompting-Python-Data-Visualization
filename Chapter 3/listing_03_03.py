from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///data/interim/sales.db", future=True)

query = text("""
SELECT order_id, order_date, customer_id, region, product_id, quantity, price, discount
FROM orders
WHERE order_date BETWEEN :start AND :end
""")

orders_sql = pd.read_sql_query(
    query,
    con=engine,
    params={"start": "2024-10-01", "end": "2024-12-31"},
    parse_dates=["order_date"]
)
print(orders_sql.head(2))
