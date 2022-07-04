# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser

EXPOSE 80
STOPSIGNAL SIGTERM
ENTRYPOINT python manage.py runserver 0.0.0.0:80