from django.urls import path
from appdan import views as views

urlpatterns = [
    path("", projeto_grupo_5_views.projeto_grupo_5, name="projeto_grupo_5" ),
]