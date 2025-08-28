from django.contrib import admin

from apps.membership.models import MembershipPlan, Preorder, PurchasedMembership, UserDiscount


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "duration_days", "price"]
    search_fields = ["id", "name"]


@admin.register(UserDiscount)
class UserDiscountAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "start_date", "end_date", "promo_code", "user__full_name"]
    raw_id_fields = ["user"]
    search_fields = ["id", "name", "user__full_name"]


@admin.register(Preorder)
class PreorderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "membership_plan", "user_discount"]
    raw_id_fields = ["user", "membership_plan", "user_discount"]
    search_fields = ["id", "membership_plan__name", "membership_plan__id", "user__full_name"]


@admin.register(PurchasedMembership)
class PurchasedMembershipAdmin(admin.ModelAdmin):
    list_display = ["id", "preorder", "price_paid", "created_at", "expires_at"]
    raw_id_fields = ["preorder"]
    search_fields = ["id", "preorder__id"]
