from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path(r"projeto_grupo_5/", include("projeto_app.urls")),
    path(r"projeto_grupo_5/breno/", include("breno.urls")),
    path('admin/', admin.site.urls)

]
