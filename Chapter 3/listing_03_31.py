# Gross and net revenue
gross = q.astype(np.float64) * p
net = gross * (1.0 - d)

orders["gross"] = gross
orders["net"] = net

# Discount bands: Low, Mid, High
conds = [d <= 0.10, (d > 0.10) & (d <= 0.25), d > 0.25]
labels = ["Low", "Mid", "High"]
disc_band = np.select(conds, labels, default="Unknown")
orders["discount_band"] = pd.Categorical(disc_band, categories=labels+["Unknown"], ordered=True)

# Replace zero prices with median
median_price = np.nanmedian(p)
p = np.where(p <= 0, median_price, p)

mask_valid = (q >= 0) & (p >= 0) & (d >= 0) & (d <= 0.95)
net_safe = np.where(mask_valid, net, np.nan)



region = orders["region"].astype("string")
regions, reg_codes = np.unique(region, return_inverse=True)

coeff_map = {r: 1.00 for r in regions}
coeff_map.update({"EMEA": 1.02, "AMER": 0.98})

coeff_arr = np.array([coeff_map[r] for r in regions])
adj = coeff_arr[reg_codes]

net_adjusted = net * adj
orders["net_adjusted"] = net_adjusted





prod = orders["product_id"].astype("string").to_numpy()
uniq_prod, prod_codes = np.unique(prod, return_inverse=True)

net_by_prod = np.bincount(prod_codes, weights=net)
by_prod_np = pd.DataFrame({"product_id": uniq_prod, "net_sum": net_by_prod})



month = orders["date"].dt.to_period("M").astype(str).to_numpy()

uniq_reg, reg_codes = np.unique(region, return_inverse=True)
uniq_mon, mon_codes = np.unique(month, return_inverse=True)

K1, K2 = len(uniq_reg), len(uniq_mon)
flat = reg_codes * K2 + mon_codes

net_by_pair = np.bincount(flat, weights=net, minlength=K1*K2).reshape(K1, K2)
heat_np = pd.DataFrame(net_by_pair, index=uniq_reg, columns=uniq_mon)

