from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class BookContributor(BaseModel):
    full_name = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("book_contributor")
        verbose_name_plural = _("book_contributors")


class Book(BaseModel):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    book_contributor = models.ForeignKey(BookContributor, on_delete=models.PROTECT)
    publisher = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("books")
        default_related_name = "books"
