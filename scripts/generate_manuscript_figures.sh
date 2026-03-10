#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${1:-/tmp/nrr-ime_current_figures}"

export XDG_CACHE_HOME="${XDG_CACHE_HOME:-$ROOT/.cache}"
export MPLCONFIGDIR="${MPLCONFIGDIR:-$ROOT/.mplconfig}"
export MPLBACKEND="${MPLBACKEND:-Agg}"
mkdir -p "$XDG_CACHE_HOME/fontconfig" "$MPLCONFIGDIR" "$OUT_DIR"

python3 "$ROOT/experiments/generate_figures.py" --output-dir "$OUT_DIR"
