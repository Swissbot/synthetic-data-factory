# Synthetic Data Factory

**DE:** Generator für synthetische Datensätze (Bilder + COCO/YOLO Labels) mit Domain Randomization. Ideal als öffentliches Portfolio-Projekt ohne Kundendaten.  
**EN:** Synthetic dataset generator (images + COCO/YOLO labels) with domain randomization. Great as a public portfolio project without leaking customer data.

*
<p>
  <strong>Author / Autor:</strong> Roger Seeberger (Swissbot)<br>
  <img src="docs/author_icon.png" alt="Author icon" width="64" />
</p>

---

## Features
- Generates PNG images with random backgrounds and simple “industrial-like” primitives
- Exports **COCO** annotations (segmentation via contours) and optional **YOLO** bounding boxes
- Includes dataset **report** and **preview** grid

---

## Installation (Ubuntu 24.04, Python 3.12)

### Quickstart / Makefile shortcuts (optional)
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

### 1) Create & activate venv
```bash
cd synthetic-data-factory

python3.12 -m venv .venv

source .venv/bin/activate

python -m pip install -U pip setuptools wheel
```

### 2) Install dependencies + project (editable)
```bash
pip install -r requirements.txt

pip install -e .
```

### 3) Verify CLI
```bash
sdf --help
```
### Generate a dataset
```bash
mkdir -p data

sdf synth --n 50 --out data/demo --seed 42
```
### Outputs:
bash
data/demo/images/*.png
data/demo/annotations/coco.json
optional: data/demo/labels/*.txt (YOLO)


### Generate YOLO labels as well
```bash
sdf synth --n 50 --out data/yolo_demo --seed 42 --yolo
```

### Create a preview grid image
```bash
mkdir -p docs

sdf preview --data data/demo --out docs/preview_grid.png --k 16
```

### Print dataset stats
```bash
sdf report --data data/demo
```

### Preview (generated)

After running the preview command above, you can embed the image in GitHub:

<img src="docs/preview_grid.png" alt="Preview grid" width="900" />

# CLI
```bash
sdf synth --n 200 --out data/demo --seed 42

sdf synth --n 200 --out data/yolo_demo --yolo

sdf preview --data data/demo --out docs/preview_grid.png --k 16

sdf report --data data/demo
```

# Notes
This project intentionally uses synthetic primitives so the repository can be public.