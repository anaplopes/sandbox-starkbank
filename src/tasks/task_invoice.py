from src.infra.celery.app import celery_app


@celery_app.task
def invoice(bind=True):
    print("hello world")
    return "hello world"
