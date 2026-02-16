# file: automate_plot.py
# Purpose: Demonstration of AI-assisted automation for data visualization.

import json
import pathlib
import runpy
import tempfile
from datetime import datetime

DATA_PATH = "data/sales.csv"
OUTPUT_DIR = pathlib.Path("artifacts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_prompt_template() -> str:
    return pathlib.Path("prompts/v1/plot_basic.md").read_text(encoding="utf-8")

def render_prompt(template: str, **params) -> str:
    return template.format(**params)

def ai_generate_code(prompt: str) -> str:
    """AI call stub - in production, use a controlled model with fixed parameters."""
    return f'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("{params.get("data_path","data.csv")}")
plt.figure()
sns.lineplot(data=df, x="{params.get("x_col","date")}", y="{params.get("y_col","value")}")
plt.title("Automated Report: Metric Dynamics")
plt.xlabel("{params.get("x_col","date")}")
plt.ylabel("{params.get("y_col","value")}")
plt.tight_layout()
plt.savefig("{params.get("output_path","artifacts/plot.png")}", dpi=150)
'''

def execute_generated_code(code_str: str):
    with tempfile.TemporaryDirectory() as td:
        script_path = pathlib.Path(td) / "gen_plot.py"
        script_path.write_text(code_str, encoding="utf-8")
        runpy.run_path(str(script_path), run_name="__main__")

def validate_artifact(path: pathlib.Path) -> dict:
    status = path.exists() and path.stat().st_size > 0
    return {"exists": path.exists(), "size": path.stat().st_size if path.exists() else 0, "ok": status}

def log_run(meta: dict):
    log_path = OUTPUT_DIR / "runs.log"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")

def main():
    ts = datetime.utcnow().isoformat()
    output_path = OUTPUT_DIR / f"plot_{ts.replace(':','-')}.png"

    template = load_prompt_template()
    prompt = render_prompt(
        template,
        data_path=DATA_PATH,
        x_col="date",
        y_col="revenue",
        plot_kind="line",
        time_budget_ms=800,
        output_path=str(output_path)
    )

    code = ai_generate_code(prompt)
    execute_generated_code(code)
    report = validate_artifact(output_path)

    log_run({
        "ts": ts,
        "prompt_version": "v1",
        "data": str(DATA_PATH),
        "output": str(output_path),
        "validation": report
    })

    if not report["ok"]:
        raise RuntimeError("The artifact did not pass basic quality validation.")

if __name__ == "__main__":
    main()
