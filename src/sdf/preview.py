from __future__ import annotations
from pathlib import Path
import random
import cv2
import numpy as np

def preview_grid(data_dir: str, out_path: str, k: int = 16):
    data = Path(data_dir)
    imgs = sorted((data / "images").glob("*.png"))
    if not imgs:
        raise FileNotFoundError(f"No images in {data/'images'}")

    pick = random.sample(imgs, k=min(k, len(imgs)))
    tiles = [cv2.imread(str(p)) for p in pick]

    n = len(tiles)
    cols = int(np.ceil(np.sqrt(n)))
    rows = int(np.ceil(n / cols))
    h, w = tiles[0].shape[:2]

    grid = np.zeros((rows * h, cols * w, 3), dtype=np.uint8)
    for i, im in enumerate(tiles):
        r, c = divmod(i, cols)
        grid[r * h:(r + 1) * h, c * w:(c + 1) * w] = im

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(out_path, grid)
