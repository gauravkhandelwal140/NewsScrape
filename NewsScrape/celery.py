from __future__ import absolute_import, unicode_literals

import os

from celery.schedules import crontab
from celery import Celery
from datetime import timedelta
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsScrape.settings')

app = Celery('NewsScrape')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
        'runs-every-60-seconds': {
        'task': 'news.tasks.get_scripe_data',
        "schedule": timedelta(seconds=60),
    },
}

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')