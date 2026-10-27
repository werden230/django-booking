PY_SRCS=src

.PHONY: help lint fmt type check
help:
	@echo "Доступные цели:"
	@echo " fix - ruff check (с автофиксом)"
	@echo " lint - ruff check"
	@echo " fmt - ruff format"
	@echo " type - mypy (проверка типов)"
	@echo " check - комплексный анализ (ruff+mypy)"
fix:
	poetry run ruff check $(PY_SRCS) --fix

lint:
	poetry run ruff check $(PY_SRCS)

fmt:
	poetry run ruff format $(PY_SRCS)

type:
	poetry run mypy $(PY_SRCS)

check: lint fmt type