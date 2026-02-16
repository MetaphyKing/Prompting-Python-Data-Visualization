import time
import requests
from tenacity import retry, stop_after_attempt, wait_exponential

API_URL = "https://example.com/api/orders"
HEADERS = {"Authorization": "Bearer <TOKEN>"}

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
def fetch_page(page: int, per_page: int = 500) -> dict:
    resp = requests.get(
        API_URL,
        headers=HEADERS,
        params={"page": page, "per_page": per_page},
        timeout=30
    )
    resp.raise_for_status()
    return resp.json()

all_items = []
page = 1
while True:
    payload = fetch_page(page)
    items = payload.get("items", [])
    if not items:
        break
    all_items.extend(items)
    if not payload.get("next_page"):
        break
    page += 1
    time.sleep(0.2)  # soft rate limit

orders_api = pd.json_normalize(all_items)
orders_api["order_date"] = pd.to_datetime(orders_api["order_date"], errors="coerce", utc=True)
orders_api["region"] = orders_api["region"].str.upper().astype("category")
