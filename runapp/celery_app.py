import os
import time

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'runapp.settings')

app = Celery('runapp')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()



@app.task()
def debug_task():
    time.sleep(20)
    print('Hello form debug_task')