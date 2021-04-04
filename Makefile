#
# Makefile

defaut: help

install: amaterasu/*.py ## install self
	python setup.py install

install-test-deps: ## install test dependencies
	pip install -e.[test]

test: install
	amaterasu sample/wandbox.j2

kamidana: install
	kamidana -a=amaterasu.amaterasu sample/wandbox.j2

sample: sample/README.md

sample/README.md: install
	amaterasu sample/README.md.j2 > sample/README.md

pytest: ## python test
	python setup.py test

tox: install-test-deps
	tox .

flake8: install-test-deps
	tox -e flake8 .

help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

docker:
	docker run -it --rm -v ${PWD}:/work -w /work python:3.8-alpine sh
	# apk add make
