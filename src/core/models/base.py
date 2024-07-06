from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at: datetime | models.DateTimeField = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True,
    )
    updated_at: datetime | models.DateTimeField = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True,
    )

    class Meta:
        abstract = True
