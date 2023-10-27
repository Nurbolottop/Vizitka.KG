"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #settings
    'ckeditor',
    
    #apps
    'apps.index',
    'apps.blog',
    'apps.advert',
    'apps.category',
    'apps.category_blog',
    'apps.users',
    
    
    # Google
    'allauth',
    'allauth.account', 
    'allauth.socialaccount', 
    'allauth.socialaccount.providers.google',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = config.LANGUAGE_CODE

TIME_ZONE = config.TIME_ZONE

USE_I18N = config.USE_I18N

USE_TZ = config.USE_TZ


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/ 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Настройки Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "Visitka.KG",  # Заголовок админ-панели
    "site_header": "Visitka.KG",  # Заголовок на экране входа
    "site_brand": "Visitka.KG",  # Бренд в верхней части админ-панели
    "welcome_sign": "Добро пожаловать в Visitka.KG",  # Приветственное сообщение
    "search_model": ["auth.User", "blog.Post"],  # Модели, доступные для поиска
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://t.me/geeksosh", "new_window": True},
        {"model": "auth.User"},
        {"app": "blog"},
    ],
    "show_sidebar": True,
    "changeform_format": "horizontal_tabs",
    "header_classes": "navbar-dark bg-dark",  # Темный фон верхней части админ-панели
    "header_color": "#000000",  # Черный цвет верхней части админ-панели
    "dark_mode_theme": True,  # Включить темный режим
    "show_language_chooser": True,  # Включить выбор языка в админ-панели
    "custom_css": None,  # Путь к пользовательскому CSS-файлу (если нужен)
    "show_ui_builder": True,  # Показать UI Builder
    
}


#Ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'  # URL to jQuery
CKEDITOR_IMAGE_BACKEND = "pillow"  # Путь к пакету Pillow для обработки изображений
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Вы можете настроить свою собственную панель инструментов CKEditor
        'height': 300,
        'width': 800,
    },
}


EMAIL_USE_TLS = True  # Использовать TLS для защищенного соединения
EMAIL_HOST = 'smtp.gmail.com'  # Адрес SMTP сервера Gmail
EMAIL_PORT = 587  # Порт для подключения к SMTP серверу Gmail
EMAIL_HOST_USER = 'bullabratan@gmail.com'
EMAIL_HOST_PASSWORD = 'zlrwdyljhsupxnfo'


#Google
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
    
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'offline'}
    }
}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ""
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ""
AUTH_USER_MODEL = 'users.User'
# LOGIN_URL = '/users/login/'
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/' 

# Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_LOGIN_ON_GET=True