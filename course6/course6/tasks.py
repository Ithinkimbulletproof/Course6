import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'main'))

from celery import shared_task
from main.tasks import run_mailing

@shared_task
def periodic_mailing():
    run_mailing()
