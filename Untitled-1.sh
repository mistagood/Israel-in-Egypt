#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# 1) activate virtualenv
if [ -f ".venv/bin/activate" ]; then
  # shellcheck source=/dev/null
  source .venv/bin/activate
else
  echo ".venv not found; activate your venv manually" >&2
  exit 1
fi

# 2) load OPENAI_API_KEY from .env (safe: strips quotes)
if [ -f ".env" ]; then
  export OPENAI_API_KEY="$(grep -m1 '^OPENAI_API_KEY=' .env | cut -d= -f2- | sed -E 's/^["'\'']|["'\'']$//g')"
fi

# 3) ensure key present
if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "OPENAI_API_KEY not set. Add it to .env or export it in your shell." >&2
  exit 2
fi

# 4) run the generator (unbuffered so you see progress)
python3 -u "video creation/video_generation.py"