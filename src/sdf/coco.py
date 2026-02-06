from __future__ import annotations

import numpy as np
import cv2

class CocoWriter:
    def __init__(self):
        self.images = []
        self.annotations = []
        self._image_id = 0
        self._ann_id = 0
        self.categories = [
            {"id": 1, "name": "circle"},
            {"id": 2, "name": "hex"},
            {"id": 3, "name": "slot"},
        ]

    def add_image(self, file_name: str, width: int, height: int) -> int:
        self._image_id += 1
        self.images.append({"id": self._image_id, "file_name": file_name, "width": width, "height": height})
        return self._image_id

    def _mask_to_polygons(self, mask: np.ndarray):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        polys = []
        for c in contours:
            if len(c) < 6:
                continue
            c = c.squeeze(1)
            poly = c.reshape(-1).astype(float).tolist()
            if len(poly) >= 6:
                polys.append(poly)
        return polys

    def add_instances(self, image_id: int, instances: list[dict]) -> None:
        for inst in instances:
            self._ann_id += 1
            mask = inst["mask"]
            bbox = inst["bbox_xywh"]
            area = int(np.sum(mask > 0))
            seg = self._mask_to_polygons(mask)

            self.annotations.append({
                "id": self._ann_id,
                "image_id": image_id,
                "category_id": int(inst["category_id"]),
                "bbox": bbox,
                "area": area,
                "iscrowd": 0,
                "segmentation": seg,
            })

    def to_dict(self):
        return {
            "images": self.images,
            "annotations": self.annotations,
            "categories": self.categories,
        }
