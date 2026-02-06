from __future__ import annotations

import numpy as np
import cv2

def _bbox_from_mask(mask: np.ndarray):
    ys, xs = np.where(mask > 0)
    if len(xs) == 0:
        return (0, 0, 0, 0)
    x1, x2 = int(xs.min()), int(xs.max())
    y1, y2 = int(ys.min()), int(ys.max())
    return (x1, y1, x2 - x1 + 1, y2 - y1 + 1)

def draw_random_object(rng: np.random.Generator, img: np.ndarray, img_size: int):
    h, w = img.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)

    kind = rng.choice(["circle", "hex", "slot"])
    cx = int(rng.integers(60, w - 60))
    cy = int(rng.integers(60, h - 60))
    size = int(rng.integers(25, 85))

    color = int(rng.integers(120, 240))
    col = (color, color, color)

    if kind == "circle":
        cv2.circle(mask, (cx, cy), size, 255, -1)
    elif kind == "hex":
        pts = []
        for k in range(6):
            ang = (np.pi / 3) * k + float(rng.uniform(-0.15, 0.15))
            pts.append([int(cx + size * np.cos(ang)), int(cy + size * np.sin(ang))])
        pts = np.array([pts], dtype=np.int32)
        cv2.fillPoly(mask, pts, 255)
    else:
        x1, y1 = cx - size, cy - int(size * 0.35)
        x2, y2 = cx + size, cy + int(size * 0.35)
        cv2.rectangle(mask, (x1, y1), (x2, y2), 255, -1)

    alpha = float(rng.uniform(0.55, 0.9))
    obj = img.copy()
    obj[mask > 0] = (alpha * np.array(col) + (1 - alpha) * obj[mask > 0]).astype(np.uint8)
    img = obj

    bbox = _bbox_from_mask(mask)
    category_id = {"circle": 1, "hex": 2, "slot": 3}[kind]
    inst = {
        "category_id": int(category_id),
        "bbox_xywh": [int(x) for x in bbox],
        "mask": mask,  # COCO writer will convert to polygons
    }
    return img, inst
