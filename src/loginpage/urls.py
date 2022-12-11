"""loginpage URL Configuration

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
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, SignupSuccess
from . import views


app_name = "loginpage"


urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout', auth_views.LoginView.as_view(template_name='loginpage/login.html'), name = 'logout'),
    path('reset-form', auth_views.LoginView.as_view(template_name='loginpage/password_reset_form.html'), name = 'reset-form'),
    path('reset-done', auth_views.LoginView.as_view(template_name='loginpage/password_reset_done.html'), name = 'reset-done'),
    path('reset-confirm', auth_views.LoginView.as_view(template_name='loginpage/password_reset_confirm.html'), name = 'reset-confirm'),
    path('reset-complete', auth_views.LoginView.as_view(template_name='loginpage/password_reset_complete.html'), name = 'reset-complete'),
    path('signup/', SignUpView.as_view(), name="signup"),
    #path('signup_success/', SignupSuccess.as_view(), name='signup_success')
    path('signup_success/', views.SignupSuccess.as_view(), name='signup_success'),

]