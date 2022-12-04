from multiprocessing import context
from tkinter import Tk
import _tkinter
from turtle import update
from urllib import response
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
#View list of Authors
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"