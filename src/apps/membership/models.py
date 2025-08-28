from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.user.models import User
from core.models.base import BaseModel


class MembershipPlan(BaseModel):
    name = models.CharField(unique=True)
    duration_days = models.IntegerField()
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = _("membership plan")
        verbose_name_plural = _("membership plans")


class UserDiscount(BaseModel):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    promo_code = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("user discount")
        verbose_name_plural = _("user discounts")


class Preorder(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.PROTECT)
    membership_plan = models.ForeignKey("MembershipPlan", on_delete=models.PROTECT)
    user_discount = models.ForeignKey("UserDiscount", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = _("preorder")
        verbose_name_plural = _("preorders")


class PurchasedMembership(BaseModel):
    preorder = models.ForeignKey("Preorder", on_delete=models.PROTECT)
    price_paid = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        verbose_name = _("purchased membership")
        verbose_name_plural = _("purchased memberships")
