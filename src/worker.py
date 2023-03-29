from celery import Celery
from src.settings import settings
from celery.schedules import crontab


celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["src.tasks.invoice"],
)


celery_app.conf.beat_schedule = {
    "invoice-every-three-hours": {
        "task": "src.tasks.invoice.check",
        "schedule": crontab(),  # crontab(minute=0, hour='*/3')
    }
}
