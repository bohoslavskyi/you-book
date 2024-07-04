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
