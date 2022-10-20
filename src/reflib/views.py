from tkinter import Tk
import _tkinter
from turtle import update
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models, forms

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
    form_class = forms.Author
    template_name = 'reflib/del_aut.html'

"""
def add_author(request):
    if request.method == "GET":
        form = forms.Author()
        context = {'form': form}
        return render(request, template_name='reflib/create.html', context=context)
    elif request.method == "POST":
        form = forms.Author(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(f'/authors_list/{obj.pk}/')
        else:
            context = {'form': form}
            return render(request, template_name='reflib/create.html', context=context)
    return HttpResponse("What is this????")

"""

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
    form_class = forms.Publisher
    template_name = 'reflib/pub_del.html'