from django.views import generic
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class IndexView(generic.TemplateView):
    template_name = "ui/index.html"
