from string import ascii_letters

from config.tools.env import env

from .base import *  # noqa: F403, F401
from .base import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY", default=ascii_letters)
ALLOWED_HOSTS: list[str] = env.list("DJANGO_ALLOWED_HOSTS")
CORS_ALLOWED_ORIGINS: list[str] = env.list("DJANGO_CORS_ALLOWED_ORIGINS")
CORS_ALLOW_HEADERS: list[str] = ["*"]

INSTALLED_APPS += []

MIDDLEWARE += []

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
