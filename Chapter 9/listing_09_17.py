import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example: raw daily events
events = pd.DataFrame({
    "timestamp": pd.date_range("2024-01-01", periods=500, freq="D"),
    "value": pd.Series(range(500)).rolling(7, min_periods=1).mean()
})

# Convert to datetime and resample weekly
events["timestamp"] = pd.to_datetime(events["timestamp"])
weekly = (
    events
    .resample("W", on="timestamp")["value"]
    .mean()
    .reset_index()
)

sns.lineplot(data=weekly, x="timestamp", y="value")
plt.xlabel("Week")
plt.ylabel("Mean value")
plt.show()
