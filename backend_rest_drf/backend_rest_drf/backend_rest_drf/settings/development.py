from .base import *
"""
.env

STATE=development

SECRET_KEY=

POSTGRES_DB=tuvc-backend
POSTGRES_USER=tuvc-backend
POSTGRES_PASSWORD=qwer1234

POSTGRES_HOST=tuvc-db
POSTGRES_PORT=5432
"""

# sudo rm -rf data
# find . -type d -name "__pycache__" -exec sudo rm -rf {} +
# find . -type d -name "migrations" -exec sudo rm -rf {} +
#   Don't forget to restore migrations/__init__.py file. it need for migrations.

# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
    }
}


ALLOWED_HOSTS = [
    'localhost',
]

# CORS_ORIGIN_ALLOW_ALL = True # If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
]

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'correlation': {
            '()': 'cid.log.CidContextFilter',
        },
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)-8s [%(asctime)s] [%(cid)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filters': ['correlation'],
            'when': 'D',
            'interval': 1,
            'backupCount': 90,
            'filename': 'log/log.dev.log',
            'formatter': 'standard',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['correlation'],
            'formatter': 'standard',
        },
        'mail_error_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['correlation'],
            'level': 'ERROR',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
