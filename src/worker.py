import time
from celery import Celery
from src.settings import settings


celery = Celery(__name__)
celery.conf.broker_url = settings.CELERY_BROKER_URL
celery.conf.result_backend = settings.CELERY_RESULT_BACKEND


@celery.task(name="create_task")
def create_task():
    print("passei aqui!")
    time.sleep(1)
    return True
