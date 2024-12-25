from pathlib import Path
import os
from decouple import config

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

DEBUG = True
ALLOWED_HOSTS = ['*']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    # package apps
    'crispy_forms',
    'crispy_bootstrap5',
    # allauth packages apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    # import all apps
    'user_account',
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user_account.middleware.check_session_activity',
    'home.middleware.PageViewMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'Magazine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Magazine.wsgi.application'

AUTH_USER_MODEL = 'user_account.CustomUser'
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Settings of third party registration
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# client id and client secret
# Google
os.environ['CLIENT_ID'] = config('CLIENT_ID')
os.environ['CLIENT_SECRET'] = config('CLIENT_SECRET')
# Facebook
os.environ['CLIENT_FCAEBOOK_ID'] = config('CLIENT_FACEBOOK_ID')
os.environ['CLIENT_FACEBOOK_SECRET'] = config('CLIENT_FACEBOOK_SECRET')

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE' : [
            'profile',
            'email'
        ],
        'APP': {
            'client_id': os.environ['CLIENT_ID'],
            'secret': os.environ['CLIENT_SECRET'],
        },
        'AUTH_PARAMS': {
            'access_type':'online',
        },

    },
    'facebook': {
        'METHOD': 'oauth2',  # روش OAuth2
        'SCOPE': ['email'],  # درخواست دسترسی به ایمیل
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
        ],
        'AUTH_PARAMS': {
            'auth_type': 'reauthenticate'
        },
        'VERIFIED_EMAIL': False,
        'VERSION': 'v16.0',  # نسخه API فیسبوک
    }
}

#for extra info
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/email-verified/message/'

# Email Backend 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hadelesmatullah@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Recptcha Settings
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')

# Session Settings
SESSION_COOKIE_AGE = 604800
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Cirspy Forms Settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Language Settings
from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('en',_('English')),
    ('fa',_('Farsi')),
]
LANGUAGE_CODE = 'en'
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

USE_I18N = True
USE_L10N = True