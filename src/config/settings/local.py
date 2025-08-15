from config.tools.env import env

from .base import *  # noqa: F403, F401

DEBUG = True
ALLOWED_HOSTS: list[str] = env.list("DJANGO_ALLOWED_HOSTS")
