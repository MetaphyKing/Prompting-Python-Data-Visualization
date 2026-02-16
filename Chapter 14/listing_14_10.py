import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logging.info("Starting monthly aggregation")

monthly = (
    df.set_index("date").resample("M").agg({"sales_a": "sum", "sales_b": "sum"})
    .rename_axis("month").reset_index()
)

logging.info("Done: %s rows", len(monthly))
logging.info("Missing values: %s", monthly.isna().sum().to_dict())
