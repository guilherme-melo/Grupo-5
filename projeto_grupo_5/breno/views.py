from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def sobre(request):
    return render(request, "app_breno/sobre.htm")

def lista(request):
    return render(request, "app_breno/lista.htm")

def tabela(request):
    return render(request, "app_breno/tabela.htm")
    
