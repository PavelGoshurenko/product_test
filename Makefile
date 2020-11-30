# Makefile

lint:
	python3 -m poetry run flake8

test:
	python3 manage.py test
	
run:
	python3 manage.py runserver

requirements:
	python3 -m poetry export -f requirements.txt -o requirements.txt

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

