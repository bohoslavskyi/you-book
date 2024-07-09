from django.contrib.admin import ModelAdmin, register
from django.utils.translation import gettext_lazy as _

from core.models import Profile


@register(Profile)
class ProfileAdmin(ModelAdmin):
    ordering: list = ["nickname"]
    list_display: list = ["nickname", "first_name", "last_name"]
    fieldsets: tuple = (
        (
            _("General information"),
            {
                "fields": (
                    "user",
                    "nickname",
                    "first_name",
                    "last_name",
                    "short_bio",
                    "date_of_birth",
                ),
            },
        ),
        (
            _("Other"),
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )
    add_fieldsets: tuple = (
        (
            None,
            {
                "fields": (
                    "user",
                    "nickname",
                    "first_name",
                    "last_name",
                    "short_bio",
                    "date_of_birth",
                ),
            },
        ),
    )
    readonly_fields: tuple = (
        "created_at",
        "updated_at",
    )
