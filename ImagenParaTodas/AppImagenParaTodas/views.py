from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import redirect, render, HttpResponse

def vestir(request):
    return render(request, "AppImagenParaTodas/vestidos.html") 

def tips(request):
    
    return render(request, "AppImagenParaTodas/cuerpos.html")      

def cuerpos(request):
     return render(request, "AppImagenParaTodas/cuerpos.html")                           
