from src.worker import celery_app


@celery_app.task
def check():
    print("Estou checando suas coisas")
