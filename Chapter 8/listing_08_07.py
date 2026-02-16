import json, platform, subprocess, sys, datetime as dt
import matplotlib as mpl
import numpy as np

def git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
    except Exception:
        return "unknown"

def snapshot_environment(path: str):
    info = {
        "timestamp": dt.datetime.utcnow().isoformat() + "Z",
        "python": sys.version.replace("\n"," "),
        "platform": platform.platform(),
        "matplotlib": mpl.__version__,
        "numpy": np.__version__,
        "backend": mpl.get_backend(),
        "rcParams_subset": {
            "font.family": mpl.rcParams.get("font.family"),
            "svg.fonttype": mpl.rcParams.get("svg.fonttype"),
            "pdf.fonttype": mpl.rcParams.get("pdf.fonttype"),
            "savefig.dpi": mpl.rcParams.get("savefig.dpi"),
        },
        "git_commit": git_commit(),
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)


from matplotlib import font_manager as fm
fm.fontManager.addfont("env/fonts/DejaVuSans.ttf")
fm.fontManager.addfont("env/fonts/DejaVuSans-Oblique.ttf")

import matplotlib as mpl
mpl.rcParams["font.family"] = "DejaVu Sans"
mpl.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42, "svg.fonttype": "none"})


import random, numpy as np
random.seed(42)
rng = np.random.default_rng(42)





