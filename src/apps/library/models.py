from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.book.models import Book
from core.models.base import BaseModel


class Library(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        verbose_name = _("library")
        verbose_name_plural = _("libraries")


class LibraryBook(BaseModel):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    total_copies = models.PositiveIntegerField(default=0)
    available_copies = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("library books")
        verbose_name_plural = _("library books")
