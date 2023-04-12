from src.celery import celery_app
from src.usecases.invoice import InvoiceUseCase


@celery_app.task
def send():
    try:
        InvoiceUseCase().send_invoices()
        return {"detail": "OK"}
    except Exception as e:
        {"detail": f"FAILED: {str(e)}"}
