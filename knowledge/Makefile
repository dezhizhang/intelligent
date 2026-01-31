.PHONY: install install-dev serve lint format test coverage help

install:
    uv pip install -e .

install-dev:
    uv pip install -e ".[dev]"

serve:
    sudo uv run server.py

serve-dev:
    sudo uv run server.py --reload

lint:
    uv run black --check .


format:
    uv run black .

test:
    uv run pytest tests

coverage:
    uv run pytest --cov=src tests/ --cov-report=term-missing --cov-report=xml

help:
    uv run server.py --help



