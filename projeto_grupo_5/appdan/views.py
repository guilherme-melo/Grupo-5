from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>deu certo?</strong>")
