from django.urls import path
from . import views
app_name = "bookview"

urlpatterns = [
    path('add_book/', views.AddBook.as_view(), name = 'add_book'),
    path('upd_book/<int:pk>/', views.UpdBook.as_view(), name = 'upd_book'),
    path('del_book/<int:pk>/', views.DelBook.as_view(), name = 'del_book'),
    path('detls_book/<int:pk>/', views.BookView.as_view(), name = 'details_book'),
    path('list_book/', views.ListBook.as_view(), name = 'list_book'),
]