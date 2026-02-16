import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sample = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=5, freq="D"),
    "sales_a": [10, 12, None, 15, 20],
    "sales_b": [8, 11, 13, float("inf"), 18],
})

sample["sales_b"].replace([float("inf")], pd.NA, inplace=True)

sns.lineplot(data=sample, x="date", y="sales_a", label="A")
sns.lineplot(data=sample, x="date", y="sales_b", label="B")
plt.tight_layout()
plt.show()
