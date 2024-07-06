from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str | None = None, **extra_fields):
        if not email:
            raise ValueError(self.__get_required_field_error("email"))
        if not password:
            raise ValueError(self.__get_required_field_error("password"))

        normalized_email: str = self.normalize_email(email)
        user: User = self.model(email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, password: str):
        user: User = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

    def __get_required_field_error(self, field: str) -> str:
        return "Missing required field: {field}".format(field=field)


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    USERNAME_FIELD: str = "email"

    email: str | models.EmailField = models.EmailField(
        verbose_name=_("user's email"),
        max_length=64,
        unique=True,
    )
    is_staff: bool | models.BooleanField = models.BooleanField(
        verbose_name=_("staff status"),
        default=False,
        help_text=_("Indicates whether the user can log into this admin site."),
    )
    is_active: bool | models.BooleanField = models.BooleanField(
        verbose_name=_("activation status"),
        default=True,
        help_text=_("Indicates whether this user should be treated as active."),
    )

    objects: UserManager = UserManager()

    class Meta:
        verbose_name: str = "user"
        verbose_name_plural: str = "users"

    def __str__(self) -> str:
        return self.email
