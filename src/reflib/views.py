from multiprocessing import context
from turtle import update
from django.views import generic
from . import models, forms
from django.urls import reverse_lazy


# Create your views here.
#View list of Authors

class ListAuthor(generic.ListView):
    model = models.Author
    template_name = 'reflib/list_aut.html'
    paginate_by = 5


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
    paginate_by = 5


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