all:
	uv run src/cairn-realmify/generate.py

test:
	uv run pytest tests
