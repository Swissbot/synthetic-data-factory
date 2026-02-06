from __future__ import annotations

import typer
from rich.console import Console

from .synth import synth_dataset
from .preview import preview_grid
from .report import report_dataset

app = typer.Typer(add_completion=False)
console = Console()

@app.command()
def synth(
    n: int = typer.Option(100, "--n", help="Number of samples"),
    out: str = typer.Option("data/demo", "--out", help="Output directory"),
    seed: int = typer.Option(42, "--seed", help="Random seed"),
    img_size: int = typer.Option(512, "--img-size", help="Square image size"),
    yolo: bool = typer.Option(False, "--yolo", help="Also export YOLO bbox labels"),
):
    synth_dataset(n=n, out_dir=out, seed=seed, img_size=img_size, export_yolo=yolo)
    console.print(f"[green]OK[/green] wrote dataset -> {out}")

@app.command()
def preview(
    data: str = typer.Option(..., "--data", help="Dataset directory (with images/)"),
    out: str = typer.Option("docs/preview_grid.png", "--out", help="Output png for preview grid"),
    k: int = typer.Option(16, "--k", help="Number of images in grid"),
):
    preview_grid(data_dir=data, out_path=out, k=k)
    console.print(f"[green]OK[/green] preview -> {out}")

@app.command()
def report(
    data: str = typer.Option(..., "--data", help="Dataset directory"),
):
    report_dataset(data_dir=data)

def main():
    app()

if __name__ == "__main__":
    main()
