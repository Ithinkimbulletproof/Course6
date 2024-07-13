from celery import shared_task
from main.tasks import run_mailing

@shared_task
def periodic_mailing():
    run_mailing()
