from django.urls import path
from breno import views as views

urlpatterns = [
    path("", views.sobre, name="sobre"),
    path("sobre/", views.sobre, name="sobre"),
    path("lista/", views.lista, name="lista"),
    path("tabela/", views.tabela, name="tabela")
]