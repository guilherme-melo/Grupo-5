from django.http import HttpResponse
from django.shortcuts import render

def quem_somos(request):
    return render(request, "app_ezequiel/quem_somos.htm")

def fale_conosco(request):
    return render(request, "app_ezequiel/fale_conosco.htm")

def apoie(request):
    return render(request, "app_ezequiel/apoie.htm")