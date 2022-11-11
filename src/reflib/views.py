from multiprocessing import context
from tkinter import Tk
import _tkinter
from turtle import update
from urllib import response
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template import RequestContext

# Create your views here.
#View list of Authors

"""
def authors_list (request):
    authors = models.Author.objects.all()
    responce = f"<h1>List of Authors {request.user.pk}:</h1>"
    for author in authors:
        responce += f"Author {author.auth_name} from country {author.auth_country} and special note: {author.auth_note}"
        return HttpResponse(responce)
"""
class ListAuthor(generic.ListView):
    model = models.Author
    template_name = 'reflib/list_aut.html'

class DetailAuthor(generic.DetailView):
    model = models.Author
    template_name = 'reflib/details_aut.html'

class AddAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.Author
    template_name = 'reflib/add.upd_aut.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Add'
        return context


class UpdAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.Author
    template_name = 'reflib/add.upd_aut.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Update'
        return context

class DelAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'reflib/del_aut.html'
    success_url = reverse_lazy("reflib:list_author")



###################################################################
#View list of Publishers
class ListPublisher(generic.ListView):
    model = models.Publisher
    template_name = 'reflib/pub_list.html'

class DetailPublisher(generic.DetailView):
    model = models.Publisher
    template_name = 'reflib/pub_details.html'

class AddPublisher(generic.CreateView):
    model = models.Publisher
    form_class = forms.Publisher
    template_name = 'reflib/pub_add.upd.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Add'
        return context


class UpdPublisher(generic.UpdateView):
    model = models.Publisher
    form_class = forms.Publisher
    template_name = 'reflib/pub_add.upd.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Update'
        return context

class DelPublisher(generic.DeleteView):
    model = models.Publisher
    template_name = 'reflib/pub_del.html'
    success_url = reverse_lazy("reflib:list_publisher")


#############################################
#View for Mainpage
class MainPage(generic.TemplateView):
    model = models.MainPage
    template_name = 'mainpage/mainpage.html'

"""
def main_page (request):
    mainpage = 'mainpage.html'
    responce = mainpage
    return HttpResponse(responce)

def main_page(request):
    if request.method == 'GET':
        return render(request, 'mainpage/mainpage.html', context)
"""


#########################################
#users
"""
def user_login(request):
    if request.method == 'GET':
        return render(request,'loginpage/loginpage.html', context={})
    if request.method == 'POST':
        user = authenticate(
            request=request,
            username=request.POST.get('login'),
            password=request.POST.get('password'),
        )
        if user is not None:
            print(user)
            login(request, user)
            return render (request, 'mainpage/mainpage.html', context_instance=RequestContext(request))

"""