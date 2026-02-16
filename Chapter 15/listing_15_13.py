# file: visual_diff.py
from PIL import ImageChops, ImageStat, Image
from pathlib import Path

def rms_diff(a: Path, b: Path) -> float:
    img1, img2 = Image.open(a).convert("RGB"), Image.open(b).convert("RGB")
    diff = ImageChops.difference(img1, img2)
    stat = ImageStat.Stat(diff)
    sq = sum([v**2 for v in stat.rms]) / 3.0
    return sq ** 0.5

def is_within_tolerance(new: Path, golden: Path, threshold=4.0) -> bool:
    return rms_diff(new, golden) <= threshold
