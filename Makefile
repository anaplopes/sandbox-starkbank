.PHONY: prepare
prepare:
	pyenv install 3.10.6
	pyenv local 3.10.6

.PHONY: install
install:
	poetry env use python3.10
	poetry install
	poetry run pre-commit install

.PHONY: lint
lint:
	black .
	flake8 .

.PHONY: run-server
run-server:
	uvicorn src.main:create_app --reload

.PHONY: run-worker
run-worker:
	celery -A src.celery worker -B --loglevel=info -E

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: test
test:
	pytest -v

.PHONY: up-infra
up-infra:
	docker compose up -d db redis dashboard

.PHONY: up
up:
	docker compose up -d --build

.PHONY: down
down:
	docker compose down --remove-orphans -v

.PHONY: clean
clean:
	docker system prune --all --force --volumes

.PHONY: keys
keys:
	python3 src/infra/starkbank/keys.py
