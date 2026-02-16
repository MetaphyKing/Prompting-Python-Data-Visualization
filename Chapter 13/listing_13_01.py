import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
order = ["Thur", "Fri", "Sat", "Sun"]

plt.figure(figsize=(9, 5))
ax = sns.barplot(
    data=tips,
    x="day",
    y="tip",
    order=order,
    errorbar=("ci", 95)
)
ax.set_title("Средний размер чаевых по дням недели")
ax.set_xlabel("День недели")
ax.set_ylabel("Чаевые, $")
ax.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("figures/tips_bar_ci.png", dpi=120)
plt.show()
