from __future__ import annotations
from pathlib import Path
import json
from rich.console import Console
from rich.table import Table

console = Console()

def report_dataset(data_dir: str):
    data = Path(data_dir)
    coco_path = data / "annotations" / "coco.json"
    if not coco_path.exists():
        raise FileNotFoundError(f"Missing {coco_path}")

    coco = json.loads(coco_path.read_text(encoding="utf-8"))
    anns = coco.get("annotations", [])
    cats = {c["id"]: c["name"] for c in coco.get("categories", [])}

    counts = {}
    areas = {}
    for a in anns:
        cid = a["category_id"]
        counts[cid] = counts.get(cid, 0) + 1
        areas.setdefault(cid, []).append(a.get("area", 0))

    t = Table(title="Synthetic Data Factory — Dataset report")
    t.add_column("category")
    t.add_column("count", justify="right")
    t.add_column("avg area", justify="right")

    for cid, name in sorted(cats.items()):
        c = counts.get(cid, 0)
        aa = areas.get(cid, [])
        avg = (sum(aa) / len(aa)) if aa else 0
        t.add_row(name, str(c), f"{avg:.1f}")

    console.print(t)
