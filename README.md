# Synthetic Data Factory

**DE:** Generator für synthetische Datensätze (Bilder + COCO/YOLO Labels) mit Domain Randomization. Ideal als öffentliches Portfolio-Projekt ohne Kundendaten.  
**EN:** Synthetic dataset generator (images + COCO/YOLO labels) with domain randomization. Great as a public portfolio project without leaking customer data.

<p>
  <strong>Author / Autor:</strong> Roger Seeberger (Swissbot)<br>
  <img src="docs/author_icon.png" alt="Author icon" width="64" />
</p>

---

## Features
- Generates PNG images with random backgrounds and simple “industrial-like” primitives
- Exports **COCO** annotations (segmentation via contours) and optional **YOLO** bounding boxes
- Includes dataset **report** and **preview** grid
- **Themes:** baseline primitives + optional fastener-like shapes (`--theme fasteners`)
- **Reproducible** via `--seed`

---

## Installation (Ubuntu 24.04, Python 3.12)

### 1) Create & activate venv
```bash
cd synthetic-data-factory
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip setuptools wheel
```

2) Install dependencies + project (editable)
```bash
pip install -r requirements.txt
pip install -e .
```

3) Verify CLI
```bash
sdf --help
```

## Quickstart (CLI)
Generate a dataset (baseline)
```bash
mkdir -p data
sdf synth --n 50 --out data/demo --seed 42
```
Outputs
data/demo/images/*.png
data/demo/annotations/coco.json
(optional) data/demo/labels/*.txt   # if --yolo is used

## Generate YOLO labels as well
```bash
sdf synth --n 50 --out data/yolo_demo --seed 42 --yolo
```
## Create a preview grid image
```bash
mkdir -p docs
sdf preview --data data/demo --out docs/preview_grid.png --k 16
```

## Print dataset stats
```bash
sdf report --data data/demo
```

## Themes (baseline vs fasteners)

--theme baseline (default): circle, hex, slot

--theme fasteners: washer, hex_head, torx_head

## Example:
```bash
sdf synth --n 80 --out data/fasteners_demo --seed 42 --theme fasteners
sdf preview --data data/fasteners_demo --out docs/preview_fasteners.png --k 16
sdf report --data data/fasteners_demo
```

## Previews

Baseline (circle/hex/slot)
<img src="docs/preview_grid.png" alt="Baseline preview grid" width="900" />

Fasteners theme (washer/hex_head/torx_head)
<img src="docs/preview_fasteners.png" alt="Fasteners preview grid" width="900" />

## Makefile shortcuts (optional)
If you prefer make:
```bash
make setup
make synth
make preview
make report
```

## CLI Reference
### baseline
```bash
sdf synth --n 200 --out data/demo --seed 42
```
### yolo export
```bash
sdf synth --n 200 --out data/yolo_demo --seed 42 --yolo
```
### fasteners theme
```bash
sdf synth --n 200 --out data/fasteners_demo --seed 42 --theme fasteners
```
### preview + report
```bash
sdf preview --data data/demo --out docs/preview_grid.png --k 16
sdf report  --data data/demo
```

## Notes

This project intentionally uses synthetic data so the repository can be public and shareable.