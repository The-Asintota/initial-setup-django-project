from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = [
    config("BACKEND_HOST", cast=str),
    config("FRONTEND_HOST", cast=str),
]

CSRF_TRUSTED_ORIGINS = [
    f"https://{config('BACKEND_HOST', cast=str)}",
    f"https://{config('FRONTEND_HOST', cast=str)}",
]

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True


# CORS settings
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [f"https://{config('FRONTEND_HOST', cast=str)}"]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = Path.joinpath(BASE_DIR, "staticfiles")


# LOGGING settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
