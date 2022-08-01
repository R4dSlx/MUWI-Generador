from django.urls import path, include
from . import views

urlpatterns = [
    path("registration/register", views.register_request, name="register"),
    path("registration/login", views.login_request, name="login"),
    path("registration/logout", views.logout_request, name="logout"),


]
