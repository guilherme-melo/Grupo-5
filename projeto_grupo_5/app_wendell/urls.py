
from django.urls import path
from app_wendell import views as views

urlpatterns = [
    path("", views.detalhes, name="detalhes"),
    path("detalhes/", views.detalhes, name="detalhes"),
    path("se_juntar/", views.se_juntar, name="se_juntar")
]
