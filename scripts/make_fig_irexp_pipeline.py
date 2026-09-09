#!/usr/bin/env python3
"""Fig 2 — harvest / cleaning workflow. Orthogonal alignment; ≥8pt body / ≥9pt headers.
Frozen counts. PDF fonttype 42 + PNG 600 dpi. Red highlights on bad QC tokens.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = "#1B3A4B"
BLUE = "#4A7EBB"
ORANGE = "#D97B32"
GREEN = "#3D8B5E"
INK = "#111111"
NOTE = "#666666"
LINE = "#C5C9CD"
FILL = "#FFFFFF"
SOFT = "#F4F6F8"
RED = "#C44E52"
RED_BG = "#FCECEC"
FONT = "DejaVu Sans"


def _box(ax, x, y, w, h, title, lines, header=BLUE, body_fs=8.0, head_fs=9.0):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="square,pad=0",
            linewidth=0.8,
            edgecolor=header,
            facecolor=FILL,
        )
    )
    hdr_h = 0.32
    ax.add_patch(
        Rectangle((x, y + h - hdr_h), w, hdr_h, facecolor=header, edgecolor=header, lw=0)
    )
    ax.text(
        x + w / 2,
        y + h - hdr_h / 2,
        title,
        ha="center",
        va="center",
        color="white",
        fontsize=head_fs,
        fontweight="bold",
    )
    # body lines centered in remaining area
    body_top = y + h - hdr_h - 0.08
    body_bot = y + 0.10
    n = len(lines)
    for i, line in enumerate(lines):
        yy = body_top - (i + 0.5) * (body_top - body_bot) / max(n, 1)
        ax.text(
            x + w / 2,
            yy,
            line,
            ha="center",
            va="center",
            fontsize=body_fs,
            color=INK,
            fontweight="normal",
        )


def _arrow(ax, x1, y1, x2, y2, color=BLUE):
    ax.add_patch(
        FancyArrowPatch(
            (x1, y1),
            (x2, y2),
            arrowstyle="-|>",
            mutation_scale=9,
            lw=1.0,
            color=color,
            shrinkA=0,
            shrinkB=0,
        )
    )


def _hl_text(ax, x, y, segments, fontsize=7.6, va="center"):
    """Draw mixed ink/red segments left-aligned from x,y (axes coords)."""
    # Use a single Annotation-like approach via fig.canvas measure is heavy;
    # approximate with fixed advances for this fixed figure width.
    cursor = x
    for text, color, weight in segments:
        ax.text(
            cursor,
            y,
            text,
            ha="left",
            va=va,
            fontsize=fontsize,
            color=color,
            fontweight=weight,
            family=FONT,
        )
        # crude advance: ~0.095 data-units per character at fs~7.6 on xlim=10
        cursor += 0.092 * len(text) * (fontsize / 7.6)


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": FONT,
            "font.size": 8.5,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.dpi": 600,
        }
    )
    fig, (axa, axb) = plt.subplots(
        2,
        1,
        figsize=(7.2, 5.70),
        gridspec_kw={"height_ratios": [1.20, 1.00], "hspace": 0.16},
    )
    fig.subplots_adjust(left=0.035, right=0.98, top=0.94, bottom=0.035)

    # ----- A -----------------------------------------------------------------
    axa.set_xlim(0, 10)
    axa.set_ylim(0, 4.35)
    axa.axis("off")
    axa.text(0.05, 4.22, "A", fontsize=12, fontweight="bold", va="top", color=INK)
    axa.text(
        0.40,
        4.22,
        "Extraction and quality-control workflow",
        fontsize=10,
        fontweight="bold",
        va="top",
        color=INK,
    )

    # Equal gaps: 5 boxes of width w with equal spacing across [0.25, 9.75]
    w, h = 1.70, 1.22
    gap = (9.50 - 5 * w) / 4  # equal gaps
    xs = [0.25 + i * (w + gap) for i in range(5)]
    y = 2.58
    mid_y = y + h / 2

    steps = [
        ("1", "PMC OA text", ["188,016 PMCIDs", "S3 plain text"], BLUE),
        ("2", "IR extract", ["Regex band lists", "+ co-reported NMR"], BLUE),
        ("3", "Structure resolve", ["OPSIN → RDKit", "SMILES / InChIKey"], BLUE),
        ("4", "Licence join", ["Europe PMC", "+ Crossref"], ORANGE),
        ("5", "Release pools", ["HF + Zenodo", "JSONL pools"], NAVY),
    ]
    for i, (num, title, lines, col) in enumerate(steps):
        x = xs[i]
        cx = x + w / 2
        # numbered circle perfectly centered above box
        circ_y = y + h + 0.22
        axa.add_patch(plt.Circle((cx, circ_y), 0.145, facecolor=col, edgecolor="none", zorder=5))
        axa.text(
            cx,
            circ_y,
            num,
            ha="center",
            va="center",
            color="white",
            fontsize=8,
            fontweight="bold",
            zorder=6,
        )
        _box(axa, x, y, w, h, title, lines, header=col, body_fs=8.0, head_fs=9.0)

    # straight orthogonal mid-box arrows
    for i in range(4):
        x1 = xs[i] + w
        x2 = xs[i + 1]
        _arrow(axa, x1 + 0.03, mid_y, x2 - 0.03, mid_y, steps[i + 1][3])

    # Chemotion ELN — under step 2, green arrow straight up into box 2
    chem_x = xs[1]
    chem_w = w
    chem_y = 1.48
    chem_h = 0.78
    axa.add_patch(
        FancyBboxPatch(
            (chem_x, chem_y),
            chem_w,
            chem_h,
            boxstyle="square,pad=0",
            linewidth=0.8,
            edgecolor=GREEN,
            facecolor=FILL,
        )
    )
    axa.text(
        chem_x + chem_w / 2,
        chem_y + chem_h - 0.24,
        "Chemotion ELN",
        ha="center",
        va="center",
        fontsize=9.0,
        fontweight="bold",
        color=GREEN,
    )
    axa.text(
        chem_x + chem_w / 2,
        chem_y + 0.26,
        "1,888 CC-BY-SA",
        ha="center",
        va="center",
        fontsize=8.0,
        color=INK,
        fontweight="normal",
    )
    # vertical orthogonal arrow into bottom of box 2
    _arrow(axa, chem_x + chem_w / 2, chem_y + chem_h + 0.02, xs[1] + w / 2, y - 0.02, GREEN)

    # Cleaning rules — aligned under steps 3–4; leave gap before Final
    rules_x = xs[2]
    rules_right = xs[3] + w
    fin_x = xs[4]
    fin_w = w
    # breathing room between rules and final
    rules_w = min(rules_right - rules_x, fin_x - rules_x - 0.28)
    rules_y = 0.12
    rules_h = 1.18
    axa.add_patch(
        FancyBboxPatch(
            (rules_x, rules_y),
            rules_w,
            rules_h,
            boxstyle="square,pad=0",
            linewidth=0.8,
            edgecolor=ORANGE,
            facecolor=SOFT,
        )
    )
    axa.text(
        rules_x + rules_w / 2,
        rules_y + rules_h - 0.22,
        "Cleaning rules",
        ha="center",
        va="center",
        fontsize=9.0,
        fontweight="bold",
        color=ORANGE,
    )
    # three short centered lines clipped to box (no spill into Final)
    rule_lines = [
        r"Band count ≥ 3 in 350–4000 cm$^{-1}$",
        r"Reject duplicate integers",
        r"$^{1}$H ≤ formula H+2  ·  $^{13}$C ≤ carbon count",
    ]
    for i, line in enumerate(rule_lines):
        axa.text(
            rules_x + rules_w / 2,
            rules_y + 0.68 - i * 0.22,
            line,
            ha="center",
            va="center",
            fontsize=7.2,
            color=INK,
            clip_on=True,
        )
    rules_cx = rules_x + rules_w / 2
    span_cx = (xs[2] + xs[3] + w) / 2
    _arrow(axa, span_cx, y - 0.02, rules_cx, rules_y + rules_h + 0.02, ORANGE)

    # Final IRexp — under step 5; arrow centered on both boxes
    fin_y = rules_y
    fin_h = rules_h
    axa.add_patch(
        FancyBboxPatch(
            (fin_x, fin_y),
            fin_w,
            fin_h,
            boxstyle="square,pad=0",
            linewidth=0.9,
            edgecolor=NAVY,
            facecolor=FILL,
        )
    )
    axa.text(
        fin_x + fin_w / 2,
        fin_y + fin_h - 0.28,
        "Final IRexp",
        ha="center",
        va="center",
        fontsize=9.0,
        fontweight="bold",
        color=NAVY,
    )
    axa.text(
        fin_x + fin_w / 2,
        fin_y + fin_h * 0.48,
        "121,233 band lists",
        ha="center",
        va="center",
        fontsize=8.0,
        fontweight="bold",
        color=INK,
    )
    axa.text(
        fin_x + fin_w / 2,
        fin_y + fin_h * 0.22,
        "43,060 structure-linked",
        ha="center",
        va="center",
        fontsize=7.6,
        fontweight="bold",
        color=ORANGE,
    )
    fin_cx = fin_x + fin_w / 2
    _arrow(axa, xs[4] + w / 2, y - 0.02, fin_cx, fin_y + fin_h + 0.02, NAVY)

    # ----- B — QC rejections with red callout rectangles + highlighted tokens -
    axb.set_xlim(0, 10)
    axb.set_ylim(0, 3.35)
    axb.axis("off")
    axb.text(0.05, 3.25, "B", fontsize=12, fontweight="bold", va="top", color=INK)
    axb.text(
        0.40,
        3.25,
        "Automated QC rejections",
        fontsize=10,
        fontweight="bold",
        va="top",
        color=INK,
    )

    examples = [
        (
            "Band count too low",
            [
                ("IR (KBr): ", INK, "normal"),
                ("3421, 2923, 2854", RED, "bold"),
                (r" cm$^{-1}$ — <3 unique peaks after de-duplication.", INK, "normal"),
            ],
            "3021–2854 group collapsed to duplicates / too few unique bands",
        ),
        (
            "IR band outside window",
            [
                ("IR (neat): 3200, 2958, ", INK, "normal"),
                ("4180", RED, "bold"),
                (r", 1520 cm$^{-1}$ — 4180 outside 350–4000 cm$^{-1}$.", INK, "normal"),
            ],
            None,
        ),
        (
            r"$^{1}$H integral vs formula",
            [
                (r"$^{1}$H: ", INK, "normal"),
                ("(5H)+(5H)+(10H)=20H", RED, "bold"),
                (r"; C$_6$H$_5$NO$_2$ (7H) — integral > H+2.", INK, "normal"),
            ],
            None,
        ),
    ]

    # Draw once so we can measure text extents for mixed-color body lines
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()

    for i, (title, segs, _note) in enumerate(examples):
        y0 = 2.45 - i * 1.00
        axb.add_patch(
            FancyBboxPatch(
                (0.22, y0),
                9.50,
                0.88,
                boxstyle="round,pad=0.02,rounding_size=0.04",
                linewidth=1.0,
                edgecolor=RED,
                facecolor=RED_BG,
            )
        )
        axb.text(0.42, y0 + 0.60, "⊘", fontsize=12, color=RED, va="center", fontweight="bold")
        axb.text(
            0.85,
            y0 + 0.60,
            title,
            fontsize=9.0,
            fontweight="bold",
            color=RED,
            va="center",
        )
        x_cursor = 0.85
        y_body = y0 + 0.26
        for frag, color, weight in segs:
            t = axb.text(
                x_cursor,
                y_body,
                frag,
                ha="left",
                va="center",
                fontsize=8.0,
                color=color,
                fontweight=weight,
            )
            fig.canvas.draw()
            bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
            bb_data = bb.transformed(axb.transData.inverted())
            x_cursor = bb_data.x1 + 0.02

    fig.savefig(OUT / "fig_irexp_pipeline.pdf", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_pipeline.png", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_pipeline.svg", bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_pipeline.pdf'}")
    print(f"wrote {OUT / 'fig_irexp_pipeline.png'}")


if __name__ == "__main__":
    main()
