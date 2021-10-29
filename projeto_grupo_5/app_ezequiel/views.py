from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<strong>Ezequiel</strong>")

def special(request):
    return render(request, "app_ezequiel/index.htm")