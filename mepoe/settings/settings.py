"""
Django settings for mepoe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# from unipath import Path
# BASE_DIR = Path(__file__).ancestor(3)
from pathlib import Path
BASE_DIR = Path(__file__).parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@frpw&7+9160zzhx*4r=5n-%d+-v&n-765-k(x4h!)8$3p_ei5'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

SITE_ID = 1

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'south',
    'haystack',
    'pyelasticsearch',
    'autofixture',
    'avatar',
    # 'bootstrapform',
    'bootstrap3',
    'easy_thumbnails',
    # 'guardian',
    'werkzeug',
    'django_extensions',
    'debug_toolbar',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'taggit',
    'compressor',
    'favorite',
    # 'request',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
    # 'userena',
    # 'social.apps.django_app.default',
    # 'djrill',
)

LOCAL_APPS = (
    # 'accounts',
    # 'userprof',
    # 'tags',
    'userprofiles',
    'poems',
    'poemsimport',
    'randomusers',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

from django.conf.global_settings import MIDDLEWARE_CLASSES as MD

MIDDLEWARE_CLASSES = MD + (
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    # 'request.middleware.RequestMiddleware',
)

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'userena.middleware.UserenaLocaleMiddleware',
# 'request.middleware.RequestMiddleware',
# )

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.core.context_processors.static",
#     "django.core.context_processors.tz",
#     "django.contrib.messages.context_processors.messages",
#     "django.core.context_processors.request",
#     "allauth.account.context_processors.account",
#     "allauth.socialaccount.context_processors.socialaccount",
# )

ROOT_URLCONF = 'mepoe.urls'

WSGI_APPLICATION = 'mepoe.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


TEMPLATE_DIRS = (
    'templates',
    'templates/allauth',
    'templates/avatar',
)

STATIC_URL = '/static/'
STATIC_ROOT = 'public/static'
STATICFILES_DIRS = (
    'mepoe/static',
)
# Para que se tengan en cuenta los directorios statics de las apps
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

# Para habilitar el hash en los statics
# STATICFILES_STORAGE = \
#     'django.contrib.staticfiles.storage.CachedStaticFiles.Storage'

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR / 'media')

FORCE_SCRIPT_NAME = '/'

# from .logging_settings import *
# LOGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'mepoe.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # 'MYAPP': {
        #     'handlers': ['file'],
        #     'level': 'DEBUG',
        # },
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s \
            [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
}

# from .thumbnail_settings import *
#

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
    'taggit': 'taggit.south_migrations',
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    # 'django.contrib.auth.backends.ModelBackend',
    # 'userprofiles.backends.EmailBackend',
)


# DJANGO-ALLAUTH
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = False
ACCOUNT_USERNAME_MIN_LENGTH = 2
ACCOUNT_USERNAME_BLACKLIST = ['username', 'mepoe', 'password']
ACCOUNT_PASSWORD_MIN_LENGTH = 6

# MAILGUN
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = 'key-0vrsqh9l0ik6d0j43b1-8c3n8wc-e3e3'
MAILGUN_SERVER_NAME = 'mepoe.com'


# EASY THUMBNAILS
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}

# DJANGO-AVATAR
AVATAR_STORAGE_DIR = 'avatars'
AVATAR_GRAVATAR_BACKUP = False
AVATAR_DEFAULT_URL = 'images/avatar_default.png'
AVATAR_AUTO_GENERATE_SIZES = (23, 80,)
# AVATAR_DEFAULT_URL = str(
#     BASE_DIR / 'userprofiles/static/images/avatar_default.png')

# HAYSTACK
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE':
        'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

# COMPRESSOR
# COMPRESS_PRECOMPILERS = (
#     ('text/less', 'lessc --include-path="' + os.path.join(SITE_ROOT, 'ebury_theme_bos/static/less') + '" {infile} {outfile}'),
# )

COMPRESS_PRECOMPILERS = (
    # ('text/coffeescript', 'coffee --compile --stdio'),
    # ('text/less', 'lessc {infile} {outfile}'),
    # ('text/x-sass', 'sass {infile} {outfile}'),
    # ('text/x-scss', 'sass --scss {infile} {outfile}'),
    ('text/stylus', 'stylus < {infile} > {outfile}'),
    # ('text/foobar', 'path.to.MyPrecompilerFilter'),
)

COMPRESS_ENABLED = True
# COMPRESS_OUTPUT_DIR = 'compiled'

# # List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
