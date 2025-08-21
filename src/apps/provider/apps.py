from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProviderConfig(AppConfig):
    name = "apps.provider"
    verbose_name = _("Provider")
