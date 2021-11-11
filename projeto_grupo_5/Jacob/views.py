from django.conf.urls import url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def primeiro(request):
    return render(request, "Jacob/primeiro.htm")

def equipe(request, pessoa):
    equipe = ["dandan", "daniel", "guilherme", "breno", "wendell", "ezequiel"]
    cd = ["guilherme", "breno"]
    map = ["dandan", "wendell", "ezequiel", "daniel"]
    if pessoa in equipe:
        if pessoa in cd:
            curso = "CIÊNCIAS DE DADOS"
        elif pessoa in map:
            curso = "MATEMÁTICA APLICADA"
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