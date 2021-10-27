
from django.urls import path
from app_wendell import views as app_wendell_views

urlpatterns = [
    path("", app_wendell_views.index, name ="index"),
    path("index/", app_wendell_views.index, name ="index"),
]
