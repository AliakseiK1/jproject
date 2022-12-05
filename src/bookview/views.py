from multiprocessing import context
from tkinter import Tk
import _tkinter
from turtle import update
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from . import models
from django.urls import reverse_lazy
from bookview.models import Book


# Create your views here.
#View list of Bookview

class ListBook(generic.ListView):
    model = models.Book
    template_name = 'bookview/booklist.html'
    paginate_by = 5
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
    paginate_by = 5
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

# USERVIEW_SALE
class ListBookSl(generic.ListView):
    model = models.Book
    template_name = 'bookview/booklist_sl.html'
    paginate_by = 5
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_sl = models.Category.objects.filter(types_of_categories="SL")[0]
        context['sale_list'] = models.Book.objects.filter(category_id=category_sl)
        return context

# USERVIEW_NEW_ARRIVALS
class ListBookNa(generic.ListView):
    model = models.Book
    template_name = 'bookview/booklist_na.html'
    paginate_by = 5
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_na = models.Category.objects.filter(types_of_categories="NA")[0]
        context['new_list'] = models.Book.objects.filter(category_id=category_na)
        return context