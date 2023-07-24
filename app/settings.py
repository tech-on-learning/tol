from pathlib import Path
import socket
import os
import sys

from django.utils.translation import gettext_lazy as _

####################################
##  Base Settings
####################################
BASE_DIR = Path(__file__).resolve().parent.parent
WSGI_APPLICATION = 'app.wsgi.application'
ROOT_URLCONF = 'app.urls'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

####################################
# Settings for secret file .env
from decouple import config, Csv, AutoConfig
# Setting to auto detect production mode
config = AutoConfig(search_path='../.env/.tol_website/.env')

####################################
##  Webapp Security Keys
####################################
SECRET_KEY=config('SECRET_KEY')
DEBUG=config('DEBUG', cast=bool)
ALLOWED_HOSTS=config('ALLOWED_HOSTS', cast=Csv())
# CSRF
CSRF_TRUSTED_ORIGINS=['https://http://techonlearning.com']

####################################
##  Application Definition
####################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Python Apps
    'imagekit',
    'django_cleanup.apps.CleanupConfig',
    # White noise
    'whitenoise.runserver_nostatic',
    # humanize
    'django.contrib.humanize',
    # Hitcounter
    'hitcount',
    'numerize',
    # HoneyPot
    'honeypot',
    # Htmx
    'django_htmx',

    # Text editor
    'tinymce',

    # COMPANY
    'company',
    'courses',
    'contact',
    'users',

    # Core
    'core',
]


####################################
##  Django Middleware
####################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Translate
    'django.middleware.locale.LocaleMiddleware',

    # WhiteNoise
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


####################################
##  Django Templates
####################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "_templates" ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom
            ],
        },
    },
]


########################################
##  DataBases Credentials // Dev // Prod
########################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


####################################
##  Password Validation
####################################
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

####################################
##  WYSIWG text Editor
####################################

# TINYMCE
TINYMCE_COMPRESSOR = False;
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "resize": "false",
    "menubar": "file edit view insert format tools table help",
    "height":550,
    "toolbar":
    "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment code typography",
    "plugins":
    "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code fullscreen insertdatetime media table powerpaste advcode help wordcount spellchecker typography",
};


####################################
##  Internationalization
####################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Port-au-Prince'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]
LOCALE_PATHS = [
    BASE_DIR / 'locale'
]


####################################
##  Media & StaticFiles 
####################################
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / '_staticfiles/'
]

STATIC_ROOT = '/home/benscler/_tol_cdn/static/' if not DEBUG else BASE_DIR / 'cdn/static/'
MEDIA_ROOT = '/home/benscler/akoladcreations_website_cdn/media/' if not DEBUG else BASE_DIR / 'cdn/media/'


####################################
##  Email Engine
####################################
EMAIL_USE_SSL=config('EMAIL_USE_SSL', cast=bool)
EMAIL_USE_TLS=config('EMAIL_USE_TLS', cast=bool)
EMAIL_BACKEND=config('EMAIL_BACKEND')
EMAIL_PORT=config('EMAIL_PORT')
EMAIL_HOST=config('EMAIL_HOST')
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
# Custom variables
EMAIL_RECIPIENT_LIST = config('EMAIL_RECIPIENT_LIST', cast=Csv())


####################################
##  Security Settings
####################################
if not DEBUG:
    # HTTPS settings
    SESSION_COOKIE_SECURE=True
    CSRF_COOKIE_SECURE=True
    SECURE_SSL_REDIRECT=True

    # HSTS settings
    SECURE_HSTS_SECONDS=31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS=True
    SECURE_HSTS_PRELOAD=True