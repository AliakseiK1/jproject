

from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import RegisterForm



# Create your views here.
#View list of Authors
class SignUpView(generic.CreateView):
    form_class = RegisterForm
    template_name = "loginpage/signup.html"
    success_url = reverse_lazy("profiles:signup_success")


class SignupSuccess(generic.TemplateView):
    template_name = "loginpage/signup_success.html"