import dj_database_url

from decouple import Csv
from .base import *

DEBUG = config('DEBUG', default=False)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL', default=''), conn_max_age=4000)
}