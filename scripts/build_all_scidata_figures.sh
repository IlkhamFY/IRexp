#!/usr/bin/env bash
# Regenerate IRexp Scientific Data figures into figures/.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "=== IRexp Scientific Data figures ==="
python3 scripts/make_fig_irexp_positioning.py
# Fig 2 (fig_irexp_pipeline) is exported from the Wonder design, not this script.
# python3 scripts/make_fig_irexp_pipeline.py
IREXP_REGEN_DISTRIBUTION=1 python3 scripts/make_fig_irexp_distribution.py

echo ""
echo "Output:"
ls -lh figures/fig_irexp_*.{pdf,png} 2>/dev/null
