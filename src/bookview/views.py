from multiprocessing import context
from tkinter import Tk
import _tkinter
from turtle import update
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from . import models
from django.urls import reverse_lazy

# Create your views here.
#View list of Bookview

class ListBook(generic.ListView):
    model = models.Book
    template_name = 'bookview/booklist.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class BookView(generic.DetailView):
    model = models.Book
    template_name = 'bookview/bookview.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['a_book'] = models.Book.objects.filter(book_image=self)
        return context

class AddBook(generic.CreateView):
    model = models.Book
    form_class = forms.Book
    template_name = 'bookview/book_add.upd.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Add'
        return context


class UpdBook(generic.UpdateView):
    model = models.Book
    form_class = forms.Book
    template_name = 'bookview/book_add.upd.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation'] = 'Update'
        return context

class DelBook(generic.DeleteView):
    model = models.Book
    template_name = 'bookview/book_del.html'
    success_url = reverse_lazy("bookview:booklist")

###################################################################
# USERVIEW
class ListBookUs(generic.ListView):
    model = models.Book
    template_name = 'bookview/booklist_user.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

# USERVIEW_SALE
class ListBookSl(generic.ListView):
    model = models.Book
    template_name = 'bookview/booklist_sl.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sale_list'] = models.Book.objects.filter(category_id="2")
        return context

# USERVIEW_NEW_ARRIVALS
class ListBookNa(generic.ListView):
    model = models.Book
    template_name = 'bookview/booklist_na.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['new_list'] = models.Book.objects.filter(category_id="3")
        return context