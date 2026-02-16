plt.figure()
ax = orders.plot(kind="hexbin", x="unit_price", y="quantity", gridsize=30, bins="log", sharex=False)
plt.title("Price vs Quantity (hexbin, log density)")
plt.xlabel("unit_price"); plt.ylabel("quantity")



num_cols = ["quantity","unit_price","discount","gross","net"]
corr = orders[num_cols].corr(numeric_only=True, method="pearson")
print(corr.round(3))

plt.figure()
plt.imshow(corr, vmin=-1, vmax=1)
plt.colorbar(label="corr")
plt.xticks(range(len(num_cols)), num_cols, rotation=45, ha="right")
plt.yticks(range(len(num_cols)), num_cols)
plt.title("Correlations (Pearson)")
plt.tight_layout()
