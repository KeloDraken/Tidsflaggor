"""
Django development settings for src project.
"""

import os

from config.settings.base import *

SECRET_KEY = "django-insecure-i_+ydg8wuu6yg&xlb$q7_$(b*b$+$&e3hp%qzli0dsp6*-@5oj"

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "flaggor_db"),
        "USER": os.getenv("POSTGRES_USER", "flaggor_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "flaggor_password"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
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

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static-local"
