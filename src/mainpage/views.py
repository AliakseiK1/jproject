from django.views import generic
from mainpage import models
from bookview import models as bw_models

# Create your views here.
#View list of Authors
class MainPage(generic.TemplateView):
    model = models.MainPage
    template_name = 'mainpage/mainpage.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sale_book1'] = bw_models.Book.objects.filter(category_id="2").order_by('-created_at')[0]
        context['sale_book2'] = bw_models.Book.objects.filter(category_id="2").order_by('-created_at')[1]
        context['sale_book3'] = bw_models.Book.objects.filter(category_id="2").order_by('-created_at')[2]
        context['sale_book4'] = bw_models.Book.objects.filter(category_id="2").order_by('-created_at')[3]
        context['fet_book1'] = bw_models.Book.objects.filter(category_id="3").order_by('-created_at')[0]
        context['fet_book2'] = bw_models.Book.objects.filter(category_id="3").order_by('-created_at')[1]
        context['fet_book3'] = bw_models.Book.objects.filter(category_id="3").order_by('-created_at')[2]
        context['fet_book4'] = bw_models.Book.objects.filter(category_id="3").order_by('-created_at')[3]
        return context