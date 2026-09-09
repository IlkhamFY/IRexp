#!/usr/bin/env python3
"""Fig 2 — harvest / cleaning workflow. Orthogonal alignment; ≥8pt body / ≥9pt headers.
Frozen counts. PDF fonttype 42 + PNG 600 dpi. Red highlights on bad QC tokens.
v0.8: title clear of numbered circles; QC icon clear of panel B title; equal box gaps.
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
        figsize=(7.2, 5.90),
        gridspec_kw={"height_ratios": [1.22, 1.00], "hspace": 0.18},
    )
    fig.subplots_adjust(left=0.035, right=0.98, top=0.955, bottom=0.035)

    # ----- A -----------------------------------------------------------------
    # Extra headroom so panel title sits above numbered circles with a clear gap.
    axa.set_xlim(0, 10)
    axa.set_ylim(0, 4.70)
    axa.axis("off")

    title_y = 4.58
    axa.text(0.05, title_y, "A", fontsize=12, fontweight="bold", va="center", color=INK)
    title_txt = axa.text(
        0.42,
        title_y,
        "Extraction and quality-control workflow",
        fontsize=10,
        fontweight="bold",
        va="center",
        color=INK,
    )

    # Equal gaps: narrower boxes → visibly equal breathing room across [0.20, 9.80]
    left, right = 0.18, 9.82
    w, h = 1.72, 1.18
    gap = (right - left - 5 * w) / 4
    assert abs(gap - ((right - left - 5 * w) / 4)) < 1e-9
    xs = [left + i * (w + gap) for i in range(5)]
    # Boxes low enough that circle tops sit well below the title band
    y = 2.42
    mid_y = y + h / 2
    circ_r = 0.145
    circ_y = y + h + 0.20  # centers only above their boxes

    steps = [
        ("1", "PMC OA text", ["188,016 PMCIDs", "S3 plain text"], BLUE),
        ("2", "IR extract", ["Regex band lists", "+ co-reported NMR"], BLUE),
        ("3", "Structure resolve", ["OPSIN → RDKit", "SMILES / InChIKey"], BLUE),
        ("4", "Licence join", ["Europe PMC", "+ Crossref"], ORANGE),
        ("5", "Release pools", ["HF + Zenodo", "JSONL pools"], NAVY),
    ]
    circle_centers = []
    for i, (num, title, lines, col) in enumerate(steps):
        x = xs[i]
        cx = x + w / 2
        circle_centers.append((cx, circ_y, circ_r))
        axa.add_patch(plt.Circle((cx, circ_y), circ_r, facecolor=col, edgecolor="none", zorder=5))
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
        _box(axa, x, y, w, h, title, lines, header=col, body_fs=8.0, head_fs=8.5)

    # Straight orthogonal mid-box arrows (true vertical midpoints)
    for i in range(4):
        x1 = xs[i] + w
        x2 = xs[i + 1]
        _arrow(axa, x1 + 0.02, mid_y, x2 - 0.02, mid_y, steps[i + 1][3])

    # Chemotion ELN — under step 2
    chem_x = xs[1]
    chem_w = w
    chem_y = 1.38
    chem_h = 0.72
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
        chem_y + chem_h - 0.22,
        "Chemotion ELN",
        ha="center",
        va="center",
        fontsize=9.0,
        fontweight="bold",
        color=GREEN,
    )
    axa.text(
        chem_x + chem_w / 2,
        chem_y + 0.24,
        "1,888 CC-BY-SA",
        ha="center",
        va="center",
        fontsize=8.0,
        color=INK,
        fontweight="normal",
    )
    _arrow(axa, chem_x + chem_w / 2, chem_y + chem_h + 0.02, xs[1] + w / 2, y - 0.02, GREEN)

    # Cleaning rules — under steps 3–4; leave gap before Final
    rules_x = xs[2]
    rules_right = xs[3] + w
    fin_x = xs[4]
    fin_w = w
    rules_w = min(rules_right - rules_x, fin_x - rules_x - 0.30)
    rules_y = 0.10
    rules_h = 1.10
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
        rules_y + rules_h - 0.20,
        "Cleaning rules",
        ha="center",
        va="center",
        fontsize=9.0,
        fontweight="bold",
        color=ORANGE,
    )
    rule_lines = [
        r"Band count ≥ 3 in 350–4000 cm$^{-1}$",
        r"Reject duplicate integers",
        r"$^{1}$H ≤ formula H+2  ·  $^{13}$C ≤ carbon count",
    ]
    for i, line in enumerate(rule_lines):
        axa.text(
            rules_x + rules_w / 2,
            rules_y + 0.64 - i * 0.20,
            line,
            ha="center",
            va="center",
            fontsize=7.0,
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
        fin_y + fin_h - 0.26,
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
    step5_cx = xs[4] + w / 2
    assert abs(fin_cx - step5_cx) < 1e-9, "Final IRexp must share horizontal center with step 5"
    _arrow(axa, step5_cx, y - 0.02, fin_cx, fin_y + fin_h + 0.02, NAVY)

    # ----- B — QC rejections; header clear of first-box prohibit icons --------
    axb.set_xlim(0, 10)
    axb.set_ylim(0, 3.55)
    axb.axis("off")
    b_title_y = 3.42
    axb.text(0.05, b_title_y, "B", fontsize=12, fontweight="bold", va="center", color=INK)
    axb.text(
        0.42,
        b_title_y,
        "Automated QC rejections",
        fontsize=10,
        fontweight="bold",
        va="center",
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
        ),
        (
            "IR band outside window",
            [
                ("IR (neat): 3200, 2958, ", INK, "normal"),
                ("4180", RED, "bold"),
                (r", 1520 cm$^{-1}$ — 4180 outside 350–4000 cm$^{-1}$.", INK, "normal"),
            ],
        ),
        (
            r"$^{1}$H integral vs formula",
            [
                (r"$^{1}$H: ", INK, "normal"),
                ("(5H)+(5H)+(10H)=20H", RED, "bold"),
                (r"; C$_6$H$_5$NO$_2$ (7H) — integral > H+2.", INK, "normal"),
            ],
        ),
    ]

    # First box top well below panel title (clear of "A" in Automated)
    box_h = 0.86
    top_box_y = 2.28  # top of first box = 2.28+0.86=3.14 << 3.42
    for i, (title, segs) in enumerate(examples):
        y0 = top_box_y - i * 1.02
        axb.add_patch(
            FancyBboxPatch(
                (0.22, y0),
                9.50,
                box_h,
                boxstyle="round,pad=0.02,rounding_size=0.04",
                linewidth=1.0,
                edgecolor=RED,
                facecolor=RED_BG,
            )
        )
        # Icon LEFT of example title with padding (box tops below panel header)
        axb.text(0.38, y0 + 0.58, "⊘", fontsize=12, color=RED, va="center", fontweight="bold")
        axb.text(
            0.72,
            y0 + 0.58,
            title,
            fontsize=9.0,
            fontweight="bold",
            color=RED,
            va="center",
            ha="left",
        )

        x_cursor = 0.72
        y_body = y0 + 0.24
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

    # --- Geometry assert: title bbox must not intersect any numbered circle ---
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    title_bb = title_txt.get_window_extent(renderer=renderer)
    title_data = title_bb.transformed(axa.transData.inverted())
    # Expand title bbox slightly for safety margin
    pad = 0.06
    t_x0, t_x1 = title_data.x0 - pad, title_data.x1 + pad
    t_y0, t_y1 = title_data.y0 - pad, title_data.y1 + pad
    for cx, cy, r in circle_centers:
        # circle intersects axis-aligned bbox if closest point is within r
        nearest_x = min(max(cx, t_x0), t_x1)
        nearest_y = min(max(cy, t_y0), t_y1)
        dist2 = (cx - nearest_x) ** 2 + (cy - nearest_y) ** 2
        assert dist2 > r * r, (
            f"Title bbox intersects circle at ({cx:.2f},{cy:.2f}): "
            f"title=[{t_x0:.2f},{t_x1:.2f}]x[{t_y0:.2f},{t_y1:.2f}]"
        )
    # Also assert circle tops below title bottom
    for cx, cy, r in circle_centers:
        assert cy + r < t_y0, f"Circle top {cy+r:.2f} not below title bottom {t_y0:.2f}"

    # Equal gap check
    gaps = [xs[i + 1] - (xs[i] + w) for i in range(4)]
    assert max(gaps) - min(gaps) < 1e-9, f"Unequal gaps: {gaps}"

    fig.savefig(OUT / "fig_irexp_pipeline.pdf", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_pipeline.png", dpi=600, bbox_inches="tight")
    fig.savefig(OUT / "fig_irexp_pipeline.svg", bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUT / 'fig_irexp_pipeline.pdf'}")
    print(f"wrote {OUT / 'fig_irexp_pipeline.png'}")
    print(f"assert OK: title/circle no-overlap; equal gaps={gaps[0]:.3f}; mid_y={mid_y:.3f}")


if __name__ == "__main__":
    main()
