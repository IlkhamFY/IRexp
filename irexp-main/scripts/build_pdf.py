#!/usr/bin/env python3
"""Compile scientific_data.tex → scientific_data.pdf (flat Overleaf-ready layout)."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_DIR = ROOT
TEX = os.path.join(TEX_DIR, "scientific_data.tex")
OUT = os.path.join(TEX_DIR, "scientific_data.pdf")


def _engine() -> str | None:
    env = os.environ.get("PDF_ENGINE")
    if env and (os.path.isfile(env) or shutil.which(env)):
        return env if os.path.isfile(env) else shutil.which(env)
    for cand in ("/tmp/tectonic", "tectonic", "pdflatex", "xelatex"):
        if cand.startswith("/") and os.path.isfile(cand) and os.access(cand, os.X_OK):
            return cand
        found = shutil.which(cand)
        if found:
            return found
    return None


def _run(cmd: list[str], cwd: str, env: dict[str, str] | None = None) -> int:
    print("+", " ".join(cmd), flush=True)
    return subprocess.call(cmd, cwd=cwd, env=env)


def main() -> int:
    if not os.path.isfile(TEX):
        print(f"missing {TEX}", file=sys.stderr)
        return 1
    tex_styles = os.path.join(ROOT, "tex")
    if not os.path.isfile(os.path.join(tex_styles, "sn-jnl.cls")):
        print("missing vendored tex/sn-jnl.cls", file=sys.stderr)
        return 2
    engine = _engine()
    if not engine:
        print("no PDF engine (tectonic/pdflatex/xelatex)", file=sys.stderr)
        return 3
    env = os.environ.copy()
    texinputs = os.pathsep.join([tex_styles, TEX_DIR, env.get("TEXINPUTS", "")])
    bstinputs = os.pathsep.join([tex_styles, TEX_DIR, env.get("BSTINPUTS", "")])
    env["TEXINPUTS"] = texinputs
    env["BSTINPUTS"] = bstinputs
    base = os.path.basename(TEX)
    if os.path.basename(engine) == "tectonic" or engine.endswith("/tectonic"):
        rc = _run([engine, "--keep-logs", "--keep-intermediates", "-o", TEX_DIR, TEX], cwd=TEX_DIR, env=env)
    else:
        for _ in range(2):
            rc = _run([engine, "-interaction=nonstopmode", base], cwd=TEX_DIR, env=env)
            if rc != 0:
                break
        bibtex = shutil.which("bibtex")
        if bibtex and os.path.isfile(os.path.join(TEX_DIR, "scientific_data.aux")):
            _run([bibtex, "scientific_data"], cwd=TEX_DIR, env=env)
        for _ in range(2):
            rc = _run([engine, "-interaction=nonstopmode", base], cwd=TEX_DIR, env=env)
    if not os.path.isfile(OUT):
        print("build produced no PDF", file=sys.stderr)
        return 4
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
