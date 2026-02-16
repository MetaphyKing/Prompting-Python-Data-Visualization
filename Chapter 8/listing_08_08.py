# src/utils/save.py
import json, pathlib
import matplotlib.pyplot as plt
from .provenance import git_commit

def save_with_provenance(fig, basename: str, meta: dict):
    out = pathlib.Path("figures") / f"{basename}"
    out.parent.mkdir(parents=True, exist_ok=True)

    commit = git_commit()
    meta = {**meta, "git_commit": commit}

    # PDF + metadata
    fig.savefig(f"{out}.pdf", bbox_inches="tight", pad_inches=0.02,
                metadata={"Title": basename, "Producer": "Matplotlib",
                          "Author": meta.get("author",""), "Subject": meta.get("subject","")})

    # Editable SVG
    import matplotlib as mpl
    old = mpl.rcParams.get("svg.fonttype")
    mpl.rcParams["svg.fonttype"] = "none"
    try:
        fig.savefig(f"{out}.svg", bbox_inches="tight", pad_inches=0.02)
    finally:
        if old is not None:
            mpl.rcParams["svg.fonttype"] = old

    # PNG
    fig.savefig(f"{out}.png", dpi=300, bbox_inches="tight", pad_inches=0.02)

    # Sidecar JSON
    with open(f"{out}.provenance.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
