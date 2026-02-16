from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@dataclass(frozen=True)
class PlotSpec:
    title: str
    subtitle: Optional[str]
    highlight_date: Optional[datetime]
    month_step: int = 2


def validate_plot_inputs(df: pd.DataFrame, date_col: str, value_cols: list[str], spec: PlotSpec) -> None:
    missing = [c for c in [date_col, *value_cols] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if not pd.api.types.is_datetime64_any_dtype(df[date_col]):
        raise TypeError(f"{date_col} must be datetime64; convert it before plotting.")

    if spec.highlight_date is not None and not isinstance(spec.highlight_date, datetime):
        raise TypeError("highlight_date must be a datetime or None.")

    if spec.month_step < 1:
        raise ValueError("month_step must be >= 1.")


def plot_with_spec(df: pd.DataFrame, spec: PlotSpec) -> plt.Axes:
    """
    Build a monthly time-series plot from a plot specification.

    Requires:
      - df["date"] is datetime64
      - df contains "sales_a" and "sales_b" as numeric columns
      - spec.highlight_date is a datetime or None
    """
    date_col = "date"
    value_cols = ["sales_a", "sales_b"]
    validate_plot_inputs(df, date_col, value_cols, spec)

    fig, ax = new_figure()

    monthly = monthly_sum(df, date_col, value_cols)

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

    ax.set_title(f"{spec.title}\n{spec.subtitle}" if spec.subtitle else spec.title)

    format_time_axis(ax, month_interval=spec.month_step)

    if spec.highlight_date:
        add_vline(ax, spec.highlight_date, "Event")

    ax.set_xlabel("Month")
    ax.set_ylabel("Total")
    ax.legend(title="Metric", loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0)

    plt.tight_layout()
    return ax


def to_monthly_index(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Convert date column to a monthly index.
    Requires: df[date_col] already in datetime64.
    """
    # Indexing by date ensures resampling works as expected
    return df.set_index(date_col).resample("M")
