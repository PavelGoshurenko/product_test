# Makefile

lint:
	python3 -m flake8 product_app

test:
	python3 manage.py test
	
run:
	python3 manage.py runserver

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

