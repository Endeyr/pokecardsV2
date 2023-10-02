from .common import *
import os
from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = 0
PRODUCTION = 1
ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgresql_pokecards",
        "USER": "postgresql_pokecards_user",
        "PASSWORD": "22tUniFq7nNNoCQxl0PqclfXD3DCbRg2",
        "HOST": "dpg-ckbghuect0pc73dm8smg-a.ohio-postgres.render.com",
        "PORT": "5432",
    }
}

SITE_ID = 2

USE_S3 = os.getenv("USE_S3") == "TRUE"

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
    # s3 static settings
    STATIC_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
    STATICFILES_STORAGE = "pokecardsV2.storage_backends.StaticStorage"
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "pokecardsV2.storage_backends.PublicMediaStorage"
    # s3 private media settings
    PRIVATE_MEDIA_LOCATION = "private"
    PRIVATE_FILE_STORAGE = "pokecardsV2.storage_backends.PrivateMediaStorage"

    AWS_S3_HOST = "s3.us-east-2.amazonaws.com"
    AWS_S3_REGION_NAME = "us-east-2"
else:
    STATIC_URL = "/staticfiles/"
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    MEDIA_URL = "/mediafiles/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_NAME")
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")


WSGI_APPLICATION = "pokecardsV2.wsgi.application"
# python manage.prod.py check --deploy
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
