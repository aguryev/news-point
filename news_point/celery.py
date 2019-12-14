# celery app for asynchronous tasks

import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_point.settings')
 
app = Celery('news_point')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs
app.autodiscover_tasks()