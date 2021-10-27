from django.contrib import admin
from django.urls import path, include
from django.urls import include
from breno import views as views
from django.urls.conf import include

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
]