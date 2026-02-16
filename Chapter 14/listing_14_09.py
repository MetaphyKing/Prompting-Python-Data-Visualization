import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(10, 5))

sns.lineplot(data=monthly_df, x="month", y="sales_a", ax=ax, label="A")

# In interactive backends, a short pause forces a draw so you can visually confirm this layer.
# Skip this in non-interactive/CI runs.
plt.pause(0.01)

sns.lineplot(data=monthly_df, x="month", y="sales_b", ax=ax, label="B")
ax.grid(True, alpha=0.3)
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0))

plt.tight_layout()
plt.show()
