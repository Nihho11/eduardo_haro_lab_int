from .base import *

SECRET_KEY = 'django-insecure-+i$*$pfympw20le#3b9f)!s&el)&mpxu!!w_@bdfvhqkdl80iw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_pokemon_owner',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'

    }
}

STATIC_URL = '/static/'

