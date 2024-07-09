.PHONY: setup \
		up \
		build \
		restart \
		down \
		build-up \
		logs

DOCKER_COMPOSE_FILE = docker-compose.yml
ENV_FILE = .env

#================#
#== CONTAINERS ==#
#================#
up:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} up --detach

build:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} build

restart:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} restart

down:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} down

build-up:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} up --build --detach

logs:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} logs -f


#==============#
#== DATABASE ==#
#==============#
generate-migrations:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} run --rm app sh -c "python manage.py makemigrations"

migrate:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} run --rm app sh -c "python manage.py migrate"


#===========#
#== TOOLS ==#
#===========#
manage:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} run --rm app sh -c "python manage.py $(command)"

lint:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} run --rm app sh -c "flake8"

code-format:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} run --rm app sh -c "isort . && black ."

test:
	docker compose --file ${DOCKER_COMPOSE_FILE} --env-file ${ENV_FILE} run --rm app sh -c "python manage.py test"

pre-commit-check:
	make lint
	make code-format
	make test
