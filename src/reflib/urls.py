from django.urls import path
from . import views
app_name = "reflib"

urlpatterns = [
    path('add_aut/', views.AddAuthor.as_view(), name = 'add_author'),
    path('upd_aut/<int:pk>/', views.UpdAuthor.as_view(), name = 'upd_author'),
    path('del_aut/<int:pk>/', views.DelAuthor.as_view(), name = 'del_author'),
    path('detls_aut/<int:pk>/', views.DetailAuthor.as_view(), name = 'details_author'),
    path('list_aut/', views.ListAuthor.as_view(), name = 'list_author'),
    
    path('add_pub/', views.AddPublisher.as_view(), name = 'add_publisher'),
    path('upd_pub/<int:pk>/', views.UpdPublisher.as_view(), name = 'upd_publisher'),
    path('del_pub/<int:pk>/', views.DelPublisher.as_view(), name = 'del_publisher'),
    path('detls_pub/<int:pk>/', views.DetailPublisher.as_view(), name = 'details_publisher'),
    path('list_pub/', views.ListPublisher.as_view(), name = 'list_publisher'),
]