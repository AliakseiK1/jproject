"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reflib import views as au_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_author/', au_views.AddAuthor.as_view()),
    path('upd_author/<int:pk>/', au_views.UpdAuthor.as_view()),
    path('del_author/<int:pk>/', au_views.DelAuthor.as_view()),
    path('details_author/<int:pk>/', au_views.DetailAuthor.as_view()),
    path('list_author/', au_views.ListAuthor.as_view()),
    
    path('add_publisher/', au_views.AddPublisher.as_view()),
    path('upd_publisher/<int:pk>/', au_views.UpdPublisher.as_view()),
    path('del_publisher/<int:pk>/', au_views.DelPublisher.as_view()),
    path('details_publisher/<int:pk>/', au_views.DetailPublisher.as_view()),
    path('list_publisher/', au_views.ListPublisher.as_view()),
]