from django.http import HttpResponse 
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Request: Sirve para realizar peticiones
# HTTPResponse: Para enviar la respuesta usando el protocolo HTTPS.

# Esto es una vista: 

def inicio(request):
	print(request.user)
	return render(request, "P1.html", {})

def hija1(request):
	return render(request, "P1W.html", {})

def contacto(request):
	return render(request, "contacto.html", {})

def acerca(request):
	return render(request, "acerca.html", {})

def hija2(request):
	return render(request, "fl.pug", {})


