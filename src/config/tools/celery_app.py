import logging
import os

import structlog
from celery import Celery

from celery.signals import setup_logging
from django_structlog.celery.steps import DjangoStructLogInitStep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("src")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.broker_connection_retry_on_startup = True
app.steps["worker"].add(DjangoStructLogInitStep)

app.conf.beat_schedule = {
    # "some_random_task": {
    #     "task": "",
    #     "schedule": crontab(minute=0, hour=0),
    # },
}
