
import os
from pathlib import Path
import dj_database_url



import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# READ_DOT_ENV_FILE = env('READ_DOT_ENV_FILE', default=False)

# if READ_DOT_ENV_FILE:
environ.Env.read_env()

#To run use $env:READ_DOT_ENV_FILE = "True"

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY=env('SECRET_KEY')



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',

    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leads',
    'tailwind',
    'theme',
    'django_browser_reload',
    'widget_tweaks',
    'agents',

    "crispy_forms",
    "crispy_tailwind",

    # amazon s3
    'storages',
]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }

DATABASE_URL = env('DATABASE_URL')


DATABASES = {
    "default":dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATIC_ROOT = BASE_DIR /'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'leads.User'

LOGIN_REDIRECT_URL = '/lead_list'
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL='/'



JAZZMIN_SETTINGS ={
    'site_header': "Ecommerce",
    'site_brand': 'You order, we deliver',
    # 'site_logo': '/images/logo.jpg',
    'copyright': 'ecommerce.com',
}



# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# # EMAIL_HOST = 'your-smtp-host'
# # EMAIL_PORT = 587
# # EMAIL_USE_TLS = True
# # EMAIL_HOST_USER = 'your-email@example.com'
# # EMAIL_HOST_PASSWORD = 'your-email-password'


EMAIL_BACKEND = env('EMAIL_BACKEND')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"


AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')
STATICFILES_STORAGE = env('STATICFILES_STORAGE')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
# AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN')

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
