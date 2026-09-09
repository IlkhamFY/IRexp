#!/usr/bin/env bash
# Regenerate IRexp Scientific Data figures into figures/.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "=== IRexp Scientific Data figures ==="
python3 scripts/make_fig_irexp_positioning.py
python3 scripts/make_fig_irexp_pipeline.py
python3 scripts/make_fig_irexp_distribution.py

echo ""
echo "Output:"
ls -lh figures/fig_irexp_*.{pdf,png} 2>/dev/null
