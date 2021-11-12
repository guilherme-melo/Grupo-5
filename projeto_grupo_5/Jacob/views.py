from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def primeiro(request):
    return render(request, "Jacob/primeiro.htm")

def equipe(request, pessoa):
    equipe = ["burro", "gafanhoto", "gasparzinho", "piriquito", "saci", "Daniel"]
    cd = ["saci", "Dandan"]
    map = ["burro", "gafanhoto", "gasparzinho", "piriquito"]
    if pessoa in equipe:
        if pessoa in cd:
            curso = "MEDICINA"
        elif pessoa in map:
            curso = "MATEMÁTICA DE DADOS"
        context ={
            "nome": "amiguinho",
            "nome_familia": pessoa.capitalize(),
            "curso": curso,
            "equipe": equipe
        }
        return render(request, "Jacob/equipe.htm", context)
    else:
        return HttpResponseNotFound("Página não existe!")

def redireciona(request):
    url_redirecionamento = reverse("primeiro")
    return HttpResponseRedirect(url_redirecionamento)