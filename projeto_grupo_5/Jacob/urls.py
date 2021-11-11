
from django.urls import path
from Jacob import views as views

urlpatterns = [
    path("", views.primeiro, name="primeiro"),
    path("primeiro/", views.primeiro, name="primeiro"),
    path("primeiro/<str:pessoa>", views.equipe, name="equipe"),
    path("redireciona/", views.redireciona, name="redireciona")
]
