#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REQ_FILE="$SCRIPT_DIR/requirements.txt"
VENV_DIR="$SCRIPT_DIR/.venv"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python was not found on this system." >&2
  exit 1
fi

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <modules.xlsx|modules.csv> [--force]"
  exit 1
fi

INPUT_FILE="$1"
shift

# Allow passing a relative input directory from the repository root.
if [ ! -e "$INPUT_FILE" ]; then
  INPUT_FILE="$SCRIPT_DIR/$INPUT_FILE"
fi

if [ ! -x "$VENV_DIR/bin/python" ]; then
  echo "Creating Python environment for the CRUD generator..."
  if ! "$PYTHON_BIN" -m venv "$VENV_DIR"; then
    echo "Python venv support is missing. Install python3-venv and try again." >&2
    exit 1
  fi
fi

PYTHON_CMD="$VENV_DIR/bin/python"
"$PYTHON_CMD" -m pip install --disable-pip-version-check -r "$REQ_FILE"

"$PYTHON_CMD" "$SCRIPT_DIR/generator.py" "$INPUT_FILE" "$@"
