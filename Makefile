.PHONY: help lint security unit integration test
.DEFAULT_GOAL := help

help: ## List all Makefile targets
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

lint: ## Run linters
	tox -e black,flake8,mypy

security: ## Run security checks
	tox -e bandit,safety

unit: ## Run unit tests
	tox -e unit

integration: ## Run integration tests
	tox -e integration

test: ## Run tests
	tox --parallel--safe-build

build: ## Build docker image
	docker build --tag intercom .

run: ## Run docker image
	docker run --rm intercom

clean: ## Remove project artifacts
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -rf
	rm -rf .venv/ venv/ .cache/ .tox/ .mypy_cache/ .pytest_cache/ .hypothesis/
