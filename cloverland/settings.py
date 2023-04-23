from pathlib import Path

from cloverland.env import (
    ALLOWED_HOST,
    APP_BASE_URL,
    MONGODB_URI,
    SECRET_KEY,
    DEBUG,
)


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SECRET_KEY
ALLOWED_HOST = ALLOWED_HOST
DEBUG = DEBUG
APP_BASE_URL = APP_BASE_URL

GRAPPELLI_ADMIN_TITLE = "Cloverland"

INSTALLED_APPS = [
    "grappelli",
    "corsheaders",
    "tinymce",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "customer",
    "lottery",
    "order",
]

TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code image paste",
    "paste_data_images": True,
    "automatic_uploads": False,
    "selector": "textarea",
}

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ALLOWED_HOSTS = [ALLOWED_HOST]
CORS_ALLOWED_ORIGINS = [APP_BASE_URL]
CSRF_TRUSTED_ORIGINS = [APP_BASE_URL]
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = "cloverland.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cloverland.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "test",
        "CLIENT": {"host": MONGODB_URI},
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CSRF_COOKIE_DOMAIN = "localhost"
