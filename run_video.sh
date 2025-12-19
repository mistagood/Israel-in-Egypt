#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/garygreen/Code/Israel in Egypt"
PY="$ROOT/.venv/bin/python"
SCRIPT="$ROOT/video creation/video_generation.py"

if [ ! -x "$PY" ]; then
  PY="$(command -v python3)"
fi

if [ ! -f "$SCRIPT" ]; then
  echo "video_generation.py not found at: $SCRIPT" >&2
  exit 1
fi

exec "$PY" "$SCRIPT" "$@"
