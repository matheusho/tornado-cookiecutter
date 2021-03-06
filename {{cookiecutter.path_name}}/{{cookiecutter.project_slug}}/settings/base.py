import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = bool(os.getenv('DEBUG', True))

SQL_ECHO = True

DATABASES = {
    'default': {
        'ENGINE': 'mssql+pymssql',
        'HOST': os.getenv('DEFAULT_HOST'),
        'NAME': os.getenv('DEFAULT_NAME'),
        'USER': os.getenv('DEFAULT_USER'),
        'PASSWORD': os.getenv('DEFAULT_PASSWORD'),
        'PORT': os.getenv('DEFAULT_PORT')
    }
}

TEMPLATE_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'templates')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

SENTRY_DSN = os.getenv('SENTRY_DSN')
