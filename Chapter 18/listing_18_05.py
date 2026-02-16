# LLM → PlotSpec → Matplotlib/Seaborn integration skeleton
from pydantic import BaseModel, Field
from typing import Optional, List, Literal, Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io, json

class Transform(BaseModel):
    kind: Literal["filter", "aggregate", "sample", "scale", "bin"]
    params: Dict[str, Any] = {}

class PlotSpec(BaseModel):
    chart: Literal["line", "bar", "scatter", "hist", "box", "violin", "heatmap"]
    data_source: str = Field(description="dataset name or file path")
    x: Optional[str] = None
    y: Optional[str] = None
    hue: Optional[str] = None
    col: Optional[str] = None
    row: Optional[str] = None
    log_x: bool = False
    log_y: bool = False
    ci: Optional[float] = None
    title: Optional[str] = None
    caption: Optional[str] = None
    transforms: List[Transform] = []
    annotate: List[str] = []
    output: Literal["png", "svg"] = "png"

def load_data(name: str) -> pd.DataFrame:
    if name == "tips":
        return sns.load_dataset("tips")
    if name.endswith(".csv"):
        return pd.read_csv(name)
    raise FileNotFoundError(f"Unknown data source: {name}")

def apply_transforms(df: pd.DataFrame, spec: PlotSpec) -> pd.DataFrame:
    out = df.copy()
    for t in spec.transforms:
        if t.kind == "filter":
            col, op, val = t.params.get("col"), t.params.get("op"), t.params.get("value")
            if op == "in":
                out = out[out[col].isin(val)]
            if op == "gt":
                out = out[out[col] > val]
        if t.kind == "sample":
            frac = float(t.params.get("frac", 1.0))
            out = out.sample(frac=frac, random_state=42)
        if t.kind == "aggregate":
            by, y, fn = t.params["by"], t.params["y"], t.params.get("fn", "mean")
            out = out.groupby(by, as_index=False)[y].agg(fn)
        if t.kind == "scale":
            axis, base = t.params.get("axis","y"), t.params.get("base","log10")
            if axis == "x": spec.log_x = True
            if axis == "y": spec.log_y = True
    return out

def render_plot(spec: PlotSpec) -> bytes:
    df = apply_transforms(load_data(spec.data_source), spec)
    fig, ax = plt.subplots()
    if spec.chart == "line":
        sns.lineplot(data=df, x=spec.x, y=spec.y, hue=spec.hue, ci=spec.ci, ax=ax)
    elif spec.chart == "bar":
        sns.barplot(data=df, x=spec.x, y=spec.y, hue=spec.hue, ax=ax, errorbar=None)
        ax.set_ylim(bottom=0)  # enforce zero baseline
    elif spec.chart == "scatter":
        sns.scatterplot(data=df, x=spec.x, y=spec.y, hue=spec.hue, ax=ax, alpha=0.7, s=30)
    elif spec.chart == "hist":
        sns.histplot(data=df, x=spec.x, hue=spec.hue, ax=ax, element="step", kde=False)
    elif spec.chart == "box":
        sns.boxplot(data=df, x=spec.x, y=spec.y, hue=spec.hue, ax=ax)
    elif spec.chart == "violin":
        sns.violinplot(data=df, x=spec.x, y=spec.y, hue=spec.hue, ax=ax, cut=0, inner="quartile")
    elif spec.chart == "heatmap":
        sns.heatmap(df, ax=ax)
    if spec.log_x: ax.set_xscale("log")
    if spec.log_y: ax.set_yscale("log")
    if spec.title: ax.set_title(spec.title)
    ax.set_xlabel(spec.x or ax.get_xlabel())
    ax.set_ylabel(spec.y or ax.get_ylabel())
    buf = io.BytesIO()
    plt.tight_layout()
    fig.savefig(buf, format=spec.output, dpi=200)
    plt.close(fig)
    return buf.getvalue()

def visualize_from_llm_json(json_text: str) -> bytes:
    obj = json.loads(json_text)
    spec = PlotSpec(**obj)
    return render_plot(spec)

