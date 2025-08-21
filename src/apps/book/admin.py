from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]


class BookContributorAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name"]


class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category__name", "book_contributor__full_name", "publishera"]
    raw_id_fields = ['category', "book_contributor"]
