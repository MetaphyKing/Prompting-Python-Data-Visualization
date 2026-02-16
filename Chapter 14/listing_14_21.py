import json, hashlib, platform
from pathlib import Path
import matplotlib, seaborn as sns, pandas as pd

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]

def file_hash(p: Path) -> str:
    return sha256_bytes(p.read_bytes())

def runtime_fingerprint() -> dict:
    return {
        "python": platform.python_version(),
        "matplotlib": matplotlib.__version__,
        "seaborn": sns.__version__,
        "pandas": pd.__version__,
        "platform": platform.platform(),
    }

def save_figure_with_passport(fig, out_png: Path, inputs: dict, params: dict):
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=300, bbox_inches="tight")
    passport = {
        "figure": out_png.name,
        "inputs": {k: file_hash(Path(v)) for k, v in inputs.items()},
        "params": params,
        "runtime": runtime_fingerprint(),
    }
    out_png.with_suffix(".json").write_text(json.dumps(passport, indent=2))


import json, hashlib, platform
from pathlib import Path
import matplotlib, seaborn as sns, pandas as pd

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]

def file_hash(p: Path) -> str:
    return sha256_bytes(p.read_bytes())

def runtime_fingerprint() -> dict:
    return {
        "python": platform.python_version(),
        "matplotlib": matplotlib.__version__,
        "seaborn": sns.__version__,
        "pandas": pd.__version__,
        "platform": platform.platform(),
    }

def save_figure_with_passport(fig, out_png: Path, inputs: dict, params: dict):
    out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_png, dpi=300, bbox_inches="tight")
    passport = {
        "figure": out_png.name,
        "inputs": {k: file_hash(Path(v)) for k, v in inputs.items()},
        "params": params,
        "runtime": runtime_fingerprint(),
    }
    out_png.with_suffix(".json").write_text(json.dumps(passport, indent=2))
