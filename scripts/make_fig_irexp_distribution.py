#!/usr/bin/env python3
"""Fig 3 — composition + band-count histogram + validation.
Uses serialized histogram/audit arrays under data/ (from spectro-agent irexp.jsonl.gz).
Design: DejaVu Sans, ink #111111, values bold in right columns, PDF42 + PNG 600dpi.
"""
from __future__ import annotations

import json
import os
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
GRAY = "#9AA0A6"
INK = "#111111"
NOTE = "#666666"
FAINT = "#E8EAEC"
TRACK = "#EEF1F4"
FONT = "DejaVu Sans"

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
MED_PMC = 9
MED_CHEM = 39

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
            "savefig.dpi": 600,
        }
    )


def _hbar_col(ax, labels, values, colors, title: str) -> None:
    """Horizontal bars with ALL counts in one right-aligned numeric column outside bars."""
    y = np.arange(len(labels))
    vmax = max(values)
    # leave room on the right for the numeric column
    ax.set_xlim(0, vmax * 1.52)
    ax.barh(y, values, color=colors, height=0.62, edgecolor="white", linewidth=0.35, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=7.6, color=INK, fontweight="normal")
    ax.invert_yaxis()
    ax.set_title(title, fontsize=9.5, fontweight="bold", color=INK, pad=7, loc="left")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=0, labelcolor=INK)
    ax.xaxis.grid(True, color=FAINT, lw=0.5, zorder=0)
    ax.set_axisbelow(True)
    # snap numeric column to a fixed x (right side), right-aligned
    x_col = vmax * 1.50
    for yi, v in zip(y, values):
        ax.text(
            x_col,
            yi,
            f"{v:,}",
            va="center",
            ha="right",
            fontsize=7.5,
            fontweight="bold",
            color=INK,
            zorder=4,
            family=FONT,
        )


def _panel(ax, letter: str, x: float = -0.14, y: float = 1.14) -> None:
    ax.text(
        x,
        y,
        letter,
        transform=ax.transAxes,
        fontsize=12,
        fontweight="bold",
        va="bottom",
        color=INK,
    )


def _load_hist():
    path = ROOT / "data" / "band_count_histogram.json"
    data = json.loads(path.read_text())
    return list(data["binned_x"]), list(data["binned_y"])


def _load_validation():
    path = ROOT / "data" / "validation_distributions.json"
    return json.loads(path.read_text())


def _validation_histogram(ax, title: str, data: np.ndarray, aggregate: float,
                          xlabel: str, xmax: float, agg_label: str = "Rate") -> None:
    bins = np.linspace(0, xmax, min(25, max(10, len(np.unique(data)) + 2)))
    ax.hist(data, bins=bins, color=BLUE, edgecolor="white", linewidth=0.3, zorder=2)
    ax.set_xlim(0, xmax)
    ax.set_xlabel(xlabel, fontsize=6.2, fontweight="normal", color=NOTE, labelpad=1)
    ax.set_title(title, fontsize=6.8, fontweight="bold", color=INK, pad=3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", left=False, labelleft=False, labelcolor=INK)
    ax.tick_params(axis="x", labelsize=5.8, labelcolor=INK, pad=1)
    med = float(np.median(data))
    ymax = ax.get_ylim()[1]
    # compact corner annotations (stay inside axes; no elbow lines that spill)
    ax.axvline(med, color=NOTE, lw=0.6, ls=(0, (2, 2)), zorder=4)
    ax.axvline(aggregate, color=ORANGE, lw=0.6, ls=(0, (2, 2)), zorder=4)
    # put labels on the opposite side of the mass to avoid bar occlusion / clipping
    side_right = aggregate < 0.45 * xmax
    tx = 0.97 if side_right else 0.03
    ha = "right" if side_right else "left"
    ax.text(
        tx,
        0.92,
        f"{agg_label} {aggregate:.3f}",
        transform=ax.transAxes,
        ha=ha,
        va="top",
        fontsize=5.8,
        fontweight="bold",
        color=INK,
        clip_on=True,
    )
    ax.text(
        tx,
        0.78,
        f"Median {med:.3f}",
        transform=ax.transAxes,
        ha=ha,
        va="top",
        fontsize=5.8,
        fontweight="bold",
        color=NOTE,
        clip_on=True,
    )


def main() -> None:
    _style()
    bx, by = _load_hist()
    # clip display to 0–40 bands (matches published v0.1 visual; long tail omitted)
    mask = [x <= 40 for x in bx]
    bx_d = [x for x, m in zip(bx, mask) if m]
    by_d = [y for y, m in zip(by, mask) if m]

    vf = _load_validation()
    tx_err = np.array(vf["transcription_errors"], dtype=float)
    paper_recall = np.array(vf["paper_recall"], dtype=float)
    list_match = np.array(vf["list_match"], dtype=float)
    fail_ct = np.array(vf["chemist_fail_counts"], dtype=float)
    agg = vf["aggregates"]

    fig = plt.figure(figsize=(7.4, 7.15))
    gs = fig.add_gridspec(
        2,
        3,
        height_ratios=[0.95, 1.25],
        hspace=0.58,
        wspace=0.50,
        left=0.09,
        right=0.99,
        top=0.94,
        bottom=0.06,
    )

    ax_a = fig.add_subplot(gs[0, 0])
    _panel(ax_a, "a")
    _hbar_col(ax_a, ["PMC OA", "Chemotion"], [PMC, CHEM], [BLUE, GREEN], "Source")

    ax_b = fig.add_subplot(gs[0, 1])
    _panel(ax_b, "b")
    _hbar_col(
        ax_b,
        ["commercial", "non-commercial", "empty / unknown", "ShareAlike", "other (ND)"],
        [COMM, NC, EMPTY, SA, OTHER],
        [BLUE, BLUE_SOFT, GRAY, GREEN, ORANGE],
        "Licence pool",
    )

    ax_c = fig.add_subplot(gs[0, 2])
    _panel(ax_c, "c")
    _hbar_col(
        ax_c,
        ["all records", "+ NMR string", "structure-linked", "full quadruplet"],
        [ALL, NMR, STRUCT, QUAD],
        [NAVY, BLUE, BLUE_SOFT, ORANGE],
        "Modality linkage",
    )

    # d — real band-count HISTOGRAM with median line (from serialized spectro-agent counts)
    ax_d = fig.add_subplot(gs[1, 0])
    _panel(ax_d, "d")
    ax_d.bar(bx_d, by_d, width=1.8, color=BLUE, edgecolor="white", linewidth=0.3, zorder=3)
    ax_d.set_xlabel("IR bands per record", fontsize=8.0, fontweight="normal", color=INK)
    ax_d.set_title("Band-count distribution", fontsize=9.5, fontweight="bold", color=INK, pad=6, loc="left")
    ax_d.spines["top"].set_visible(False)
    ax_d.spines["right"].set_visible(False)
    ax_d.set_xlim(0, 42)
    ax_d.yaxis.grid(True, color=FAINT, lw=0.5, zorder=0)
    ax_d.set_axisbelow(True)
    ax_d.tick_params(length=3, color=NOTE, labelcolor=INK, labelsize=7.2)
    ymax = max(by_d) if by_d else 1
    ax_d.axvline(MED_PMC, color=NOTE, lw=0.9, ls=(0, (3, 2)), zorder=4)
    ax_d.text(
        MED_PMC + 0.7,
        ymax * 0.92,
        f"PMC median {MED_PMC}",
        fontsize=7.2,
        fontweight="bold",
        color=INK,
        zorder=5,
    )
    # subtle Chemotion note
    ax_d.text(
        0.98,
        0.04,
        f"Chemotion median {MED_CHEM}",
        transform=ax_d.transAxes,
        ha="right",
        va="bottom",
        fontsize=6.6,
        color=NOTE,
    )

    # e — elemental distribution
    gs_e = gs[1, 1].subgridspec(1, 2, wspace=0.45)
    ax_e0 = fig.add_subplot(gs_e[0, 0])
    ax_e1 = fig.add_subplot(gs_e[0, 1])
    _panel(ax_e0, "e", x=-0.28)
    ax_e0.set_title("Elemental distribution", fontsize=9.5, fontweight="bold", color=INK, pad=8, loc="left")

    def _el(ax, pairs, heading: str) -> None:
        labs = [p[0] for p in pairs]
        vals = [p[1] for p in pairs]
        y = np.arange(len(labs))
        ax.barh(y, vals, color=BLUE, height=0.58, edgecolor="white", linewidth=0.3, zorder=3)
        ax.set_yticks(y)
        ax.set_yticklabels(labs, fontsize=7.2, color=INK, fontweight="normal")
        ax.invert_yaxis()
        ax.set_xlabel(heading, fontsize=7.0, color=NOTE)
        xmax = max(vals) * 1.55 if max(vals) else 1
        ax.set_xlim(0, xmax)
        x_col = xmax * 0.98
        for i, v in enumerate(vals):
            ax.text(x_col, i, f"{v:,}", ha="right", va="center", fontsize=6.6, fontweight="bold", color=INK)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(axis="x", length=0, labelbottom=False)
        ax.tick_params(axis="y", length=0, labelcolor=INK)

    _el(ax_e0, EL_MAJOR, "Major")
    _el(ax_e1, EL_TRACE, "Trace")

    # f — 2×2 validation histograms (real audit arrays)
    gs_f = gs[1, 2].subgridspec(2, 2, hspace=1.15, wspace=0.70)
    # letter on a phantom axes spanning the cell
    ax_f_phantom = fig.add_subplot(gs[1, 2])
    ax_f_phantom.set_axis_off()
    # letter only — avoid title collision with 2x2 subplot titles
    _panel(ax_f_phantom, "f", x=-0.06, y=1.10)
    ax_f_phantom.text(
        0.0,
        1.02,
        "Automated validation",
        transform=ax_f_phantom.transAxes,
        fontsize=9.5,
        fontweight="bold",
        color=INK,
        va="bottom",
        ha="left",
        clip_on=False,
    )

    ax_f1 = fig.add_subplot(gs_f[0, 0])
    _validation_histogram(
        ax_f1,
        "Transcription (n=200)",
        tx_err,
        float(agg["mae_proxy"]),
        "error rate",
        1.05,
        agg_label="MAE proxy",
    )
    ax_f2 = fig.add_subplot(gs_f[0, 1])
    _validation_histogram(
        ax_f2,
        "Band recall (n=120)",
        paper_recall,
        float(agg["band_recall_rate"]),
        "band rate",
        1.05,
        agg_label="Pool",
    )
    ax_f3 = fig.add_subplot(gs_f[1, 0])
    _validation_histogram(
        ax_f3,
        "List match (n=120)",
        list_match,
        float(agg["list_match_rate"]),
        "list rate",
        1.05,
        agg_label="Pool",
    )
    ax_f4 = fig.add_subplot(gs_f[1, 1])
    _validation_histogram(
        ax_f4,
        "Chemist-proxy (n=280)",
        fail_ct,
        float(agg["chemist_fail_rate"]),
        "fail count",
        max(4.0, float(fail_ct.max()) + 0.5),
        agg_label="Fail rate",
    )

    fig.savefig(OUT / "fig_irexp_distribution.pdf", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_distribution.png", dpi=600, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_distribution.pdf'}")
    print(f"wrote {OUT / 'fig_irexp_distribution.png'}")


if __name__ == "__main__":
    if os.environ.get("IREXP_REGEN_DISTRIBUTION") != "1":
        raise SystemExit(
            "Refusing to overwrite fig_irexp_distribution.* without "
            "IREXP_REGEN_DISTRIBUTION=1 (requires data/band_count_histogram.json)."
        )
    main()
