#!/bin/bash


poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

poetry run celery worker --app=worker.celery --loglevel=info --logfile=logs/celery.log

poetry run flower --app=worker.celery --port=5555 --broker=redis://redis:6379/0
