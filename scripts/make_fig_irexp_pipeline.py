#!/usr/bin/env python3
"""Fig 2 — harvest / cleaning workflow. Frozen counts; postcard figures/ output."""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#1B3A4B"
BLUE = "#4A7EBB"
ORANGE = "#D97B32"
GREEN = "#3D8B5E"
INK = "#1A1A1A"
NOTE = "#5C636A"
LINE = "#C5C9CD"
FILL = "#FFFFFF"
SOFT = "#F4F6F8"
RED = "#C44E52"
FONT = "DejaVu Sans"


def _box(ax, x, y, w, h, title, lines, header=BLUE):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="square,pad=0",
            linewidth=0.7,
            edgecolor=header,
            facecolor=FILL,
        )
    )
    ax.add_patch(plt.Rectangle((x, y + h - 0.28), w, 0.28, facecolor=header, edgecolor=header, lw=0))
    ax.text(x + w / 2, y + h - 0.14, title, ha="center", va="center", color="white", fontsize=7.5, fontweight="bold")
    for i, line in enumerate(lines):
        ax.text(x + w / 2, y + 0.38 - i * 0.16, line, ha="center", va="center", fontsize=6.8, color=NOTE)


def _arrow(ax, x1, y1, x2, y2, color=BLUE):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=8,
            lw=0.9,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": FONT,
            "font.size": 8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    fig, (axa, axb) = plt.subplots(
        2,
        1,
        figsize=(7.2, 5.35),
        gridspec_kw={"height_ratios": [1.15, 0.95], "hspace": 0.18},
    )
    fig.subplots_adjust(left=0.04, right=0.98, top=0.93, bottom=0.04)

    # ----- A -----------------------------------------------------------------
    axa.set_xlim(0, 10)
    axa.set_ylim(0, 4.2)
    axa.axis("off")
    axa.text(0.05, 4.05, "A", fontsize=12, fontweight="bold", va="top")
    axa.text(0.35, 4.05, "Extraction and quality-control workflow", fontsize=9, fontweight="bold", va="top", color=INK)

    steps = [
        (0.25, "1", "PMC OA text", ["188,016 PMCIDs", "S3 plain text"], BLUE),
        (2.15, "2", "IR extract", ["Regex band lists", "+ co-reported NMR"], BLUE),
        (4.05, "3", "Structure resolve", ["OPSIN → RDKit", "SMILES / InChIKey"], BLUE),
        (5.95, "4", "Licence join", ["Europe PMC", "+ Crossref"], ORANGE),
        (7.85, "5", "Release pools", ["HF + Zenodo", "JSONL pools"], NAVY),
    ]
    w, h = 1.72, 1.15
    y = 2.55
    for x, num, title, lines, col in steps:
        axa.add_patch(plt.Circle((x + w / 2, 3.88), 0.13, facecolor=col, edgecolor="none"))
        axa.text(x + w / 2, 3.88, num, ha="center", va="center", color="white", fontsize=7, fontweight="bold")
        _box(axa, x, y, w, h, title, lines, header=col)
    for i in range(4):
        x1 = steps[i][0] + w
        x2 = steps[i + 1][0]
        _arrow(axa, x1 + 0.02, y + h / 2, x2 - 0.02, y + h / 2, steps[i + 1][4])

    # Chemotion join
    axa.add_patch(
        FancyBboxPatch(
            (0.25, 1.55),
            1.72,
            0.72,
            boxstyle="square,pad=0",
            linewidth=0.7,
            edgecolor=GREEN,
            facecolor=FILL,
        )
    )
    axa.text(1.11, 2.05, "Chemotion ELN", ha="center", va="center", fontsize=7.5, fontweight="bold", color=GREEN)
    axa.text(1.11, 1.78, "1,888 CC-BY-SA", ha="center", va="center", fontsize=6.8, color=NOTE)
    _arrow(axa, 1.97, 1.95, 2.15, 2.55, GREEN)

    # Cleaning rules
    axa.add_patch(
        FancyBboxPatch(
            (2.55, 0.22),
            4.55,
            1.15,
            boxstyle="square,pad=0",
            linewidth=0.7,
            edgecolor=ORANGE,
            facecolor=SOFT,
        )
    )
    axa.text(4.82, 1.18, "Cleaning rules", ha="center", va="center", fontsize=7.5, fontweight="bold", color=ORANGE)
    axa.text(
        4.82,
        0.72,
        "Band count ≥ 3 in 350–4000 cm$^{-1}$   ·   Reject duplicate integers\n"
        r"$^{1}$H integral ≤ formula H+2   ·   $^{13}$C peaks ≤ carbon count",
        ha="center",
        va="center",
        fontsize=6.6,
        color=NOTE,
    )
    _arrow(axa, 6.81, 2.55, 5.9, 1.38, ORANGE)

    # Final
    axa.add_patch(
        FancyBboxPatch(
            (7.55, 0.22),
            2.15,
            1.15,
            boxstyle="square,pad=0",
            linewidth=0.8,
            edgecolor=NAVY,
            facecolor=FILL,
        )
    )
    axa.text(8.62, 1.12, "Final IRexp", ha="center", va="center", fontsize=7.5, fontweight="bold", color=NAVY)
    axa.text(8.62, 0.78, "121,233 band lists", ha="center", va="center", fontsize=7.2, color=INK)
    axa.text(8.62, 0.52, "43,060 structure-linked", ha="center", va="center", fontsize=6.8, color=NOTE)
    _arrow(axa, 8.71, 2.55, 8.62, 1.38, NAVY)

    # ----- B -----------------------------------------------------------------
    axb.set_xlim(0, 10)
    axb.set_ylim(0, 3.2)
    axb.axis("off")
    axb.text(0.05, 3.1, "B", fontsize=12, fontweight="bold", va="top")
    axb.text(0.35, 3.1, "Automated QC rejections", fontsize=9, fontweight="bold", va="top", color=INK)

    examples = [
        (
            "Band count too low",
            r"IR (KBr): 3421, 2923, 2854 cm$^{-1}$ — <3 unique peaks after de-duplication.",
        ),
        (
            "IR band outside window",
            r"IR (neat): 3200, 2958, 4180, 1520 cm$^{-1}$ — 4180 outside 350–4000 cm$^{-1}$.",
        ),
        (
            r"$^{1}$H integral vs formula",
            r"$^{1}$H: (5H)+(5H)+(10H)=20H; C$_6$H$_5$NO$_2$ (7H) — integral > H+2.",
        ),
    ]
    for i, (title, body) in enumerate(examples):
        y = 2.35 - i * 0.95
        axb.add_patch(
            FancyBboxPatch(
                (0.25, y),
                9.45,
                0.82,
                boxstyle="square,pad=0",
                linewidth=0.5,
                edgecolor=LINE,
                facecolor=SOFT,
            )
        )
        axb.text(0.45, y + 0.55, "⊘", fontsize=11, color=RED, va="center")
        axb.text(0.85, y + 0.55, title, fontsize=7.5, fontweight="bold", color=RED, va="center")
        axb.text(0.85, y + 0.24, body, fontsize=7, color=INK, va="center")

    fig.savefig(OUT / "fig_irexp_pipeline.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_pipeline.png", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_pipeline.svg", bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_pipeline.pdf'}")


if __name__ == "__main__":
    main()
