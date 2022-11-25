from django.views import generic
from django.views.generic import TemplateView


class MainPage(generic.TemplateView):
    template_name = 'mainpage/mainpage.html'