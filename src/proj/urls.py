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
from django.urls import path, include
from reflib import views
from mainpage import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage.as_view(), name = 'main'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('reflib/', include('reflib.urls', namespace="reflib")),
    path('bookview/', include('bookview.urls', namespace="bookview")),
    path('profiles/', include('loginpage.urls',namespace="profiles")),
    path('cartview/', include('cartview.urls', namespace="cartview")),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)