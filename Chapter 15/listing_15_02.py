# Jupyter cell: helpers
from pathlib import Path
from string import Template
from datetime import datetime

def load_prompt(path="prompts/v1/plot_basic.md"):
    return Path(path).read_text(encoding="utf-8")

def render_prompt(tmpl: str, **params) -> str:
    # Supports both {name} and $name placeholders depending on the template syntax
    try:
        return tmpl.format(**params)
    except Exception:
        return Template(tmpl).safe_substitute(**params)

def make_context(data_path, x_col, y_col, plot_kind, output_dir="artifacts", time_budget_ms=800):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().isoformat().replace(":", "-")
    return {
        "data_path": data_path,
        "x_col": x_col,
        "y_col": y_col,
        "plot_kind": plot_kind,
        "time_budget_ms": time_budget_ms,
        "output_path": f"{output_dir}/plot_{ts}.png",
        "prompt_version": "v1"
    }


# Jupyter cell: context + prompt
ctx = make_context(
    data_path="data/sales.csv",
    x_col="date",
    y_col="revenue",
    plot_kind="line"
)
tmpl = load_prompt("prompts/v1/plot_basic.md")
prompt_text = render_prompt(tmpl, **ctx)
print(prompt_text[:800] + "...\n\n[truncated]")


# Jupyter cell: generation + execution (mock)
import runpy, tempfile, json

def call_model_return_code(prompt: str) -> str:
    # Stub: in production, this would call the AI model with fixed parameters
    code = f"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("{ctx['data_path']}")
plt.figure()
sns.lineplot(data=df, x="{ctx['x_col']}", y="{ctx['y_col']}")
plt.title("Automated Report: Trend Visualization")
plt.xlabel("{ctx['x_col']}")
plt.ylabel("{ctx['y_col']}")
plt.tight_layout()
plt.savefig("{ctx['output_path']}", dpi=150)
"""
    return code

def execute_code(code: str):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "gen_plot.py"
        p.write_text(code, encoding="utf-8")
        runpy.run_path(str(p), run_name="__main__")

code = call_model_return_code(prompt_text)
execute_code(code)

Path("artifacts/runs.log").parent.mkdir(parents=True, exist_ok=True)
with open("artifacts/runs.log", "a", encoding="utf-8") as f:
    f.write(json.dumps({"ctx": ctx, "prompt_version": ctx["prompt_version"]}, ensure_ascii=False) + "\n")

Path(ctx["output_path"])
