from django.urls import path
from appdan import views as views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
]