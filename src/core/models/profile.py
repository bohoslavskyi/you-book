from datetime import date

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.models.user import User


class Profile(BaseModel):
    user: User | models.OneToOneField = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nickname: str | models.CharField = models.CharField(
        verbose_name="user's nickname",
        max_length=50,
    )
    first_name: str | models.CharField = models.CharField(
        verbose_name=_("user's first name"),
        max_length=50,
    )
    last_name: str | models.CharField = models.CharField(
        verbose_name=_("user's last name"),
        max_length=50,
    )
    short_bio: str | models.CharField | None = models.CharField(
        verbose_name=_("user's short bio"),
        max_length=200,
        blank=True,
        null=True,
    )
    date_of_birth: date | models.DateField | None = models.DateField(
        verbose_name=_("user's date of birth"),
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name: str = _("profile")
        verbose_name_plural: str = _("profiles")
        ordering: list = ["nickname"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
