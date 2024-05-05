all: clean build up alembic-migrate

include .env


# docker
build:
	docker compose build

up:
	@echo "bringing up project...."
	docker compose up -d
	@echo "waiting for database reachability...."
	docker compose exec backend bash -c "while !</dev/tcp/db/5432; do sleep 1; done;"
	@echo "Done. DB reachable...."

down:
	@echo "bringing down project...."
	docker compose down

example-query: up
	@echo "searching for 'A. Del Maestro' with max query result 10"
	curl -s -X GET "http://$(NGINX_HOST)/v1/arxiv/search?author=A.%20Del%20Maestro&max_query_results=10"

# @ before command suppresses output on console and prevents accidental password leaking
select-all-from-query: up
	@PGPASSWORD=$(DB_PASSWORD) psql -h $(NGINX_HOST) -p $(DB_PORT) -U $(DB_USER) $(DB_DB) -c "SELECT * FROM query"

select-all-from-article: up
	@PGPASSWORD=$(DB_PASSWORD) psql -h $(NGINX_HOST) -p $(DB_PORT) -U $(DB_USER) $(DB_DB) -c "SELECT * FROM article"

select-all-from-author: up
	@PGPASSWORD=$(DB_PASSWORD) psql -h $(NGINX_HOST) -p $(DB_PORT) -U $(DB_USER) $(DB_DB) -c "SELECT * FROM author"

clean: down
	@echo "Cleaning up..."
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '*.egg-info' -exec rm -vrf {} \; 2>/dev/null
	@echo "Done."


bash:
	@echo "connecting to container...."
	docker compose exec backend bash

# alembic
alembic-scaffold:
	@echo "scaffolding migrations folder..."
	docker compose exec backend alembic init -t async migrations

alembic-init:
	@echo "initializing first migration...."
	docker compose exec backend alembic revision --autogenerate -m "init"

alembic-make-migrations:
	@echo "creating migration file...."
	docker compose exec backend alembic revision --autogenerate -m "change me"

alembic-migrate:
	@echo "applying migration...."
	docker compose exec backend alembic upgrade head

alembic-downgrade:
	@echo "reverting migration...."
	docker compose exec backend alembic downgrade -1

# lint
test:
	@echo "running pytest...."
	docker compose exec backend pytest --cov-report xml --cov=app/ tests/

lint:
	@echo "running ruff...."
	docker compose exec backend ruff check app

black:
	@echo "running black...."
	docker compose exec backend black .

mypy:
	@echo "running mypy...."
	docker compose exec backend mypy app/


# misc

git:
	@echo "installing pre-commit hooks...."
	pre-commit install
