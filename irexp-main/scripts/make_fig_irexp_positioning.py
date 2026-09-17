#!/usr/bin/env python3
"""Fig 1 - IRexp vs major IR resources. Frozen counts only; no invented DOIs.

Nature Scientific Data Fig. 1: grouped resource bars (A) + compact attribute
list (B). Palette aligned with fig_irexp_pipeline (navy/blue/orange/green).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Patch, Rectangle
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

# Frozen release counts (data/irexp_stats.json / manuscript caption)
N_ALL = 121_233
N_STRUCT = 43_060
N_COMM = 88_545
SDBS = 54_100
NIST = 17_000
ZIPOLI = 177_461

NAVY = "#1B3A4B"
BLUE = "#4A7EBB"
ORANGE = "#D97B32"
GREEN = "#3D8B5E"
PEACH = "#E8B86D"  # structure-linked (warm accent, matches pipeline orange family)
INK = "#1A1A1A"
NOTE = "#5C636A"
GRAY = "#B7BDC3"
COMPUTED = "#C5D4E8"
FAINT = "#E8EAEC"
SOFT = "#F7F8FA"
LINE = "#D0D4D8"
FONT = "DejaVu Sans"


def _thousands(x: float, _pos: int | None = None) -> str:
    if x >= 1000:
        return f"{x / 1000:.0f}k"
    return f"{x:.0f}"


def _fmt(n: int) -> str:
    return f"{n:,}"


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
        figsize=(7.2, 3.65),
        gridspec_kw={"width_ratios": [1.58, 0.95], "wspace": 0.10},
    )
    ax, axb = axes
    fig.subplots_adjust(left=0.09, right=0.985, top=0.86, bottom=0.24)

    # --- A: grouped bars -------------------------------------------------
    # View-only | Computed | This work (IRexp triple)
    x0 = [0.0, 1.05, 2.45, 4.10]
    width = 0.30
    ax.axhline(0, color=INK, lw=0.55, zorder=2)

    # SDBS / NIST (view-only, hatched)
    for i, (total, face) in enumerate([(SDBS, GRAY), (NIST, GRAY)]):
        x = x0[i]
        bars = ax.bar(
            [x],
            [total],
            width=0.46,
            color=face,
            edgecolor="#8A9096",
            linewidth=0.55,
            zorder=3,
        )
        bars[0].set_hatch("///")
        ax.text(
            x,
            total + 4200,
            _fmt(total),
            ha="center",
            va="bottom",
            fontsize=6.8,
            color=NOTE,
        )

    # Zipoli (computed)
    x = x0[2]
    ax.bar(
        [x],
        [ZIPOLI],
        width=0.46,
        color=COMPUTED,
        edgecolor="white",
        linewidth=0.4,
        zorder=3,
    )
    ax.text(
        x,
        ZIPOLI + 4200,
        _fmt(ZIPOLI),
        ha="center",
        va="bottom",
        fontsize=6.8,
        color=NOTE,
    )

    # IRexp triple - same bar width as Zipoli (0.46); centers >=0.52 apart
    x = x0[3]
    irexp_w = 0.46
    irexp_gap = 0.52  # center-to-center so wide bars do not overlap
    xs = [x - irexp_gap, x, x + irexp_gap]
    vals = [N_ALL, N_STRUCT, N_COMM]
    cols = [NAVY, PEACH, BLUE]
    labels_short = ["All", "Struct.", "CC-BY/CC0"]
    ax.bar(
        xs,
        vals,
        width=irexp_w,
        color=cols,
        edgecolor="white",
        linewidth=0.4,
        zorder=3,
    )
    # Per-bar labels (same style as Zipoli/SDBS): total + 4200 offset
    for xv, v in zip(xs, vals):
        ax.text(
            xv,
            v + 4200,
            _fmt(v),
            ha="center",
            va="bottom",
            fontsize=6.8,
            color=NOTE,
        )

    ax.set_xticks(x0)
    ax.set_xticklabels(
        [
            "SDBS\nFT-IR",
            "NIST\ngas-phase",
            "Zipoli et al.\nsimulated",
            "IRexp\nband lists",
        ],
        fontsize=7.8,
        color=INK,
    )
    ax.set_ylabel("Number of IR records", fontsize=9, color=INK)
    ax.yaxis.set_major_formatter(FuncFormatter(_thousands))
    ax.set_ylim(0, 210_000)
    ax.set_xlim(-0.55, 5.05)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=3, color=NOTE, labelcolor=INK)
    ax.yaxis.grid(True, color=FAINT, lw=0.5, zorder=0)
    ax.set_axisbelow(True)

    def _bracket(x1: float, x2: float, y: float, text: str) -> None:
        ax.plot(
            [x1, x1, x2, x2],
            [y - 4500, y, y, y - 4500],
            color=NOTE,
            lw=0.7,
            clip_on=False,
        )
        ax.text(
            (x1 + x2) / 2,
            y + 2800,
            text,
            ha="center",
            va="bottom",
            fontsize=7,
            color=NOTE,
            fontweight="medium",
        )

    _bracket(-0.30, 1.35, 202_000, "View-only")
    _bracket(2.20, 2.70, 202_000, "Computed")
    _bracket(3.40, 4.80, 202_000, "This work")

    ax.text(
        -0.14,
        1.10,
        "A",
        transform=ax.transAxes,
        fontsize=12,
        fontweight="bold",
        va="bottom",
    )

    legend = [
        Patch(facecolor=NAVY, edgecolor="none", label="All"),
        Patch(facecolor=PEACH, edgecolor="none", label="Structure-linked"),
        Patch(facecolor=BLUE, edgecolor="none", label="CC-BY/CC0"),
        Patch(
            facecolor=GRAY,
            edgecolor="#8A9096",
            hatch="///",
            label="View-only",
        ),
    ]
    ax.legend(
        handles=legend,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.20),
        ncol=4,
        frameon=False,
        fontsize=7.2,
        handlelength=1.15,
        columnspacing=1.05,
        handletextpad=0.45,
    )

    # --- B: tight bordered attribute list (manuscript caption facts) -----
    axb.set_xlim(0, 1)
    axb.set_ylim(0, 1)
    axb.axis("off")
    axb.text(
        -0.06,
        1.10,
        "B",
        transform=axb.transAxes,
        fontsize=12,
        fontweight="bold",
        va="bottom",
    )

    # Outer card
    left, bottom, width_b, height_b = 0.02, 0.02, 0.96, 0.96
    axb.add_patch(
        FancyBboxPatch(
            (left, bottom),
            width_b,
            height_b,
            boxstyle="round,pad=0.012,rounding_size=0.02",
            linewidth=0.9,
            edgecolor=LINE,
            facecolor="white",
            transform=axb.transAxes,
            clip_on=False,
        )
    )
    # Navy header strip
    header_h = 0.13
    axb.add_patch(
        Rectangle(
            (left, bottom + height_b - header_h),
            width_b,
            header_h,
            facecolor=NAVY,
            edgecolor=NAVY,
            linewidth=0,
            transform=axb.transAxes,
            clip_on=False,
        )
    )
    axb.text(
        0.5,
        bottom + height_b - header_h / 2,
        "IRexp",
        ha="center",
        va="center",
        fontsize=10.5,
        fontweight="bold",
        color="white",
        transform=axb.transAxes,
    )

    # Manuscript-aligned facts (caption Panel B + abstract)
    rows = [
        ("Object", "Peak lists (cm$^{-1}$), not absorbance traces"),
        ("Redistribution", "Bulk download (JSONL)"),
        ("Licences", "Per-record pools (commercial / NC* / SA)"),
        ("Provenance", "DOI-traceable PMC OA or Chemotion"),
        ("Commercial pool", f"{N_COMM:,} CC-BY/CC0 records"),
    ]

    n = len(rows)
    y_top = bottom + height_b - header_h - 0.04
    y_bot = bottom + 0.04
    row_h = (y_top - y_bot) / n

    for i, (key, val) in enumerate(rows):
        y_c = y_top - (i + 0.5) * row_h
        # subtle alternating band
        if i % 2 == 0:
            axb.add_patch(
                Rectangle(
                    (left + 0.015, y_c - row_h * 0.42),
                    width_b - 0.03,
                    row_h * 0.84,
                    facecolor=SOFT,
                    edgecolor="none",
                    transform=axb.transAxes,
                    clip_on=False,
                    zorder=0,
                )
            )
        # left accent bar
        axb.add_patch(
            Rectangle(
                (left + 0.025, y_c - row_h * 0.28),
                0.012,
                row_h * 0.56,
                facecolor=BLUE if i != 4 else GREEN,
                edgecolor="none",
                transform=axb.transAxes,
                clip_on=False,
                zorder=1,
            )
        )
        axb.text(
            left + 0.055,
            y_c + row_h * 0.16,
            key,
            ha="left",
            va="center",
            fontsize=7.0,
            fontweight="bold",
            color=INK,
            transform=axb.transAxes,
            zorder=2,
        )
        axb.text(
            left + 0.055,
            y_c - row_h * 0.18,
            val,
            ha="left",
            va="center",
            fontsize=6.6,
            color=NOTE,
            transform=axb.transAxes,
            zorder=2,
        )

    fig.savefig(OUT / "fig_irexp_positioning.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_positioning.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_positioning.pdf'}")
    print(f"wrote {OUT / 'fig_irexp_positioning.png'}")


if __name__ == "__main__":
    main()
