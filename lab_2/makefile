.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	# Ваш код тут
	@sudo -H pip install -U pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install ntplib
	@pipenv install pytest

test:
	@echo "Start tests."
	# Ваш код тут
	@touch results.txt
	@pipenv run pytest tests.py | tee results.txt

run:
	@echo "Run Python app."
	# Ваш код тут
	@pipenv run python app.py | tee -a results.txt
	@pipenv --rm

deploy:
	@echo "Adding and Committing results.txt to git."
	# Ваш код тут
	@git add results.txt
	@git commit -m "lab2: autoadd"
	@git push origin master
