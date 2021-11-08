from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path(r"app_guilherme/", include("app_guilherme.urls")),
    path(r"projeto_grupo_5/breno/", include("breno.urls")),
    path(r"Jacob/", include("Jacob.urls")),
    path(r"app_ezequiel/", include("app_ezequiel.urls")),
    path(r"app_wendell/", include("app_wendell.urls")),
    path(r"appdan/", include("appdan.urls")),
    path('admin/', admin.site.urls)
]
