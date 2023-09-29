from .common import *
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = 0
PRODUCTION = 1
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default="postgresql://postgres:postgres@localhost:5432/pokecardsV2",
        conn_max_age=600,
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]

STATIC_URL = "static/"
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

# Turn on WhiteNoise storage backend that takes care of compressing static files
# and creating unique names for each version so they can safely be cached forever.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_NAME")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")
