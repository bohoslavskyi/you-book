from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models.user import User


@register(User)
class UserAdmin(BaseUserAdmin):
    ordering: list = ["id"]
    list_display: list = ["email", "is_active"]
    fieldsets: tuple = (
        (
            _("Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _("Other"),
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets: tuple = (
        (
            _("Credentials"),
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
        (
            _("Permissions"),
            {
                "classes": ("wide",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    readonly_fields: tuple = (
        "password",
        "created_at",
        "updated_at",
        "last_login",
    )
