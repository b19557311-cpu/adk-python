#!/bin/bash
set -e

echo "=== Installing uv ==="
curl -LsSf https://astral.sh/uv/install.sh | sh

# Source cargo/env or add uv to path for the rest of the script
export PATH="$HOME/.local/bin:$PATH"

echo "=== Creating Virtual Environment ==="
uv venv --python "python3.11" ".venv"
source .venv/bin/activate

echo "=== Installing dependencies for development ==="
uv sync --all-extras

echo "=== Installing development tools ==="
uv tool install pre-commit
uv tool install tox --with tox-uv

echo "=== Setting up pre-commit hooks ==="
pre-commit install

echo "=== Setup completed successfully ==="
