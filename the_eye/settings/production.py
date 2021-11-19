import os

from django.core.exceptions import ImproperlyConfigured

from .common import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except KeyError:
    raise ImproperlyConfigured("Missing DJANGO_SECRET_KEY env var")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

try:
    DB_NAME = os.environ["DB_NAME"]
    DB_USER = os.environ["DB_NAME"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_HOST = os.environ["DB_PASSWORD"]
except KeyError:
    raise ImproperlyConfigured(
        "DB configuration is missing from the environment"
    )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'TEST': {
            'CHARSET': 'UTF8',
        },
    }
}

try:
    CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]
except KeyError:
    raise ImproperlyConfigured("Celery configuration missing from the environment")
