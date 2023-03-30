from src.celery import celery_app
from src.usecases.invoice import InvoiceUseCase


@celery_app.task(serializer="json")
async def send():
    return await InvoiceUseCase().send_invoices()
