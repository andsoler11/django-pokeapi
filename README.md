# globant-challenge

API to get the poke berries stats from the poke berries API

## Features

- Get the poke berries stats from the poke berries API
- python 3.9
- [Django REST Framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs.
- [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
- [Docker](https://www.docker.com/) - Docker is an open platform for developing, shipping, and running applications.
- [Docker Compose](https://docs.docker.com/compose/) - Compose is a tool for defining and running multi-container Docker applications.

## Installation

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.9](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Clone the repository

```bash
git clone https://github.com/andsoler11/globant-challenge.git
```

### Create the .env file

```bash
cd globant-challenge
touch .env
```
Add the variables to the .env file


### Run the project

```bash
docker-compose up
```

you can access to the API in http://localhost:8000/allBerryStats

### Run the tests

```bash
docker-compose run --rm backend sh -c "python manage.py test apps/berries/tests"
```

## API Documentation

### Get all the berries stats

```bash
GET /allBerryStats
```

this endpoint will return all the berries stats from the poke berries API and will update the history of the stats

Response: {
    "berries_names": [...],
    "min_growth_time": "" // time, int
    "median_growth_time": "", // time, float
    "max_growth_time": "" // time, int
    "variance_growth_time": "" // time, float
    "mean_growth_time": "", // time, float
    "frequency_growth_time": "", // time, {growth_time:    frequency, ...}
}
