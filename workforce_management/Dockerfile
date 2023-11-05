FROM python:3.10.12-alpine

WORKDIR /workforce_management

COPY . .

RUN pip3 install poetry
RUN poetry export --output requirements.txt
RUN pip3 uninstall poetry -y
RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]