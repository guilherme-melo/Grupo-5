from django.urls import path
from appdan import views as views

urlpatterns = [
    path("", views.outracoisa, name="outracoisa"),
    path("coisa/<str:fruta>", views.coisa, name="coisa"),
    path("outracoisa", views.outracoisa, name="outracoisa"),
    path("nada", views.nada, name="nada"),
    path("outracoisa/<str:fruta>", views.coisa, name="coisa"),
    path("redireciona/", views.redireciona, name="redireciona")
]