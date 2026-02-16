from __future__ import annotations

from typing import Iterable, Optional
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_monthly_totals(
    df: pd.DataFrame,
    date_col: str,
    value_cols: Iterable[str],
    title: str,
    subtitle: Optional[str] = None,
    ax: Optional[plt.Axes] = None,
) -> plt.Axes:
    """
    Plot monthly totals for selected columns.
    Expectations: df[date_col] must be datetime64; value_cols must be numeric.
    Returns Axes for further composition.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(10, 5))

    value_cols = list(value_cols)

    monthly = (
        df.set_index(date_col)
          .resample("M")
          .agg({c: "sum" for c in value_cols})
          .rename_axis("month")
          .reset_index()
    )

    # Seaborn prefers long-form data + a single call with hue
    monthly_long = monthly.melt(
        id_vars=["month"],
        value_vars=value_cols,
        var_name="metric",
        value_name="total",
    )

    sns.lineplot(
        data=monthly_long,
        x="month",
        y="total",
        hue="metric",
        ax=ax,
        linewidth=2,
    )

    ax.set_title(f"{title}\n{subtitle}" if subtitle else title)
    ax.set_xlabel("Month")
    ax.set_ylabel("Total")

    ax.grid(True, alpha=0.25)
    ax.legend(title="Metric", loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0)

    plt.tight_layout()
    return ax
