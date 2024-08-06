"""
Django settings for exotic project.

Generated by 'django-admin startproject' using Django 4.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = 'customer.Customer'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kdwpt=%ad=!*(k)p+cg^bv#=sz!q3u!7^t_-qnf!w@auwn5(sq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["127.0.0.1", "exoticbackend.exoticshop.eu", "localhost", "localhost:5174"]

ALLOWED_HOSTS = [
    'http://localhost:5174',
    'localhost:5174',
    'localhost',
    '127.0.0.1',
    'https://exoticshop.eu',
    'exoticshop.eu',
    'http://exoticbackend.exoticshop.eu',
    'exoticbackend.exoticshop.eu',
    'https://exoticcity-a0dfd0ddc0h2h9hb.northeurope-01.azurewebsites.net',
    'exoticcity-a0dfd0ddc0h2h9hb.northeurope-01.azurewebsites.net'
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5174',
    'http://localhost',
    'https://exoticshop.eu',
    'http://exoticshop.eu',
    'http://exoticbackend.exoticshop.eu',
    'https://exoticbackend.exoticshop.eu',
    'https://exoticcity-a0dfd0ddc0h2h9hb.northeurope-01.azurewebsites.net'
    'exoticcity-a0dfd0ddc0h2h9hb.northeurope-01.azurewebsites.net'
    # Add other allowed origins as needed
]

CORS_ALLOW_ALL_ORIGINS = True  # Allows all origins, adjust as needed

# CORS_ORIGIN_WHITELIST = [
#     'https://exoticshop.eu',
#     'exoticshop.eu',
#     'localhost:5173',
#     'http://localhost:5174',
#     'http://exoticbackend.exoticshop.eu',
#     'exoticbackend.exoticshop.eu'
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_apscheduler',
    'rest_framework',
    'django_filters',
    'items',
    "django.contrib.admindocs",
    "customer",
]

DATA_UPLOAD_MAX_NUMBER_FIELDS = 999999

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware'
]

ROOT_URLCONF = 'exotic.urls'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000000

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

WSGI_APPLICATION = 'exotic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'msisgnqytn',
        'PASSWORD': '$7oaI$heGSjF7lRE',
        'HOST': 'exoticserver.postgres.database.azure.com',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend", "frontend", "public"),
    os.path.join(BASE_DIR, "frontend", "frontend", "dist")
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.office365.com'  # Microsoft's SMTP server

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'info@exoticcity.be'  # Your Microsoft 365 email

EMAIL_HOST_PASSWORD = 'ptfwpxvnpbyttwzz'  # Your Microsoft 365 email password

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SCHEDULER_CONFIG = {
    'apscheduler.timezone': 'UTC',
}
