from django.contrib import admin

from apps.book.models import Book, BookContributor, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]


@admin.register(BookContributor)
class BookContributorAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category__name", "book_contributor__full_name", "publishera"]
    raw_id_fields = ['category', "book_contributor"]
