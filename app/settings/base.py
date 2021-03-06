CONFIG = __import__("app.config").config

SECRET_KEY = CONFIG.env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = ["*"]

SITE_ID = 1
SITE_URL = ""

#########################
# Application definition
#########################

INSTALLED_APPS = (
    # django package
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "suvorov_park.apps.SuvorovParkConfig",
    "django.contrib.admin",
    # third-party packages
    "rest_framework",
    "solo.apps.SoloAppConfig",
    "corsheaders",
    # project applications
    "suvorov_park.users",
    "suvorov_park.common",
    "suvorov_park.polls",
    "suvorov_park.services",
    "suvorov_park.forum",
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "app.urls"

WSGI_APPLICATION = "app.wsgi.application"
BASE_URL = "http://suvorovpark.ru"

#########################
# Database
#########################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": CONFIG.env("DB_NAME"),
        "USER": CONFIG.env("DB_USER"),
        "PASSWORD": CONFIG.env("DB_PASSWORD"),
        "HOST": CONFIG.env("DB_HOST"),
        "PORT": CONFIG.env("DB_PORT", str, ""),
    }
}

#########################
# Language
#########################

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

#########################
# Static files
#########################


STATIC_ROOT = CONFIG.PATHS["STATIC_DIR"]

STATIC_URL = "/django-static/"

MEDIA_ROOT = CONFIG.PATHS["DATA_DIR"]

STATICFILES_DIRS = (CONFIG.PATHS["APP_DIR"] + "/app/static/",)
MEDIA_URL = "/data/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

FILE_UPLOAD_TEMP_DIR = CONFIG.PATHS["TMP_DIR"]

SESSION_FILE_PATH = CONFIG.PATHS["TMP_DIR"]

ADMIN_URL = "admin/"

#########################
# Other settings (Templates, Locale, Context)
#########################

LOCALE_PATHS = (str(CONFIG.APP_DIR.path("app", "locale")),)

AUTH_PASSWORD_VALIDATORS = ()

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(CONFIG.APP_DIR.path("app", "templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.csrf",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "debug": False,
        },
    }
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "stat_time": {"format": "[%(asctime)s] %(message)s"},
        "verbose": {"format": "{levelname} {asctime} {message}", "style": "{"},
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.db.backends": {"level": "DEBUG", "handlers": ["console"]},
    },
}

AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "app.authentication.CsrfExemptSessionAuthentication",
    ),
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

################
# Email sending
################


EMAIL_HOST = CONFIG.env("EMAIL_HOST")
EMAIL_HOST_USER = CONFIG.env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = CONFIG.env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = CONFIG.env("DEFAULT_FROM_EMAIL")
EMAIL_PORT = CONFIG.env("EMAIL_PORT")
EMAIL_USE_SSL = True

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
