init:
	pip install -Ue .
init-dev:
	pip install -Ue .[dev]
test:
	pytest tests
freeze:
	pip-compile
check:
	ruff .
run:
	bot-run
