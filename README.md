# Api Gateway

[![.github/workflows/pipeline.yml](https://github.com/Team-Lisa/api-gateway/actions/workflows/pipeline.yml/badge.svg?branch=master)](https://github.com/Team-Lisa/api-gateway/actions/workflows/pipeline.yml)
[![Coverage Status](https://coveralls.io/repos/github/Team-Lisa/api-gateway/badge.svg?branch=master)](https://coveralls.io/github/Team-Lisa/api-gateway?branch=master)

## Env

* Production: https://idiomaplay-gateway.herokuapp.com/

## Local Mode

#### Requirements

- Python 3.9
- [Poetry](https://python-poetry.org/docs/#installation)

#### Setup
1. run ```poetry install``` 
2. run ```poetry shell``` (create a venv)

#### Running locally
- ```uvicorn api.main:app```

## Using Docker

#### Requirements
- Docker

#### Running locally

1. ```make build``` 
2. ```make start```


## Documentation
You can see the automatic interactive API documentation using the endpoint: ```/docs```
