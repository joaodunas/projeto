from django.urls import path
from . import views


urlpatterns = [
    path("backend/register/", views.registerUser),
    path("backend/login/", views.loginUser ),
    path("backend/halloffame/", views.get_top_users),
    ]