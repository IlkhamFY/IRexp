#!/usr/bin/env python3
"""Fig 1 — IRexp vs major IR resources. Broken y-axis; Zipoli as stub/callout only.
Frozen counts only. Design system: DejaVu Sans, ink #111111, PDF fonttype 42, PNG 600 dpi.
v0.8: no full-height Zipoli bar; wider IRexp gaps; view-only labels #444.
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
INK = "#111111"
NOTE = "#444444"  # view-only / secondary labels (was #999/#666 — quieter than IRexp bold)
GRAY = "#9AA0A6"
ZIPOLI_FILL = "#DCE6F0"
ZIPOLI_EDGE = "#9BB0C4"
FAINT = "#E8EAEC"
SOFT = "#F7F8FA"
LINE = "#D0D4D8"
FONT = "DejaVu Sans"

# Bottom axis holds all experimental bars (IRexp 121k); Zipoli lives in top callout only
Y_BOT_MAX = 130_000
Y_TOP_MIN = 165_000
Y_TOP_MAX = 185_000


def _fmt(n: int) -> str:
    return f"{n:,}"


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
            "savefig.dpi": 600,
        }
    )

    fig = plt.figure(figsize=(7.2, 3.85))
    gs = fig.add_gridspec(
        1,
        2,
        width_ratios=[1.58, 0.95],
        wspace=0.12,
        left=0.10,
        right=0.985,
        top=0.86,
        bottom=0.24,
    )
    gs_left = gs[0, 0].subgridspec(2, 1, height_ratios=[0.18, 1.0], hspace=0.06)
    ax_top = fig.add_subplot(gs_left[0, 0])
    ax = fig.add_subplot(gs_left[1, 0], sharex=ax_top)
    axb = fig.add_subplot(gs[0, 1])

    x0 = [0.0, 1.05, 2.45, 3.95]
    width_irexp = 0.24
    gap = 0.50  # wider gap so IRexp value labels do not crowd

    def _draw_experimental(ax_draw) -> None:
        ax_draw.axhline(0, color=INK, lw=0.55, zorder=2)

        # SDBS / NIST (view-only, hatched mid-gray)
        for i, total in enumerate([SDBS, NIST]):
            x = x0[i]
            bars = ax_draw.bar(
                [x],
                [total],
                width=0.46,
                color=GRAY,
                edgecolor="#6E747A",
                linewidth=0.55,
                zorder=3,
            )
            bars[0].set_hatch("///")
            ax_draw.text(
                x,
                total + 2800,
                _fmt(total),
                ha="center",
                va="bottom",
                fontsize=7.0,
                fontweight="normal",
                color=NOTE,
            )

        # Zipoli — NO full-height bar. Narrow stub + "see ↑" in computed column only.
        x = x0[2]
        stub_h = 12_000  # short marker, does not fill the strip / bottom panel
        ax_draw.bar(
            [x],
            [stub_h],
            width=0.22,
            color=ZIPOLI_FILL,
            edgecolor=ZIPOLI_EDGE,
            linewidth=0.7,
            zorder=3,
        )
        ax_draw.text(
            x,
            stub_h + 3500,
            "see ↑",
            ha="center",
            va="bottom",
            fontsize=6.8,
            fontweight="bold",
            color=NOTE,
        )

        # IRexp triple — strong fills, wider gaps, bold dark values
        x = x0[3]
        xs = [x - gap, x, x + gap]
        vals = [N_ALL, N_STRUCT, N_COMM]
        cols = [NAVY, ORANGE, BLUE]
        ax_draw.bar(
            xs,
            vals,
            width=width_irexp,
            color=cols,
            edgecolor="white",
            linewidth=0.35,
            zorder=3,
        )
        for xv, v in zip(xs, vals):
            ax_draw.text(
                xv,
                v + 2200,
                _fmt(v),
                ha="center",
                va="bottom",
                fontsize=7.0,
                fontweight="bold",
                color=INK,
            )

    def _draw_zipoli_callout(ax_draw) -> None:
        """Top strip: thin marker + secondary label — never a full-width tall bar."""
        x = x0[2]
        # short horizontal stub / tick marker at mid of top window
        y_mark = (Y_TOP_MIN + Y_TOP_MAX) / 2
        ax_draw.plot(
            [x - 0.14, x + 0.14],
            [y_mark, y_mark],
            color=ZIPOLI_EDGE,
            lw=2.2,
            solid_capstyle="round",
            zorder=4,
            clip_on=False,
        )
        ax_draw.plot(
            [x],
            [y_mark],
            marker="o",
            markersize=4.5,
            color=ZIPOLI_FILL,
            markeredgecolor=ZIPOLI_EDGE,
            markeredgewidth=0.8,
            zorder=5,
            clip_on=False,
        )
        ax_draw.text(
            x,
            y_mark + 4500,
            f"{_fmt(ZIPOLI)} (simulated)",
            ha="center",
            va="bottom",
            fontsize=6.8,
            fontweight="bold",
            color=NOTE,
            clip_on=False,
        )

    _draw_experimental(ax)
    _draw_zipoli_callout(ax_top)

    ax_top.set_ylim(Y_TOP_MIN, Y_TOP_MAX)
    ax.set_ylim(0, Y_BOT_MAX)
    ax_top.set_xlim(-0.55, 4.65)
    ax.set_xlim(-0.55, 4.65)

    ax_top.spines["bottom"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax_top.tick_params(axis="x", bottom=False, labelbottom=False, length=0)
    ax_top.spines["top"].set_visible(False)
    ax_top.spines["right"].set_visible(False)
    ax.spines["right"].set_visible(False)

    d = 0.015
    kwargs = dict(transform=ax_top.transAxes, color=INK, clip_on=False, lw=0.7)
    ax_top.plot((-d, +d), (-d * 3, +d * 3), **kwargs)
    ax_top.plot((1 - d, 1 + d), (-d * 3, +d * 3), **kwargs)
    kwargs.update(transform=ax.transAxes)
    ax.plot((-d, +d), (1 - d * 3, 1 + d * 3), **kwargs)
    ax.plot((1 - d, 1 + d), (1 - d * 3, 1 + d * 3), **kwargs)

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
    ax.set_ylabel("Number of IR records", fontsize=9, color=INK, labelpad=4)
    for a in (ax, ax_top):
        a.yaxis.set_major_formatter(FuncFormatter(_thousands))
        a.tick_params(length=3, color="#666666", labelcolor=INK)
        a.yaxis.grid(True, color=FAINT, lw=0.5, zorder=0)
        a.set_axisbelow(True)

    def _bracket(x1: float, x2: float, y: float, text: str) -> None:
        ax_top.plot(
            [x1, x1, x2, x2],
            [y - 2500, y, y, y - 2500],
            color="#666666",
            lw=0.7,
            clip_on=False,
        )
        ax_top.text(
            (x1 + x2) / 2,
            y + 1200,
            text,
            ha="center",
            va="bottom",
            fontsize=7.2,
            color="#666666",
            fontweight="normal",
            clip_on=False,
        )

    _bracket(-0.30, 1.35, 183_500, "View-only")
    _bracket(2.20, 2.70, 183_500, "Computed")
    _bracket(3.45, 4.45, 183_500, "This work")

    ax_top.text(
        -0.14,
        1.55,
        "A",
        transform=ax_top.transAxes,
        fontsize=12,
        fontweight="bold",
        va="bottom",
        color=INK,
    )

    legend = [
        Patch(facecolor=NAVY, edgecolor="none", label="All"),
        Patch(facecolor=ORANGE, edgecolor="none", label="Structure-linked"),
        Patch(facecolor=BLUE, edgecolor="none", label="CC-BY/CC0"),
        Patch(facecolor=GRAY, edgecolor="#6E747A", hatch="///", label="View-only"),
        Patch(facecolor=ZIPOLI_FILL, edgecolor=ZIPOLI_EDGE, label="Computed (callout)"),
    ]
    ax.legend(
        handles=legend,
        loc="upper left",
        bbox_to_anchor=(0.0, -0.22),
        ncol=3,
        frameon=False,
        fontsize=7.0,
        handlelength=1.15,
        columnspacing=1.0,
        handletextpad=0.4,
    )

    # --- B: attribute card ---------------------------------------------------
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
        color=INK,
    )

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
    header_h = 0.135
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
        fontsize=11.5,
        fontweight="bold",
        color="white",
        transform=axb.transAxes,
    )

    rows = [
        ("Object", "Peak lists (cm$^{-1}$), not absorbance traces"),
        ("Redistribution", "Bulk download (JSONL)"),
        ("Licences", "Per-record pools (commercial / NC* / SA)"),
        ("Provenance", "DOI-traceable PMC OA or Chemotion"),
        ("Commercial pool", f"{N_COMM:,} CC-BY/CC0 records"),
    ]
    n = len(rows)
    y_top = bottom + height_b - header_h - 0.035
    y_bot = bottom + 0.035
    row_h = (y_top - y_bot) / n

    for i, (key, val) in enumerate(rows):
        y_c = y_top - (i + 0.5) * row_h
        if i % 2 == 0:
            axb.add_patch(
                Rectangle(
                    (left + 0.015, y_c - row_h * 0.44),
                    width_b - 0.03,
                    row_h * 0.88,
                    facecolor=SOFT,
                    edgecolor="none",
                    transform=axb.transAxes,
                    clip_on=False,
                    zorder=0,
                )
            )
        axb.add_patch(
            Rectangle(
                (left + 0.025, y_c - row_h * 0.30),
                0.012,
                row_h * 0.60,
                facecolor=BLUE if i != 4 else GREEN,
                edgecolor="none",
                transform=axb.transAxes,
                clip_on=False,
                zorder=1,
            )
        )
        axb.text(
            left + 0.055,
            y_c + row_h * 0.18,
            key,
            ha="left",
            va="center",
            fontsize=8.0,
            fontweight="bold",
            color=INK,
            transform=axb.transAxes,
            zorder=2,
        )
        axb.text(
            left + 0.055,
            y_c - row_h * 0.22,
            val,
            ha="left",
            va="center",
            fontsize=7.6,
            color="#666666",
            transform=axb.transAxes,
            zorder=2,
        )

    fig.savefig(OUT / "fig_irexp_positioning.pdf", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_positioning.png", dpi=600, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_positioning.pdf'}")
    print(f"wrote {OUT / 'fig_irexp_positioning.png'}")


if __name__ == "__main__":
    main()
