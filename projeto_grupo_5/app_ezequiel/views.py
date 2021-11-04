from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def quem_somos(request):
    return render(request, "app_ezequiel/quem_somos.htm")

def fale_conosco(request):
    return render(request, "app_ezequiel/fale_conosco.htm")

def apoie(request):
    return render(request, "app_ezequiel/apoie.htm")
    
def equipe(request, pessoa):
    equipe = ["dandan", "daniel", "guilherme", "bruno", "wendell", "ezequiel"]
    if pessoa in equipe:
        return HttpResponse("<strong>Pessoa incrível</strong>")
    else:
        return HttpResponseNotFound("Página não existe!")

def redireciona(request):
    #url_redirecionamento = reverse("equipe", args=["ezequiel"])
    #return HttpResponseRedirect(url_redirecionamento)
    return HttpResponseRedirect("/app_ezequiel/quem_somos")