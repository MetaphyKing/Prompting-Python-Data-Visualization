# file: validate_artifact.py
from PIL import Image, PngImagePlugin
from pathlib import Path

def basic_checks(path: Path) -> dict:
    if not path.exists():
        return {"ok": False, "reason": "File not found"}
    if path.stat().st_size < 2000:
        return {"ok": False, "reason": "File too small"}
    img = Image.open(path)
    w, h = img.size
    dpi = img.info.get("dpi", (72, 72))[0]
    return {"ok": True, "w": w, "h": h, "dpi": dpi}

def save_with_metadata(fig, path: Path, meta: dict):
    info = PngImagePlugin.PngInfo()
    for k, v in meta.items():
        info.add_text(k, str(v))
    fig.savefig(path, dpi=meta.get("dpi", 150), pnginfo=info)
