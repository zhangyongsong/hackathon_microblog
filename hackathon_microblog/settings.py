"""
Django settings for hackathon_microblog project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k*in#co1%4&x*vbxc(d3n1cu%tb!2+in!6ptv0!!em*$+in_(+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DOMAIN_NAME = 'liverpool2015.fo3.garena.com'
ALLOWED_HOSTS = [DOMAIN_NAME]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hackathon_microblog.microblog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'hackathon_microblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hackathon_microblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hackathon_microblog_db',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'hackathon_microblog', 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Garena OAuth and User Login
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'EXCEPTION_HANDLER': 'gtoext.rest.rest_exc_handler',
    'UNAUTHENTICATED_USER': None,
    'UNAUTHENTICATED_TOKEN': None,
}

GTOEXT_GARENA_OAUTH = {
    # oauth server/client settings
    'oauth': {
        # Required
        'host': 'auth.garena.com',
        'client_id': 200001,
        'client_secret': 'a80f2956e1ae040fa6be94585931d78ae966099f45e89f253e545a3cc32d00fe',
        'root_url': 'http://%s/garena_oauth/' % DOMAIN_NAME,

        # Options, default: None
        'response_type': 'code',  # authorization code grant
        'scope': None,
        'display': None,
        'locale': 'en-SG',
        'platform': None,
        'all_platforms': None,
    },

    # others
    'login_url': '/garena_oauth/login/',
    'login_clear_session': False,
    'login_redirect_to': '/',
    'logout_redirect_to': '/',
}


LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_FILE = os.path.join(LOG_DIR, 'django.log')
ERROR_LOG_FILE = os.path.join(LOG_DIR, 'django_error.log')

LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(asctime)s %(message)s'
            },
        },
        'handlers': {
            'root': {
                'level': 'DEBUG',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': LOG_FILE,
                'formatter': 'verbose',
            },
            'error': {
                'level': 'DEBUG',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename':  ERROR_LOG_FILE,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'main': {
                'handlers':  ['root', ],
                'level': 'DEBUG',
            },
            'django.request': {
                'handlers': ['error'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }


