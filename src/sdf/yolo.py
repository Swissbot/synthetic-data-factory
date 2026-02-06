from __future__ import annotations
from pathlib import Path

def write_yolo_labels(out_dir: Path, image_fn: str, instances: list[dict], img_size: int):
    lbl_dir = out_dir / "labels"
    lbl_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(image_fn).stem
    lines = []
    for inst in instances:
        cls = int(inst["category_id"]) - 1  # 0..N-1
        x, y, w, h = inst["bbox_xywh"]
        cx = (x + w / 2) / img_size
        cy = (y + h / 2) / img_size
        ww = w / img_size
        hh = h / img_size
        lines.append(f"{cls} {cx:.6f} {cy:.6f} {ww:.6f} {hh:.6f}")
    (lbl_dir / f"{stem}.txt").write_text("\n".join(lines), encoding="utf-8")
