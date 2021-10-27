
from django.urls import path
from Jacob import views as Jacob_views

urlpatterns = [
    path("",Jacob_views.index, name="index"),
    path("index/", Jacob_views.index, name ="index")
]
