from django.http import HttpResponse

from django.shortcuts import render

def detalhes(request):
    return render(request, "app_wendell/detalhes.htm")

def se_juntar(request):
    return render(request, "app_wendell/se_juntar.htm")
