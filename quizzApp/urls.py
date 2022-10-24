from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path("register/", views.registerView, name= "register"),
    path("login/", views.loginView, name = "login"),
    path("halloffame/", views.halloffameView, name= "halloffame"),
    ]