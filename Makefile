install:
	poetry install

lint:
	ruff --config .ruff.toml --fix .

test:
	pytest .