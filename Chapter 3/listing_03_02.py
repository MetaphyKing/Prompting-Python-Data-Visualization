products = pd.read_excel(
    "data/raw/products.xlsx",
    sheet_name="sku",
    engine="openpyxl",
    usecols=["product_id", "name", "category", "cost"],
    dtype={"product_id": "string", "name": "string", "category": "string", "cost": "float64"}
)
products["category"] = products["category"].str.strip().str.title().astype("category")
print(products.head(3))


#If the file is large or contains many sheets, use a “scanner”:

with pd.ExcelFile("data/raw/products.xlsx", engine="openpyxl") as xf:
    print("Sheets:", xf.sheet_names)
    prod = xf.parse("sku", usecols="A:D")



