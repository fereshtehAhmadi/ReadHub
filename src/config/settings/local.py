from config.tools.env import env
ALLOWED_HOSTS: list[str] = env.list("DJANGO_ALLOWED_HOSTS")
DEBUG=True
