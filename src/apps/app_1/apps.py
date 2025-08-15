from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class App1Config(AppConfig):
    name = "apps.app_1"
    verbose_name = _("App_1")
