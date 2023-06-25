FROM python:3.9

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./src/ /app
COPY .env /app/config/.env

# create migrations for berries
RUN python manage.py makemigrations berries
RUN python manage.py migrate

# import berries from poke api
RUN python manage.py import_berries

# create or update histogram
RUN python manage.py generate_histogram