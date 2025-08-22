from django.contrib import admin

from apps.membership.models import MembershipPlan, UserDiscount


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "duration_days", "price"]
    search_fields = ["id", "name"]


@admin.register(UserDiscount)
class UserDiscountAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "start_date", "end_date", "promo_code", "user__full_name"]
    raw_id_fields = ['user']
    search_fields = ["id", "name", "user__full_name"]
