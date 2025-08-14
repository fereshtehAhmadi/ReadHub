from config.tools.env import env

DATABASES = {
    'default': {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DB_NAME"),
            "USER": env("DB_USER"),
            "PASSWORD": env("DB_PASSWORD"),
            "HOST": env("DB_HOST"),
            "PORT": env("DB_PORT"),
        }
    }
}



DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"
