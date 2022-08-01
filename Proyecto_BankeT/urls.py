"""Proyecto_BankeT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from Proyecto_BankeT.views import *
from . import views 
from zeus.views import *
from Cliente.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hija1/', hija1),
    path('hija2/', hija2),
    path('register/', register_request, name="register"),
    path('login/', login_request, name="login"),
    path('gestion', home, name="gestioncomidas"),
    path('', views.inicio , name='Doctor'),
    path('contacto/', views.contacto,  name="contacto"),
    path('acerca/', views.acerca,  name="acerca"),
    path("logout", logout_request, name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Cliente/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Cliente/password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", password_reset_request, name="password_reset")

]
