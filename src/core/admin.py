from django.contrib import admin

from core import models


admin.site.register(model_or_iterable=models.User)
