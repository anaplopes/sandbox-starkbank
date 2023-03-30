#!/bin/bash

arg=${NAME}

if [ $arg == 'worker' ];
then
poetry run celery -A src.celery worker -B --loglevel=info -E
elif [ $arg == 'dashboard' ];
then
poetry run celery flower -A src.celery --port=5555 --broker=redis://redis:6379/0
else
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
fi
