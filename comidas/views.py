from django.shortcuts import render
from .models import Banquete

# Create your views here.
def portfolio(request):
    projects = Banquete.objects.all()
    return render(request, "comidas/catalogo.html", {'projects' : projects})