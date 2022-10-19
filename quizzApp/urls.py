from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path("register/", views.registerView, name= "register"),
    path("backend/register/", views.registerUser),
    path("login/", views.loginView, name = "login"),
    path("backend/login/", views.loginUser ),
    path("halloffame/", views.halloffameView, name= "halloffame"),
    path("backend/halloffame/", views.get_top_users),
    path("gen_users/<int:num_users>",views.gen_users),
    ]