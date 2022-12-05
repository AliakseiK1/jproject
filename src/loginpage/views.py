from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
#View list of Authors
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "loginpage/signup.html"