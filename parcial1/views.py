from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bienvenido a la página de inicio</h1>")

def about(request):
    return HttpResponse("<h1>Acerca de: Proyecto examen - parcial1</h1>")

# Create your views here.
