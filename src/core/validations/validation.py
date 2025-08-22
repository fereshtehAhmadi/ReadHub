from django.core import validators
from django.utils.translation import gettext_lazy as _


class MobileNumberValidators(validators.RegexValidator):
    regex = r"^09\d{9}$"
    message = _("mobile number is not valid.")
    flags = 0


class UsernameValidators(validators.RegexValidator):
    regex = r"^[a-zA-Z][a-zA-Z0-9_]*$"
    message = _("Username must start with a letter and can only contain letters, numbers, and underscores.")
    flags = 0
