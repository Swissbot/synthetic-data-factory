from __future__ import annotations

from pathlib import Path
import json
import numpy as np
import cv2
from tqdm import tqdm

from .render import render_sample
from .coco import CocoWriter
from .yolo import write_yolo_labels

def synth_dataset(n: int, out_dir: str, seed: int, img_size: int, export_yolo: bool) -> None:
    out = Path(out_dir)
    img_dir = out / "images"
    ann_dir = out / "annotations"
    img_dir.mkdir(parents=True, exist_ok=True)
    ann_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(seed)

    coco = CocoWriter()
    for i in tqdm(range(n), desc="synth"):
        img, instances = render_sample(rng, img_size=img_size)

        fn = f"{i:05d}.png"
        cv2.imwrite(str(img_dir / fn), img)

        image_id = coco.add_image(file_name=f"images/{fn}", width=img_size, height=img_size)
        coco.add_instances(image_id=image_id, instances=instances)

        if export_yolo:
            write_yolo_labels(out, fn, instances, img_size)

    (ann_dir / "coco.json").write_text(json.dumps(coco.to_dict(), indent=2), encoding="utf-8")
