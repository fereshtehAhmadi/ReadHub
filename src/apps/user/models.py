from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.validations.validation import MobileNumberValidators, UsernameValidators


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, null=True)
    mobile = models.CharField(_("mobile"), validators=[MobileNumberValidators()], max_length=11, db_index=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[UnicodeUsernameValidator(), UsernameValidators()],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    REQUIRED_FIELDS: list[str] = ["mobile", "first_name", "last_name"]

    class Meta:
        ordering: list[str] = ["-id"]

    @property
    def get_full_name(self) -> str:
        first_name = getattr(self, "first_name", "")
        last_name = getattr(self, "last_name", "")
        return f"{first_name} {last_name}".strip()


class LibraryStaff(BaseModel):
    user = models.ForeignKey("User", on_delete=models.PROTECT)
    library = models.ForeignKey("library.Library", on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)
    class Meta:
        verbose_name = _("library staff")
        verbose_name_plural = _("library staff")
