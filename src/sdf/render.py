from __future__ import annotations

import numpy as np
import cv2
from .shapes import draw_random_object

def random_background(rng: np.random.Generator, img_size: int) -> np.ndarray:
    base = rng.integers(20, 80)
    grad = np.linspace(base, base + rng.integers(20, 90), img_size, dtype=np.float32)
    bg = np.tile(grad[None, :], (img_size, 1))
    bg = np.stack([bg, bg, bg], axis=-1)

    noise = rng.normal(0, rng.uniform(3, 12), size=(img_size, img_size, 3)).astype(np.float32)
    bg = np.clip(bg + noise, 0, 255).astype(np.uint8)

    yy, xx = np.mgrid[0:img_size, 0:img_size].astype(np.float32)
    cx, cy = img_size / 2, img_size / 2
    r = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    r = r / r.max()
    v = (1.0 - 0.35 * r)[..., None]
    bg = np.clip(bg.astype(np.float32) * v, 0, 255).astype(np.uint8)
    return bg

def render_sample(rng: np.random.Generator, img_size: int = 512):
    img = random_background(rng, img_size)
    instances = []

    num_objs = int(rng.integers(1, 6))
    for _ in range(num_objs):
        img, inst = draw_random_object(rng, img, img_size)
        instances.append(inst)

    if rng.random() < 0.35:
        k = int(rng.choice([3, 5]))
        img = cv2.GaussianBlur(img, (k, k), sigmaX=float(rng.uniform(0.3, 1.2)))

    return img, instances
