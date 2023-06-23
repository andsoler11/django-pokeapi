FROM python:3.9

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./src/ /app
COPY .env /app/config/.env
