#!/usr/bin/env python3
"""Fig 1 — IRexp vs major IR resources. Frozen counts only; no invented DOIs."""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Frozen release counts (data/irexp_stats.json / qc_structure_nmr.json)
N_ALL = 121_233
N_STRUCT = 43_060
N_COMM = 88_545
SDBS = 54_100
NIST = 17_000
ZIPOLI = 177_461

NAVY = "#1B3A4B"
INK = "#1A1A1A"
NOTE = "#5C636A"
PEACH = "#E8B86D"
BLUE = "#4A7EBB"
GRAY = "#B7BDC3"
COMPUTED = "#C5D4E8"
FAINT = "#E8EAEC"
FONT = "DejaVu Sans"


def _thousands(x: float, _pos: int | None = None) -> str:
    if x >= 1000:
        return f"{x / 1000:.0f}k"
    return f"{x:.0f}"


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": FONT,
            "font.size": 8.5,
            "axes.linewidth": 0.6,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(7.2, 3.55),
        gridspec_kw={"width_ratios": [1.55, 1.0], "wspace": 0.08},
    )
    ax, axb = axes
    fig.subplots_adjust(left=0.08, right=0.98, top=0.88, bottom=0.22)

    # --- A: grouped bars -------------------------------------------------
    clusters = [
        ("SDBS\nFT-IR", SDBS, None, None, True, GRAY),
        ("NIST\ngas-phase", NIST, None, None, True, GRAY),
        ("Zipoli et al.\nsimulated", ZIPOLI, None, None, False, COMPUTED),
        ("IRexp\nband lists", N_ALL, N_STRUCT, N_COMM, False, NAVY),
    ]
    x0 = [0, 1, 2.35, 3.7]
    width = 0.28
    ax.axhline(0, color=INK, lw=0.6)
    for i, (label, total, struct, comm, view_only, face) in enumerate(clusters):
        x = x0[i]
        if struct is None:
            bars = ax.bar(
                [x],
                [total],
                width=0.42,
                color=face,
                edgecolor="white",
                linewidth=0.4,
                zorder=3,
            )
            if view_only:
                bars[0].set_hatch("///")
                bars[0].set_edgecolor("#8A9096")
            ax.text(
                x,
                total + 3500,
                f"{total:,}",
                ha="center",
                va="bottom",
                fontsize=7,
                color=NOTE,
            )
        else:
            xs = [x - width, x, x + width]
            vals = [total, struct, comm]
            cols = [NAVY, PEACH, BLUE]
            ax.bar(xs, vals, width=width * 0.95, color=cols, edgecolor="white", linewidth=0.4, zorder=3)
            for xv, v in zip(xs, vals):
                ax.text(
                    xv,
                    v + 3500,
                    f"{v:,}",
                    ha="center",
                    va="bottom",
                    fontsize=6.5,
                    color=NOTE,
                    rotation=0,
                )

    ax.set_xticks(x0)
    ax.set_xticklabels([c[0] for c in clusters], fontsize=8, color=INK)
    ax.set_ylabel("Number of IR records", fontsize=9, color=INK)
    ax.yaxis.set_major_formatter(FuncFormatter(_thousands))
    ax.set_ylim(0, 205_000)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=3, color=NOTE, labelcolor=INK)
    ax.yaxis.grid(True, color=FAINT, lw=0.5, zorder=0)
    ax.set_axisbelow(True)

    # Group brackets
    def _bracket(x1: float, x2: float, y: float, text: str) -> None:
        ax.plot([x1, x1, x2, x2], [y - 4000, y, y, y - 4000], color=NOTE, lw=0.7, clip_on=False)
        ax.text((x1 + x2) / 2, y + 2500, text, ha="center", va="bottom", fontsize=7, color=NOTE)

    _bracket(-0.28, 1.28, 198_000, "View-only")
    _bracket(2.12, 2.58, 198_000, "Computed")
    _bracket(3.35, 4.05, 198_000, "This work")

    ax.text(-0.18, 1.08, "A", transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")

    legend = [
        Patch(facecolor=NAVY, edgecolor="none", label="All"),
        Patch(facecolor=PEACH, edgecolor="none", label="Structure-linked"),
        Patch(facecolor=BLUE, edgecolor="none", label="CC-BY/CC0"),
    ]
    ax.legend(
        handles=legend,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.18),
        ncol=3,
        frameon=False,
        fontsize=7.5,
        handlelength=1.1,
        columnspacing=1.2,
    )

    # --- B: attributes as a plain list (not a feature card) --------------
    axb.set_xlim(0, 1)
    axb.set_ylim(0, 1)
    axb.axis("off")
    axb.text(-0.02, 1.08, "B", transform=axb.transAxes, fontsize=12, fontweight="bold", va="bottom")
    axb.text(0.0, 0.96, "IRexp", fontsize=10, fontweight="bold", color=INK, va="top")
    rows = [
        ("Object", "Peak lists, not absorbance traces"),
        ("Redistribution", "Bulk download (JSONL)"),
        ("Licences", "Per-record pools (commercial / NC* / SA)"),
        ("Provenance", "DOI-traceable PMC or Chemotion"),
        ("Commercial pool", f"{N_COMM:,} CC-BY/CC0 records"),
    ]
    y = 0.82
    for key, val in rows:
        axb.text(0.0, y, key, fontsize=7.5, fontweight="bold", color=INK, va="center")
        axb.text(0.0, y - 0.07, val, fontsize=7.5, color=NOTE, va="center")
        y -= 0.16
        axb.plot([0.0, 0.98], [y + 0.055, y + 0.055], color=FAINT, lw=0.6)

    fig.savefig(OUT / "fig_irexp_positioning.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_positioning.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_positioning.pdf'}")


if __name__ == "__main__":
    main()
