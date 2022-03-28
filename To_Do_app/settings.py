"""
Django settings for To_Do_app project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.


BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--*2xc-$$&3%490ad*abt^&7r#5=fpqqamd)t&yx7l4hp+wm%n1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # для css/js, swagger, graphql
    # подключенные библиотеки
    'rest_framework', # django rest framework - для работы через api
    'django_filters',  # фильтрация
    'corsheaders',  # библиотека для взаимодействия с frontend
    'rest_framework.authtoken',  # авторизация по токену
    'drf_yasg',  # авто документация
    'graphene_django', # библиотека для работы с GraphQL (pip install graphene-django)
    # мои приложения
    'users_app',
    'projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # библиотека для взаимодействия с frontend
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'To_Do_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'To_Do_app.wsgi.application'

AUTH_USER_MODEL = 'users_app.Users'  # тут указана модель, по которой будет происходить авторизация

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# адрес с которого идет взаимодействие с frontend
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',  # для предотвращения проблем на ubuntu
]

# настрока renderers для всего проекта:
# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ],
# }

# настрока renderers для всего проекта:
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        # используется camelCase:
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',

    ),
    # настройки для постраничного вывода:
    # !!! ВКЛЮЧАТЬ КОГДА НЕ НУЖЕН FRONTEND !!!
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 100,
    # настройка для фильтрации:
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    # следующие 2 настройки используются для camelCase
    # !!! ВКЛЮЧАТЬ ТОЛЬКО КОГДА НЕ НУЖНА HTML ФОРМА ДЛЯ РУЧНОГО ВНЕСЕНИЯ ДАННЫХ !!!
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
    # система авторизации:
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # система прав:
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.IsAuthenticated', # все права только для авторизованных пользователей
    ],
    'DEFAULT_VERSIONING_CLASS':
        'rest_framework.versioning.QueryParameterVersioning',

}

#работа с GraphQL:
GRAPHENE = {
    'SCHEMA': 'schemas.schema.schema',
}