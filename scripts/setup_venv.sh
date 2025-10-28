#!/usr/bin/env bash
set -e

# Create a virtual environment in .venv, activate it and install requirements
python3 -m venv .venv
# shellcheck source=/dev/null
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Virtual environment created at .venv and requirements installed."