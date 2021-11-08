from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def detalhes(request):
    return render(request, "app_wendell/detalhes.htm")

def se_juntar(request):
    return render(request, "app_wendell/se_juntar.htm")

def redes_sociais(request, rede):
    redes = ["instagram", "twitter", "github", "facebook"]
    if rede in redes:
        context ={
            "rede": rede,
            "instagram":"/grupo5",
            "twitter":"/grupo5", 
            "github":"/guilherme-melo/Grupo-5",
            "facebook":"grupo5"
        }
        return render(request, "app_wendell/redes.htm", context)
    else:
        return HttpResponseNotFound("Página não existe!")