.PHONE:
superuser:
	python3 manage.py createsuperuser

.PHONE:
migrations:
	python3 manage.py makemigrations
	python3 manage.py migrate

.PHONE:
run-local:
	python3 manage.py runserver

.PHONE:
run-docker:
	docker build -t workforce .
	docker run --rm -p 8000:8000 workforce
