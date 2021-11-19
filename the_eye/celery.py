import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_eye.settings.development')

app = Celery('the_eye')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
