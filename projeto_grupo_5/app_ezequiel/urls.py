from django.urls import path
from app_ezequiel import views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("special/", views.special, name="special")
]
