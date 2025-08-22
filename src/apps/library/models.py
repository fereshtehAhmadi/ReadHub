from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel


class Library(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        verbose_name = _("library")
        verbose_name_plural = _("libraries")
