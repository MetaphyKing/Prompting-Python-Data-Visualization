import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
m = df.set_index("date").resample("M").sum().reset_index()
plt.figure(figsize=(10,5))
sns.lineplot(x="date", y="a", data=m)
sns.lineplot(x="date", y="b", data=m)
plt.title("Sales")
plt.legend(["A","B"])
plt.grid()
plt.show()



apply_house_style()
fig, ax = new_figure()

# 1) Data preparation (keep resampling/grouping OUT of plotting functions)
monthly = monthly_sum(df, "date", ["a", "b"])

monthly_long = monthly.melt(
    id_vars=["month"],
    value_vars=["a", "b"],
    var_name="metric",
    value_name="total",
)

# 2) Plotting (pure rendering step)
sns.lineplot(
    data=monthly_long,
    x="month",
    y="total",
    hue="metric",
    ax=ax,
    linewidth=2,
)

ax.set_title("Monthly Sales")
format_time_axis(ax, month_interval=2)
ax.set_xlabel("Month")
ax.set_ylabel("Total")
ax.legend(title="Metric", loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0)
plt.show()
