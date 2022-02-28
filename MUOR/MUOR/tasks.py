from celery import shared_task
from django.core import management


@shared_task(name="clear_sessions")
def clear_sessions():
    management.call_command('clearsessions')
