from pathlib import Path
reports = Path("reports"); reports.mkdir(exist_ok=True)

by_region.to_parquet(reports / "by_region.parquet", index=False)
monthly_region.to_parquet(reports / "monthly_region.parquet", index=False)
share_tbl.to_parquet(reports / "share_by_month_region_category.parquet", index=False)
pareto.to_parquet(reports / "pareto_region_product.parquet", index=False)
size_region.to_csv(reports / "size_region_structure.csv")  # CSV convenient for matrix use

