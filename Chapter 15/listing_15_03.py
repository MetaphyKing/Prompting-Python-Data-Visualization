# file: chain_visualization.py
from __future__ import annotations
import json
from pathlib import Path
from dataclasses import dataclass, asdict

DATA_PATH = "data/sales.csv"
ART_DIR = Path("artifacts"); ART_DIR.mkdir(parents=True, exist_ok=True)

@dataclass
class TaskSpec:
    goal: str
    data_path: str
    preferences: dict

@dataclass
class DesignSpec:
    chart_type: str
    x: str
    y: str
    title: str
    xlabel: str
    ylabel: str
    image: dict
    constraints: dict

def step_clarify_user_intent(raw_text: str) -> TaskSpec:
    return TaskSpec(
        goal="Show daily revenue trends",
        data_path=DATA_PATH,
        preferences={"avoid_heavy_ops": True, "style": "clean"}
    )

def step_design_visualization(task: TaskSpec) -> DesignSpec:
    return DesignSpec(
        chart_type="line",
        x="date",
        y="revenue",
        title="Revenue Dynamics",
        xlabel="Date",
        ylabel="Revenue",
        image={"path": str(ART_DIR / "plot.png"), "dpi": 150, "figsize": [6,4]},
        constraints={"max_points": 5000, "time_budget_ms": 800}
    )

def step_generate_code(design: DesignSpec, data_path: str) -> str:
    return f'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("{data_path}")
plt.figure(figsize=({design.image["figsize"][0]}, {design.image["figsize"][1]}))
sns.lineplot(data=df, x="{design.x}", y="{design.y}")
plt.title("{design.title}")
plt.xlabel("{design.xlabel}")
plt.ylabel("{design.ylabel}")
plt.tight_layout()
plt.savefig("{design.image["path"]}", dpi={design.image["dpi"]})
'''

def step_execute_and_validate(code: str, expected_path: str) -> dict:
    import tempfile, runpy
    from time import perf_counter
    t0 = perf_counter()
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "gen_plot.py"
        p.write_text(code, encoding="utf-8")
        runpy.run_path(str(p), run_name="__main__")
    t1 = perf_counter()
    out = Path(expected_path)
    ok = out.exists() and out.stat().st_size > 0
    return {"ok": ok, "path": expected_path, "ms": int((t1 - t0)*1000), "size": out.stat().st_size if out.exists() else 0}

def step_summarize(design: DesignSpec, validation: dict) -> str:
    base = f"A {design.chart_type} chart titled '{design.title}' was generated with axes {design.xlabel} and {design.ylabel}."
    quality = "Artifact successfully created." if validation["ok"] else "Artifact not created."
    return f"{base} {quality} See file: {validation['path']}."

def run_chain(raw_request: str):
    logs = []
    spec = step_clarify_user_intent(raw_request); logs.append(("spec", asdict(spec)))
    design = step_design_visualization(spec);      logs.append(("design", asdict(design)))
    code = step_generate_code(design, spec.data_path); logs.append(("code", code[:200] + "..."))
    val = step_execute_and_validate(code, design.image["path"]); logs.append(("validation", val))
    note = step_summarize(design, val);            logs.append(("summary", note))
    with open(ART_DIR / "chain_run.jsonl", "a", encoding="utf-8") as f:
        for k, v in logs:
            f.write(json.dumps({"step": k, "payload": v}, ensure_ascii=False) + "\n")
    return note

if __name__ == "__main__":
    print(run_chain("Create a revenue trend chart by date"))
