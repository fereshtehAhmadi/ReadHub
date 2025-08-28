from django.contrib import admin

from apps.library.models import Library, LibraryBook


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]


@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):
    list_display = ["id", "library__name", "book__name", "total_copies", "available_copies"]
    search_fields = ["library__name", "book__name", "library__id", "book__id", "total_copies", "available_copies"]
    list_editable = ["total_copies", "available_copies"]
    raw_id_fields = ['library', "book"]
