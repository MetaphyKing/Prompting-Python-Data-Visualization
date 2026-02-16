import matplotlib
matplotlib.use("Agg")  # before pyplot import



# src/build_figures.py
import argparse
from production_style import use_production_style
from utils.provenance import snapshot_environment

def build_all_ch8():
    use_production_style()
    snapshot_environment("figures/_provenance/env_snapshot.json")
    # call build functions here
    # build_sine(); build_layout(); build_heatmap(); ...

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", type=int, default=8)
    args = ap.parse_args()
    if args.chapter == 8:
        build_all_ch8()
