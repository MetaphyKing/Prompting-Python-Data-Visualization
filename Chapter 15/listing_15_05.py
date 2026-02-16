# file: run_visuals.py
import argparse, json, sys, os
from datetime import datetime
from pathlib import Path
from chain_visualization import run_chain  # from previous section

ART = Path("artifacts"); ART.mkdir(parents=True, exist_ok=True)
LOG = ART / "scheduler.log"

def log(event: str, **meta):
    rec = {"ts": datetime.utcnow().isoformat(), "event": event, **meta}
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--request", default="Create a revenue trend chart by date")
    p.add_argument("--dataset", default="data/sales.csv")
    p.add_argument("--dry-run", action="store_true", help="check environment only")
    args = p.parse_args()

    os.environ["DATASET_PATH"] = args.dataset
    log("start", request=args.request, dataset=args.dataset, dry=args.dry_run)

    if args.dry_run:
        log("dry_ok"); print("DRY-RUN: OK"); return 0

    try:
        note = run_chain(args.request)
        log("done", note=note)
        print(note)
        return 0
    except Exception as e:
        log("error", error=str(e))
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
