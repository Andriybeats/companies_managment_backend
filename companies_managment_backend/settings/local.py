from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'companies_managment_db',
        'USER' : 'db_user',
        'PASSWORD' : 'password',
        'HOST' : '127.0.0.1',
        'PORT' : '5432'
    }
}