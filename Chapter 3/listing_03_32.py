

bins = np.geomspace(max(1e-2, np.nanmin(net[net>0])), np.nanmax(net), 30)
counts, edges = np.histogram(net[np.isfinite(net) & (net > 0)], bins=bins)

size_bins = np.array([0, 50, 200, 1000, np.inf])
idx = np.digitize(net, size_bins, right=False) - 1
labels = np.array(["Very Small", "Small", "Medium", "Large"])
order_size = np.where((idx >= 0) & (idx < len(labels)), labels[idx], "Unknown")
orders["order_size"] = pd.Categorical(order_size, categories=list(labels)+["Unknown"], ordered=True)


from numpy.lib.stride_tricks import sliding_window_view

daily = (orders.set_index("date").sort_index()
         .resample("D").agg(net_total=("net","sum")))
x = daily["net_total"].to_numpy(dtype=np.float64)

# 7-day moving average via convolution
w = np.ones(7) / 7
ma7 = np.convolve(x, w, mode="same")

# Arbitrary function with sliding windows
windows = sliding_window_view(x, 7)
centered_ma7 = np.empty_like(x); centered_ma7[:] = np.nan
centered_ma7[3:-3] = windows.mean(axis=1)



N = 5
idx_top = np.argpartition(-net, N-1)[:N]
idx_top = idx_top[np.argsort(-net[idx_top])]
top5 = orders.iloc[idx_top][["product_id", "region", "net"]]



prod = orders["product_id"].astype("string").to_numpy()
uniq_prod, prod_codes = np.unique(prod, return_inverse=True)

# Suppose cost_arr aligns with uniq_prod
cost_per_row = np.take(cost_arr, prod_codes)
orders["profit"] = net - cost_per_row * q




import time
t0 = time.perf_counter()
# NumPy code
elapsed = time.perf_counter() - t0
print(f"Elapsed: {elapsed:.4f} s")



m = np.memmap("data/interim/bigarr.dat",
              dtype=np.float64, mode="w+",
              shape=(10_000_000,))
m[:1_000_000] = np.linspace(0, 1, 1_000_000)
m.flush()



reg = orders["region"].astype("string").to_numpy()
uniq_reg, reg_codes = np.unique(reg, return_inverse=True)
K = len(uniq_reg)

x = p  # unit price

sum_by_reg = np.bincount(reg_codes, weights=x, minlength=K)
cnt_by_reg = np.bincount(reg_codes, minlength=K)
mean_by_reg = sum_by_reg / np.maximum(cnt_by_reg, 1)

sum2_by_reg = np.bincount(reg_codes, weights=x*x, minlength=K)
var_by_reg = sum2_by_reg / np.maximum(cnt_by_reg, 1) - mean_by_reg**2
std_by_reg = np.sqrt(np.clip(var_by_reg, 0, None))

mu = mean_by_reg[reg_codes]
sd = np.where(std_by_reg[reg_codes] > 0, std_by_reg[reg_codes], np.nan)

z_price = (x - mu) / sd
orders["unit_price_z_by_region"] = z_price




rng = np.random.default_rng(42)
N = len(orders)
take = min(N, 100_000)
idx = rng.choice(N, size=take, replace=False)
sample = orders.iloc[idx]
