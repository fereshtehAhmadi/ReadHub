from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MembershipConfig(AppConfig):
    name = "apps.membership"
    verbose_name = _("Membership")
