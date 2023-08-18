# POETRY COMMANDS

.PHONY: pinstall pbuild requirements black pytest black

pinstall:
	poetry install

pbuild: install
	poetry build

requirements:
	poetry export -f requirements.txt --without-hashes -o requirements.txt

black:
	poetry run black .

pytest:
	poetry run pytest --cov=./tests --black -rAP 

black:
	isort .
	black .


# Script Commands

prun:
	poetry run python main.py

prun_env:
	export ENV=dev && poetry run python main.py

prun_argparse:
	poetry run python main.py --env prod


# DOCKER / CONTAINER REGISTRY COMMANDS
.PHONY: build run push attach

build:
	docker build -t us-central1-docker.pkg.dev/$(PROJECT_ID)/$(REGISTRY_NAME)/$(CONTAINER_NAME) .

run: build
	docker run -it -p 8080:8080 --name ${CONTAINER_NAME} us-central1-docker.pkg.dev/$(PROJECT_ID)/$(REGISTRY_NAME)/$(CONTAINER_NAME)

push: build
	docker push us-central1-docker.pkg.dev/$(PROJECT_ID)/$(REGISTRY_NAME)/$(CONTAINER_NAME)

exec:
	docker exec -it $(CONTAINER_NAME) /bin/bash