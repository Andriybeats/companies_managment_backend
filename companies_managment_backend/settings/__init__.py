from decouple import config

environment = config('ENVIRONMENT', cast=str, default='local')

if environment == 'local':
    try:
        from .local import *
    except ImportError:
        pass
elif environment == 'qa':
    try:
        from .qa import *
    except ImportError:
        pass
elif environment == 'production':
    try:
        from .production import *
    except ImportError:
        pass