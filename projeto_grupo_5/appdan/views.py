from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def nada(request):
    return render(request, "appdan/nada.htm")

def outracoisa(request):
    return render(request, "appdan/outracoisa.htm")
    
def coisa(request, fruta):
    frutas = ["banana", "morango", "melancia", "kiwi", "romã"]
    ruim = ["kiwi", "romã"]
    bom = ["banana", "morango", "melancia"]
    if fruta in frutas:
        if fruta in ruim:
            bomounao = "HORRÍVEL"
        elif fruta in bom:
            bomounao = "INCRÍVEL"
        context ={
            "fruta": "comida",
            "nome_da_fruta": fruta.capitalize(),
            "bomounao": bomounao,
            "frutas": frutas
        }
        return render(request, "appdan/coisa.htm", context)
    else:
        return HttpResponseNotFound("Página não existe!")

def redireciona(request):
    url_redirecionamento = reverse("quem_somos")
    return HttpResponseRedirect(url_redirecionamento)
    #return HttpResponseRedirect("/app_ezequiel/quem_somos")
