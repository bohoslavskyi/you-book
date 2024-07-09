from django.urls import path

from ui.views import IndexView

app_name: str = "ui"
urlpatterns: list = [path(route="", view=IndexView.as_view(), name="index")]
