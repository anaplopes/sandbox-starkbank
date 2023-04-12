from celery import Celery
from src.settings import settings
from celery.schedules import crontab
from celery.result import AsyncResult


celery_app = Celery(
    settings.CELERY_APP_NAME,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=["src.tasks.invoice"],
)

celery_app.conf.event_serializer = "pickle"
celery_app.conf.task_serializer = "pickle"
celery_app.conf.result_serializer = "pickle"
celery_app.conf.accept_content = ["application/json", "application/x-python-serialize"]
celery_app.conf.beat_schedule = {
    "invoice-every-three-hours": {
        "task": "src.tasks.invoice.send",
        "schedule": crontab(minute=0, hour="*/3"),
    }
}


def get_task_info(task_id):
    """
    return task info for the given task_id
    """
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return result
