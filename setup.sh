#!/usr/bin/env bash
set -euo pipefail

# Optional helper script to create a venv and install requirements locally.
# SWAN's Venv builder usually handles creation and installation automatically,
# but you can include this for local testing or extra setup steps.

VENV_DIR=".venv"
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
if [ -f requirements.txt ]; then
  pip install -r requirements.txt
fi

echo "Local venv created at $VENV_DIR and requirements installed."
