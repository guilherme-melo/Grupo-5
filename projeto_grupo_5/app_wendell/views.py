from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<strong>app_wendell</strong>")