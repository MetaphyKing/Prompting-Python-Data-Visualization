import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Add tip percentage and plot distributions by day
(
    tips
    .assign(tip_pct=lambda df: df["tip"] / df["total_bill"])
    .pipe(
        lambda df: sns.catplot(
            data=df,
            x="day", y="tip_pct", hue="sex",
            kind="violin", inner="quartile",
            height=4, aspect=1.2
        )
    )
)
plt.show()

# Average tip share by day and gender with bootstrap CI
summ = (
    tips
    .assign(tip_pct=lambda df: df["tip"] / df["total_bill"])
    .groupby(["day", "sex"], as_index=False)["tip_pct"]
    .agg(["mean"])
    .reset_index()
    .rename(columns={"mean": "tip_pct_mean"})
)

ax = sns.barplot(
    data=summ,
    x="day", y="tip_pct_mean", hue="sex",
)
ax.set_ylabel("Average tip share")
plt.show()



order = pd.CategoricalDtype(categories=["Thur", "Fri", "Sat", "Sun"], ordered=True)
tips_ord = tips.assign(day=tips["day"].astype(order))

sns.boxplot(data=tips_ord, x="day", y="total_bill", hue="smoker")
plt.show()


flights = sns.load_dataset("flights")  # already long: year, month, passengers

# Example of reshaping from wide to long and back
wide = flights.pivot(index="year", columns="month", values="passengers")
long = wide.reset_index().melt(id_vars="year", var_name="month", value_name="passengers")

sns.lineplot(data=long, x="year", y="passengers", hue="month")
plt.show()




tbl = pd.pivot_table(
    flights,
    index="year",
    columns="month",
    values="passengers",
    aggfunc="mean",
    fill_value=0
)
sns.heatmap(tbl)
plt.show()



flights_dt = (
    flights
    .assign(
        date=lambda df: pd.to_datetime(
            df["year"].astype(int).astype(str) + "-" + df["month"] + "-01"
        )
    )
    .set_index("date")
    .sort_index()
)

flights_ma = flights_dt.assign(
    passengers_ma=lambda df: df["passengers"].rolling(window=6, min_periods=1).mean()
)

sns.lineplot(data=flights_ma.reset_index(), x="date", y="passengers", label="monthly")
sns.lineplot(data=flights_ma.reset_index(), x="date", y="passengers_ma", label="6-month MA")
plt.show()




tips_summ = (
    tips
    .assign(tip_pct=lambda df: df["tip"] / df["total_bill"])
    .groupby(["day", "time", "sex"], as_index=False)["tip_pct"]
    .mean()
    .rename(columns={"tip_pct": "tip_pct_mean"})
)

g = sns.catplot(
    data=tips_summ,
    x="day", y="tip_pct_mean",
    hue="sex", col="time",
    kind="bar", height=3.2, aspect=1.2
)
g.set_axis_labels("Day", "Average tip share")
g.set_titles("Time = {col_name}")
g.add_legend()
plt.show()



sns.set_theme()
ax = sns.lineplot(data=flights, x="year", y="passengers", ci=None)
ax.figure.set_size_inches(8, 4)
ax.figure.savefig("flights_trend.png", dpi=200, bbox_inches="tight")

