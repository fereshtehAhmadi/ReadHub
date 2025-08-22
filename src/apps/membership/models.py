from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel


class MembershipPlan(BaseModel):
    name = models.CharField(unique=True)
    duration_days = models.IntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = _("membership plan")
        verbose_name_plural = _("membership plans")


class UserDiscount(BaseModel):
    name = models.CharField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    promo_code = models.CharField(max_length=20)

    class Meta:
        verbose_name = _("user discount")
        verbose_name_plural = _("user discounts")
