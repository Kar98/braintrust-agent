# Install all dependencies (all groups and workspace projects)
sync:
    uv sync --all-groups --all-packages

# Run all checks (lint, format check, type check)
check: lint format-check typecheck

# Run all checks and fix what can be fixed
fix: lint-fix format

# Lint the codebase
lint:
    uv run ruff check .

# Lint and auto-fix
lint-fix:
    uv run ruff check --fix .

# Check formatting (no changes)
format-check:
    uv run ruff format --check .

# Format the codebase
format:
    uv run ruff format .

# Type check
typecheck:
    uv tool run ty check .
