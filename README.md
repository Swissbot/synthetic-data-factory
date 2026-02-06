# Synthetic Data Factory

**DE:** Generator für synthetische Datensätze (Bilder + COCO/YOLO Labels) mit Domain Randomization. Ideal als öffentliches Portfolio-Projekt ohne Kundendaten.  
**EN:** Synthetic dataset generator (images + COCO/YOLO labels) with domain randomization. Great as a public portfolio project without leaking customer data.

**Authors / Autoren:** Roger Seeberger (Swissbot) + ChatGPT (OpenAI)

---

## Features
- Generates PNG images with random backgrounds and simple “industrial-like” primitives
- Exports **COCO** annotations (segmentation via contours) and optional **YOLO** bounding boxes
- Includes dataset **report** and **preview** grid

---

## Setup (Ubuntu 24.04, Python 3.12)
```bash
make setup
```
# Quickstart

Generate a dataset:
```bash
make synth
```

Preview a grid:
```bash
make preview
```

Show dataset stats:
```bash
make report
```
# CLI
```bash
sdf synth --n 200 --out data/demo --seed 42

sdf synth --n 200 --out data/yolo_demo --yolo

sdf preview --data data/demo --out docs/preview_grid.png

sdf report --data data/demo
```

# Notes

This project intentionally uses synthetic primitives so the repository can be public.