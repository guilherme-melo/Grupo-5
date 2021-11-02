from django.urls import path
from app_ezequiel import views as views

urlpatterns = [
    path("", views.quem_somos, name="quem_somos"),
    path("quem_somos/", views.quem_somos, name="quem_somos"),
    path("fale_conosco/", views.fale_conosco, name="fale_conosco"),
    path("apoie/", views.apoie, name="apoie")
]