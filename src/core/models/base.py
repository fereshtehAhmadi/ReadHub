from django.db import models
from django.utils.translation import gettext_lazy as _

from core.managers.base import ActiveModelManager, NotActiveModelManager


class BaseModel(models.Model):
    is_active = models.BooleanField(_("is_active"), default=True)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("modified_at"), auto_now=True)

    objects = models.Manager()
    actives = ActiveModelManager()
    not_actives = NotActiveModelManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def, override]
        self.is_active = False
        self.save(update_fields=["is_active"])
        return None
