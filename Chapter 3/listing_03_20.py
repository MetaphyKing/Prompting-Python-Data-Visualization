fy_shift = 3
orders["fiscal_year"] = (orders["date"].dt.year +
                         ((orders["date"].dt.month - 1 - fy_shift) // 12))
orders["fiscal_quarter"] = ((orders["date"].dt.month - 1 - fy_shift) % 12) // 3 + 1
