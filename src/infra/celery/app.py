from celery import Celery
from src.settings import settings
from celery.schedules import crontab


celery_app = Celery(
    settings.WORKER_NAME,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)


celery_app.conf.beat_schedule = {
    "invoice-every-three-hours": {
        "task": "src.tasks.task_invoice.invoice",
        "schedule": crontab(),  # crontab(minute=0, hour='*/3')
    }
}
