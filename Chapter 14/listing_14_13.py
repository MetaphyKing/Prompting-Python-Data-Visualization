import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


HOUSE_RC = {
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "legend.frameon": False,
    "figure.autolayout": True,
}

def apply_house_style(use_seaborn: bool = True) -> None:
    """
    Apply a reproducible, project-wide style.
    If Seaborn is used, set its theme explicitly and keep rc overrides in one place.
    """
    if use_seaborn:
        # Seaborn may override Matplotlib defaults; keep overrides explicit via rc=
        sns.set_theme(context="notebook", style="whitegrid", rc=HOUSE_RC)
    else:
        mpl.rcParams.update(HOUSE_RC)

def new_figure(width: float = 10, height: float = 5) -> tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(width, height))
    return fig, ax




def monthly_sum(df: pd.DataFrame, date_col: str, value_cols: list[str]) -> pd.DataFrame:
    """
    Return monthly totals for value_cols.
    """
    monthly = (
        df.set_index(date_col)
          .resample("M")
          .agg({c: "sum" for c in value_cols})
          .rename_axis("month")
          .reset_index()
    )
    return monthly
