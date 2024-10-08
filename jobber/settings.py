import os
import django_heroku # Usando o django heroku
import dj_database_url
from pathlib import Path
from decouple import config
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.parent / 'data' / 'web'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', 'change-me')

# SECURITY WARNING: don't run with debug turned on in production! - Se não houver
DEBUG = config('DEBUG', default=False, cast=bool)

CORS_ALLOW_CREDENTIALS = True

ALLOWED_HOSTS = [
    h.strip() for h in config('ALLOWED_HOSTS', '').split(',')
    if h.strip()
]

# Configurações CORS
CORS_ALLOWED_ORIGINS = [
    h.strip() for h in config('CORS_ALLOWED_ORIGINS', '').split(',')
    if h.strip()
] 

# Configurações AWS S3
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='us-east-1')

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

AWS_DEFAULT_ACL = None  # Garantir que os arquivos tenham controle de acesso correto
AWS_QUERYSTRING_AUTH = False  # Evita que o URL gerado contenha tokens de autenticação
AWS_S3_VERITY = True  # Verificar se a configuração de verificação de SSL está ativa
AWS_S3_FILE_OVERWRITE = False


STORAGES = {

    # Media file (image) management
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage"
    },

    # Staticfiles management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage"
    },
}



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'tasks', # Chamando meu app rest da todolist
    'storages'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    ]

ROOT_URLCONF = 'jobber.urls'

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

WSGI_APPLICATION = 'jobber.wsgi.application'

# Verifique se estamos no Heroku
ON_HEROKU = 'DYNO' in os.environ

if ON_HEROKU:
    # Configurações específicas para o Heroku
    DATABASES = {
        'default': dj_database_url.config(default=config('DATABASE_URL'))
    }
    DEBUG = config('DEBUG', default=False, cast=bool)

    # Usando o AWS S3
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
else:
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    # Configurações específicas para o ambiente local
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE'),
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('POSTGRES_HOST'),
            'PORT': config('POSTGRES_PORT'),
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

# Internationalization - Configurado para o Brasil

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals(), staticfiles=False)
