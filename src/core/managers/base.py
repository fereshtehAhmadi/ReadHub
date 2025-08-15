from django.db import models


class ActiveModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class NotActiveModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)
