"""Fig 3 - composition + automated validation. Frozen counts only (no bulk JSONL).

IMPORTANT - publication assets:
  Panel (d) must remain a real band-count HISTOGRAM with median line, and panel (f)
  must keep mini-histograms / clear metrics. Those panels require bulk JSONL /
  validation artefacts that are NOT in this postcard repo. Regenerating from this
  script alone yields a degraded median-bar + text-card figure (v0.5 regression).

  Keep the frozen PNG/PDF under figures/ (restored from release v0.4 / commit
  3f7e128). Do NOT overwrite fig_irexp_distribution.png/.pdf from this script
  unless bulk inputs are restored and panel d/f match v0.4 quality.

  Guard: set IREXP_REGEN_DISTRIBUTION=1 to force regeneration.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#1B3A4B"
BLUE = "#4A7EBB"
BLUE_SOFT = "#8FB4D9"
ORANGE = "#D97B32"
GREEN = "#3D8B5E"
GRAY = "#B7BDC3"
PEACH = "#E8B86D"
INK = "#1A1A1A"
NOTE = "#5C636A"
FAINT = "#E8EAEC"
TRACK = "#EEF1F4"
FONT = "DejaVu Sans"

# Frozen (data/irexp_stats.json, data/qc_structure_nmr.json, resolved_stats.json)
PMC = 119_345
CHEM = 1_888
COMM = 88_545
NC = 21_823
EMPTY = 8_963
SA = 1_897
OTHER = 5
ALL = 121_233
NMR = 87_075
STRUCT = 43_060
QUAD = 33_201

# Elemental presence in structure-linked subset, transcribed from the
# previous frozen figure (do not invent new chemistry counts).
EL_MAJOR = [
    ("C", 43_047),
    ("O", 38_870),
    ("N", 36_292),
    ("S", 12_258),
    ("Cl", 7_675),
    ("F", 5_939),
    ("Br", 3_923),
    ("Si", 959),
    ("P", 855),
]
EL_TRACE = [
    ("I", 904),
    ("Se", 384),
    ("B", 270),
    ("Fe", 119),
    ("Te", 73),
    ("Sn", 64),
    ("K", 24),
    ("Na", 16),
    ("Ge", 1),
]


def _style() -> None:
    plt.rcParams.update(
        {
            "font.family": FONT,
            "font.size": 8,
            "axes.linewidth": 0.6,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def _hbar(ax, labels, values, colors, title: str, log: bool = False) -> None:
    y = np.arange(len(labels))
    ax.barh(y, values, color=colors, height=0.62, edgecolor="white", linewidth=0.4)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=7.5, color=INK)
    ax.invert_yaxis()
    ax.set_title(title, fontsize=9, fontweight="bold", color=INK, pad=6, loc="left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=0, labelcolor=INK)
    ax.xaxis.grid(True, color=FAINT, lw=0.5)
    ax.set_axisbelow(True)
    if log:
        ax.set_xscale("log")
        ax.set_xlabel(r"log$_{10}$ records", fontsize=7, color=NOTE)
    xmax = max(values) * (1.28 if not log else 2.2)
    if not log:
        ax.set_xlim(0, xmax)
    for yi, v in zip(y, values):
        ax.text(v * (1.03 if not log else 1.15), yi, f"{v:,}", va="center", ha="left", fontsize=6.8, color=NOTE)


def _panel(ax, letter: str) -> None:
    ax.text(-0.12, 1.12, letter, transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")


def main() -> None:
    _style()
    fig = plt.figure(figsize=(7.2, 6.55))
    gs = fig.add_gridspec(
        2,
        3,
        height_ratios=[1.0, 1.12],
        hspace=0.55,
        wspace=0.55,
        left=0.10,
        right=0.98,
        top=0.93,
        bottom=0.07,
    )

    ax_a = fig.add_subplot(gs[0, 0])
    _panel(ax_a, "a")
    _hbar(ax_a, ["PMC OA", "Chemotion"], [PMC, CHEM], [BLUE, GREEN], "Source")

    ax_b = fig.add_subplot(gs[0, 1])
    _panel(ax_b, "b")
    _hbar(
        ax_b,
        ["commercial", "non-commercial", "empty / unknown", "ShareAlike", "other (ND)"],
        [COMM, NC, EMPTY, SA, OTHER],
        [BLUE, BLUE_SOFT, GRAY, GREEN, ORANGE],
        "Licence pool",
    )

    ax_c = fig.add_subplot(gs[0, 2])
    _panel(ax_c, "c")
    _hbar(
        ax_c,
        ["all records", "+ NMR string", "structure-linked", "full quadruplet"],
        [ALL, NMR, STRUCT, QUAD],
        [NAVY, BLUE, BLUE_SOFT, ORANGE],
        "Modality linkage",
    )

    # d - published medians only (bulk JSONL / per-record histogram not in this repo)
    ax_d = fig.add_subplot(gs[1, 0])
    _panel(ax_d, "d")
    med_labels = ["PMC", "Chemotion"]
    med_vals = [9, 39]
    ax_d.bar([0, 1], med_vals, color=[BLUE, GREEN], width=0.55, edgecolor="white", linewidth=0.4)
    for x, v in zip((0, 1), med_vals):
        ax_d.text(x, v + 1.2, str(v), ha="center", va="bottom", fontsize=8, color=NOTE)
    ax_d.set_xticks([0, 1])
    ax_d.set_xticklabels(med_labels, fontsize=8)
    ax_d.set_ylabel("Median bands / record", fontsize=7.5, color=INK)
    ax_d.set_ylim(0, 48)
    ax_d.set_title("Band-count medians", fontsize=9, fontweight="bold", color=INK, pad=6, loc="left")
    ax_d.spines["top"].set_visible(False)
    ax_d.spines["right"].set_visible(False)
    ax_d.tick_params(length=3, color=NOTE, labelcolor=INK)
    ax_d.yaxis.grid(True, color=FAINT, lw=0.5)
    ax_d.set_axisbelow(True)

    gs_e = gs[1, 1].subgridspec(1, 2, wspace=0.55)
    ax_e0 = fig.add_subplot(gs_e[0, 0])
    ax_e1 = fig.add_subplot(gs_e[0, 1])
    _panel(ax_e0, "e")
    ax_e0.set_title("Elemental distribution", fontsize=9, fontweight="bold", color=INK, pad=8, loc="left")
    y = np.arange(len(EL_MAJOR))

    def _el(ax, pairs, heading: str) -> None:
        labs = [p[0] for p in pairs]
        vals = [p[1] for p in pairs]
        ax.barh(y, vals, color=BLUE, height=0.58, edgecolor="white", linewidth=0.3)
        ax.set_yticks(y)
        ax.set_yticklabels(labs, fontsize=7)
        ax.invert_yaxis()
        ax.set_xlabel(heading, fontsize=7, color=NOTE)
        xmax = max(vals) * 1.45 if max(vals) else 1
        ax.set_xlim(0, xmax)
        for i, v in enumerate(vals):
            ax.text(v + xmax * 0.03, i, f"{v:,}", ha="left", va="center", fontsize=6.2, color=NOTE)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", length=0, labelbottom=False)
        ax.tick_params(axis="y", length=0)

    _el(ax_e0, EL_MAJOR, "Major")
    _el(ax_e1, EL_TRACE, "Trace")

    ax_f = fig.add_subplot(gs[1, 2])
    _panel(ax_f, "f")
    ax_f.set_title("Automated validation", fontsize=9, fontweight="bold", color=INK, pad=6, loc="left")
    ax_f.set_xlim(0, 10)
    ax_f.set_ylim(0, 10)
    ax_f.axis("off")
    cells = [
        (0.15, 5.25, "Transcription  n=200", "99.51% bands", "MAE 0.0049"),
        (5.25, 5.25, "Band recall  n=120", "0.9903", "CI 0.9879-0.9922"),
        (0.15, 0.35, "List match  n=120", "0.9848", "CI 0.9743-0.9911"),
        (5.25, 0.35, "Chemist-proxy  n=280", "271/280", "fail 0.0321"),
    ]
    for x, y, title, big, small in cells:
        ax_f.add_patch(plt.Rectangle((x, y), 4.6, 4.4, fill=True, facecolor=TRACK, edgecolor=FAINT, lw=0.6))
        ax_f.text(x + 2.3, y + 3.5, title, ha="center", va="center", fontsize=6.6, color=NOTE)
        ax_f.text(x + 2.3, y + 2.2, big, ha="center", va="center", fontsize=8.2, fontweight="bold", color=NAVY)
        ax_f.text(x + 2.3, y + 1.1, small, ha="center", va="center", fontsize=6.2, color=ORANGE)

    fig.savefig(OUT / "fig_irexp_distribution.pdf", dpi=300, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_distribution.png", dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_distribution.pdf'}")


if __name__ == "__main__":
    import os
    # FROZEN_DISTRIBUTION_ASSETS: refuse overwrite unless explicitly forced.
    if os.environ.get("IREXP_REGEN_DISTRIBUTION") != "1":
        raise SystemExit(
            "Refusing to overwrite fig_irexp_distribution.* - frozen v0.4 "
            "histogram assets require bulk JSONL. Set IREXP_REGEN_DISTRIBUTION=1 "
            "to force."
        )
    main()
