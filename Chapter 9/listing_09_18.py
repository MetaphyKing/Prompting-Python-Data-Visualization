
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

(
    tips
    .query("total_bill > 0 and tip > 0")                            # filtering
    .assign(tip_rate=lambda d: d["tip"] / d["total_bill"])          # new metric
    .astype({"day": "category", "time": "category", "sex": "category"})
    .pipe(lambda d: d.sort_values("day"))                           # stable order
    .pipe(lambda d: sns.relplot(
        data=d,
        x="total_bill", y="tip_rate",
        hue="day", style="time",
        kind="scatter", height=3.2, aspect=1.35
    ))
)
plt.xlabel("Total bill (USD)")
plt.ylabel("Tip rate")
plt.show()
