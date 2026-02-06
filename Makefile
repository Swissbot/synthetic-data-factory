.PHONY: setup synth preview report test

setup:
	python3.12 -m venv .venv
	. .venv/bin/activate && python -m pip install -U pip setuptools wheel
	. .venv/bin/activate && pip install -r requirements.txt
	. .venv/bin/activate && pip install -e .

synth:
	. .venv/bin/activate && sdf synth --n 50 --out data/demo --seed 42

preview:
	. .venv/bin/activate && sdf preview --data data/demo --out docs/preview_grid.png

report:
	. .venv/bin/activate && sdf report --data data/demo

test:
	. .venv/bin/activate && pytest -q
