install:
	poetry install
tests:
	pytest tests
coverage:
	coverage run -m pytest tests && coverage report --fail-under=90 --omit=tests/*
lint:
	pylint src tests
typehint:
	mypy src tests
checklist: tests lint typehint

.PHONY: tests coverage lint typehint checklist