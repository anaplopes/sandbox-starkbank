from src.celery import celery_app
from src.usecases.invoice import InvoiceUseCase


@celery_app.task
def send():
    InvoiceUseCase().send_invoices()
